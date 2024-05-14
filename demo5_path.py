from fastapi import FastAPI, Path, Query
from typing import Optional
import uvicorn

app = FastAPI()


# 元数据

# 路径参数始终是必需的，因为它必须是路径的一部分
# 所以，Path 的 default 参数值必须设为 ...

# 元数据不应该使用 alias来设置别名
# 因为路径参数并不能通过 参数名=value 的形式来传值，所以没有办法通过 alias = value 的方式给别名传值，最终将会报错

# 限制传参的int值大小
# # 大于
# gt: Optional[float] = None
#
# # 大于等于
# ge: Optional[float] = None
#
# # 小于
# lt: Optional[float] = None
#
# # 小于等于
# le: Optional[float] = None

@app.get("/number/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The IDsss", gt=10, le=20),
        name: str = None):
    return {"item_id": item_id, "name": name}


# Query 和 Path 综合使用
@app.get("/path_query/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., description="path", ge=1, lt=5, example=1),
        name: str,
        age: float = Query(..., description="query", gt=0.0, le=10)):
    return {"item_id": item_id, "age": age, "name": name}


if __name__ == "__main__":
    uvicorn.run(app="demo5_path:app", host="127.0.0.1", port=80, reload=True)
