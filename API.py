from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int

class TwoSumResponse(BaseModel):
    indices: List[int]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

@app.post("/two-sum", response_model=TwoSumResponse)
def two_sum_api(request: TwoSumRequest):
    result = two_sum(request.nums, request.target)
    if result is None:
        raise HTTPException(status_code=400, detail="No valid pair found")
    return {"indices": result}
