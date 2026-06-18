# build-vllm

Pre-built CPU wheels for [vLLM](https://github.com/vllm-project/vllm), across
Python, operating systems, and CPU architectures.

## Installation

CPU wheels are published to Astral's dedicated CPU index. Each wheel has a
`+cpu` local version suffix, such as `vllm==0.22.0+cpu`.

Pre-built wheels are available on
[Astral's package indexes](https://wheels.astral.sh/index.html).
To install a CPU build:

```console
$ uv add vllm --index astral-cpu=https://wheels.astral.sh/simple/cpu/
```

This configures the index and uses it as the source for `vllm`:

```toml
[tool.uv.sources]
vllm = { index = "astral-cpu" }

[[tool.uv.index]]
name = "astral-cpu"
url = "https://wheels.astral.sh/simple/cpu/"
```

Or, with `uv pip`:

```console
$ uv pip install --index https://wheels.astral.sh/simple/cpu/ vllm
```

## Supported versions

Wheels are available for the following `vllm` versions:

- [`0.22.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.22.0)
- [`0.21.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.21.0)
- [`0.20.2`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.20.2)
- [`0.20.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.20.1)
- [`0.20.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.20.0)
- [`0.19.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.19.1)
- [`0.19.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.19.0)
- [`0.18.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.18.1)
- [`0.18.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.18.0)
- [`0.17.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.17.1)
- [`0.17.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.17.0)
- [`0.16.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.16.0-r1)
- [`0.15.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.15.1-r1)
- [`0.15.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.15.0)
- [`0.14.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.14.1)
- [`0.14.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.14.0)
- [`0.13.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.13.0)
- [`0.12.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.12.0)
- [`0.11.2`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.11.2)
- [`0.11.1`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.11.1)
- [`0.11.0`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.11.0)
- [`0.10.2`](https://github.com/astral-sh-build/build-vllm/releases/tag/v0.10.2)

The latest release, vLLM 0.22.0, supports the following combinations:

| Operating system | CPU architecture    | Python    |
| ---------------- | ------------------- | --------- |
| Linux            | `x86_64`, `aarch64` | 3.10–3.14 |
| macOS            | `arm64`             | 3.10–3.14 |

## License

build-vllm is licensed under the [Apache License, Version 2.0](LICENSE).

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
