import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/demo1/", status_code=201)
async def create_item(name: str):
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run(app="demo13_Response_status_code:app", host="127.0.0.1", port=8080, reload=True)