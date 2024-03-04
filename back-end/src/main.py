import typing as t
from fastapi import FastAPI, Request
from src.core.enchant import EnchantClient
import pydantic

class Rule(pydantic.BaseModel):
    rule: str
    scoring_condition: str

    def __init__(self, rule: str, scoring_condition: str = None) -> None:
        rule = rule
        scoring_condition: str | None  = scoring_condition


DEFAULT_RULES = ["You must use the three letters provided.", "The three letters must appear respectively."]
SCORE_RULES = ["Come up with the longest word you can think of."]


class GuessWordReq(pydantic.BaseModel):
    word: str = pydantic.Field(description="Word guess sent by player")

# class RulesReq(pydantic.BaseModel):
    # rules: dict[str, str] = pydantic.Field(description=)

app = FastAPI()
 
@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@app.get("/rules", status_code=200)
async def rules():
    game_rules = []

    game_rules = DEFAULT_RULES
    game_rules.append(SCORE_RULES[0])
    return {"rules": game_rules[:3]}


# @app.get("/letters", status_code=200)
# async def game():

#     import json
#     with open("letters.json", "r") as f:
# j       



    # return {"game": "rules"}

@app.post("/guess", status_code=201)
async def guess(word_guess: str):
    client = EnchantClient()
    return client.check_word(word_guess)

from fastapi.staticfiles import StaticFiles
app.mount("/ui", StaticFiles(directory="ui"), name="ui")