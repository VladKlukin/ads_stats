from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from .database import SessionLocal
from sqlalchemy import exists,select,func
app = FastAPI()
from .models import Searches,Measurements


class SearchCreate(BaseModel):
    phrase: str
    region: str


class StatResponse(BaseModel):
    id:int
    start_time: str
    end_time: str

@app.post("/search",tags=["search"], summary="Add a new search")
def add_search(search: SearchCreate):
    ad =  {
        "id" : 1,
        "phrase": search.phrase,
        "region": search.region
    }
    with SessionLocal() as session:
        query = select(Searches).where(Searches.phrase == ad["phrase"],Searches.region == ad["region"])
        check_query = session.execute(query).scalar_one_or_none()
        if  check_query:
            return check_query.id
        else:  
            data = Searches(phrase=ad["phrase"],region=ad["region"])
            session.add(data)
            session.commit()
            return  data.id
    

@app.get("Stat",tags=["stat"], summary="Get statistics for a search")
def get_stat(stat: StatResponse):
    info = {
        "id":1,
        "start_time":stat.start_time,
        "end_time":stat.end_time
    }
    


    
if __name__ == "__main__":   
    uvicorn.run("app.main:app",reload=True)