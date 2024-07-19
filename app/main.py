from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .aggregator import aggregate_salaries

app = FastAPI()


class AggregationRequest(BaseModel):
    dt_from: str
    dt_upto: str
    group_type: str


class AggregationResponse(BaseModel):
    dataset: List[int]
    labels: List[str]


@app.post("/aggregate", response_model=AggregationResponse)
async def aggregate(request: AggregationRequest):
    try:
        result = aggregate_salaries(request.dt_from, request.dt_upto, request.group_type)
        return result
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

