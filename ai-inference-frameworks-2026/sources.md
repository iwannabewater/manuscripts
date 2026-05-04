# Sources

作者：Winston
资料口径：截至 2026-05-04

## Method

本报告优先采用项目官方仓库、官方文档、论文页面和技术报告。仓库公开元数据保存在 `data/repository-metadata.tsv`，用于辅助判断项目状态、许可和生态关注度；正文不按关注度排序，也不将仓库热度视为框架质量结论。

推理框架更新速度较快，正式选型前应复核目标版本、目标模型族、硬件形态、量化格式、license、权重许可、服务协议、观测能力和安全边界。训练框架、Agent 应用框架、评测平台、云厂商托管产品和向量数据库不纳入主体，仅在推理链路边界中作为上下游说明。

## Primary Sources

### 在线推理服务引擎

- vLLM: https://github.com/vllm-project/vllm
- vLLM documentation: https://docs.vllm.ai/
- Efficient Memory Management for Large Language Model Serving with PagedAttention: https://arxiv.org/abs/2309.06180
- SGLang: https://github.com/sgl-project/sglang
- SGLang documentation: https://docs.sglang.ai/
- SGLang paper: https://arxiv.org/abs/2312.07104
- NVIDIA TensorRT-LLM: https://github.com/NVIDIA/TensorRT-LLM
- TensorRT-LLM documentation: https://nvidia.github.io/TensorRT-LLM/
- Hugging Face Text Generation Inference: https://github.com/huggingface/text-generation-inference
- Text Generation Inference documentation: https://huggingface.co/docs/text-generation-inference
- LMDeploy: https://github.com/InternLM/lmdeploy
- LMDeploy documentation: https://lmdeploy.readthedocs.io/
- LightLLM: https://github.com/ModelTC/LightLLM
- Aphrodite Engine: https://github.com/aphrodite-engine/aphrodite-engine

### 分布式服务与运行平台

- NVIDIA Dynamo: https://github.com/ai-dynamo/dynamo
- Dynamo documentation: https://docs.nvidia.com/dynamo/
- Triton Inference Server: https://github.com/triton-inference-server/server
- Triton Inference Server documentation: https://docs.nvidia.com/deeplearning/triton-inference-server/
- Ray Serve LLM: https://docs.ray.io/en/latest/serve/llm/
- Ray: https://github.com/ray-project/ray

### 本地、边缘与低成本推理

- llama.cpp: https://github.com/ggml-org/llama.cpp
- Ollama: https://github.com/ollama/ollama
- MLC LLM: https://github.com/mlc-ai/mlc-llm
- MLX-LM: https://github.com/ml-explore/mlx-lm
- ONNX Runtime GenAI: https://github.com/microsoft/onnxruntime-genai
- OpenVINO GenAI: https://github.com/openvinotoolkit/openvino.genai
- KTransformers: https://github.com/kvcache-ai/ktransformers
- ExLlamaV2: https://github.com/turboderp-org/exllamav2
- mistral.rs: https://github.com/EricLBuehler/mistral.rs

### 内核、结构化输出与推理组件

- FlashInfer: https://github.com/flashinfer-ai/flashinfer
- llguidance: https://github.com/guidance-ai/llguidance
- Outlines: https://github.com/dottxt-ai/outlines

### 图像与视频生成推理

- Hugging Face Diffusers: https://github.com/huggingface/diffusers
- Diffusers documentation: https://huggingface.co/docs/diffusers/
- ComfyUI: https://github.com/Comfy-Org/ComfyUI
- ComfyUI documentation: https://docs.comfy.org/
