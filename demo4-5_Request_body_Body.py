from typing import Optional

import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item,
        user: User,
        # 主要作用：可以将单类型的参数成为 Request Body 的一部分，即从查询参数变成请求体参数
        # 和 Query、Path 提供的额外校验、元数据是基本一致的
        importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


if __name__ == "__main__":
    uvicorn.run(app="demo4-5_Request_body_Body:app", host="127.0.0.1", port=80, reload=True)