from typing import Optional
import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()

# 提出疑问：函数参数命名为 accept_encoding 为什么能识别到 Accept-Encoding？
# 首先，Accept-Encoding 这种变量名在 Python 是无效的
# 因此， Header 默认情况下，会用下划线 _ 代替 - ，这就是 convert_underscores 参数的作用
# 重点：HTTP Header 是不区分大小写的，所以写 accept_encoding 还是 Accept_Encoding 是一样效果的
@app.get("/demo1/")
async def read_items(accept_encoding: Optional[str] = Header(None)):
    return {"Accept-Encoding": accept_encoding}



# 设置 Response Header
from starlette.responses import JSONResponse


@app.get("/demo2/")
def Login():
    content = {
        "name": "poloyy",
        "age": 10
    }
    response = JSONResponse(content=content)
    token = {
        "x-token-name": "token",
        "x-token-value": "test_header"
    }
    # 设置 Header
    response.init_headers(token)
    return response


if __name__ == "__main__":
    uvicorn.run(app="demo11_Header:app", host="127.0.0.1", port=8080, reload=True)
