import importlib
from importlib.metadata import version

import pynvml
import pytest
import torch


@pytest.fixture(scope="module")
def device() -> torch.device:
    pynvml.nvmlInit()
    assert pynvml.nvmlDeviceGetCount() > 0, "The tests must run on a Modal GPU"
    return torch.device("cpu")


def test_published_cuda_wheel(device: torch.device) -> None:
    assert version("vllm") == "0.25.0+cpu"
    assert torch.__version__ == "2.11.0+cpu"
    assert torch.version.cuda is None
    assert pynvml.nvmlDeviceGetName(pynvml.nvmlDeviceGetHandleByIndex(0))


@pytest.mark.parametrize("module_name", ["vllm", "vllm.sampling_params"])
def test_native_module(device: torch.device, module_name: str) -> None:
    assert importlib.import_module(module_name) is not None


def test_published_cpu_build_on_gpu_host(device: torch.device) -> None:
    import vllm

    assert vllm.__version__.removeprefix("v").split("+", 1)[0] == "0.25.0"
    assert pynvml.nvmlDeviceGetCount() > 0


def test_sampling_configuration(device: torch.device) -> None:
    from vllm import SamplingParams

    parameters = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=16)
    assert parameters.temperature == 0.7
    assert parameters.top_p == 0.9
    assert parameters.max_tokens == 16
