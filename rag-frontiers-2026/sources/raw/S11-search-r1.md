# [2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

> Source: https://arxiv.org/abs/2503.09516

Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate

> cs > arXiv:2503.09516

Computer Science > Computation and Language

arXiv:2503.09516 (cs)

[Submitted on 12 Mar 2025 (v1), last revised 5 Aug 2025 (this version, v5)]

Title:Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

Authors:Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Arik, Dong Wang, Hamed Zamani, Jiawei Han

View a PDF of the paper titled Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning, by Bowen Jin and 7 other authors

View PDF
HTML (experimental)

Abstract:Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact optimally with the search engine. This paper introduces Search-R1, an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval. Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions, leveraging retrieved token masking for stable RL training and a simple outcome-based reward function. Experiments on seven question-answering datasets show that Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines under the same setting. This paper further provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning. The code and model checkpoints are available at this https URL.

Comments:
31 pages

Subjects:

Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Information Retrieval (cs.IR)

Cite as:
arXiv:2503.09516 [cs.CL]

(or
arXiv:2503.09516v5 [cs.CL] for this version)

https://doi.org/10.48550/arXiv.2503.09516

Focus to learn more

arXiv-issued DOI via DataCite

Submission history
From: Bowen Jin [view email]

[v1]
Wed, 12 Mar 2025 16:26:39 UTC (196 KB)

[v2]
Wed, 19 Mar 2025 21:40:12 UTC (196 KB)

[v3]
Tue, 8 Apr 2025 14:03:26 UTC (311 KB)

[v4]
Mon, 21 Jul 2025 03:50:13 UTC (251 KB)

[v5]
Tue, 5 Aug 2025 19:08:38 UTC (251 KB)

Full-text links:

Access Paper:

View a PDF of the paper titled Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning, by Bowen Jin and 7 other authors

View PDF

HTML (experimental)

TeX Source

view license

Current browse context:

cs.CL

< prev

|
next >

new
|
recent
| 2025-03

Change to browse by:

cs

cs.AI

cs.IR

References & Citations

NASA ADS

Google Scholar

Semantic Scholar

export BibTeX citation
Loading...

BibTeX formatted citation

×

loading...

Data provided by:

Bookmark

Bibliographic Tools

Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer (What is the Explorer?)

Connected Papers Toggle

Connected Papers (What is Connected Papers?)

Litmaps Toggle

Litmaps (What is Litmaps?)

scite.ai Toggle

scite Smart Citations (What are Smart Citations?)

Code, Data, Media

Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv (What is alphaXiv?)

Links to Code Toggle

CatalyzeX Code Finder for Papers (What is CatalyzeX?)

DagsHub Toggle

DagsHub (What is DagsHub?)

GotitPub Toggle

Gotit.pub (What is GotitPub?)

Huggingface Toggle

Hugging Face (What is Huggingface?)

ScienceCast Toggle

ScienceCast (What is ScienceCast?)

Demos

Demos

Replicate Toggle

Replicate (What is Replicate?)

Spaces Toggle

Hugging Face Spaces (What is Spaces?)

Spaces Toggle

TXYZ.AI (What is TXYZ.AI?)

Related Papers

Recommenders and Search Tools

Link to Influence Flower

Influence Flower (What are Influence Flowers?)

Core recommender toggle

CORE Recommender (What is CORE?)

Author

Venue

Institution

Topic

About arXivLabs

arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

Which authors of this paper are endorsers? |
Disable MathJax (What is MathJax?)
