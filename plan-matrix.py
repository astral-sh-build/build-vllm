# /// script
# requires-python = ">=3.12"
# ///

import json
import os

# Supported Python versions for vLLM CPU builds.
PYTHON_VERSIONS = ["cp310", "cp311", "cp312", "cp313", "cp314"]

# Supported operating systems/runners.
RUNNERS = [
    ("depot-ubuntu-24.04", "linux"),
    ("depot-ubuntu-24.04-arm", "linux"),
    ("macos-latest", "macos"),
]

# Exercise one Linux and one macOS build on pull requests by default.
PR_SMOKE_RUNNERS = {"depot-ubuntu-24.04", "macos-latest"}
PR_SMOKE_PYTHON = PYTHON_VERSIONS[-1]


def main() -> None:
    rows = []
    for runner, platform in RUNNERS:
        for python_version in PYTHON_VERSIONS:
            row = {
                "RUNNER": runner,
                "python-version": python_version,
                "platform": platform,
            }
            rows.append(row)

    if os.environ.get("LIMIT_MATRIX") == "1":
        rows = [
            row
            for row in rows
            if row["RUNNER"] in PR_SMOKE_RUNNERS
            and row["python-version"] == PR_SMOKE_PYTHON
        ]

    print(json.dumps(rows))


if __name__ == "__main__":
    main()
