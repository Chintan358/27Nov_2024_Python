from fastapi import FastAPI
app  = FastAPI()
import uvicorn
from pydantic import BaseModel, Field

class Student(BaseModel):
    name : str
    email  :str

@app.get("/hello")
async def myapi():
    return {"message":"Hello Fast API"}

@app.get("/hello/{data}")
async def myapi(data):
    return {"message":data}


@app.post("/hello")
async def myapi(s1:Student):
    print(s1)
    return {"message":"post api calling"}




@app.get("/data")
async def myapi(id:int):
    return {"message":id}


if __name__ == "__main__":
   uvicorn.run("myapp:app", host="127.0.0.1", port=8000, reload=True)


