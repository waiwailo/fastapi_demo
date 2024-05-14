from typing import List, Optional, Set, Dict, Tuple
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# FastApi(14) 路径操作函数参数的类型是一个嵌套 Pydantic Model 的使用场景


# 模型一
class Image(BaseModel):
    url: str
    name: str


# 模型二
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    # tags 虽然声明为 Set()，但在接口层面并没有集合这个概念，所以还是传数组 [ ] 格式哦，并不是传 { } 哦
    # 但是！集合的特性仍然会保留：去重
    tags: Set[str] = set()
    # Image 模型组成的列表类型
    image: Optional[List[Image]] = None


@app.post("/items/{item_id}")
async def update_item(
        item_id: int,
        # 声明类型为：嵌套模型的 Item
        item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run(app="demo7_Pydantic_Nest:app", host="127.0.0.1", port=8080, reload=True)
