# T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation - ACL Anthology

> Source: https://aclanthology.org/2026.eacl-long.8/

T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation

Jan Strich,
Enes Kutay Isgorur,
Maximilian Trescher,
Chris Biemann,
Martin Semmann

Correct Metadata for

ALL author names match the snapshot above—including
middle initials, hyphens, and accents.
Create GitHub issue for staff review

Abstract
Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces T2-RAGBench, a benchmark comprising 23,088 question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under Oracle Context settings, T2-RAGBench challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3% context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies Hybrid BM25 , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that T2-RAGBench remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. T2-RAGBench provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: https://github.com/uhh-hcds/g4kmu-paper

Anthology ID:2026.eacl-long.8Volume:Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)Month:MarchYear:2026Address:Rabat, MoroccoEditors:Vera Demberg,
Kentaro Inui,
Lluís MarquezVenue:EACLSIG:Publisher:Association for Computational LinguisticsNote:Pages:165–191Language:URL:https://aclanthology.org/2026.eacl-long.8/DOI:10.18653/v1/2026.eacl-long.8Bibkey:strich-etal-2026-t2Cite (ACL):Jan Strich, Enes Kutay Isgorur, Maximilian Trescher, Chris Biemann, and Martin Semmann. 2026. T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation. In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 165–191, Rabat, Morocco. Association for Computational Linguistics.Cite (Informal):T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation (Strich et al., EACL 2026)Copy Citation:BibTeX
Markdown
MODS XML
Endnote
More
options…PDF:https://aclanthology.org/2026.eacl-long.8.pdfChecklist:
2026.eacl-long.8.checklist.pdf

PDF
Cite
Search

Checklist

Fix data

Export citation

BibTeX

MODS XML

Endnote

Preformatted

@inproceedings{strich-etal-2026-t2,
title = "T$^2$-{RAGB}ench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation",
author = "Strich, Jan  and
Isgorur, Enes Kutay  and
Trescher, Maximilian  and
Biemann, Chris  and
Semmann, Martin",
editor = "Demberg, Vera  and
Inui, Kentaro  and
Marquez, Llu{\'i}s",
booktitle = "Proceedings of the 19th Conference of the {E}uropean Chapter of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
month = mar,
year = "2026",
address = "Rabat, Morocco",
publisher = "Association for Computational Linguistics",
url = "https://aclanthology.org/2026.eacl-long.8/",
doi = "10.18653/v1/2026.eacl-long.8",
pages = "165--191",
ISBN = "979-8-89176-380-7",
abstract = "Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces \textbf{$T^2-RAGBench$}, a benchmark comprising $\textbf{23,088}$ question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under $\textit{Oracle Context}$ settings, \textbf{$T^2-RAGBench$} challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3{\%} context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies $\textit{Hybrid BM25}$ , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that \textbf{$T^2-RAGBench$} remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. \textbf{$T^2-RAGBench$} provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: \url{https://github.com/uhh-hcds/g4kmu-paper}"
}
Download as
File
Copy to Clipboard

<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3">
<mods ID="strich-etal-2026-t2">
<titleInfo>
<title>T²-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation</title>
</titleInfo>
<name type="personal">
<namePart type="given">Jan</namePart>
<namePart type="family">Strich</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Enes</namePart>
<namePart type="given">Kutay</namePart>
<namePart type="family">Isgorur</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Maximilian</namePart>
<namePart type="family">Trescher</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Chris</namePart>
<namePart type="family">Biemann</namePart>
<role>
<roleTerm authority="marcrelator" type="text">author</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Martin</namePart>
<namePart type="family">Semmann</namePart>
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
<title>Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)</title>
</titleInfo>
<name type="personal">
<namePart type="given">Vera</namePart>
<namePart type="family">Demberg</namePart>
<role>
<roleTerm authority="marcrelator" type="text">editor</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Kentaro</namePart>
<namePart type="family">Inui</namePart>
<role>
<roleTerm authority="marcrelator" type="text">editor</roleTerm>
</role>
</name>
<name type="personal">
<namePart type="given">Lluís</namePart>
<namePart type="family">Marquez</namePart>
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
<identifier type="isbn">979-8-89176-380-7</identifier>
</relatedItem>
<abstract>Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces T²-RAGBench, a benchmark comprising 23,088 question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under Oracle Context settings, T²-RAGBench challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3% context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies Hybrid BM25 , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that T²-RAGBench remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. T²-RAGBench provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: https://github.com/uhh-hcds/g4kmu-paper</abstract>
<identifier type="citekey">strich-etal-2026-t2</identifier>
<identifier type="doi">10.18653/v1/2026.eacl-long.8</identifier>
<location>
<url>https://aclanthology.org/2026.eacl-long.8/</url>
</location>
<part>
<date>2026-03</date>
<extent unit="page">
<start>165</start>
<end>191</end>
</extent>
</part>
</mods>
</modsCollection>

Download as
File
Copy to Clipboard

%0 Conference Proceedings
%T T²-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation
%A Strich, Jan
%A Isgorur, Enes Kutay
%A Trescher, Maximilian
%A Biemann, Chris
%A Semmann, Martin
%Y Demberg, Vera
%Y Inui, Kentaro
%Y Marquez, Lluís
%S Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)
%D 2026
%8 March
%I Association for Computational Linguistics
%C Rabat, Morocco
%@ 979-8-89176-380-7
%F strich-etal-2026-t2
%X Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces T²-RAGBench, a benchmark comprising 23,088 question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under Oracle Context settings, T²-RAGBench challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3% context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies Hybrid BM25 , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that T²-RAGBench remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. T²-RAGBench provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: https://github.com/uhh-hcds/g4kmu-paper
%R 10.18653/v1/2026.eacl-long.8
%U https://aclanthology.org/2026.eacl-long.8/
%U https://doi.org/10.18653/v1/2026.eacl-long.8
%P 165-191
Download as
File
Copy to Clipboard

Markdown (Informal)

[T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation](https://aclanthology.org/2026.eacl-long.8/) (Strich et al., EACL 2026)

T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation (Strich et al., EACL 2026)

ACL

Jan Strich, Enes Kutay Isgorur, Maximilian Trescher, Chris Biemann, and Martin Semmann. 2026. T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation. In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 165–191, Rabat, Morocco. Association for Computational Linguistics.

Copy Markdown to
Clipboard
Copy ACL to
Clipboard
