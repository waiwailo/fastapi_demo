from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 自定义模型类 1
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# 自定义模型类 2
class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Item,  # 指定第一个 Model 类型
                      user: User):  # 指定第二个 Model 类型
    results = {
        "item_id": item_id,
        "item": item,
        "user": user
    }
    return results

# 传参
# {
#     "item":{
#         "name": "wzy",
#         "description": "描述",
#         "price":1,
#         "tax":2
#     },
#     "user":{
#         "username": "wzy",
#         "full_name":"wang"
#     }
# }



if __name__ == "__main__":
    uvicorn.run(app="demo4-4_Request_body_Multiplec:app", host="127.0.0.1", port=80, reload=True)
