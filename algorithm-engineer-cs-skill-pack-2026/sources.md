# Sources

作者：Winston
资料口径：截至 2026-05-31

## Method

本技能包基于公开一手材料、官方文档、开源项目文档与研究论文整理。公司实践部分只引用公开可验证的信息，不推断 Google、Meta、OpenAI、Anthropic、NVIDIA、ByteDance 等公司的非公开内部流程。

正文把资料分为四层使用：

- 公司标准：用于抽取工程文化、生产鲁棒性、评测、安全和 GPU 系统能力。
- 官方工具文档：用于确定算法工程师真实会接触的 Git、Hive、Spark、Kafka、Kubernetes、Docker、MLflow、Kubeflow、Ray、vLLM、KServe、Triton 等工具边界。
- 研究与系统论文：用于补足 ML 生产就绪、A/B 实验、推荐系统、向量检索等流程标准。
- 安全与治理框架：用于约束 LLM、数据、模型供应链、隐私和风险管理。

本文不替代目标团队的安全、合规、发布、数据治理或知识产权制度。正式落地前应复核目标公司的权限模型、数据分级、变更流程、发布窗口、实验平台、告警策略、模型审计要求和事故升级规则。

## Company and Engineering Benchmarks

- Google, Rules of Machine Learning: https://developers.google.com/machine-learning/guides/rules-of-ml/
- Google SRE Book: https://sre.google/sre-book/table-of-contents/
- Google Engineering Practices: https://google.github.io/eng-practices/
- Google Research, The ML Test Score: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/
- TensorFlow Extended, TFX: https://www.tensorflow.org/tfx
- Meta Engineering, ML prediction robustness: https://engineering.fb.com/2024/07/10/data-infrastructure/machine-learning-ml-prediction-robustness-meta/
- Meta Research, FBLearner Flow: https://research.facebook.com/publications/fblearner-flow-a-machine-learning-platform-for-user-generated-content-at-facebook/
- Meta AI, Faiss: https://ai.meta.com/tools/faiss/
- Meta Engineering, Sapling source control: https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/
- OpenAI Evals GitHub: https://github.com/openai/evals
- OpenAI Cookbook, Getting Started with OpenAI Evals: https://cookbook.openai.com/examples/evaluation/getting_started_with_openai_evals
- OpenAI API docs, Evaluation best practices: https://platform.openai.com/docs/guides/evaluation-best-practices
- OpenAI careers, Software Engineer, Distributed Systems: https://openai.com/careers/principal-software-engineer-b2b-engineering-remote-us/
- Triton language and compiler: https://github.com/triton-lang/triton
- Anthropic Responsible Scaling Policy: https://www.anthropic.com/news/anthropics-responsible-scaling-policy
- Anthropic ML Infrastructure Engineer, Safeguards: https://www.anthropic.com/careers/jobs/4778843008
- NVIDIA CUDA Toolkit Documentation: https://docs.nvidia.com/cuda/
- NVIDIA Nsight Systems Documentation: https://docs.nvidia.com/nsight-systems/
- NVIDIA Triton Inference Server: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/
- NVIDIA TensorRT-LLM: https://nvidia.github.io/TensorRT-LLM/
- NVIDIA NeMo Framework: https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html
- ByteDance Monolith: https://github.com/bytedance/monolith
- CloudWeGo: https://www.cloudwego.io/

## Core Software Engineering

- Git reference: https://git-scm.com/docs
- Pro Git, Branching Workflows: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows
- GitHub Flow: https://docs.github.com/en/get-started/using-github/github-flow
- GitHub pull request reviews: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- GitHub protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Actions documentation: https://docs.github.com/en/actions/
- Docker documentation: https://docs.docker.com/
- Kubernetes documentation: https://kubernetes.io/docs/home/

## Data, Streaming, and Orchestration

- Apache Hive: https://hive.apache.org/
- Apache Spark documentation: https://spark.apache.org/docs/latest/
- Apache Flink documentation: https://nightlies.apache.org/flink/flink-docs-stable/
- Apache Kafka documentation: https://kafka.apache.org/documentation/
- Apache Airflow documentation: https://airflow.apache.org/docs/
- Argo Workflows: https://argo-workflows.readthedocs.io/
- Apache Iceberg: https://iceberg.apache.org/
- Apache Hudi: https://hudi.apache.org/
- Delta Lake: https://delta.io/

## ML Platform, Serving, and Retrieval

- MLflow documentation: https://mlflow.org/docs/latest/
- Kubeflow Pipelines: https://www.kubeflow.org/docs/components/pipelines/
- Feast feature store: https://docs.feast.dev/
- Ray documentation: https://docs.ray.io/en/latest/
- Ray Serve: https://docs.ray.io/en/latest/serve/
- vLLM documentation: https://docs.vllm.ai/
- KServe model serving frameworks overview: https://kserve.github.io/website/docs/model-serving/predictive-inference/frameworks/overview
- KServe project page: https://kserve.github.io/kserve/
- Faiss documentation: https://faiss.ai/
- Google ScaNN: https://github.com/google-research/google-research/tree/master/scann
- Apache Lucene: https://lucene.apache.org/core/
- Elasticsearch kNN search: https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html

## Experimentation, Reliability, Security, Governance

- Microsoft Research, Online Experimentation at Microsoft: https://www.microsoft.com/en-us/research/publication/online-experimentation-at-microsoft/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Google Secure AI Framework: https://safety.google/cybersecurity-advancements/saif/
- SLSA, Supply-chain Levels for Software Artifacts: https://slsa.dev/
- OpenTelemetry documentation: https://opentelemetry.io/docs/
- Prometheus documentation: https://prometheus.io/docs/introduction/overview/
- Grafana documentation: https://grafana.com/docs/
