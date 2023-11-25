from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from loguru import logger

from notifier.scrapper_to_db import StoreDB, Platform


router = APIRouter(
    prefix='/scrapper-tasks',
    tags=['scrapper-tasks']
)


@router.post('/scrapper')
def crawl_data(
        name: Platform,
        url: Optional[str]=None,
        max_count: Optional[int]=50
        ):
    
    try:    
        data = StoreDB.get_data(
                                name=name,
                                url=url,
                                max_count=max_count
                                )
        
        logger.success('Successfully crawl data')

        return JSONResponse(content=data)
    
    except Exception as e:

        logger.error(e)

        raise HTTPException (status_code=400, detail="Failed to crawl data")