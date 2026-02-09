from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import PlainTextResponse

app = FastAPI()


class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None


@app.post("/two-sum", response_class=PlainTextResponse)
def two_sum_api(request: TwoSumRequest):
    result = two_sum(request.nums, request.target)
    if result is None:
        raise HTTPException(status_code=400, detail="No valid pair found")
    return f"{result[0]} {result[1]}"
