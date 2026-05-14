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
        rows = rows[:1]

    print(json.dumps(rows))


if __name__ == "__main__":
    main()
