from typing import Dict

from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 不使用 Pydantic的例子
@app.post("/demo")
async def read_item(var: dict):
    return {"var": var}


@app.post("/Dict/")
# 键为 str，值为 float ，使用 Dict 相比直接用 dict 的好处
# 声明为 Dict[str, float]，FastAPI 会对每一个键值对都做数据校验，校验失败会有友好的错误提示
async def create_index_weights(weights: Dict[str, float]):
    return weights


if __name__ == "__main__":
    uvicorn.run(app="demo4.4_Request_body:app", host="127.0.0.1", port=80, reload=True)
