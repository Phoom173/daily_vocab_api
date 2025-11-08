from fastapi import FastAPI
from app.schemas import WordResponse
from fastapi import HTTPException
from app.routers import words
from app.database import Base, engine
from app.routers import words, practice

Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(words.router, prefix="/api", tags=["words"])
app.include_router(practice.router, prefix='/api', tags=["practice"])

@app.get("/api/word" , response_model = WordResponse)
def get_random_word():
    """Get a random word"""
    # TODO Write logic here....
    word = []
    if len(word) == 0:
        raise HTTPException(
            status_code = 404,
            detail = "No words available in database"
        )

@app.get("/")
def read_root():
    return {
        "message": "Vocabulary Practice API",
        "version": "1.0.0",
        "endpoints": {
            "random_word": "/api/word",
            "validate": "/api/validate-sentence",
            "summary": "/api/summary",
            "history": "/api/history"
        }
    }