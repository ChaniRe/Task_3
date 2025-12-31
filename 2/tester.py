import json
import os
from number2 import app # מייבא את האפליקציה מהקובץ שלך
from typer.testing import CliRunner

runner = CliRunner()

def test_my_code():
    # 1. בדיקת הוספה
    print("Testing 'add' command...")
    payload = json.dumps({"id": 1, "task": "success", "status": "working"})
    result = runner.invoke(app, ["add", payload])
    print(f"Output: {result.stdout}")

    # 2. בדיקת קריאה
    print("\nTesting 'getrecent' command...")
    result = runner.invoke(app, ["getrecent"])
    print(f"Data from file:\n{result.stdout}")

if __name__ == "__main__":
    test_my_code()