from fastapi import FastAPI
import uvicorn

app = FastAPI()


class SearchCreate(BaseModel):
    phrase: str
    region: str






if __name__ == "__main__": 
    uvicorn.run("main:app",reload=True)