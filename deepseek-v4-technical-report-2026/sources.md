# Sources

## Source Policy

本文只使用可追溯公开资料。模型发布时间、规模、架构、训练配置、benchmark 数字等事实优先采用 DeepSeek 官方材料。涉及“为什么这样设计”“对实践意味着什么”的段落为本文作者基于公开报告的工程推断，不视作 DeepSeek 官方声明。

## Primary Sources

1. DeepSeek Transparency Center, `DeepSeek-V4`, release date 2026-04-24.  
   https://www.deepseek.com/en/transparency/

2. DeepSeek-AI, `DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence`, technical report, arXiv:2606.19348.
   https://arxiv.org/abs/2606.19348

3. DeepSeek-AI, `DeepSeek V4 Model Card`, English PDF.  
   https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf

4. DeepSeek-AI, `DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models`, technical report.  
   https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/assets/paper.pdf

5. DeepSeek-AI, `DeepSeek-V3 Technical Report`, arXiv:2412.19437.  
   https://arxiv.org/abs/2412.19437

6. DeepSeek-AI, `DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning`, arXiv:2501.12948.  
   https://arxiv.org/abs/2501.12948

## Verification Notes

- DeepSeek 官方透明中心列出 DeepSeek-V4，release date 为 2026-04-24。
- DeepSeek V4 model card 列出 release date 2026-04-24，并说明 Pro / Flash、1M context、三种 reasoning modes 与 MIT 权重许可。
- DeepSeek_V4.pdf 本地抽取显示 PDF 共 58 页，标题为 `DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence`。
- V4-Flash 参数量在公开材料中存在轻微口径差异：technical report 写 284B，model card 写 285B，Hugging Face collection 页面展示 292B-Base。正文采用 technical report 的 284B，并在描述中注明约 285B 量级。
- 所有与 Claude、GPT、Gemini、Kimi、GLM 的对比均来自 DeepSeek V4 technical report 的官方评测表；本文不声明这些数字已经由第三方独立复现。

## Out of Scope

- 未纳入非官方泄露、社交媒体传闻、未给出可追溯来源的 benchmark 排名。
- 未对 DeepSeek V4 权重进行本地推理复现或服务性能实测。
- 未覆盖尚未公开的多模态版本或后续报告更新。
