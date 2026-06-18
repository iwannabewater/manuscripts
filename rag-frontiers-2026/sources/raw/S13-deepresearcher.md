# [2504.03160] DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environmentsopen searchopen navigation menu

> Source: https://arxiv.org/abs/2504.03160

Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate

> cs > arXiv:2504.03160

Computer Science > Artificial Intelligence

arXiv:2504.03160 (cs)

[Submitted on 4 Apr 2025 (v1), last revised 17 Apr 2025 (this version, v4)]

Title:DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments

Authors:Yuxiang Zheng, Dayuan Fu, Xiangkun Hu, Xiaojie Cai, Lyumanshan Ye, Pengrui Lu, Pengfei Liu

View a PDF of the paper titled DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments, by Yuxiang Zheng and 6 other authors

View PDF
HTML (experimental)

Abstract:Large Language Models (LLMs) equipped with web search capabilities have demonstrated impressive potential for deep research tasks. However, current approaches predominantly rely on either manually engineered prompts (prompt engineering-based) with brittle performance or reinforcement learning within controlled Retrieval-Augmented Generation (RAG) environments (RAG-based) that fail to capture the complexities of real-world interaction. In this paper, we introduce DeepResearcher, the first comprehensive framework for end-to-end training of LLM-based deep research agents through scaling reinforcement learning (RL) in real-world environments with authentic web search interactions. Unlike RAG-based approaches that assume all necessary information exists within a fixed corpus, our method trains agents to navigate the noisy, unstructured, and dynamic nature of the open web. We implement a specialized multi-agent architecture where browsing agents extract relevant information from various webpage structures and overcoming significant technical challenges. Extensive experiments on open-domain research tasks demonstrate that DeepResearcher achieves substantial improvements of up to 28.9 points over prompt engineering-based baselines and up to 7.2 points over RAG-based RL agents. Our qualitative analysis reveals emergent cognitive behaviors from end-to-end RL training, including the ability to formulate plans, cross-validate information from multiple sources, engage in self-reflection to redirect research, and maintain honesty when unable to find definitive answers. Our results highlight that end-to-end training in real-world web environments is not merely an implementation detail but a fundamental requirement for developing robust research capabilities aligned with real-world applications. We release DeepResearcher at this https URL.

Subjects:

Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

Cite as:
arXiv:2504.03160 [cs.AI]

(or
arXiv:2504.03160v4 [cs.AI] for this version)

https://doi.org/10.48550/arXiv.2504.03160

Focus to learn more

arXiv-issued DOI via DataCite

Submission history
From: Yuxiang Zheng [view email]

[v1]
Fri, 4 Apr 2025 04:41:28 UTC (959 KB)

[v2]
Mon, 7 Apr 2025 10:45:47 UTC (958 KB)

[v3]
Tue, 15 Apr 2025 02:57:20 UTC (959 KB)

[v4]
Thu, 17 Apr 2025 04:46:08 UTC (959 KB)

Full-text links:

Access Paper:

View a PDF of the paper titled DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments, by Yuxiang Zheng and 6 other authors

View PDF

HTML (experimental)

TeX Source

view license

Current browse context:
cs.AI

< prev

|
next >

new
|
recent
| 2025-04

Change to browse by:

cs

cs.CL

cs.LG

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
