from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from loguru import logger

from database.crud import get_comment
from database.db import get_db
from notifier.scrapper_to_db import StoreDB, Platform


router = APIRouter(
    prefix='/notifier-tasks',
    tags=['notifier-tasks']
)

@router.post('/database-notifier')
async def store_data(
    name: Optional[Platform],
    db: Session = Depends(get_db),                  
    url: Optional[str] = None,
    max_count: Optional[int] = 50
    ):
    
    try:    
        data = StoreDB.get_data(
            name=name,
            url=url,
            max_count=max_count
            )
        for item in data:
            get_comment(db, item)
        
        logger.success('Successfully store data')
        
        return {'Status': 'Success'}

    except Exception as e:

        logger.error(e)

        raise HTTPException(status_code=500, detail="Failed to store data")
