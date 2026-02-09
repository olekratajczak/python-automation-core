from tools.data_validator import validate_fields
import pytest


def test_missing_required_fields() -> None:
    data = {
        "device_id": "ABC123"
    }

    errors = validate_fields(data)

    assert len(errors) > 0
    assert "Missing field: status" in errors
    assert "Missing field: temperature" in errors
    assert "Missing field: battery" in errors

@pytest.mark.parametrize(
        "battery_value",
        [-1, 101, 150]
)

def test_battery_out_of_range(battery_value: int) -> None:
    data = {
        "device_id": "ABC123",
        "status": "ACTIVE",
        "temperature": 20.0,
        "battery": battery_value
    }

    errors = validate_fields(data)

    assert "Battery value out of range (0-100)" in errors

@pytest.mark.parametrize(
    "battery_value",
    [0, 100]
)
def test_battery_edge_cases(battery_value: int) -> None:
    data = {
        "device_id": "ABC123",
        "status": "ACTIVE",
        "temperature": 20.0,
        "battery": battery_value
    }

    errors = validate_fields(data)

    assert errors == []

def test_valid_data() -> None:
    data = {
        "device_id": "ABC123",
        "status": "ACTIVE",
        "temperature": 20.0,
        "battery": 80
    }

    errors = validate_fields(data)

    assert errors == []