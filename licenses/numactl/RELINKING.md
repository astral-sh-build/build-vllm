# libnuma relinking information

Linux vLLM CPU wheels may contain a dynamically linked copy of `libnuma` from
the numactl project. `libnuma` is licensed under the GNU Lesser General Public
License version 2.1.

Recipients may replace or relink the LGPL-covered `libnuma` component with a
modified compatible build of libnuma. One practical route is to unpack the
wheel, replace the auditwheel-managed `libnuma` shared object under the
package's `.libs` directory with an ABI-compatible build, and repack the wheel.
Recipients may also rebuild vLLM from source against their chosen libnuma build.

The corresponding sources are available from:

- vLLM: https://github.com/vllm-project/vllm
- numactl/libnuma: https://github.com/numactl/numactl
