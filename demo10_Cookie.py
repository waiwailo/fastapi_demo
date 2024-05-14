from typing import Optional

import uvicorn
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/demo1/")
async def read_items(name: Optional[str] = Cookie(None)):
    return {"name": name}


from fastapi.responses import JSONResponse


@app.get("/demo2/")
def Login():
    content = {"message": "yy_cookie"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value="zlkt")
    return response


if __name__ == "__main__":
    uvicorn.run(app="demo10_Cookie:app", host="127.0.0.1", port=8080, reload=True)
