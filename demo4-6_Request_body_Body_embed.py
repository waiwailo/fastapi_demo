from typing import Optional

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
# 当函数只有一个参数指定了 Pydantic Model 且没有其他 Body 参数时，传参的时候请求体可以不指定参数名
# 需要给 item 指定请求体的字段名时，就是通过 embed 参数

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        # 将 embed 设置为 True
        item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    uvicorn.run(app="demo4-demo4-6_Request_body_Body_embed:app", host="127.0.0.1", port=80)