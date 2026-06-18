# Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot - ACL Anthology

> Source: https://aclanthology.org/2026.eacl-industry.13/

Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot

Daniel González Juclà,
Mohit Tuteja,
Marcos Esteve Casademunt,
Keshav Unnikrishnan,
Yasir Usmani,
Arvind Roshaan

Correct Metadata for

ALL author names match the snapshot above—including
middle initials, hyphens, and accents.
Create GitHub issue for staff review

Abstract
Retrieval-Augmented Generation (RAG) systems depend critically on retrieval quality to enable accurate, contextually relevant LLM responses. While LLMs excel at synthesis, their RAG performance is bottlenecked by document relevance. We evaluate advanced retrieval techniques including embedding model comparison, Reciprocal Rank Fusion (RRF), embedding concatenation and list-wise and adaptive LLM-based re-ranking, demonstrating that zero-shot LLMs outperform traditional cross-encoders in identifying high-relevance passages. We also explore context-aware embeddings, diverse chunking strategies, and model fine-tuning. All methods are rigorously evaluated on a proprietary dataset powering our deployed production chatbot, with validation on three public benchmarks: FiQA, HotpotQA, and SciDocs. Results show consistent gains in Recall@10, closing the gap with Recall@50 and yielding actionable pipeline recommendations. By prioritizing retrieval enhancements, we significantly elevate downstream LLM response quality in real-world, customer-facing applications.

Anthology ID:2026.eacl-industry.13Volume:Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track)Month:MarchYear:2026Address:Rabat, MoroccoEditors:Yevgen Matusevych,
Gülşen Eryiğit,
Nikolaos AletrasVenue:EACLSIG:Publisher:Association for Computational LinguisticsNote:Pages:169–180Language:URL:https://aclanthology.org/2026.eacl-industry.13/DOI:10.18653/v1/2026.eacl-industry.13Bibkey:jucla-etal-2026-retrievalCite (ACL):Daniel González Juclà, Mohit Tuteja, Marcos Esteve Casademunt, Keshav Unnikrishnan, Yasir Usmani, and Arvind Roshaan. 2026. Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot. In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track), pages 169–180, Rabat, Morocco. Association for Computational Linguistics.Cite (Informal):Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot (Juclà et al., EACL 2026)Copy Citation:BibTeX
Markdown
MODS XML
Endnote
More
options…PDF:https://aclanthology.org/2026.eacl-industry.13.pdf

PDF
Cite
Search

Fix data

Export citation

BibTeX

MODS XML

Endnote

Preformatted

