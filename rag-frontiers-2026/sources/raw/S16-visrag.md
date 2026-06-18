# [2410.10594] VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documentsopen searchopen navigation menu

> Source: https://arxiv.org/abs/2410.10594

Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate

> cs > arXiv:2410.10594

Computer Science > Information Retrieval

arXiv:2410.10594 (cs)

[Submitted on 14 Oct 2024 (v1), last revised 2 Mar 2025 (this version, v2)]

Title:VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents

Authors:Shi Yu, Chaoyue Tang, Bokai Xu, Junbo Cui, Junhao Ran, Yukun Yan, Zhenghao Liu, Shuo Wang, Xu Han, Zhiyuan Liu, Maosong Sun

View a PDF of the paper titled VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents, by Shi Yu and 10 other authors

View PDF
HTML (experimental)

Abstract:Retrieval-augmented generation (RAG) is an effective technique that enables large language models (LLMs) to utilize external knowledge sources for generation. However, current RAG systems are solely based on text, rendering it impossible to utilize vision information like layout and images that play crucial roles in real-world multi-modality documents. In this paper, we introduce VisRAG, which tackles this issue by establishing a vision-language model (VLM)-based RAG pipeline. In this pipeline, instead of first parsing the document to obtain text, the document is directly embedded using a VLM as an image and then retrieved to enhance the generation of a VLM. Compared to traditional text-based RAG, VisRAG maximizes the retention and utilization of the data information in the original documents, eliminating the information loss introduced during the parsing process. We collect both open-source and synthetic data to train the retriever in VisRAG and explore a variety of generation methods. Experiments demonstrate that VisRAG outperforms traditional RAG in both the retrieval and generation stages, achieving a 20--40% end-to-end performance gain over traditional text-based RAG pipeline. Further analysis reveals that VisRAG is efficient in utilizing training data and demonstrates strong generalization capability, positioning it as a promising solution for RAG on multi-modality documents. Our code and data are available at this https URL.

Subjects:

Information Retrieval (cs.IR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Cite as:
arXiv:2410.10594 [cs.IR]

(or
arXiv:2410.10594v2 [cs.IR] for this version)

https://doi.org/10.48550/arXiv.2410.10594

Focus to learn more

arXiv-issued DOI via DataCite

Submission history
From: Shi Yu [view email]

[v1]
Mon, 14 Oct 2024 15:04:18 UTC (25,369 KB)

[v2]
Sun, 2 Mar 2025 01:19:51 UTC (25,883 KB)

Full-text links:

Access Paper:

View a PDF of the paper titled VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents, by Shi Yu and 10 other authors

View PDF

HTML (experimental)

TeX Source

view license

Current browse context:
cs.IR

< prev

|
next >

new
|
recent
| 2024-10

Change to browse by:

cs

cs.AI

cs.CL

cs.CV

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

Links to Code Toggle

Papers with Code (What is Papers with Code?)

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
