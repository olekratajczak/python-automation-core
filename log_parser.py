from typing import List

ERROR_KEYWORDS = ["ERROR", "FAIL", "CRITICAL"]

def load_logs(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()

def find_errors(lines: List[str]) -> List[str]:
    errors = []

    for line in lines:
        for keyword in ERROR_KEYWORDS:
            if keyword in line:
                errors.append(line.strip())
                break
    
    return errors

def generate_report(errors: List[str]) -> None:
    print("=== LOG ANALYSIS REPORT ===")

    if not errors:
        print("No errors found")
        return
    
    print(f"Errors found: {len(errors)}")
    for error in errors:
        print(f"- {error}")

def main() -> None:
    logs = load_logs("logs/system.log")
    errors = find_errors(logs)
    generate_report(errors)

if __name__ == "__main__":
    main()