# Sources

## Scope

本文档面向希望从 0 到 1 系统掌握 ms-swift 的工程师和研究者，目标是解释框架的整体逻辑、训练链路、源码结构、参数体系、后训练与规模化路线。本文不是官方文档替代品，也不覆盖每一个模型专属参数。

源码与正文核对日期：2026-05-19。稳定发布版于 2026-06-09 再次复核。

## Primary Sources

1. ModelScope `modelscope/ms-swift` GitHub repository
   - URL: https://github.com/modelscope/ms-swift
   - Snapshot method: shallow clone of the official repository at the commit below
   - Main commit checked: `7dd6b0e7be14796a600e7099e6b2f0c23ce91298`
   - Commit date: 2026-05-19 19:30:34 +0800
   - Usage: README 当前能力、源码目录、CLI 路由、pipeline、trainer、RL trainer、Megatron-SWIFT 目录。

2. PyPI `ms-swift`
   - URL: https://pypi.org/project/ms-swift/
   - Version checked: `4.2.1`
   - Release date on PyPI: 2026-05-17
   - Usage: 抓取日稳定包版本、安装命令、Python requirement、extras。

3. GitHub Releases
   - Release page at capture time: https://github.com/modelscope/ms-swift/releases/tag/v4.2.1
   - Major release page checked: https://github.com/modelscope/ms-swift/releases/tag/v4.2.0
   - Usage: 抓取日稳定发布、v4.2.0 新特性与变更口径。

## Release Recheck

- 2026-06-09 复核：最新稳定版为 `v4.2.3`，发布于 2026-05-31。
- Release: https://github.com/modelscope/ms-swift/releases/tag/v4.2.3
- 正文源码路径与参数说明仍对应 commit `7dd6b0e`；新版本能力应以 `v4.2.3` 文档和迁移说明为准。

4. Swift ReadTheDocs Chinese latest
   - URL: https://swift.readthedocs.io/zh-cn/latest/
   - Version label observed: `swift 4.3.0.dev0`
   - Usage: 安装、命令参数、预训练与微调、GRPO、Megatron-SWIFT、自定义模型/数据/架构说明。

5. SWIFT paper on arXiv
   - URL: https://arxiv.org/abs/2408.05517
   - Version checked: v4, last revised 2025-05-19
   - Usage: 框架论文口径、设计动机、学术引用。

6. AAAI Proceedings
   - URL: https://ojs.aaai.org/index.php/AAAI/article/view/35383
   - Published: 2025-04-11
   - DOI: https://doi.org/10.1609/aaai.v39i28.35383
   - Usage: AAAI 2025 发表信息和正式引用。

## Upstream Files Inspected

The following paths are relative to `modelscope/ms-swift` at commit `7dd6b0e7be14796a600e7099e6b2f0c23ce91298`:

- `README_CN.md`
- `setup.py`
- `swift/cli/main.py`
- `swift/cli/sft.py`
- `swift/pipelines/train/sft.py`
- `swift/trainers/trainer.py`
- `swift/trainers/arguments.py`
- `swift/rlhf_trainers/*.py`
- `docs/source/GetStarted/SWIFT-installation.md`
- `docs/source/Instruction/Command-line-parameters.md`
- `docs/source/Instruction/Pre-training-and-Fine-tuning.md`
- `docs/source/Instruction/GRPO/GetStarted/GRPO.md`
- `docs/source/Megatron-SWIFT/Quick-start.md`
- `docs/source/Megatron-SWIFT/Mcore-Bridge.md`
- `docs/source/Customization/Architecture.md`
- `docs/source/Customization/Custom-dataset.md`
- `docs/source/Customization/Custom-model.md`

## Boundaries

- README 中 “600+ text-only / 400+ multimodal / 150+ datasets” 等数量按官方当前描述记录；没有重新逐项验算每个模型和数据集的可运行性。
- ReadTheDocs latest 标示为 4.3.0.dev0，可能包含未进入 PyPI 稳定版的开发中内容；本文在版本口径中单独标注。
- 本文重绘架构图和流程图用于解释，不复刻官方图片。
- 本文不提供硬件基准复测，不声称任何速度或显存数据超过官方给出的口径。
