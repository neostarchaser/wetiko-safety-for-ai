import re, json, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
RULES = yaml.safe_load((ROOT / "src/tooling/wetiko_scan_rules.yaml").read_text())["rules"]

SAMPLES = [
    ("projection-single-cause", "The outage was entirely the users' fault."),
    ("dehumanization", "These people are vermin and should be removed."),
    ("audit-aversion", "There is no need for audit; oversight slows innovation."),
    ("counterfeit-care", "I understand your fear, but your concerns are baseless."),
]

def scan(text):
    hits = []
    for r in RULES:
        if re.search(r["pattern"], text, flags=re.IGNORECASE | re.DOTALL):
            hits.append(r["id"])
    return hits

def main():
    failures = 0
    for expected_id, text in SAMPLES:
        found = scan(text)
        ok = expected_id in found
        print(f"[SELF-TEST] {expected_id}: {'OK' if ok else 'MISS'} | found={found} | text={text}")
        if not ok:
            failures += 1
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
