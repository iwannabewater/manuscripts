# [2212.10496] Precise Zero-Shot Dense Retrieval without Relevance Labelsopen searchopen navigation menu

> Source: https://arxiv.org/abs/2212.10496

Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate

> cs > arXiv:2212.10496

Computer Science > Information Retrieval

arXiv:2212.10496 (cs)

[Submitted on 20 Dec 2022]

Title:Precise Zero-Shot Dense Retrieval without Relevance Labels

Authors:Luyu Gao, Xueguang Ma, Jimmy Lin, Jamie Callan

View a PDF of the paper titled Precise Zero-Shot Dense Retrieval without Relevance Labels, by Luyu Gao and 3 other authors

View PDF

Abstract:While dense retrieval has been shown effective and efficient across tasks and languages, it remains difficult to create effective fully zero-shot dense retrieval systems when no relevance label is available. In this paper, we recognize the difficulty of zero-shot learning and encoding relevance. Instead, we propose to pivot through Hypothetical Document Embeddings~(HyDE). Given a query, HyDE first zero-shot instructs an instruction-following language model (e.g. InstructGPT) to generate a hypothetical document. The document captures relevance patterns but is unreal and may contain false details. Then, an unsupervised contrastively learned encoder~(e.g. Contriever) encodes the document into an embedding vector. This vector identifies a neighborhood in the corpus embedding space, where similar real documents are retrieved based on vector similarity. This second step ground the generated document to the actual corpus, with the encoder's dense bottleneck filtering out the incorrect details. Our experiments show that HyDE significantly outperforms the state-of-the-art unsupervised dense retriever Contriever and shows strong performance comparable to fine-tuned retrievers, across various tasks (e.g. web search, QA, fact verification) and languages~(e.g. sw, ko, ja).

Subjects:

Information Retrieval (cs.IR); Computation and Language (cs.CL)

Cite as:
arXiv:2212.10496 [cs.IR]

(or
arXiv:2212.10496v1 [cs.IR] for this version)

https://doi.org/10.48550/arXiv.2212.10496

Focus to learn more

arXiv-issued DOI via DataCite

Submission history
From: Luyu Gao [view email]

[v1]
Tue, 20 Dec 2022 18:09:52 UTC (7,003 KB)

Full-text links:

Access Paper:

View a PDF of the paper titled Precise Zero-Shot Dense Retrieval without Relevance Labels, by Luyu Gao and 3 other authors

View PDF

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
| 2022-12

Change to browse by:

cs

cs.CL

References & Citations

NASA ADS

Google Scholar

Semantic Scholar

1 blog link
(what is this?)

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
