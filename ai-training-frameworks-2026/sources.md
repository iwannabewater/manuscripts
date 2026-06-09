# Sources

作者：Winston
资料口径：截至 2026-05-04

## Method

本报告优先采用一手资料，包括项目官方仓库、官方文档、论文页面和技术报告。仓库公开元数据保存在 `data/repository-metadata.tsv`，用于辅助判断项目状态、许可和生态关注度；正文不按关注度排序，也不将仓库热度视为框架质量结论。

项目更新速度较快，正式选型前应复核目标版本、目标模型族、依赖硬件、license、权重许可和训练 recipe 的维护状态。纯推理服务框架不纳入本报告主体，仅在 RL rollout、导出验证或训练性能依赖中作为上下游组件出现。

## Primary Sources

### 从零训练与分布式底座

- NVIDIA Megatron-LM / Megatron Core: https://github.com/NVIDIA/Megatron-LM
- Megatron Core documentation: https://docs.nvidia.com/megatron-core/developer-guide/latest/
- DeepSpeed: https://github.com/deepspeedai/DeepSpeed
- DeepSpeed ZeRO documentation: https://deepspeed.readthedocs.io/en/stable/zero3.html
- PyTorch TorchTitan: https://github.com/pytorch/torchtitan
- TorchTitan paper: https://arxiv.org/abs/2410.06511
- NVIDIA NeMo: https://github.com/NVIDIA-NeMo/NeMo
- NVIDIA Megatron Bridge: https://github.com/NVIDIA-NeMo/Megatron-Bridge
- Megatron Bridge documentation: https://docs.nvidia.com/nemo/megatron-bridge/
- ByteDance Seed VeOmni: https://github.com/ByteDance-Seed/VeOmni
- VeOmni paper: https://arxiv.org/abs/2508.02317
- Hugging Face Nanotron: https://github.com/huggingface/nanotron
- Nanotron documentation: https://huggingface.co/docs/transformers/community_integrations/nanotron
- ColossalAI: https://github.com/hpcaitech/ColossalAI
- EleutherAI GPT-NeoX: https://github.com/EleutherAI/gpt-neox
- Databricks LLM Foundry: https://github.com/mosaicml/llm-foundry
- LitGPT: https://github.com/Lightning-AI/litgpt
- Meta Lingua: https://github.com/facebookresearch/lingua

### SFT、LoRA 与偏好优化

- Hugging Face Transformers: https://github.com/huggingface/transformers
- Hugging Face Accelerate: https://github.com/huggingface/accelerate
- Hugging Face PEFT: https://github.com/huggingface/peft
- PEFT documentation: https://huggingface.co/docs/peft
- Hugging Face TRL: https://github.com/huggingface/trl
- TRL documentation: https://huggingface.co/docs/trl
- PyTorch torchtune: https://github.com/pytorch/torchtune
- torchtune documentation: https://docs.pytorch.org/torchtune/
- Axolotl documentation: https://docs.axolotl.ai/
- LlamaFactory: https://github.com/hiyouga/LLaMA-Factory
- LlamaFactory paper: https://arxiv.org/abs/2403.13372
- ModelScope ms-swift: https://github.com/modelscope/ms-swift
- Unsloth: https://github.com/unslothai/unsloth
- XTuner: https://github.com/InternLM/xtuner
- Llama Cookbook: https://github.com/meta-llama/llama-cookbook
- AllenAI open-instruct: https://github.com/allenai/open-instruct
- Open Thoughts: https://github.com/open-thoughts/open-thoughts

### RL 后训练与 rollout 组件

- verl: https://github.com/verl-project/verl
- HybridFlow paper: https://arxiv.org/abs/2409.19256
- OpenRLHF: https://github.com/OpenRLHF/OpenRLHF
- NeMo RL: https://github.com/NVIDIA-NeMo/RL
- NVIDIA NeMo RL technical blog: https://developer.nvidia.com/blog/reinforcement-learning-with-nvidia-nemo-rl-reproducing-a-deepscaler-recipe-using-grpo/
- AReaL: https://github.com/inclusionAI/AReaL
- slime: https://github.com/THUDM/slime
- slime documentation: https://thudm.github.io/slime/
- vLLM: https://github.com/vllm-project/vllm
- SGLang: https://github.com/sgl-project/sglang
- Liger Kernel: https://github.com/linkedin/Liger-Kernel
- FlashAttention: https://github.com/Dao-AILab/flash-attention
- xFormers: https://github.com/facebookresearch/xformers
- torchao: https://github.com/pytorch/ao

### 多模态与视觉语言模型

- LLaVA: https://github.com/haotian-liu/LLaVA
- LLaVA-NeXT: https://github.com/LLaVA-VL/LLaVA-NeXT
- InternVL: https://github.com/OpenGVLab/InternVL
- VILA: https://github.com/NVlabs/VILA
- Qwen3-VL: https://github.com/QwenLM/Qwen3-VL
- OpenMMLab MMEngine: https://github.com/open-mmlab/mmengine
- OpenMMLab MMPreTrain: https://github.com/open-mmlab/mmpretrain

### 图像与视频生成训练

- Hugging Face Diffusers: https://github.com/huggingface/diffusers
- Diffusers training documentation: https://huggingface.co/docs/diffusers/en/training/overview
- kohya-ss sd-scripts: https://github.com/kohya-ss/sd-scripts
- SimpleTuner: https://github.com/bghira/SimpleTuner
- ai-toolkit: https://github.com/ostris/ai-toolkit
- OneTrainer: https://github.com/Nerogar/OneTrainer
- diffusion-pipe: https://github.com/tdrussell/diffusion-pipe
- musubi-tuner: https://github.com/kohya-ss/musubi-tuner
- Open-Sora: https://github.com/hpcaitech/Open-Sora
- Open-Sora 2.0 paper: https://arxiv.org/abs/2503.09642
- Open-Sora-Plan: https://github.com/PKU-YuanGroup/Open-Sora-Plan
- HunyuanVideo: https://github.com/Tencent-Hunyuan/HunyuanVideo
- HunyuanVideo paper: https://arxiv.org/abs/2412.03603
- Wan: https://github.com/Wan-Video/Wan2.1
- Wan technical report: https://arxiv.org/abs/2503.20314
- CogVideo: https://github.com/zai-org/CogVideo
- LTX-Video: https://github.com/Lightricks/LTX-Video
- NVIDIA Cosmos: https://github.com/NVIDIA/Cosmos
- SkyReels-V2: https://github.com/SkyworkAI/SkyReels-V2
- Infinity: https://github.com/FoundationVision/Infinity
