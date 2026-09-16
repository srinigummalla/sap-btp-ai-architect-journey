"""Run known learning cases. No model call, network access or third-party packages."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", action="store_true")
    args = parser.parse_args()
    if args.reference:
        from reference_classifier import classify
    else:
        from student_classifier import classify
    root = Path(__file__).resolve().parents[1]
    cases = json.loads((root / "data/cases.json").read_text(encoding="utf-8"))
    expected = json.loads((root / "data/expected_results.json").read_text(encoding="utf-8"))
    passed = 0
    for case in cases:
        try:
            actual = classify(case)
        except NotImplementedError as ex:
            print(f"Exercise unfinished: {ex}")
            return 2
        wanted = expected[case["case_id"]]
        ok = actual == wanted
        passed += int(ok)
        print(f"{case['case_id']} {'PASS' if ok else 'FAIL'} {actual['outcome']} {actual['flags']}")
        if not ok:
            print(f"  Expected: {wanted}")
    mode = "REFERENCE" if args.reference else "STUDENT"
    print(f"{mode}: {passed}/{len(cases)} learning cases passed")
    print("Known synthetic cases only; not production SAP validation or an AI benchmark.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
