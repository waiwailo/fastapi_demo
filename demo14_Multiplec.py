import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, EmailStr

app = FastAPI()


# 请求模型
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# 响应模型
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


# 数据库模型
class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


# 加密算法
def fake_password_hasher(password: str) -> str:
    return "supersecret" + password


# 数据库存储
def fake_save_user(user: UserIn):
    # 取出用户的密码进行加密
    hash_password = fake_password_hasher(user.password)
    # 转换为数据库模型
    userInDB = UserInDB(**user.dict(), hashed_password=hash_password)
    # 返回数据
    return userInDB


@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    # 创建用户，落库
    user_saved = fake_save_user(user)
    # 返回存储后的用户信息
    return user_saved

if __name__ == "__main__":
    uvicorn.run(app="19_extra_models:app", host="127.0.0.1", port=8080, reload=True)