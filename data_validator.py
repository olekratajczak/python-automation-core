import json
from typing import Dict, List

REQUIRED_FIELDS = ["device_id", "status", "temperature", "battery"]

def load_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def validate_fields(data: Dict) -> List[str]:
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing field: {field}")
        
    if "temeperature" in data and not isinstance(data["temperature"], (int, float)):
        errors.append("Temperature must be a number.")

    if "battery" in data and not (0 <= data["battery"] <= 100):
        errors.append("Battery value out of range (0-100)")

    return errors

def main() -> None:
    data = load_json("data/sample.json")
    errors = validate_fields(data)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Data validation passed")

if __name__ == "__main__":
    main()