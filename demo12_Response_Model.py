from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# 路径操作关于响应模型的参数
# response_model: Any = Default(None)
# response_model_include: Optional[IncEx] = None,
# response_model_exclude: Optional[IncEx] = None,
# response_model_by_alias: bool = True,
# response_model_exclude_unset: bool = False,
# response_model_exclude_defaults: bool = False,
# response_model_exclude_none: bool = False,

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


# demo1 请求模型和响应模型都是同一个 Pydantic Model,将输出数据限制为 model 的数据
@app.post("/demo1/", response_model=Item)
async def create_item(item: Item):
    return item


# demo2========================================
# 区分请求模型和响应模型的栗子
# 需求
# 假设一个注册功能
# 输入账号、密码、昵称、邮箱，注册成功后返回个人信息
# 正常情况下不应该返回密码，所以请求体和响应体肯定是不一样的
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/demo2/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# demo3========================================
# response_model_include 的栗子
# 结合上面注册功能的栗子：请求要密码，响应不要密码
class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/demo3/", response_model=User, response_model_include={"username", "email", "full_name"})
async def create_user(user: User):
    return user


# demo4========================================
# 有时候数据会有默认值，比如数据库中设置了默认值，不想返回这些默认值怎么办？
# response_model_exclude_unset=True  设置该参数后就不会返回默认值，只会返回实际设置的值，假设没设置值，则不返回该字段
class Item(BaseModel):
    name: str
    price: float
    # 下面三个字段有默认值
    description: Optional[str] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/demo4/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    # 从上面 items 字典中，根据 item_id 取出对应的值并返回
    return items[item_id]


if __name__ == "__main__":
    uvicorn.run(app="demo12_Response_Model:app", host="127.0.0.1", port=8080, reload=True)
