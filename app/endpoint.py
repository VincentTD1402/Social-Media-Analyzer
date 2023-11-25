from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import analyzer, scrapper, notifier


app = FastAPI(openapi_url="/api/v1/neurond-social-medial-tool/tasks/openapi.json",
              docs_url="/api/v1/neurond-social-medial-tool/tasks/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(scrapper.router, prefix='/api/v1/scrapper')
app.include_router(analyzer.router, prefix='/api/v1/analyzer')
app.include_router(notifier.router, prefix='/api/v1/notifier')

if __name__ == '__main__':
    uvicorn.run("endpoint:app", reload=True, host='0.0.0.0', port=4000)
