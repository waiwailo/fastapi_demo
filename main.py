import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


# 路径参数
@app.get("/get/{username}")
async def root(username):
    return {"message": f"Hello {username}，欢迎登录"}


# 限定类型的路径参数
@app.get("/items/{item_id}/article/{num:int}")
async def path_test(item_id: str, num: int):
    return {"item_id": item_id, "num": num}


# 路径转换器
# 在路由路径中，{file_path:path} 使 file_path 能匹配包含任意数量斜杠的完整路径，而 {file_name:str} 或 {file_name} 在路径参数中不能包含斜杠。
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}




if __name__ == '__main__':
    # 启动服务器
    uvicorn.run(app="main:app", host="127.0.0.1", port=80, reload=True)
    # http://127.0.0.1/docs 查看文档
