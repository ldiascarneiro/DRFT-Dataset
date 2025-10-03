# DRFT-Dataset
DRFT: A Corpus of Draft–Review–Final Triples for Modeling and Evaluating the Peer-Review Cycle

Abstract. We present DRFT, a corpus of 225 draft–review–final triples that document the full peer-review cycle, from initial submissions to the final published versions of papers. Each instance includes the base draft, concatenated reviews, and the published arXiv version, all packaged in a single spreadsheet file (.xlsx), and publicly released through a GitHub repository. We attach two complementary automatic metrics: (i) BERTScore (draft↔final) for semantic preservation, and (ii) G-Eval, an LLM-as-a-judge score (1–10) with GPT-5o-mini (review→final), for review uptake, with a brief justification. We describe collection and curation from ICLR via OpenReview and PeerRead, provide a standardized schema, and report corpus statistics (baseline BERTScore ≈ 0.82; G-Eval ≈ 8.31; moderate negative correlation r ≈ −0.33), indicating complementarity. Beyond corpus construction, DRFT targets three primary use cases: (i) review-conditioned edit planning, (ii) evaluating automatic revisions against human finals, and (iii) analyzing which review aspects drive substantial changes. Overall, DRFT offers a compact, high-value benchmarking resource for transparent, assistive systems that help authors respond faithfully to peer feedback.

![Fluxo do DRFT](figures/FlowChart.png)

