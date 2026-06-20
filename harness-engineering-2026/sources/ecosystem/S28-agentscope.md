---
source_url: https://raw.githubusercontent.com/agentscope-ai/agentscope/fd1c2cd2acbf261d55823bb636b5295507dfce0d/README.md
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
> Source: https://raw.githubusercontent.com/agentscope-ai/agentscope/fd1c2cd2acbf261d55823bb636b5295507dfce0d/README.md

[**中文主页**](https://github.com/agentscope-ai/agentscope/blob/main/README_zh.md) | [**Documentation**](https://docs.agentscope.io/) | [**Roadmap**](https://github.com/orgs/agentscope-ai/projects/2/views/1)

## What is AgentScope 2.0?

AgentScope 2.0 is a production-ready, easy-to-use agent framework with essential abstractions that work with rising model capability and built-in support for .

- [**Event System** →](https://docs.agentscope.io/v2/building-blocks/message-and-event) A unified event bus to the frontend and human-in-the-loop support.
- [**Permission System** →](https://docs.agentscope.io/v2/building-blocks/permission-system) Fine-grained, configurable control over tools and resources.
- [**Multi-tenancy & Multi-session Service** →](https://docs.agentscope.io/v2/deploy/agent-service) Production-grade serving with isolation across tenants and sessions.
- [**Workspace / Sandbox Support** →](https://docs.agentscope.io/v2/building-blocks/workspace) Run tools and code in isolated environments, with built-in backends for local, Docker, and E2B.
- [**Extensible Middleware System** →](https://docs.agentscope.io/v2/building-blocks/middleware) Composable hooks to customize and extend the agent's reasoning-acting loop.

We design for increasingly agentic LLMs.
Our approach leverages the models' reasoning and tool use abilities
rather than constraining them with strict prompts and opinionated orchestrations.

## News

- **[2026-06] `INTE`:** Mem0 supported. [Example](https://github.com/agentscope-ai/agentscope/tree/main/examples/long_term_memory) | [Docs](https://docs.agentscope.io/v2)
- **[2026-06] `FEAT`:** Agent Team supported. [Example](https://github.com/agentscope-ai/agentscope/tree/main/examples/agent_service) | [Docs](https://docs.agentscope.io/v2/deploy/agent-team)
- **[2026-05] `RELS`:** AgentScope 2.0 released! [Docs](https://docs.agentscope.io/)

[More news →](./docs/NEWS.md)

## Community

Welcome to join our community on

| [Discord](https://discord.gg/eYMpfnkG8h)                                                                                         | DingTalk                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
|  |  |

## Quickstart

### Installation

> AgentScope requires **Python 3.11** or higher.

#### From PyPI

```bash
uv pip install agentscope
# or
# pip install agentscope
```

#### From source

```bash
# Pull the source code from GitHub
git clone -b main https://github.com/agentscope-ai/agentscope.git

# Install the package in editable mode
cd agentscope

uv pip install -e .
# or
# pip install -e .
```

## Hello AgentScope!

Start your first agent with AgentScope 2.0:

```python
from agentscope.agent import Agent
from agentscope.tool import Toolkit, Bash, Grep, Glob, Read, Write, Edit
from agentscope.credential import DashScopeCredential
from agentscope.model import DashScopeChatModel
from agentscope.message import UserMsg
from agentscope.event import EventType

import os, asyncio

async def main() -> None:
agent = Agent(
name="Friday",
system_prompt="You're a helpful assistant named Friday.",
model=DashScopeChatModel(
credential=DashScopeCredential(
api_key=os.environ["DASHSCOPE_API_KEY"]
),
model="qwen3.6-plus",
),
toolkit=Toolkit(
tools=[
Bash(),
Grep(),
Glob(),
Read(),
Write(),
Edit(),
]
),
)

async for evt in agent.reply_stream(UserMsg("Tony", "Hi, Friday!")):
# Handle the event stream, e.g., print the message, update UI, etc.
match evt.type:
case EventType.REPLY_START:
...
case EventType.MODEL_CALL_START:
...
case EventType.TEXT_BLOCK_START:
...
case EventType.TEXT_BLOCK_DELTA:
...
case EventType.TEXT_BLOCK_END:
...

# Handle other event types

asyncio.run(main())
```

## Hello Agent Service!

An extensible FastAPI based **multi-tenancy**, **multi-session** agent service with pre-built Web UI in `examples/web_ui`

Agent team — a leader agent spawns workers and coordinates them through the built-in team tools.

Task planning — the agent breaks complex work into a tracked plan and updates it as it goes.

Permission control in bypass mode — the agent runs end-to-end without pausing for tool-call confirmations.

Background task offloading — a long-running tool moves to the background; its result later wakes the agent up and the conversation resumes.

Run the following commands to start the agent service backend and the web UI:

```bash
git clone -b main https://github.com/agentscope-ai/agentscope.git
cd agentscope/examples/agent_service

# start the agent service backend
python main.py
```

Then open another terminal to start the web UI:

```bash
cd agentscope/examples/web_ui

# start the webui
pnpm install
pnpm dev
```

## Contributing

We welcome contributions from the community! Please refer to our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines
on how to contribute.

## License

AgentScope is released under Apache License 2.0.

## Publications

If you find our work helpful for your research or application, please cite our papers.

- [AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications](https://arxiv.org/abs/2508.16279)

- [AgentScope: A Flexible yet Robust Multi-Agent Platform](https://arxiv.org/abs/2402.14034)

```
@article{agentscope_v1,
author  = {Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li, Bolin Ding, Jingren Zhou}
title   = {AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications},
journal = {CoRR},
volume  = {abs/2508.16279},
year    = {2025},
}

@article{agentscope,
author  = {Dawei Gao, Zitao Li, Xuchen Pan, Weirui Kuang, Zhijian Ma, Bingchen Qian, Fei Wei, Wenhao Zhang, Yuexiang Xie, Daoyuan Chen, Liuyi Yao, Hongyi Peng, Zeyu Zhang, Lin Zhu, Chen Cheng, Hongzhu Shi, Yaliang Li, Bolin Ding, Jingren Zhou}
title   = {AgentScope: A Flexible yet Robust Multi-Agent Platform},
journal = {CoRR},
volume  = {abs/2402.14034},
year    = {2024},
}
```

## Contributors

All thanks to our contributors:
