from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import python._types as _types
import fuctool

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000", ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/test")
def root():
    return {"message": "test"}


@app.post("/api/subject")
async def search_subject(
        search_info: _types.LevelModel
):
    return fuctool.getSubject(
        search_info.level.value
    )


@app.post("/api/year")
async def search_year(
        search_info: _types.SubjectModel
):
    return fuctool.getYear(
        search_info.level.value,
        search_info.subject
    )


@app.post("/api/papers")
async def search_paper(
        search_info: _types.PaperModel
):
    return fuctool.getPaper(
        search_info.level.value,
        search_info.subject,
        search_info.year
    )


@app.get("/api/paper")
async def paper_downloader(
    paper_info: str
):
    return FileResponse(paper_info)


if __name__ == "__main__":
    import uvicorn
    import os

    print(os.getcwd())
    uvicorn.run("main:app")
