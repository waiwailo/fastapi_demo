from typing import Optional

import uvicorn
from fastapi import FastAPI, Body
from typing import List, Tuple, Set

app = FastAPI()


# 假设里面的元素传了非 int 且无法自动转换成 int
# typing 的 List、Set、Tuple 都会指定里面参数的数据类型
# 而 FastAPI 会对声明了数据类型的数据进行数据校验，所以会针对序列里面的参数进行数据校验
# 如果校验失败，会报一个友好的错误提示
@app.put("/demo1/{item_id}")
async def update_item(
        list_: List[int] = Body(...),
        tuple_: Tuple[int] = Body(...),
        set_: Set[int] = Body(...),
):
    results = {"list_": list_, "tuple_": tuple_, "set_": set_}
    return results


# 用 Python 自带的 list、set、tuple 类，是无法指定序列里面参数的数据类型，所以 FastAPI 并不会针对里面的参数进行数据校验
# 要充分利用 FastAPI 的优势，强烈建议用 typing 的 List、Set、Tuple 来表示列表、集合、元组类型
@app.put("/demo2/{item_id}")
async def update_item(
        list_: list = Body(...),
        tuple_: tuple = Body(...),
        set_: set = Body(...),
):
    results = {"list_": list_, "tuple_": tuple_, "set_": set_}
    return results


if __name__ == "__main__":
    uvicorn.run(app="demo6_typing:app", host="127.0.0.1", port=80, reload=True)
