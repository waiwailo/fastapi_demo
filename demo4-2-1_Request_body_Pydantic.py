import uvicorn
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# 接口传参方式之一：通过发送请求体（Request Body）来传递请求数据
# 在 FastAPI，提倡使用 Pydantic 模型来定义请求体

# 自定义一个 Pedantic 模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/demo/{path}")
# item 参数的类型指定为 Item 模型
async def create_item(
        *,
        path: str = Path(...),
        item: Item):
    return path,item


if __name__ == "__main__":
    uvicorn.run(app="demo4-2_Request_body_Pydantic:app", host="127.0.0.1", port=80, reload=True)
