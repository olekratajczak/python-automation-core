import json
from typing import Dict, List
from core.logger import setup_logger
from pathlib import Path

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
    logger = setup_logger(name="data_validator", log_file="reports/data_validator.log")

    BASE_DIR = Path(__file__).resolve().parents[1]  # root repo
    data = load_json(str(BASE_DIR / "data" / "sample.json"))

    errors = validate_fields(data)

    if errors:
        logger.error("Validation failed with %s error(s)", len(errors))
        for error in errors:
            logger.error("ERR: %s", error)
    else:
        logger.info("Data validation passed")

if __name__ == "__main__":
    main()