@inproceedings{jucla-etal-2026-retrieval,
title = "Retrieval Enhancements for {RAG}: Insights from a Deployed Customer Support Chatbot",
author = "Jucl{\`a}, Daniel Gonz{\'a}lez  and
Tuteja, Mohit  and
Casademunt, Marcos Esteve  and
Unnikrishnan, Keshav  and
Usmani, Yasir  and
Roshaan, Arvind",
editor = {Matusevych, Yevgen  and
Eryi{\u{g}}it, G{\"u}l{\c{s}}en  and
Aletras, Nikolaos},
booktitle = "Proceedings of the 19th Conference of the {E}uropean Chapter of the {A}ssociation for {C}omputational {L}inguistics (Volume 5: Industry Track)",
month = mar,
year = "2026",
address = "Rabat, Morocco",
publisher = "Association for Computational Linguistics",
url = "https://aclanthology.org/2026.eacl-industry.13/",
doi = "10.18653/v1/2026.eacl-industry.13",
pages = "169--180",
ISBN = "979-8-89176-384-5",
abstract = "Retrieval-Augmented Generation (RAG) systems depend critically on retrieval quality to enable accurate, contextually relevant LLM responses. While LLMs excel at synthesis, their RAG performance is bottlenecked by document relevance. We evaluate advanced retrieval techniques including embedding model comparison, Reciprocal Rank Fusion (RRF), embedding concatenation and list-wise and adaptive LLM-based re-ranking, demonstrating that zero-shot LLMs outperform traditional cross-encoders in identifying high-relevance passages. We also explore context-aware embeddings, diverse chunking strategies, and model fine-tuning. All methods are rigorously evaluated on a proprietary dataset powering our deployed production chatbot, with validation on three public benchmarks: FiQA, HotpotQA, and SciDocs. Results show consistent gains in Recall@10, closing the gap with Recall@50 and yielding actionable pipeline recommendations. By prioritizing retrieval enhancements, we significantly elevate downstream LLM response quality in real-world, customer-facing applications."
}
Download as
File
Copy to Clipboard

<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3">
<mods ID="jucla-etal-2026-retrieval">
<titleInfo>
<title>Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot</title>
</titleInfo>
<name type="personal">
<namePart type="given">Daniel</namePart>
<namePart type="given">González</namePart>
<namePart type="family">Juclà</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Mohit</namePart>
<namePart type="family">Tuteja</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Marcos</namePart>
<namePart type="given">Esteve</namePart>
<namePart type="family">Casademunt</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Keshav</namePart>
<namePart type="family">Unnikrishnan</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Yasir</namePart>
<namePart type="family">Usmani</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Arvind</namePart>
<namePart type="family">Roshaan</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<originInfo>
<dateIssued>2026-03</dateIssued>
</originInfo>
<typeOfResource>text</typeOfResource>
<relatedItem type="host">
<titleInfo>
<title>Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track)</title>
</titleInfo>
<name type="personal">
<namePart type="given">Yevgen</namePart>
<namePart type="family">Matusevych</namePart>
<role>
<roleTerm authority="marcrelator" type="text">editor</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Gülşen</namePart>
<namePart type="family">Eryiğit</namePart>
<role>
<roleTerm authority="marcrelator" type="text">editor</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Nikolaos</namePart>
<namePart type="family">Aletras</namePart>
<role>
<roleTerm authority="marcrelator" type="text">editor</roleTerm>
</role>
</name>
<originInfo>
<publisher>Association for Computational Linguistics</publisher>
<place>
<placeTerm type="text">Rabat, Morocco</placeTerm>
</place>
</originInfo>
<genre authority="marcgt">conference publication</genre>
<identifier type="isbn">979-8-89176-384-5</identifier>
</relatedItem>
<abstract>Retrieval-Augmented Generation (RAG) systems depend critically on retrieval quality to enable accurate, contextually relevant LLM responses. While LLMs excel at synthesis, their RAG performance is bottlenecked by document relevance. We evaluate advanced retrieval techniques including embedding model comparison, Reciprocal Rank Fusion (RRF), embedding concatenation and list-wise and adaptive LLM-based re-ranking, demonstrating that zero-shot LLMs outperform traditional cross-encoders in identifying high-relevance passages. We also explore context-aware embeddings, diverse chunking strategies, and model fine-tuning. All methods are rigorously evaluated on a proprietary dataset powering our deployed production chatbot, with validation on three public benchmarks: FiQA, HotpotQA, and SciDocs. Results show consistent gains in Recall@10, closing the gap with Recall@50 and yielding actionable pipeline recommendations. By prioritizing retrieval enhancements, we significantly elevate downstream LLM response quality in real-world, customer-facing applications.</abstract>
<identifier type="citekey">jucla-etal-2026-retrieval</identifier>
<identifier type="doi">10.18653/v1/2026.eacl-industry.13</identifier>
<location>
<url>https://aclanthology.org/2026.eacl-industry.13/</url>
</location>
<part>
<date>2026-03</date>
<extent unit="page">
<start>169</start>
<end>180</end>
</extent>
</part>
</mods>
</modsCollection>

Download as
File
Copy to Clipboard

%0 Conference Proceedings
%T Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot
%A Juclà, Daniel González
%A Tuteja, Mohit
%A Casademunt, Marcos Esteve
%A Unnikrishnan, Keshav
%A Usmani, Yasir
%A Roshaan, Arvind
%Y Matusevych, Yevgen
%Y Eryiğit, Gülşen
%Y Aletras, Nikolaos
%S Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track)
%D 2026
%8 March
%I Association for Computational Linguistics
%C Rabat, Morocco
%@ 979-8-89176-384-5
%F jucla-etal-2026-retrieval
%X Retrieval-Augmented Generation (RAG) systems depend critically on retrieval quality to enable accurate, contextually relevant LLM responses. While LLMs excel at synthesis, their RAG performance is bottlenecked by document relevance. We evaluate advanced retrieval techniques including embedding model comparison, Reciprocal Rank Fusion (RRF), embedding concatenation and list-wise and adaptive LLM-based re-ranking, demonstrating that zero-shot LLMs outperform traditional cross-encoders in identifying high-relevance passages. We also explore context-aware embeddings, diverse chunking strategies, and model fine-tuning. All methods are rigorously evaluated on a proprietary dataset powering our deployed production chatbot, with validation on three public benchmarks: FiQA, HotpotQA, and SciDocs. Results show consistent gains in Recall@10, closing the gap with Recall@50 and yielding actionable pipeline recommendations. By prioritizing retrieval enhancements, we significantly elevate downstream LLM response quality in real-world, customer-facing applications.
%R 10.18653/v1/2026.eacl-industry.13
%U https://aclanthology.org/2026.eacl-industry.13/
%U https://doi.org/10.18653/v1/2026.eacl-industry.13
%P 169-180
Download as
File
Copy to Clipboard

Markdown (Informal)

[Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot](https://aclanthology.org/2026.eacl-industry.13/) (Juclà et al., EACL 2026)

Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot (Juclà et al., EACL 2026)

ACL

Daniel González Juclà, Mohit Tuteja, Marcos Esteve Casademunt, Keshav Unnikrishnan, Yasir Usmani, and Arvind Roshaan. 2026. Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot. In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track), pages 169–180, Rabat, Morocco. Association for Computational Linguistics.

Copy Markdown to
Clipboard
Copy ACL to
Clipboard
