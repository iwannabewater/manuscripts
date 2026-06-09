# Sources

资料核对日期：2026-05-18。本文优先采用官方仓库、官方文档与论文原始页面。GitHub API 在本环境中触发 rate limit，因此发布标签通过 `git ls-remote --tags --refs https://github.com/verl-project/verl.git` 核对。

## 主要来源

1. verl 官方仓库 README  
   URL: https://github.com/verl-project/verl  
   用途：项目定位、维护主体、关键特性、支持后端、算法列表、2026 年新闻、迁移到 `verl-project`、扩展项目与生态。

2. verl 官方文档首页  
   URL: https://verl.readthedocs.io/en/latest/  
   用途：文档结构、官方定义、HybridFlow、配置、算法、Worker、性能、异步、硬件支持章节定位。

3. HybridFlow Programming Guide  
   URL: https://verl.readthedocs.io/en/latest/hybrid_flow.html  
   用途：单控制器与多进程计算流的设计动机、WorkerGroup、ResourcePool、PPO 主循环、仓库结构。

4. The Design of `verl.single_controller`  
   URL: https://verl.readthedocs.io/en/latest/single_controller.html  
   用途：`@register`、dispatch/execute/collect 三段式调用链、`DP_COMPUTE_PROTO`、`ONE_TO_ALL`、RayWorkerGroup 绑定机制。

5. PPO Example Architecture  
   URL: https://verl.readthedocs.io/en/latest/examples/ppo_code_architecture.html  
   用途：数据 schema、RewardManager、角色映射、ActorRolloutRefWorker、TrainingWorker、`trainer.fit()` 入口。

6. PPO Ray Trainer  
   URL: https://verl.readthedocs.io/en/latest/workers/ray_trainer.html  
   用途：数据加载、WorkerGroup 初始化、PPO 训练循环、`generate_sequences`、`compute_log_prob`、`compute_values`、`update_actor`。

7. Engine Workers  
   URL: https://verl.readthedocs.io/en/latest/workers/engine_workers.html  
   用途：统一 `ActorRolloutRefWorker` / `TrainingWorker`、后端选择、EngineRegistry 支持矩阵、legacy worker 迁移口径。

8. Model Engine  
   URL: https://verl.readthedocs.io/en/latest/workers/model_engine.html  
   用途：BaseEngine 层次、训练引擎职责、模型类型、checkpoint 体系与扩展新 backend 的规则。

9. Config Explanation  
   URL: https://verl.readthedocs.io/en/latest/examples/config.html  
   用途：`data`、`actor_rollout_ref`、`rollout`、`reward_model`、`algorithm`、`trainer` 关键配置语义。

10. PPO / GRPO / DAPO 官方算法页  
    URLs:
    - https://verl.readthedocs.io/en/latest/algo/ppo.html
    - https://verl.readthedocs.io/en/latest/algo/grpo.html
    - https://verl.readthedocs.io/en/latest/algo/dapo.html  
    用途：PPO、GRPO、DAPO 在 verl 中的核心配置、KL 控制、优势估计、动态采样与 loss aggregation。

11. Performance Tuning Guide / Best Practices  
    URLs:
    - https://verl.readthedocs.io/en/latest/perf/perf_tuning.html
    - https://verl.readthedocs.io/en/latest/perf/best_practices.html  
    用途：rollout 吞吐、batch 语义、dynamic batch size、remove padding、Ulysses、FSDP2、显存调优。

12. Agentic RL Training  
    URL: https://verl.readthedocs.io/en/latest/start/agentic_rl.html  
    用途：server-based async rollout、AgentLoop、LLMServerClient、AsyncServer、多轮工具调用。

13. verl v0.7 release blog  
    URL: https://verl.readthedocs.io/en/latest/blog/v0.7.html  
    用途：v0.7 架构口径、verl-core / verl-trainer 划分、Model Engine、Rollout Engine、TransferQueue、Checkpoint Engine、同步/一步 off-policy/全异步 pipeline。

14. HybridFlow: A Flexible and Efficient RLHF Framework  
    URL: https://arxiv.org/abs/2409.19256  
    用途：HybridFlow 的论文定义、吞吐提升范围、3D-HybridEngine、单控制器与多控制器混合范式。

15. DAPO: An Open-Source LLM Reinforcement Learning System at Scale  
    URL: https://arxiv.org/abs/2503.14476  
    用途：DAPO 问题背景、公开系统、AIME 2024 结果口径、与 verl 的关系。

16. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models  
    URL: https://arxiv.org/abs/2402.03300  
    用途：GRPO 来源与算法背景。

## 本地核对

- 官方仓库浅克隆：`https://github.com/verl-project/verl.git`
- 本次 clone 的 `main` HEAD：`657cfa5ee7884a30d2a2912cefa56956c081c33c`
- HEAD 日期：2026-05-18
- HEAD 标题：`[trainer] feat: async generation dump with exception propagation and streaming write (#6324)`
- 版本文件：`verl/version/version` -> `0.8.0.dev`
- 远端标签核对结果中最新标签：`v0.7.1`

## 边界

- 本文不是性能 benchmark，不重新跑训练任务；所有性能数字只引用官方论文或官方文档口径。
- 本文不把开发分支能力等同于稳定发布能力；凡涉及 `0.8.0.dev`、TransferQueue、fully async 等内容均按“主线/实验/路线”措辞处理。
- 本文不替代官方安装文档；环境依赖、Docker tag、vLLM/SGLang 版本组合应以运行当天官方文档和项目 CI 为准。

