from fastapi import FastAPI
import random    # api going to return to the user random number that we query


app = FastAPI()


@app.get('/')
async def root():
    return {"example":"This is an example", "data": 999}

