from tools.data_validator import validate_fields


def test_missing_required_fields() -> None:
    data = {
        "device_id": "ABC123"
    }

    errors = validate_fields(data)

    assert len(errors) > 0
    assert "Missing field: status" in errors
    assert "Missing field: temperature" in errors
    assert "Missing field: battery" in errors



def test_battery_out_of_range() -> None:
    data = {
        "device_id": "ABC123",
        "status": "ACTIVE",
        "temperature": 20.0,
        "battery": 150
    }

    errors = validate_fields(data)

    assert "Battery value out of range (0-100)" in errors



def test_valid_data() -> None:
    data = {
        "device_id": "ABC123",
        "status": "ACTIVE",
        "temperature": 20.0,
        "battery": 80
    }

    errors = validate_fields(data)

    assert errors == []