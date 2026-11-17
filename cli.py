"""Write a portable study/report bundle for offline Grok-HedgeOps review."""
import argparse
import json
from pathlib import Path
from market_model import evaluate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("study")
    parser.add_argument("--output")
    args = parser.parse_args()
    study = json.loads(Path(args.study).read_text())
    bundle = {"study": study, "report": evaluate(study)}
    content = json.dumps(bundle, indent=2, allow_nan=False)
    if args.output:
        with open(args.output, "x", encoding="utf-8") as stream:
            stream.write(content)
    else:
        print(content)

if __name__ == "__main__":
    main()
