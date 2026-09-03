from pathlib import Path
import json
import sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

finding_schema = json.loads((SCHEMAS / "review-finding.schema.json").read_text(encoding="utf-8"))
history_schema = json.loads((SCHEMAS / "history-note.schema.json").read_text(encoding="utf-8"))


def validate_file(path: Path, schema: dict):
    data = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        print(f"[FAIL] {path}")
        for e in errors:
            print(" -", e.message)
        return False
    print(f"[PASS] {path}")
    return True


ok = True
for path in (ROOT / "reviews").rglob("*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if "findings" not in data:
        ok &= validate_file(path, finding_schema)

for path in (ROOT / "history" / "notes").rglob("*.json"):
    ok &= validate_file(path, history_schema)

# Template must stay valid.
ok &= validate_file(ROOT / "templates" / "review-finding.json", finding_schema)

# Gate rule for chapter-review-shaped files.
for path in (ROOT / "reviews").rglob("*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if "findings" not in data:
        continue
    unresolved = [
        f for f in data["findings"]
        if f.get("severity") in {"CRITICAL", "MUST_FIX"}
        and f.get("status", "OPEN") not in {"ACCEPTED", "REJECTED", "RESOLVED"}
    ]
    if unresolved and data.get("gate") in {"PASS", "PASS_WITH_NOTES"}:
        print(f"[FAIL] {path}: unresolved critical/must-fix findings but gate={data.get('gate')}")
        ok = False

sys.exit(0 if ok else 1)
