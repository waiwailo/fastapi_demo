from typing import Optional

import uvicorn
from fastapi import FastAPI, Body
from pydantic import Field, BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        default=None,
        title="标题",
        description="描述",
        max_length=5
    )
    price: float = Field(..., gt=0, description="需要大于0")
    tax: Optional[float] = None


@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run(app="demo4-2-2_Request_body_Pydantic_Fields:app", host="127.0.0.1", port=80, reload=True)