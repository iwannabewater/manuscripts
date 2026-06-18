# From Local to Global: A Graph RAG Approach to Query-Focused Summarization - Microsoft ResearchYour Privacy Choices Opt-Out Icon

> Source: https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/

Skip to main content

Research

Publications
Code & data
People
Microsoft Research blog

Artificial intelligence
Audio & acoustics
Computer vision
Graphics & multimedia
Human-computer interaction
Human language technologies
Search & information retrieval

Data platforms and analytics
Hardware & devices
Programming languages & software engineering
Quantum computing
Security, privacy & cryptography
Systems & networking

Algorithms
Mathematics

Ecology & environment
Economics
Medical, health & genomics
Social sciences
Technology for emerging markets

Academic programs
Events & academic conferences
Microsoft Research Forum

Behind the Tech podcast
Microsoft Research blog
Microsoft Research Forum
Microsoft Research podcast

About Microsoft Research
Careers & internships
People
Emeritus program
News & awards
Microsoft Research newsletter

Africa
AI for Science
AI Frontiers
Asia-Pacific
Cambridge
Health Futures
India
Montreal
New England
New York City
Redmond

Applied Sciences
Mixed Reality & AI - Cambridge
Mixed Reality & AI - Zurich

Register: Research Forum

Microsoft Security
Azure
Dynamics 365
Microsoft 365
Microsoft Teams
Windows 365

Microsoft AI
Azure Space
Mixed reality
Microsoft HoloLens
Microsoft Viva
Quantum computing
Sustainability

Education
Automotive
Financial services
Government
Healthcare
Manufacturing
Retail

Find a partner
Become a partner
Partner Network
Microsoft Marketplace
Software companies

Blog
Microsoft Advertising
Developer Center
Documentation
Events
Licensing
Microsoft Learn
Microsoft Research

View Sitemap

From Local to Global: A Graph RAG Approach to Query-Focused Summarization

Darren Edge

,

Ha Trinh

,

Newman Cheng

,

Joshua Bradley

,

Alex Chao
,

Apurva Mody
,

Steven Truitt

,

Dasha Metropolitansky

,

Robert Osazuwa Ness

,

Jonathan Larson

April 2024

Download BibTex

The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections. However, RAG fails on global questions directed at an entire text corpus, such as “What are the main themes in the dataset?”, since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task. Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems. To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text. Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities. Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user. For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

Opens in a new tab

Follow us:

Follow on X

Like on Facebook

Follow on LinkedIn

Subscribe on Youtube

Follow on Instagram

Subscribe to our RSS feed

Share this page:

Share on X

Share on Facebook

Share on LinkedIn

Share on Reddit

Surface Pro
Surface Laptop
Surface Laptop Ultra
Surface RTX Spark Dev Box
Copilot for organizations
Copilot for personal use
Explore Microsoft products
Windows 11 apps

Account profile
Download Center
Microsoft Store support
Returns
Order tracking
Certified Refurbished
Microsoft Store Promise
Flexible Payments

Microsoft in education
Devices for education
Microsoft Teams for Education
Microsoft 365 Education
How to buy for your school
Educator training and development
Deals for students and parents
AI for education

Microsoft AI
Microsoft Security
Dynamics 365
Microsoft 365
Microsoft Power Platform
Microsoft Teams
Microsoft 365 Copilot
Small Business

Azure
Microsoft Developer
Microsoft Learn
Support for AI marketplace apps
Microsoft Tech Community
Microsoft Marketplace
Software companies
Visual Studio

Careers
About Microsoft
Company news
Privacy at Microsoft
Investors
Diversity and inclusion
Accessibility
Sustainability

Your Privacy Choices

Consumer Health Privacy

Sitemap
Contact Microsoft
Privacy
Manage cookies
Terms of use
Trademarks
Safety & eco
Recycling
About our ads
