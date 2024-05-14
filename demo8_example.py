from typing import Optional
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Body

app = FastAPI()


# 一、pydantic模型 增加示例
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    # 内部类，固定写法
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/demo1/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# Body内置的依赖项 增加示例
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/demo2/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(
            default=...,
            examples={
                "normal": {
                    "summary": "正常的栗子",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "会自动转换类型的栗子",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "校验失败的栗子",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run(app="demo8_example:app", host="127.0.0.1", port=8080, reload=True)
