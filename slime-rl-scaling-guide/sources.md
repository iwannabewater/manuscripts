# Sources

## Research Scope

本文基于 2026-05-06 抓取的公开资料撰写，主要来源为 THUDM/slime 官方仓库、官方文档、release notes、源码文件和 LMSYS 技术博客。本文没有在本地执行多 GPU 训练，所有启动命令、参数名称和实现路径均按官方仓库与源码复核；生产环境仍需按实际 GPU、驱动、CUDA、NCCL、模型规模和数据任务做验证。

## Snapshot

- Repository: <https://github.com/THUDM/slime>
- Default branch: `main`
- Captured commit: `82007faf4b398abd32bd8e07f9638f6cfeb70729`
- Commit date: 2026-05-06 14:36:18 +0800
- Commit subject: `Only allow --allgather-cp for DSA model (#1891)`
- Latest release at capture time: `v0.2.4`, published 2026-03-29
- Research method: official repository clone, official documentation capture, source-code review and release metadata review during this writing session.

## Primary Documentation

- THUDM/slime README: <https://github.com/THUDM/slime>
- Official documentation index: <https://thudm.github.io/slime/>
- Quick Start: <https://github.com/THUDM/slime/blob/main/docs/en/get_started/quick_start.md>
- Usage: <https://github.com/THUDM/slime/blob/main/docs/en/usage.md>
- Customization: <https://github.com/THUDM/slime/blob/main/docs/en/usage/customization.md>
- Q&A: <https://github.com/THUDM/slime/blob/main/docs/en/qa.md>
- SGLang configuration: <https://github.com/THUDM/slime/blob/main/docs/en/usage/sglang_config.md>
- Fault tolerance: <https://github.com/THUDM/slime/blob/main/docs/en/usage/fault_tolerance.md>
- Low precision: <https://github.com/THUDM/slime/blob/main/docs/en/usage/low_precision.md>
- On-policy distillation: <https://github.com/THUDM/slime/blob/main/docs/en/usage/on_policy_distillation.md>
- Speculative decoding: <https://github.com/THUDM/slime/blob/main/docs/en/usage/speculative_decoding.md>
- PD disaggregation: <https://github.com/THUDM/slime/blob/main/docs/en/usage/pd_disaggregation.md>
- Reproducibility: <https://github.com/THUDM/slime/blob/main/docs/en/usage/reproducibility.md>
- Introducing slime: <https://github.com/THUDM/slime/blob/main/docs/en/blogs/introducing_slime.md>
- Release v0.1.0 blog: <https://github.com/THUDM/slime/blob/main/docs/en/blogs/release_v0.1.0.md>
- Release v0.2.4: <https://github.com/THUDM/slime/releases/tag/v0.2.4>
- LMSYS blog, slime: <https://lmsys.org/blog/2025-07-09-slime/>

## Source Files Reviewed

- `train.py`
- `train_async.py`
- `slime/ray/rollout.py`
- `slime/ray/placement_group.py`
- `slime/ray/actor_group.py`
- `slime/backends/megatron_utils/actor.py`
- `slime/backends/megatron_utils/loss.py`
- `slime/backends/megatron_utils/update_weight/update_weight_from_distributed.py`
- `slime/backends/megatron_utils/update_weight/update_weight_from_tensor.py`
- `slime/backends/megatron_utils/update_weight/common.py`
- `slime/backends/sglang_utils/sglang_engine.py`
- `slime/backends/sglang_utils/arguments.py`
- `slime/backends/sglang_utils/sglang_config.py`
- `slime/rollout/sglang_rollout.py`
- `slime/rollout/data_source.py`
- `slime/utils/types.py`
- `slime/utils/arguments.py`
- `slime/utils/ppo_utils.py`
- `scripts/run-glm4-9B.sh`
- `scripts/run-qwen3-4B.sh`
- `scripts/models/glm4-9B.sh`
- `scripts/models/qwen3-4B.sh`

## Boundary Notes

- 本文不是 slime 官方文档的翻译，而是基于源码和官方资料重组后的工程读本。
- 本文不覆盖每一个模型脚本和所有 CLI 参数，参数完整定义应以当前源码为准。
- 性能数字仅引用官方 release/blog 中有明确语境的描述，不做跨模型、跨硬件外推。
- GitHub star、fork、release 和 HEAD 信息具有时效性，本文只保留抓取日口径。
