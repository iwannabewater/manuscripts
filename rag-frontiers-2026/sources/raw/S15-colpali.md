# [2407.01449] ColPali: Efficient Document Retrieval with Vision Language Modelsopen searchopen navigation menu

> Source: https://arxiv.org/abs/2407.01449

Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate

> cs > arXiv:2407.01449

Computer Science > Information Retrieval

arXiv:2407.01449 (cs)

[Submitted on 27 Jun 2024 (v1), last revised 28 Feb 2025 (this version, v6)]

Title:ColPali: Efficient Document Retrieval with Vision Language Models

Authors:Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot, Pierre Colombo

View a PDF of the paper titled ColPali: Efficient Document Retrieval with Vision Language Models, by Manuel Faysse and 6 other authors

View PDF
HTML (experimental)

Abstract:Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents -often through lengthy and brittle processes-, they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG). To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. We release models, data, code and benchmarks under open licenses at this https URL.

Comments:
Published as a conference paper at ICLR 2025

Subjects:

Information Retrieval (cs.IR); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Cite as:
arXiv:2407.01449 [cs.IR]

(or
arXiv:2407.01449v6 [cs.IR] for this version)

https://doi.org/10.48550/arXiv.2407.01449

Focus to learn more

arXiv-issued DOI via DataCite

Submission history
From: Tony Wu [view email]

[v1]
Thu, 27 Jun 2024 15:45:29 UTC (12,102 KB)

[v2]
Tue, 2 Jul 2024 13:02:58 UTC (12,102 KB)

[v3]
Mon, 7 Oct 2024 07:46:00 UTC (12,117 KB)

[v4]
Wed, 5 Feb 2025 08:42:57 UTC (15,111 KB)

[v5]
Thu, 6 Feb 2025 09:57:56 UTC (15,111 KB)

[v6]
Fri, 28 Feb 2025 08:51:57 UTC (15,110 KB)

Full-text links:

Access Paper:

View a PDF of the paper titled ColPali: Efficient Document Retrieval with Vision Language Models, by Manuel Faysse and 6 other authors

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
| 2024-07

Change to browse by:

cs

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
