# 需要先导入 Query 库
from fastapi import Query
from fastapi import FastAPI
from typing import Optional, List
import uvicorn

app = FastAPI()


# 可选参数有默认值+长度最大为 10
@app.get("/demo/")
async def read_items(name: Optional[str] = Query(default=None, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if name:
        results.update({"name": name})
    return results


# 多条校验
@app.get("/demo2/")
async def read_items(name: Optional[str] = Query(default=None, min_length=3, max_length=10)):
    return {"name": name}


# 正则表达式校验
@app.get("/demo3/")
async def read_items(
        name: Optional[str] = Query(
            default=None,
            min_length=3,
            max_length=10,
            pattern="^小.*菠萝$"
        )):
    return {"name": name}


# 必传参数， 需要将 ... 赋值给 default 参数，FastAPI 就会知道这个参数是必传的
@app.get("/demo4")
async def read_items(name: Optional[str] = Query(default=..., max_length=10)):
    return {"name": name}


# List类型
# http://127.0.0.1/list?address=gz&address=sz
@app.get("/list")
async def read_item(address: Optional[List[str]] = Query([], max_length=2)):
    return {"address": address}


# List 类型的查询参数有多个默认值
@app.get("/list/default")
async def read_item(address: Optional[List[str]] = Query(["广州", "深圳"])):
    return {"address": address}


# 元数据
# Query 可以添加元数据相关信息，这些信息将包含在生成的 OpenAPI 中，并由文档用户界面和外部工具使用
# # 别名 定义了 alias，必须要用 alias 进行传参
# alias: Optional[str] = None
# # 标题
# title: Optional[str] = None
# # 描述
# description: Optional[str] = None
# # 是否弃用
# deprecated: Optional[bool] = None
#
# 元数据
# http://127.0.0.1/demo6/all/?name_alias_query=菠萝
@app.get("/demo6/all/")
async def read_items(
        name: Optional[str] = Query(
            default=None,
            min_length=2,
            max_length=50,
            pattern="^菠萝$",
            alias="name_alias_query",
            title="标题",
            description="很长很长的描述",
            deprecated=True,
        )
):
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run(app="demo3_Query:app", host="127.0.0.1", port=80, reload=True)
