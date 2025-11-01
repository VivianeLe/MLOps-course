from enum import Enum
from pydantic import BaseModel
from fastapi import APIRouter

calculation_router = APIRouter(prefix="/calculation")

class Method(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

class CalculateRequest(BaseModel):
    method: Method
    num1: float
    num2: float

class CalculateResponse(BaseModel):
    result: float

@calculation_router.post("/calculate", response_model=CalculateResponse)
def calculate(request: CalculateRequest) -> CalculateResponse:
    if request.method == Method.add:
        result = request.num1 + request.num2
    elif request.method == Method.subtract:
        result = request.num1 - request.num2
    elif request.method == Method.multiply:
        result = request.num1 * request.num2
    elif request.method == Method.divide:
        result = request.num1 / request.num2
    else:
        raise ValueError(f"Invalid method: {request.method}")
    return CalculateResponse(result=result)