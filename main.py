from pydantic import BaseModel
from fastapi import FastAPI, Response
import os
root = os.path.dirname(os.path.abspath(__file__))


app = FastAPI()

listFruits = [{"name": "apple"}, {"name": "banana"}, {"name": "orange"}, {"name": "pineapple"}]

class Fruit(BaseModel):
    name: str
    
@app.get("/")
async def main():
    #print(root)
    with open(os.path.join(root, 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

#Get all fruits
@app.get("/fruits")
def read_root():
    return listFruits

#Get fruits by id
@app.get("/fruit/{id}")
def read_root(id: int):
    return listFruits[id]

#Post a new fruit
@app.post("/fruit/")
async def create_item(fruit: Fruit):
    return fruit