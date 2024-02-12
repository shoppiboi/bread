from fastapi import FastAPI, Request
from src.core.enchant import EnchantClient
import pydantic

class GuessWordReq(pydantic.BaseModel):
    word: str = pydantic.Field(description="Word guess sent by player")



app = FastAPI()

 
@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@app.get("/game", status_code=200)
async def game():
    return {"game": "rules"}

@app.post("/guess", status_code=201)
async def guess(word_guess: str):
    client = EnchantClient()
    return client.check_word(word_guess)
    