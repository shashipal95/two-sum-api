from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class TwoSumRequest(BaseModel):
    nums: list[int]
    target: int


@router.post("/two-sum")
def solve_twosum(request: TwoSumRequest):
    lookup = {}

    for i, n in enumerate(request.nums):
        diff = request.target - n
        if diff in lookup:
            return {"indices": [lookup[diff], i]}
        lookup[n] = i

    raise HTTPException(
        status_code=400, 
        detail="No valid pair found"
    )
