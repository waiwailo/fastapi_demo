from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(
        # 路径参数
        item_id: int,
        # 请求体，模型类型
        item: Item,
        # 查询参数
        name: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    print(result)
    if name:
        # 如果查询参数 name 不为空，则替换掉 item 参数里面的 name 属性值
        result.update({"name": name})
    return result

if __name__ == "__main__":
    uvicorn.run(app="demo4_Request_body&path&params:app", host="127.0.0.1", port=80, reload=True)
