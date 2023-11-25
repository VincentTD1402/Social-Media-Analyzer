from fastapi import APIRouter, Response, status
from typing import Optional

from analyzer.keyword_analyzer import KeywordExtraction

router = APIRouter(
    prefix='/analyzer-tasks',
    tags=['analyzer-tasks']
)

@router.post('/keyword-analyzer')
async def upload(response: Response, text: Optional[str] = None , lan: Optional[str] = 'vi', max_ngram: Optional[int] = 4, numberofkeywords: Optional[int] = 10):
    if text is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'message': 'Invalid text parameter!'}
    results = KeywordExtraction.keywordpredict(text=text, lan=lan, max_ngram=max_ngram , numberofkeywords=numberofkeywords)
    response.status_code = status.HTTP_200_OK
    return results