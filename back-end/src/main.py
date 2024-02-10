from fastapi import FastAPI

app = FastAPI()

 
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/game")
async def root():
    return {"game": "rules"}