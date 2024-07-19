from pydantic import BaseModel
from typing import List


class AggregationRequest(BaseModel):
    dt_from: str
    dt_upto: str
    group_type: str


class AggregationResponse(BaseModel):
    dataset: List[int]
    labels: List[str]
