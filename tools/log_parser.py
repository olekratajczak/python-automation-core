from typing import List
from core.logger import setup_logger
from pathlib import Path

ERROR_KEYWORDS = ["ERROR", "FAIL", "CRITICAL"]


def load_logs(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def find_errors(lines: List[str]) -> List[str]:
    errors: List[str] = []

    for line in lines:
        for keyword in ERROR_KEYWORDS:
            if keyword in line:
                errors.append(line.strip())
                break

    return errors


def main() -> None:
    logger = setup_logger(name="log_parser", log_file="reports/log_parser.log")

    logger.info("Starting log parsing")
    logs = load_logs("logs/system.log")
    logger.info("Loaded %s lines from log file", len(logs))

    errors = find_errors(logs)

    if errors:
        logger.error("Errors found: %s", len(errors))
        for err in errors:
            logger.error("ERR: %s", err)
    else:
        logger.info("No errors found")

    logger.info("Finished log parsing")


if __name__ == "__main__":
    main()