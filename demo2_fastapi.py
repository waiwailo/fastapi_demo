from typing import Optional

from fastapi import FastAPI
import uvicorn

app2 = FastAPI()


# 路径参数+必填请求参数
# 调用 http://127.0.0.1/demo2/123?name=zhangsan
@app2.get("/demo1/{id}")
async def read_item(id: str, name: str):
    return {"id": id, "name": name}


# 路径参数+选填请求参数
# 调用 http://127.0.0.1/demo2/123
@app2.get("/demo2/{id}")
async def read_item(id: str, name: Optional[str] = None):
    return {"id": id, "name": name}


if __name__ == "__main__":
    uvicorn.run(app="demo2_fastapi:app2", host="127.0.0.1", port=80, reload=True)
