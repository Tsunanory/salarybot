import pytest
from app.aggregator import aggregate_salaries


def test_aggregate_salaries_month():
    result = aggregate_salaries("2022-01-01T00:00:00", "2022-12-31T23:59:00", "month")
    assert "dataset" in result
    assert "labels" in result
    assert len(result["dataset"]) > 0
    assert len(result["labels"]) > 0


def test_aggregate_salaries_day():
    result = aggregate_salaries("2022-01-01T00:00:00", "2022-01-31T23:59:00", "day")
    assert "dataset" in result
    assert "labels" in result
    assert len(result["dataset"]) > 0
    assert len(result["labels"]) > 0


def test_aggregate_salaries_hour():
    result = aggregate_salaries("2022-01-01T00:00:00", "2022-01-01T23:59:00", "hour")
    assert "dataset" in result
    assert "labels" in result
    assert len(result["dataset"]) > 0
    assert len(result["labels"]) > 0


def test_invalid_group_type():
    with pytest.raises(ValueError):
        aggregate_salaries("2022-01-01T00:00:00", "2022-12-31T23:59:00", "invalid")
