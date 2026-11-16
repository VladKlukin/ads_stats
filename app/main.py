from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

bd = []

class SearchCreate(BaseModel):
    phrase: str
    region: str


@app.post("/search",tags=["search"], summary="Add a new search")
def add_search(search: SearchCreate):
    ad =  {
        "id" : 1,
        "phrase": search.phrase,
        "region": search.region
    }
    bd.append(ad)
    print(bd)
    return ad



    
if __name__ == "__main__": 
    uvicorn.run("main:app",reload=True)