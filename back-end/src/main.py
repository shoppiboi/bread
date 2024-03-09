import json
import random
from src.core.enchant import EnchantClient
import pydantic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Rule(pydantic.BaseModel):
    rule: str
    scoring_condition: str

    def __init__(self, rule: str, scoring_condition: str = None) -> None:
        rule = rule
        scoring_condition: str | None = scoring_condition


DEFAULT_RULES = [
    "You must use the three letters provided.",
    "The three letters must appear respectively.",
]
SCORE_RULES = ["Come up with the longest word you can think of."]


class GuessWordReq(pydantic.BaseModel):
    word: str = pydantic.Field(description="Word guess sent by player")


# class RulesReq(pydantic.BaseModel):
# rules: dict[str, str] = pydantic.Field(description=)

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_rules() -> list[str]:
    return DEFAULT_RULES + SCORE_RULES


def get_letters() -> str:
    d = {}
    with open("./src/letters.json") as f:
        d = json.loads(f.read())

    return random.choice(d["letters"]).upper()

@app.get("/", status_code=200)
async def root():
    return {"game": {"rules": get_rules(), "letters": get_letters()}}

@app.get("healthcheck", status_code=200)
async def healthcheck():
    return {"ok": True}


# @app.get("/rules", status_code=200)
# async def rules():
#     game_rules = []

#     game_rules = DEFAULT_RULES
#     game_rules.append(SCORE_RULES[0])
#     return {"rules": game_rules[:3]}



@app.get("/game", status_code=200)
async def game():
    return {"game": {"rules": get_rules(), "letters": get_letters()}}


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
