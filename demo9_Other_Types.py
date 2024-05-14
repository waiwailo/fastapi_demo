import uuid
from datetime import datetime, time, timedelta
from decimal import Decimal
from typing import Optional
from uuid import UUID
import uvicorn
from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(

        item_id: UUID,
        start_datetime: Optional[datetime] = Body(None),
        end_datetime: Optional[datetime] = Body(None),
        repeat_at: Optional[time] = Body(None),
        process_after: Optional[timedelta] = Body(None),
        address: Optional[frozenset] = Body(None),
        computer: Optional[bytes] = Body(None),
        age: Optional[Decimal] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
        "address": address,
        "computer": computer,
        "age": age,
    }


if __name__ == "__main__":
    print(uuid.uuid1())
    uvicorn.run(app="demo9_Other_Types:app", host="127.0.0.1", port=8080, reload=True)