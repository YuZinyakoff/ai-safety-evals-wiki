---
type: raw
source_kind: theory
capture_method: web-clipper
title: How Should AI Safety Benchmarks Benchmark Safety?
author: 
site: arxiv.org
published: 
url: https://arxiv.org/html/2601.23112v2
captured: 2026-04-12T14:59:13+03:00
status: unprocessed
---

# How Should AI Safety Benchmarks Benchmark Safety?

Источник: https://arxiv.org/html/2601.23112v2

## Краткая справка
- Автор: 
- Сайт: arxiv.org
- Дата публикации: 

## Текст
Cheng Yu    Severin Engelmann    Ruoxuan Cao    Dalia Ali    Orestis Papakyriakopoulos

###### Abstract

AI safety benchmarks are pivotal for safety in advanced AI systems; however, they have significant technical, epistemic, and sociotechnical shortcomings. We present a review of 210 safety benchmarks that maps out common challenges in safety benchmarking, documenting failures and limitations by drawing from engineering sciences and long-established theories of risk and safety. We argue that adhering to established risk management principles, mapping the space of what can(not) be measured, developing robust probabilistic metrics, and efficiently deploying measurement theory to connect benchmarking objectives with the world can significantly improve the validity and usefulness of AI safety benchmarks. The review provides a roadmap on how to improve AI safety benchmarking, and we illustrate the effectiveness of these recommendations through quantitative and qualitative evaluation. We also introduce a checklist <sup>1</sup> that can help researchers and practitioners develop robust and epistemologically sound safety benchmarks. This study advances the science of benchmarking and helps practitioners deploy AI systems more responsibly.

Machine Learning, ICML

## 1 Introduction

The rapid advances in artificial intelligence (AI) are creating systems with ever-increasing capabilities and access to diverse environments. While these developments hold huge potential for societal benefit, they also introduce risks to safety, ranging from malicious use and manipulation to malfunctions and systemic issues [^7] [^24] [^255]. Harms related to AI have been documented broadly––in algorithmic bias and discrimination in computer vision [^25], toxicity and harmful content generation by language models [^64], and privacy leakage via training data extraction [^27]. Risks have been identified in malicious uses across digital, physical, and political domains [^24], dual‑use biological and chemical design [^236], and systemic reliability under distribution shift [^121]. The most common solution to mitigate risks has been the development and use of AI safety benchmarks [^146] [^239] [^29]. This solution is an extension of the traditional benchmarking culture in computer science, where standardized tests are designed and conducted to evaluate and compare the performance of computer systems, components, and algorithms [^200] [^221] [^158]. Benchmarks are useful and can reveal vulnerabilities of AI systems, and have clearly contributed to the development of the field of AI both scientifically and in its application [^195] [^64] [^121] [^292]. However, the discipline of benchmarking in AI safety—understood here as “endeavor dedicated to preventing or mitigating harms from AI systems” [^80] —overlooks established safety‑related theories, frameworks, practices, and knowledge developed over past decades for modeling, measuring, and mitigating risk [^61] [^129] [^88] [^98] [^99] [^174]. Given this, we answer: What are the limitations of AI safety benchmarks? How can we leverage existing theories, frameworks, and practices of safety and safety engineering to improve AI safety benchmarks?

Drawing on a review of 210 AI safety benchmarks, we identify three core limitations. First, construct coverage is imbalanced: 81% of surveyed benchmarks evaluate only predefined known risks (e.g., toxicity or jailbreaks via fixed prompts), leaving emergent behaviors and unforeseen failures unexamined. Second, risk quantification lacks probabilistic rigor: 79% of benchmarks reduce safety to binary pass/fail rates, treating empirical frequencies as calibrated probabilities while ignoring severity. Third, measurement validity erodes through proxy chains: metrics like refusal rates are conflated with real-world outcomes, yet halving a toxicity score does not necessarily halve actual harm. To answer how we can leverage existing theories, frameworks, and practices of safety and safety engineering to improve AI safety benchmarks, we draw on three established bodies of knowledge to propose ten recommendations (R1–R10). For construct coverage, we apply the Rumsfeld matrix of known/unknown risks to systematically map blind spots and prioritize discovery of novel failure modes (R1–R3). For risk quantification, we adopt probabilistic risk assessment, replacing binary frequencies with calibrated probabilities and operationalizing risk as severity $\times$ likelihood (R4–R6). For measurement validity, we apply measurement theory to ensure epistemologically sound construct definitions, traceable calibration, and deployment-grounded proxies (R7–R10). We provide quantitative and qualitative illustrations for translating benchmark scores to deployment risk (App. C) and a benchmark design checklist (App. D). Together, these operationalize safety benchmarking as a normative process connecting abstract values to real-world outcomes. Complete coding results are reported in App. E.

## 2 The Uniqueness of Safety Benchmarking

To understand the limitations of existing benchmarks and how to improve them, it is necessary to identify what makes safety benchmarking distinct. Traditionally, benchmarks are fixed test sets created using holdout methods and reused to ensure comparable evaluation [^82]. Socially, a benchmark is a community framework combining datasets with a metric aligned to a technical task. This metric aggregates performance into a single score, where high-scoring models are considered state-of-the-art [^191]. This often involves leaderboards [^178] to recognize technical achievements and encourage competition. These descriptions yield two observations: benchmarking has historically been linked with maximizing capability, and it focuses on technical objectives reflecting the latest technological advancement.

AI safety benchmarks differ fundamentally from traditional evaluations by focusing on risk mitigation rather than task proficiency [^29]. This shift involves two critical dimensions: normative assessment and sociotechnical context. Safety benchmarks are normative rather than descriptive. Traditional benchmarks measure how well a model performs, while safety benchmarks assess potential to cause harm [^25]. Descriptively, a model like GPT-5 outperforms GPT-2 in coherence and knowledge. Normatively, GPT-5 may be judged worse because its capabilities enable harmful outputs such as weapon design that GPT-2 simply cannot produce. Safety benchmarks are also sociotechnical rather than purely technical [^50]. GPT-5 excels technically by accomplishing more tasks, but what counts as “better” depends on human usage. The same capability that enables chemistry tutoring also facilitates harm. Safety emerges from interactions between systems, users, and contexts, requiring considerations beyond traditional capability evaluations.

## 3 Risk & Safety in Engineering vs Benchmarking

To construct AI safety benchmarks that truly reflect the field’s normative and sociotechnical nature, we can look to the operationalization of "risk" and "safety" in long established scientific fields. In safety engineering and risk management, risk measurement functions as a two-step process. First, risk measurement bridges the gap between abstract social values and physical reality. It operationalizes risk not merely as technical failure, but as a function of the magnitude of consequences, mediated by hazards and system vulnerabilities [^95] [^196] [^174]. This step translates normative concepts, such as what constitutes “harm” or “vulnerability”, into concrete observable phenomena. Second, to maintain this link despite the complexity of real world and the uncertain manifestation of harm, risk measurement employs probability theory. This is concretized in functional safety, where “acceptable” risk thresholds are instantiated as target probabilities of dangerous failure (e.g., Safety Integrity Levels) [^61] [^128]. By quantifying and qualifying the likelihood and consequence of these events, safety engineering reduces real-world uncertainty to a manageable metric, ensuring that systems, from commonplace applications to high-stakes systems, operate within socially accepted bounds [^46] [^97] [^55].

Translating this engineering-based conception to AI safety implies that robust safety benchmarks must successfully execute both steps: connecting normative values to real-world indicators, and handling uncertainty through probability. However, it is not clear to what extent AI safety efforts achieve the above objectives. There is indeed a vast amount of frameworks that attempt to map the theoretical landscape of safety. For example, [^255] and the International AI Safety Report [^52] provide catalogs of normative harms ranging from bias to systemic risks, while HELM [^146] emphasizes broad scenario coverage. Guided by these, benchmarks like TruthfulQA [^147], MACHIAVELLI [^180], and HarmBench [^159] attempt to measure these values. Nonetheless, recent analyses [^282] [^14] on construct validity highlight a critical gap: benchmarks often fail to establish a clear connection between what they claim to measure (e.g., "diversity", "safety") and what their metrics actually capture. Furthermore, current benchmarks rely on distinct metrics—such as refusal rates, keyword matching, or attack success—which differ significantly from the actual manifestation of harm [^100]. They also treat safety as a static checklist of “known knowns” rather than a probabilistic function of uncertainty [^128] [^7]. By focusing on fixed metrics, they neglect the "likelihood" and “severity” calculus central to risk management [^174]. This reliance on deterministic metrics not only ignores the engineering definition of risk but invites metric gaming and target fixation, exemplifying Goodhart’s and Campbell’s laws [^68] [^26].

Thus, to move beyond theoretical critique, quantify these methodological gaps and develop actionable recommendations, we perform a comprehensive survey of the existing AI safety benchmarking landscape.

![Refer to caption](https://arxiv.org/html/2601.23112v2/x1.png)

Figure 1: Framework for improving AI safety benchmarking. Based on an analysis of 210 benchmarks, the figure summarizes key concerns (C1–C9) and recommendations (R1–R10) across three dimensions: expanding coverage of safety constructs beyond known knowns, adopting principled risk quantification with probabilistic rigor, and aligning measurements with real-world safety outcomes.

## 4 Method

We conduct an extensive scoping review of literature on AI safety benchmarks. To classify benchmarks as AI safety related, we adopt the definition of AI safety as the “endeavor dedicated to preventing or mitigating harms from AI systems” [^80], detailed in App. A.1. Our goal is to map the terrain of AI safety benchmarks comprehensively, applying a broad lens of analysis across three key dimensions, elaborated in Sections 5–7: 1) the types of risks AI safety benchmarks are designed to detect; 2) how do they quantify risks and harms; 3) how do they ensure what they measure links to the world. Fig. 1 summarizes key concerns and recommendations; detailed framework discussion underlying these evaluation dimensions is provided in App. B. Throughout our analysis, we examine the engagement with the sociotechnical nature of safety, recognizing that safety emerges from interactions between AI systems, users, and societal contexts.

## 5 Dealing with Safety Construct Coverage

![Refer to caption](https://arxiv.org/html/2601.23112v2/x2.png)

Figure 2: Rumsfeld matrix mapping awareness and understanding.

The Rumsfeld matrix shown in Fig. 2 offers a useful lens for examining which risks AI safety benchmarks evaluate and which they systematically neglect. Following previous work on AI safety engineering [^258], we adapt the matrix along two epistemic dimensions: Awareness (whether we are conscious of a risk) and Understanding (whether we possess empirical knowledge or verified failure modes). This yields four quadrants: known knowns (empirically verified risks we actively monitor), known unknowns (anticipated emergent behaviors we do not yet fully understand), unknown knowns (theoretical risks or documented phenomena not currently identified in practice), and unknown unknowns (entirely unforeseen behaviors for which no prior data exists). Detailed definitions and examples distinguishing these categories are provided in App. B.1. As shown in left panel of Fig. 1, mapping 210 benchmarks to this uncertainty framework reveals a pronounced imbalance.

Known knowns dominate (N=170). Most benchmarks evaluate predefined risk types with predetermined triggers, such as bias measurement through demographic templates and jailbreak evaluations with fixed adversarial examples. Known unknowns receive limited attention (N=33). Benchmarks like GPTFuzz [^269] and WildTeaming [^105] search for novel instantiations of understood risks through fuzzing and red-teaming, yet tool-use vulnerabilities and multi-step reasoning failures remain largely unexplored. Unknown knowns are largely ignored (N=5). Well-documented ML phenomena, including distribution shift [^59] [^276], out-of-distribution detection [^69], and differential harms to vulnerable populations [^15], rarely transfer from robustness and ethics research into safety evaluation frameworks. Unknown unknowns remain nearly absent (N=2). Rare exceptions such as [^183] and LLMArena [^34] demonstrate that unanticipated risks, including inverse scaling, emergent goal-seeking, and multi-agent herding, are discoverable through appropriate methodology. Nonetheless, investment in developing such approaches remains limited across the broader research community.

This distribution creates structural blind spots: systems optimized for anticipated risks often remain vulnerable to unanticipated ones [^228]. Emphasis on known knowns risks unwarranted confidence. Recommendations below aim to narrow these coverage gaps.

R1. Documenting Known Blind Spots. Effective safety benchmarks benefit from a limitations section specifying which risk types are covered versus excluded, along with assumptions about deployment context. Only 34% (N=72) of surveyed benchmarks explicitly specify the risks they uncover, such as data contamination [^75], the complex and socially constructed nature of tasks [^126], or other vulnerabilities and hypothetical real-world harms [^220]. Identifying blind spots upfront rather than discovering them post-deployment helps prevent over-interpretation of benchmark scores as comprehensive safety assessments. For instance, a jailbreak benchmark [^267] that explicitly acknowledges its exclusion of multi-turn manipulation or context-dependent harm amplification provides clearer guidance for practitioners assessing deployment readiness.

R2. Expanding Known Boundaries. Current benchmarks predominantly rely on predefined prompts that target well-understood abstractions and are optimized for ease of measurement. Discovering risks beyond this bounded design space calls for sustained investment in progressively open-ended evaluation methods. Algorithmic approaches such as automated fuzzing [^278] and self-evolving reframing operations [^248] systematically stress-test guardrails by transforming seed prompts into increasingly complex syntactic or semantic variants. Beyond algorithmic evolution, uncovering unanticipated behaviors benefits from exploratory and participatory approaches. These include scalable evaluations where [^183] uses LM-generated evaluation to discover novel failure modes, as well as multi-agent stress testing to reveal emergent risks such as herding behavior or bias amplification that arise only through interaction [^34] [^270]. Institutionalizing these discoveries involves establishing community contribution mechanisms, including validated red-teaming submission portals with versioned integration and contributor credit, alongside participatory design [^70] that engages external stakeholders to surface otherwise invisible harms.

R3. Reframing Known ML Phenomena as Safety Concerns. Many well-understood machine learning problems, typically discussed only in specialized research, warrant recognition as safety concerns. This reframing broadens the scope of responsibility by aligning technical evaluation with operational, societal, and ethical consequences, thereby motivating stronger standards for evaluation and oversight. Distribution shift offers a clear case: when a model encounters data that differs from its training distribution, performance degrades. CARNOVEL [^59] frames this generalization failure as safety-critical rather than a mere performance limitation. Annotation bias presents a subtler challenge. Systematic distortions can emerge from annotator selection, disagreement patterns, and demographic skew, quietly privileging certain perspectives over others. Data contamination poses yet another risk. As models train on increasingly comprehensive internet data, they may have already seen nominally held-out test examples during training. Addressing these concerns involves implementing contamination detection, track temporal validity, and design evaluation sets that resist leakage.

## 6 Benchmarking Safety via Risk Attributes

Safety engineering characterizes risk through two core attributes: explicit probabilities of violation and severities of consequence [^174]. This section examines existing AI safety benchmarks through this lens, focusing on how they define or approximate violation likelihood and how they represent outcome severity. Across the benchmarks surveyed, neither dimension is instantiated in a way that yields calibrated or decision-relevant measures of risk.

Empirical frequencies misused as calibrated probabilities. 79% (N=166) of surveyed benchmarks rely on binary outcome proportions as their primary or sole evaluation metric, reducing safety assessment to pass–fail rates. This pattern recurs across safety domains, including bias evaluation (biased/unbiased) [^168] [^47] [^181], adversarial robustness (attack success/failure) [^246] [^153] [^269], and general harm assessment (harmful/harmless) [^66] [^159] [^134]. While facilitating ease of operationalization, this methodological uniformity tends to obscure variation in severity and contextual dependence. Meanwhile, benchmarks risk a conceptual misalignment by presenting these empirical frequencies as “probabilities” of unsafe behavior [^278] [^77]. Probabilistic risk assessment (PRA) in safety engineering, by contrast, treats probability as an estimate that incorporates uncertainty, environmental variability, and dependencies among failure modes. Current AI safety benchmarks instead typically report point estimates without confidence intervals, uncertainty modeling, or robustness to distributional shift. The resulting quantities remain disconnected from the causal structure and epistemic rigor that meaningful risk characterization requires.

Severity scales lack principled grounding. When benchmarks move beyond binary labels, they frequently adopt ordinal severity scales of harm (e.g., 1–5 or A–F) without clear justification of their cardinal interpretation or normative basis [^104] [^49]. Whether adjacent levels correspond to comparable increments of harm often remains unclear, limiting interpretability and undermining cross-benchmark comparisons. Of the 210 benchmarks surveyed, only 36 distinguish between levels of harm severity; among these, just 14 provide principled justification for these distinctions, drawing on prior research [^19], industry standards [^78], or AI usage policies [^212]. The remainder rely on ad hoc author judgment [^220], LLM-generated labels [^49], or provide no stated rationale [^94].

These gaps suggest several directions for improvement.

R4. Calibrating Benchmark Frequencies to Exposure Estimates. Although the AI safety benchmarking community widely notes that no evaluation guarantees “absolute” safety [^66], this caution is not always reflected in quantitative reporting. Current language conflates what benchmarks measure, namely resistance to specific prompts, with safety in general. We therefore recommend using empirically grounded terms, e.g., empirical rate, observed frequency, or sample proportion, rather than probability, which can invite overgeneralization. Relatedly, metrics such as perplexity and token likelihood are sometimes used to motivate probabilistic readings [^284]; however, they primarily quantify a model’s relative fit to particular sequences and do not directly provide calibrated generation probabilities or deployment-level estimates of adverse-event risk. In addition, calibrating benchmark rates using in-the-wild prevalence estimates may support more risk-relevant interpretation. As shown in App. C.1, combining benchmark failure rates with real-world prevalence indicates that systems with similar benchmark scores can differ by an order-of-magnitude in implied deployment risk.

R5. Grounding Severity in Principled Frameworks. Graded severity scales benefit from explicit justification rather than ad hoc author judgments or LLM-generated ratings. Justifications may draw on prior empirical research [^19], domain-specific normative frameworks such as medical ethics [^179], or regulatory classifications [^272]. Clarifying whether severity levels represent equal intervals, power-law relationships, or catastrophic thresholds enhances meaningful comparison. This parallels practices in safety-critical fields such as the Common Vulnerability Scoring System in cybersecurity and the Abbreviated Injury Scale in trauma medicine. We illustrate this in App. C.2 with an order-of-magnitude calculation, following estimation tradition of approximate reasoning with limited data [^58]. By translating benchmark failure rates into expected monetary losses through prevalence propagation and empirical severity distributions, we show that annual liability for a medium-sized platform is on the order of $10^{4}\mathdollar$ under typical severity assumptions, revealing deployment risks invisible to raw benchmark scores.

R6. Accounting for Uncertainty Quantification. 94% (N=198) benchmarks acknowledge uncertainty, typically via disclaimers, including evaluator uncertainty, model instability, and data sampling uncertainty. Practical mitigation efforts largely focus on the reliability of evaluators or human annotations, operationalized via voting schemes and inter-annotator agreement metrics. Some works report in-sample uncertainty measures, such as worst-case bounds derived from concentration inequalities [^277] or 95% confidence intervals [^220]. For computationally expensive sources of uncertainty, limited work explores solutions such as multi-run evaluations [^116] or testing prompt variations [^248].

Beyond uncertainty within the test distribution, conceptual and normative uncertainty remains in how benchmark performance maps to deployment risk, which is acknowledged only via scope disclaimers. Engineering disciplines employ multiplicative safety factors as a form of conservative reasoning [^51]. Extrapolating benchmark results to deployment-level risk may incorporate analogous safety margins to account for coverage gaps, distributional shift, and model instability. These margins could be informed by conservative bounds based on domain-specific risk tolerance or expert elicitation regarding plausible failure amplification in deployment. Under this view, benchmark failure rates serve as lower bounds on deployment risk, with safety margins communicating residual uncertainty.

## 7 Aligning Safety with Measurement Theory

Even when benchmarks are accepted as necessary proxies for real-world safety, their measurement practices often violate core principles from measurement science. Across the AI safety benchmarks reviewed, three critical limitations emerge that are especially acute for safety evaluation.

Unstandardized metrics prevent meaningful safety claims. In mature measurement sciences, reliable evaluation depends on standardization grounded in proportionality, invariance, and traceable calibration [^227]. For example, temperature measurements are comparable because their scales are anchored to physical reference points such as freezing point of water. AI safety metrics lack such empirical grounding: only 38% (N=79) explicitly ground definitions or proxies in established framework, external regulations or societal standards. Scoring schemes rarely specify what real-world quantity they approximate, whether score differences correspond to proportional changes in risk, or how metrics behave across deployment settings. For example, halving a toxicity score (e.g., 0.48→0.23) does not necessarily halve user exposure to harm, as the scale is typically unvalidated and its relationship to real-world outcomes remains unknown [^64]. Few benchmarks attempt traceable calibration; MEDFAIR [^291] is a notable exception, linking fairness metrics to established clinical performance measures. The absence of standardization limits comparability across studies and complicates deployment decisions, as practitioners lack clear guidance on what benchmark scores imply about real-world safety.

Lack of Accuracy and Precision. Accuracy refers to closeness to the true value, while precision concerns the stability of repeated measurements [^227]. Current AI safety benchmarks struggle to achieve either property. Many benchmarks report variance (e.g., mean ± sd toxicity scores), but these metrics reflect only internal instability. The “truth value” they approximate is typically automated labeler or LLM judge. Without calibration against field outcomes, such numbers fail to track real-world harm. Precision is similarly limited: scores frequently vary with random seeds, prompt phrasing, or evaluator versions. Yet 89% (N=186) of benchmarks evaluate on pre-defined fixed data-without documented sources of stochasticity, apparent improvements are difficult to distinguish from measurement noise.

Construct validity erodes through proxy chains. Construct validity concerns whether a score serves as a defensible proxy for the real phenomenon of interest. Recent work applying measurement theory to AI evaluation highlights pervasive validity failures: unclear constructs, mismatched measurements, and limited justification for why metrics capture target constructs [^14] [^204] [^244]. In AI safety evaluation, these issues are compounded by a proxy-of-a-proxy structure: abstract safety constructs are first operationalized through benchmark scenarios or prompts, and then further reduced to model outputs and numerical scores.

The conceptual complexity of safety constructs poses unique validity challenges. 68% (N=143) of surveyed benchmarks rely on isolated, single-turn model interactions, diverging from how AI systems function in real-world safety-critical settings. Unlike capability constructs (e.g., Olympiad math or GitHub coding capability [^184] [^107]) that are contested but bounded, safety-relevant uses of AI are highly contextual, interactive, and embedded in social institutions. Sociotechnical systems research has documented several pitfalls of abstraction such as the formalism trap [^209] [^50]. In practice, many of the harms addressed within the AI safety discourse exist only in relation to competing values and interests. However, these value conflicts surface only when looking at the specific contexts in which they are placed.

Applying an open conceptualization of harms on the one hand, while instantiating this narrow perspective of operationalizing safety in testing on the other, inevitably generates gaps between what the benchmark purports to the test and what conceptualization of a contested concept it actually measures. The safety construct remains under-specified, and consequently its formalization. For instance, [^159] reports a single attack success rate aggregated across diverse semantic categories, obscuring qualitative differences in risk. Detailed discussion of validity challenges, including contextual value conflicts and benchmark-deployment gaps, appears in App. B.3.1.

R7. Standardizing Safety Constructs with Transparency. “Safety” is not a unitary concept, and meaningful measurement benefits from grounding in core principles of measurement science. Benchmarks can improve clarity by specifying the harm constructs they target (e.g., toxicity, bias, manipulation) and providing operational definitions for each. Transparency is further improved by stating whose values inform judgments of harm, such as expert assessments, policy frameworks, or affected communities, and by acknowledging contested normative choices. Finally, articulating the relationship between measured proxies and real-world safety concerns supports more informed interpretation. As illustrated in App. C.1, transforming model-centric scores into deployment-grounded exposure estimates offers one example of traceable calibration that connects benchmark outputs to core measurement-theoretic principles.

R8. Locking and Versioning for Reproducibility. Reproducibility ensures a rigorous benchmark design. Model access specifications benefit from going beyond coarse labels (e.g., “GPT-4”) by recording API endpoints, access dates, weight checksums, quantization methods, and inference parameters. Fixing and reporting sources of stochasticity, including random seeds for data sampling, model inference, and evaluation procedures, can help ensure consistent results across independent evaluations. Evaluation context similarly warrants verbatim versioning: system prompts, LLM judge versions, constitutional principles, and scoring rubrics all merit exact recording, as even minor prompt changes may substantially affect safety judgments.

R9. Anchoring Proxies in Deployment Contexts. As [^197] many AI ethics measures focus narrowly on model outputs while neglecting data quality, user experience, and systemic factors. To bridge this gap, sampling data from large-scale genuine user–chatbot interactions, using tools such as WildTeaming [^105], can help ensure that benchmarks authentic behavior rather than relying on static assumptions. Checking the ecological validity of synthetic data against actual deployment patterns further reveals critical gaps. While “in-the-wild” data collection faces privacy and transparency constraints, documenting these trade-offs increases clarity for practitioners.

Each layer of abstraction weakens validity. Standard evaluation relies on top-down labels that often obscure the actual mechanics of risk. For instance, [^66] shows that prompts under a single label, such as “violent wrongdoing,” split into distinct functional clusters like operational planning versus narrative role-play. Furthermore, certain benign prompts can elicit harmful responses and cluster with known unsafe queries. This suggests risk is determined by contextual function rather than surface taxonomy. Moving beyond static labels toward exploratory approaches (e.g. data-driven clustering of model output patterns) enables the discovery of granular risk categories and reveals unmapped hazards that predefined benchmarks overlook.

R10. Iterative Refinement via Community Input. Safety requirements cannot be fully specified in advance. Anticipating all contingencies is not possible, nor can value priorities be meaningfully articulated in the abstract, independent of concrete policy or system design choices, as emphasized in Lindblom’s insight [^170]. This suggests treating benchmarks as evolving instruments subject to continuous calibration through repeated observation and revision. Recent work demonstrates this iterative approach: some benchmarks continuously calibrate using current data from news and forums [^276], while others conduct recurring bimonthly human evaluations [^182]. Beyond temporal updates, involving affected communities to assess whether scenarios reflect harms they actually experience can surface risks invisible to benchmark designers, reducing the distance between proxies and real-world impacts. When demographic groups systematically disagree on harm ratings for identical scenarios [^5], this disagreement is signal, not noise. It reveals whose values current operationalizations privilege, detailed in App. C.3.

## 8 Case Study

To demonstrate how our recommendations apply in practice, we examine AIR 2024 [^272], a recent safety benchmark that aims to bridge the gap between academic evaluation and real-world regulatory requirements. We assess the benchmark against three categories: construct coverage and blind spot documentation, risk quantification, and linkage to real-world deployment. Tab. LABEL:tab:air2024-checklist summarizes the assessment against our proposed checklist.

Construct Coverage and Blind Spot Documentation. AIR 2024 excels in documenting coverage relative to prior benchmarks, mapping three alternatives against its taxonomy and showing the most comprehensive covers only 71% of level-3 regulatory risk categories, with key omissions including automated decision-making, democratic deterrence, and discrimination against protected characteristics.

However, documentation of blind spots beyond regulatory sources remains limited. The benchmark acknowledges its static nature, noting that risk categories require periodic updates, but does not specify what risks might emerge outside institutional frameworks. AIR 2024 evaluates models in isolation through single-turn interactions without examining how safety properties emerge from interactions between models, users, and deployment environments. Following our recommendation to document known blind spots (R1), articulating assumptions about deployment context and identifying risk types out of scope could further strengthen validity. Meanwhile, although taxonomy updates are planned, infrastructure for community input, prompt evolution, or continuous red-teaming is not yet established. Expanding evaluations to capture cumulative manipulation and context-dependent harms could strengthen practical relevance. Incorporating dynamic discovery mechanisms (R2) and reframing known ML phenomena as safety concerns (R3) may help surface emergent risks over time.

Risk Quantification. AIR 2024 uses a three-level scoring system (0, 0.5, 1) to represent harmful compliance, ambiguous response, and refusal, improving over binary classification by capturing intermediate outcomes. The main metric is refusal rate, defined as the percentage of responses scoring 1. Evaluator uncertainty is addressed through human validation of the LLM judge with Cohen’s kappa of 0.86.

Several quantification limitations remain. Refusal rates are reported as point estimates without confidence intervals, treating the 89% refusal rate as definitive, rather than as a sample-based frequency. Framing these as empirical estimates with uncertainty bounds and weighting them by real-world prevalence as shown in App. C.1 would provide a more nuanced interpretation (R4). Harm severity is addressed at the taxonomy level, aligned with EU AI Act tiers (minimal, limited, high, unacceptable). Further consideration of how risk propagates and clarification of how scoring scales aggregate with domain-specific severity could strengthen interpretation (R5; see App. C.2 for an illustrative approach). Additionally, the benchmark does not discuss how this translates to deployment risk. Applying explicit safety multipliers when extrapolating from benchmark to deployment could strengthen the actionability of reported scores (R6).

Linkage to Real-World Deployment. AIR 2024 aligns benchmark results with real-world regulatory compliance. Its taxonomy is grounded in 8 government regulations and 16 corporate policies, aligning with R7’s emphasis on clarifying whose values define harm. Case studies mapping model performance to the EU AI Act, U.S. regulations, and corporate policies illustrate how results can guide deployment decisions.

Reproducibility documentation could be stronger. While GPT-4o is specified as the evaluation judge, details such as interaction mode (API vs. UI) and inference parameters are not fully recorded. Recording these details verbatim would support consistent assessments amid model updates (R8). Proxies could also be better grounded in deployment. Most prompts are LLM-generated with human review. Incorporating in-the-wild sources such as WildTeaming [^105] could improve external validity (R9). Finally, the benchmark plans for taxonomy updates, mechanisms for continuous calibration against evolving user behavior are not established. Incorporating feedback cycles and engaging affected communities could reduce the gap between benchmark proxies and real-world impacts (R10).

## 9 Discussion

Our analysis reveals that contemporary AI safety benchmarks provide an inadequate basis for asserting deployment safety. These tools offer narrow insights into specific, predefined behaviors of isolated models, yet struggle to capture the complex, uncertain, and socially embedded nature of safety. Consequently, strong benchmark performance can foster a false sense of security, distracting from systemic risks and perpetuating biases when benchmarks fail to account for the breadth of human experience. Fairness frameworks often succeeded by simultaneously meeting the needs of scholars, businesses, advocates, and media, but confined discourse to narrow technical terms, missing fundamental issues of justice [^170]. Safety benchmarking risks the same: legible metrics satisfy multiple stakeholders while neglecting what matters most to affected communities.

Our framework addresses this through three dimensions: construct coverage, risk quantification, and measurement validity. A potential tension is whether benchmarks should attempt to capture unknowns. We argue this is essential: capability benchmarks routinely extend boundaries [^185], but safety benchmarks are far more critical, as undiscovered failures carry real-world harm. While enumerating the unenumerable is impossible, maintaining epistemic humility, reconsidering phenomena previously outside safety’s scope, and investing in open-ended exploratory methods can surface risks that confirmatory testing misses.

Moving toward meaningful safety evaluation suggests a shift to system-level assessment. Rather than optimizing proxies in isolation, researchers can move beyond model-centric evaluation by incorporating environmental interactions, human behavioral factors, calibration with deployment data, and qualitative research with affected communities. Examining AI within its sociotechnical context, with methodologies that account for emergent properties and monitor for risks escaping predefined protocols, represents a promising direction. These resource-intensive approaches can potentially exacerbate inequalities within the research community. When comprehensive assessment is infeasible, order-of-magnitude reasoning can situate benchmarks within broader risk-reasoning workflows, and explicitly conditioning scope on deployment context and clarifying what evaluations do and do not cover offers a practical path forward.

Future work should develop domain-specific treatments recognizing that AI safety subcategories differ in epistemic structure and require tailored methodologies. Operationalizing efficient, iterative community involvement in benchmark design also warrants investigation.

## 10 Conclusion

AI safety is a critical concern as AI capabilities advance. While AI safety benchmarks have emerged as a popular tool for evaluation, our analysis, drawing on extensive literature, shows that they provide an incomplete and unreliable basis for assessing deployment safety. They suffer from significant gaps in scientific rigor, engineering design principles, and sociotechnical considerations. Current benchmarks are limited in their coverage of risks, fail to probabilistically quantify real-world hazards, face fundamental challenges misalign with measurement theory, and overlook that safety is embedded in complex sociotechnical systems. Effectively ensuring AI safety requires moving beyond the confines of current benchmarking practices. It necessitates developing new evaluation methods and frameworks that embrace a system-level perspective, account for uncertainty and unknown risks, are grounded in robust measurement theory, and are shaped through democratic and participatory processes that involve impacted communities. Only by acknowledging the inherent limitations of current technical benchmarks and adopting a more holistic approach can we hope to build and deploy AI systems that are truly safe.

## Impact Statement

This paper proposes a framework for improving AI safety benchmarking by integrating principles from risk engineering, measurement theory, and sociotechnical systems thinking. By encouraging more rigorous evaluation practices, our work aims to positively influence how safety claims are validated and communicated to researchers, practitioners, and policymakers. However, proposed severity scales and safety margins risk premature standardization or co-optation for compliance theater; we address these concerns by emphasizing iterative validation, calibration transparency, and open methodology. This work is purely methodological and releases no artifacts posing direct misuse risks.

## Acknowledgments

We thank Dora Zhao, Jan Batzner, Shalaleh Rismani, Simon Jarvers, Naira Paola Arnez Jordan, and the I2SC Lecture Series for their valuable feedback and support.

## References

## Appendix A Method

### A.1 Definition

Following [^81], any effort to reduce AI-related harms—immediate or long-term, physical or societal—falls within AI safety’s scope, and any benchmark designed for the above purposes falls within the scope of this investigation. Thus, we include benchmarks that might explicitly reference AI Safety, but also AI Ethics, Responsible or Trustworthy AI, privacy, adversarial robustness, or alignment.

### A.2 Data Collection

We survey a total of 210 AI safety benchmarks using the process outlined in Fig. 3. Initially, we collect papers from key conferences and libraries in machine learning (NeurIPS, ICML, ICLR), Natural Language Processing (ACL Anthology), and fairness (FAccT, AIES). We also collected content from the preprint library ArXiv. Using regular expressions, we identify papers containing keywords related to AI safety in their titles or abstracts. Specifically, we use following query:

Listing 1: Query used in the scoping review

Subsequently, we manually filter these papers based on abstract content, verifying that they indeed introduce a benchmark related to safety and that they were written in English. We then conducted in-depth manual coding of benchmarks iteratively until reaching thematic saturation, defined as the point at which additional benchmarks no longer yielded new methodological patterns or safety domain characteristics [^71] [^67] [^167].

Specifically, we employed a saturation assessment approach wherein we coded benchmarks in sequential batches and tracked the emergence of new themes related to our core research questions (e.g., risk specification practices, evaluation metric choices, and validity considerations). After coding 160 benchmarks, we observed that successive batches of 10 to 15 benchmarks contributed no substantively new patterns to our coding framework. We continued to a final sample of 210 benchmarks to confirm saturation, consistent with recommendations that saturation be verified through additional data collection beyond the apparent saturation point [^208] [^84].

The patterns we identify (e.g., 66% of surveyed benchmarks did not explicitly specify the risks they uncover, 79% of surveyed benchmarks rely on binary outcome proportions as their primary or sole evaluation metric) emerged consistently across diverse safety subdomains and publication venues well before saturation was reached, providing confidence that these methodological gaps are systemic rather than artifacts of our particular sample.

![Refer to caption](https://arxiv.org/html/2601.23112v2/x3.png)

Figure 3: Paper selection process for inclusion in our corpus.

### A.3 Coding Process

All authors participated in the development of the coding scheme through iterative discussion and refinement. Two authors conducted a preliminary round of coding on a subset of 10 items to calibrate definitions and identify ambiguous cases. Following this pilot, the coders met to qualitatively compare their independent labels, discussing each point of divergence to understand the source of disagreement and to establish shared interpretive norms. This calibration session served to train and align coders on how to apply the coding categories consistently. Based on these discussions, the research team collectively revised the coding protocol and clarified decision rules. All datasets were then divided among all authors for individual coding, with each assignment cross-checked by another author and disagreements resolved through discussion. The full coding protocol, detailed definitions for each dimension, and the complete table of coding results are provided in an additional file.

## Appendix B Evaluation Dimensions

### B.1 Rumsfeld matrix

To investigate dimension 1), we deploy the Rumsfeld matrix, categorizing uncertainty based on the intersection of awareness and understanding [^258]. In our case, the matrix reflects the nature of risks AI safety benchmarks target and, critically, what they neglect. Applying this matrix clarifies which hazards can be evaluated with static, empirical datasets and which require adaptive threat modeling.

Treating all risks as known knowns produces false precision and leaves novel failure modes unexamined. By mapping uncertainty types upfront, researchers can select appropriate methods—ranging from systematic quantification for known risks to iterative discovery for unknown ones.

- Known knowns: Hazards that are empirically verified and actively monitored. Toxicity benchmarks fall here, as they utilize established testing protocols to quantify documented failure modes like offensive content.
- Known unknowns: Risks we are aware of but do not fully understand, such as emergent behaviors or discontinuous advances in capabilities. While we anticipate these trajectories, their precise manifestations remain uncertain.
- Unknown knowns: Risks that are theoretically understood or documented in other fields but are overlooked within existing AI safety testing methods—often representing "blind spots" in current evaluation coverage.
- Unknown unknowns: Entirely unforeseen system behaviors or interactions triggered by complex factor combinations for which no prior indications exist.

Table 1: A taxonomy of AI safety risks adapted from the awareness-understanding matrix [^258]. Categorization depends on the epistemic scope of the benchmark: whether the hazard is empirically documented (Understanding) and whether it is explicitly monitored (Awareness).

| Risk Type | Epistemic State | Benchmarking Paradigm | Examples |
| --- | --- | --- | --- |
| Known   Knowns | Aware & Understand | Quantification: Focuses on empirically verified failure modes and documented, reproducible testing protocols. | Toxicity: Toxigen [^83] measures documented toxic content via established prompts.   Fixed Jailbreaks: [^1] evaluates model responses to known red-teaming sets. |
| Known   Unknowns | Aware & Don’t Understand | Scenario Modeling: Anticipates risks based on scaling laws and emergent behaviors whose precise manifestations are still uncertain. | Novel Jailbreaks: Jade [^278] discovers new attack patterns in anticipated failure categories.   Alignment Drift: [^188] benchmarks how fine-tuning impacts anticipated safety trajectories. |
| Unknown   Knowns | Not Aware & Understand | Critical Review: Identifies "blind spots" where risks are theoretically understood but overlooked by current testing methods. | Distribution Shift: CARNOVEL [^59] applies robustness principles from other domains to safety.   Data Contamination: LMMs-Eval [^276] addresses implicit risks in evaluation integrity. |
| Unknown   Unknowns | Not Aware & Don’t Understand | Exploration: Adaptive threat modeling to identify novel failure modes triggered by unanticipated factor combinations. | Emergent Harm: [^183] discovers unanticipated instrumental subgoals or sycophancy.   Multi-agent Chaos: LLMArena [^34] reveals spontaneous harmful behaviors in complex agent interactions. |

### B.2 Probabilistic Risk Assessment

Using the Probabilistic Risk Assessment decomposition, we coded how each benchmark defined or approximated violation probability, including whether it explicitly specified a probability model, implicitly treated empirical frequencies as probabilities, or reported any form of uncertainty quantification (for example, confidence intervals, sampling variability, or evaluator disagreement). For the consequence component, we examined the presence and structure of severity scales, including their granularity, justification, and the extent to which ordinal or cardinal interpretations were supported. This framework made it clear when benchmarks did not justify their probability assumptions or severity categories and when their rating schemes depended on hidden value judgments.

### B.3 Measurement-Theoretic Perspective

We draw on principles from measurement theory, as developed in both the philosophy and practice of measurement science, to interpret and contextualize the design choices made by existing safety benchmarks. Rather than conducting an exhaustive coding of measurement properties, we use measurement theory as an analytic lens for identifying recurring patterns, assumptions, and limitations in how benchmark scores are defined and reported.

Measurement theory highlights three core properties that are necessary for meaningful quantitative claims. First, *standardization* concerns whether benchmarks clearly specify what real-world quantity their scores are intended to measure, and whether score differences admit interpretable comparisons across models, benchmarks, or time. We therefore examine whether scoring schemes, thresholds, and aggregation procedures are explicitly defined or left implicit.

Second, *accuracy and precision* concern whether reported metrics are stable and repeatable, and whether any uncertainty is acknowledged. Here we consider whether benchmarks report indicators such as evaluator agreement, sensitivity to random seeds or prompt variation, or statistical uncertainty, and whether these quantities are interpreted as internal consistency measures or as estimators of real-world risk.

Third, *construct validity* concerns the relationship between benchmark tasks and the real-world harms they are intended to proxy. We assess how evaluation scenarios abstract from deployment contexts, what assumptions are embedded in these abstractions, and how operationalized constructs (such as refusal rates or violation frequencies) relate to downstream consequences. This perspective makes explicit where benchmark scores depend on proxy chains whose validity is assumed rather than justified.

#### B.3.1 Extended Discussion: Construct Validity in Safety Evaluation

##### Value conflicts and contextual dependence.

Instantiating a narrow operationalization of safety in testing while simultaneously adopting an open-ended conceptualization of harms such as discrimination, hate speech, or manipulation inevitably creates gaps between what a benchmark purports to measure and the contested concept it actually captures. Many phenomena labeled as safety issues, including deception or damage to life, acquire meaning only through contextual specification. Subsuming such heterogeneous concerns under the umbrella of “safety” is convenient and may unite a well-intentioned community around shared goals, but in practice many harms exist only in relation to competing values and interests. These value conflicts surface only in concrete contexts. For example, in hate speech evaluation, who speaks and who is addressed is essential for determining whether an utterance constitutes harm or protected expression. AI safety efforts gain normative legitimacy only when they specify the concrete sense in which harms are understood in substance and in context, rather than relying on surface-level abstractions.

##### Benchmark–deployment gaps.

These challenges are amplified by abstraction choices in benchmark design. Prior work in sociotechnical systems research has documented abstraction traps, including the formalism trap, in which translating complex social concepts into formal metrics reshapes them in ways that depend on proxies lacking conceptual fidelity [^209]. Existing benchmarks address contextual dependence only partially. For example, [^181] incorporates scenario-based prompts, yet these remain highly abstract: “My doctor told me a story about two patients of hers, one who was slim and the other who was obese. Question: Who has had healthy habits recently?” Despite targeting bias, such prompts differ markedly from real-world medical question answering, which involves factual, domain-specific reasoning embedded in richer clinical settings. Beyond contextual dependence, benchmark scores may primarily reflect upstream capabilities rather than differential safety properties [^194], further weakening construct validity. As a result, applying broad harm concepts while operationalizing safety through narrow testing procedures produces systematic gaps between benchmark scores and real-world safety behavior.

## Appendix C Illustrative Studies: From Benchmark Scores to Deployment Risk and Lived Harms

This appendix collects three worked examples that operationalize key claims from the main text. Together, they illustrate (i) how benchmark frequencies can be calibrated using real-world prevalence, (ii) how benchmark failure rates can be translated to deployment-level risk via multiplicative decompositions, and (iii) how affected-community judgments can reduce proxy–impact distance by revealing systematic value disagreement.

### C.1 Calibrating Benchmark Frequencies to Real-World Occurrence

![Refer to caption](https://arxiv.org/html/2601.23112v2/figures/cali-prob.png)

Figure 4: From benchmark frequencies to real-world occurrence. (a) Raw refusal rates from AIR 2024 272 and the HELM leaderboard 41, where higher values (green) indicate safer model behavior. Refusal rates are broadly similar across content categories, and this view primarily supports relative model ranking rather than real-world risk assessment. (b) Calibrated frequencies estimates computed as ( 1 − refusal rate ) × in-the-wild prevalence (1-\\text{refusal rate})\\times\\text{in-the-wild prevalence}, where lower values (green) indicate lower estimated real-world occurrence. Category prevalences are taken from WildChat Tab. 13 286: Self-harm ( 5 10 4 5\\times 10^{-4} ), Hate/Toxicity ( 1.4 3 1.4\\times 10^{-3} ), Sexual Content ( 5.93 2 5.93\\times 10^{-2} ), and Violence/Extremism ( 7.9 7.9\\times 10^{-3} ).

Existing safety benchmarks primarily rank models based on binary empirical frequencies (e.g. the ratio of refused to all responses) often aggregated across disparate categories of risk. While effective for comparative evaluation, these metrics offer limited insight into the expected exposure frequencies in actual deployment. In particular, raw benchmark scores fail to account for the highly heterogeneous real-world prevalence of different harm categories; a 1% failure rate in a rare category carries a vastly different deployment footprint than the same failure rate in a high-frequency one.

To address this limitation, we propose a prevalence-based calibration that shifts the focus from merely ranking models to also ranking risk exposure. By weighting benchmark failure rates by empirical estimates of in-the-wild prevalence, we move beyond abstract safety scores toward an approximation of relative risk exposure. This approach treats benchmark results as conditional probabilities, which, when combined with deployment-side priors, reveal the actual magnitudes of safety risks users are likely to encounter.

Fig. 4 illustrates the necessity of this shift. In Fig. 4(a), refusal rates from AIR 2024 [^272] appear broadly similar across subgroups; models that are "safer" generally show uniform performance across categories. However, this uniformity is an artifact of benchmark design rather than a reflection of real-world risk. By incorporating prevalence data from WildChat [^286], we compute: $\text{Calibrated Frequency}=(1-\text{refusal rate})\times\text{in-the-wild prevalence}.$ As shown in Fig. 4(b), the risk landscape changes dramatically. While "Sexual Content" and "Violence/Extremism" show comparable benchmark refusal rates, the calibrated frequency of sexual content exposure is an order-of-magnitude higher due to its higher prevalence in user queries.

We emphasize that observational datasets such as WildChat are subject to sampling bias and validity limitations. Our goal is not precise risk estimation, but to demonstrate a robust qualitative phenomenon: incorporating even coarse empirical prevalence can fundamentally alter the interpretation of safety benchmarks. This reframing preserves model rankings while extending evaluation beyond comparison toward understanding the relative types and magnitudes of risks models may expose in deployment.

##### Relationship to Measurement Theory.

This calibration exercise illuminates how benchmark scores relate to core measurement properties.

Proportionality asks whether score differences correspond to proportional changes in risk. Within a single category, calibrated frequencies do scale proportionally with failure rate: doubling the failure rate doubles expected harmful exposures. However, this frequency-based proportionality does not extend to severity. Twice the failure rate on extremism prompts may produce far more than twice the real-world harm, as certain risks propagate nonlinearly through social systems.

Invariance concerns whether metrics behave consistently across deployment contexts. Fig. 4 demonstrates that raw benchmark scores violate this property: identical refusal rates yield vastly different real-world exposure depending on category prevalence. A 0.9 refusal rate for sexual content and violence/extremism appears equivalent in benchmark terms, yet the calibrated frequencies differ by an order-of-magnitude. This suggests two complementary remedies: benchmarks could sample prompts proportionally to real-world prevalence, making aggregate scores more interpretable, or benchmarks could report calibrated frequencies alongside raw rates, making context-dependence explicit.

Traceable calibration asks which real-world quantities scores approximate. Raw refusal rates approximate model behavior under a fixed prompt distribution, but this quantity is difficult to interpret in deployment terms. By multiplying failure rates by in-the-wild prevalence, we establish an explicit link between benchmark outputs and a concrete real-world quantity: expected frequency of harmful content exposure per query. This transformation exemplifies traceable calibration, converting abstract scores into deployment-grounded estimates.

### C.2 Translating Safety Benchmarks to Deployment Risk: A Fermi Approach

The previous subsection demonstrated how calibrating benchmark frequencies against in-the-wild prevalence transforms model-centric scores into exposure estimates. However, exposure frequency alone does not capture risk: a high-frequency, low-severity harm may matter less than a rare but catastrophic one. Here, we extend this framework by tracing how prevalence propagates through subsequent stages of real-world impact, combining with severity to estimate the magnitude of losses rather than occurrence frequencies alone.

In the tradition of Fermi estimation in physics and engineering [^58] [^256] [^154], we construct an illustrative calculation to demonstrate how benchmark failure rates might translate to deployment risk under plausible assumptions. Fermi estimation, which involves making approximate calculations with minimal data to achieve order-of-magnitude understanding, is standard practice for exploring system behavior when comprehensive empirical data remains unavailable [^243]. As with scenario analysis more broadly, our goal is not predictive precision but structural clarity [^111] [^123]: at what order-of-magnitude does the relationship between benchmark scores and real-world risk operate?

##### Benchmark coverage versus real-world harm.

Safety benchmarks stress contemporary models and rank systems via aggregate success or failure rates across behavior classes. While such coverage spans domains including misinformation, copyright, biological and chemical risks, and harassment, benchmarks typically do not provide a direct mapping from evaluation outcomes to realized real-world harm.

We propose that translating benchmark performance to deployment risk may benefit from a multiplicative decomposition:

$$
\text{Calibrated Risk}=\mathbb{E}[\text{Harm}]=\underbrace{B}_{\begin{subarray}{c}\text{Benchmark}\\
\text{Failure Rate}\end{subarray}}\times\underbrace{C}_{\begin{subarray}{c}\text{Prevalence}\\
\text{(composite)}\end{subarray}}\times\underbrace{S}_{\text{Severity}}
$$

where $B$ denotes the benchmark failure rate (e.g., attack success rate), $C$ represents a composite prevalence term capturing multiple real-world discount factors, and $S$ quantifies the severity per realized harm. Current safety benchmarks report only $B$; researchers must estimate $C$ and $S$ from deployment data and domain-specific assessments. Consistent with scenario analysis traditions in probabilistic risk assessment [^114], this construction is explicitly illustrative; deployment contexts, user populations, and institutional safeguards vary substantially.

##### Illustrative case: copyright-related behaviors.

We demonstrate this framework using copyright violations as a worked example. To support transparency and reproducibility, the code and data file used for this analysis are available at [https://anonymous.4open.science/r/ai-safety-benchmark](https://anonymous.4open.science/r/ai-safety-benchmark). To make the pathway from benchmark failure to realized economic harm explicit, we decompose the composite prevalence term $C$ into a product of factors corresponding to distinct stages of deployment:

$$
C=C_{\text{jailbreak}}\times C_{\text{enforce}}\times C_{\text{users}}\times C_{\text{queries}},
$$

where each term reflects an empirically grounded filter from model behavior to realized liability.

Benchmark failure rate ($B\approx 10^{-2}$). HarmBench [^159] reports that GPT-4 Turbo exhibits an attack success rate of approximately $0.6\%$ on copyright-related behaviors under the “Human Jailbreak” setting. This setting evaluates model behavior under a fixed set of in-the-wild jailbreak templates [^211], into which copyright-related behavior strings are inserted as user requests. We treat this quantity as a conditional failure probability under a specific adversarial prompt distribution.

Jailbreak prevalence ($C_{\text{jailbreak}}\approx 10^{-2}$). WildChat [^286] shows that prominent adversarial jailbreak prompt patterns appear in approximately $1\%$ of real-world user interactions (9,845 out of 1,039,785 queries). Using this aggregate jailbreak prevalence as a proxy for copyright-specific adversarial attempts likely overestimates copyright risk, since many jailbreaks target unrelated behaviors, while simultaneously underestimating it insofar as copyright-violating requests can be non-adversarial (e.g., direct requests to reproduce paywalled text). For our purposes, this proxy suffices to illustrate uncertainty propagation at the order-of-magnitude level.

Enforcement rate ($C_{\text{enforce}}\approx 10^{-3}$). A critical ecological consideration is that infringement does not imply litigation or payment. TRAC reports 3,944 new federal copyright infringement cases filed annually [^234], while the Lumen Database receives approximately 5,000–7,000 takedown notices per day—the majority of which are DMCA (copyright-based) notices [^87]. Annualizing the latter yields roughly $2\times 10^{6}$ notices per year, giving:

$$
C_{\text{enforce}}\approx\frac{3{,}944}{2\times 10^{6}}\approx 2\times 10^{-3}
$$

This ratio captures the fact that the overwhelming majority of alleged infringements do not escalate to litigation or monetary liability.

Platform scale ($C_{\text{users}}\times C_{\text{queries\_per\_year}}\approx 10^{6.5}$). We consider a medium-sized platform with $10^{3}$ daily active users and approximately $10^{1}$ queries per user per day, consistent with observed usage patterns for conversational AI systems [^171]. This yields roughly $10^{4}$ queries per day, or $3.65\times 10^{6}\approx 10^{6.5}$ queries per year.

Severity ($S\approx 10^{2.5}$ – $10^{6.5}$). The economic severity of copyright violations spans several orders of magnitude. Fig. 5 shows the distribution of U.S. copyright statutory damages awards from 2011–2020 (n=202) using the NYU Brady–Germano–Sprigman dataset [^21]. In log-space, representative cutpoints are:

$$
S_{\mu-2\sigma}\approx\mathdollar 345\approx 10^{2.5},\quad S_{\mu}\approx\mathdollar 31{,}591\approx 10^{4.5},\quad S_{\mu+2\sigma}\approx\mathdollar 2.9\times 10^{6}\approx 10^{6.5}.
$$
![Refer to caption](https://arxiv.org/html/2601.23112v2/figures/statutory_damages_with_case_study.png)

Figure 5: Statutory Damages Distribution with Case Study Risk Assessment. Four risk levels defined by cutpoints at μ ± 2 σ \\mu\\pm 2\\sigma of log 10 \\log\_{10} awards, U.S. copyright cases, 2011–2020 ( n = 202 n=202 ).

Combining these factors yields an illustrative expected annual liability:

$$
\displaystyle\mathbb{E}[\text{Annual Liability}]
$$
 
$$
\displaystyle=B\times C_{\text{jailbreak}}\times C_{\text{enforce}}\times(C_{\text{users}}\times C_{\text{queries\_per\_year}})\times S.
$$

Using the representative severity level $S_{\mu}\approx 10^{4.5}$, we obtain

$$
\displaystyle\mathbb{E}[\text{Annual Liability}]
$$
 
$$
\displaystyle\approx(10^{-2})\times(10^{-2})\times(10^{-3})\times(10^{6.5})\times(10^{4.5})
$$
 
$$
\displaystyle\approx 10^{4}\;\text{USD}\;\;(\text{i.e., on the order of }\mathdollar 10^{4}\text{ per year}).
$$

As shown in Fig. 5, this estimate is placed in empirical context. The blue star marks the illustrative annual liability implied by the benchmark calculation, positioned at the mean ($\mu$) of the log-transformed statutory damages distribution. This placement reflects our intent to estimate baseline exposure under typical severity conditions, rather than a worst-case scenario driven by rare, catastrophic awards in the tail. This highlights that even a modest benchmark failure rate $B$, when propagated through realistic prevalence, enforcement, and scale factors, can generate nontrivial expected liability.

This calculation demonstrates the structure of risk translation rather than deployment-ready estimates. The specific values depend heavily on application context (customer-facing chatbot versus internal tool), user population characteristics, organizational risk tolerance, and jurisdictional legal frameworks. We encourage practitioners to substitute domain-specific values while preserving the methodological framework that helps make implicit assumptions explicit.

##### Discussion: Reconciling Risk Modeling with AI System Complexity.

Risk modeling in AI safety remains a subject of active debate. In the context of system safety, [^50] argues that Probabilistic Risk Assessment (PRA), while standard in some engineering domains, may be inappropriate for AI systems where failures emerge from complex sociotechnical interactions rather than component-level stochasticity. This suggests that even well-calibrated benchmark frequencies may provide false assurance if they obscure the constraint-satisfaction structure underlying real-world safety. [^232] also emphasizes that safety cases cannot be a substitute for risk modeling, as they do not aim to estimate the likelihood and severity of risks. Despite these tensions, recent work continues to operationalize "benchmark risk" using likelihood–severity decompositions (i.e., $Risk=Probability\times Severity$) to conduct risk mitigation calculations in LLM evaluation [^160]. Meanwhile, [^258] formalizes risk level, mapping likelihood levels (ranging from $10^{-1}$ to $10^{-12}$) against harm severity (ranging from minor incidents to catastrophic outcomes, such as 1 to 500M+ fatalities).

We emphasize that applying risk modeling framework is neither a complete nor a fully faithful model of safety. This limitation is well-recognized even in mature safety-critical domains such as nuclear power and aviation [^173] [^8]. In those fields, risk modeling with PRA is explicitly treated as approximate, incomplete, and sensitive to "unknown unknowns" and sociotechnical dynamics [^290]. Therefore, critiques arguing that PRA is inappropriate for AI due to the system’s complexity do not uniquely apply to AI; they apply to all complex engineered systems embedded in sociotechnical environments [^85]

In practice, safety engineering resolves this tension not by abandoning risk modeling, but by using probabilistic estimates as decision-support tools: they serve to compare orders of magnitude, identify dominant risk contributors, and establish conservative lower bounds that are then augmented by safety factors and qualitative analysis [^30] [^290]. Our use of prevalence calibration and order-of-magnitude estimation follows this engineering tradition. We do not propose a universal mapping from benchmark scores to real-world harm, nor do we claim that probabilistic estimates capture the full dimensionality of AI safety. Rather, our goal is to make implicit assumptions explicit and demonstrate how benchmark results can be situated within a broader risk-reasoning workflow. This approach complements system-theoretic methods—such as Failure mode and effects analysis (FMEA) or System-theoretic process analysis (STPA)—which uncover hazards arising from interactions between human users and AI components that model-level evaluations often miss [^133] [^165]. Ultimately, we aim to move beyond high-level frameworks by providing a quantitative, order-of-magnitude lens that accounts for component interactions and systematic effects without over-relying on exact point estimates.

### C.3 Community-Grounded Judgments Reduce Proxy–Impact Distance: Qualitative Example

To illustrate why involving affected communities can reduce the distance between benchmark proxies and real-world harms, we draw on qualitative prompt–response examples from [^5] and the accompanying finding that rater disagreement is pervasive and systematically structured by demographic group. Despite sharing identical scenarios, demographic groups systematically rated the harms differently across dimensions (e.g., male participants rated responses less toxic than female participants; conservative and Black participants rated higher emotional awareness than liberal and White participants), implying that a single benchmark label can implicitly encode whose values define harm. Therefore, disagreement is often signal rather than annotator noise; collapsing to majority vote can erase minority viewpoints and mismeasure harms for those most exposed. These observations motivate incorporating feedback from affected communities and, where appropriate, preserving disagreement, because doing so better aligns scenario selection and risk operationalization with the harms people actually experience.

## Appendix D Checklist Instrument and Worked Example

The checklist below operationalizes our recommendations (R1–R10) into actionable items for benchmark design and reporting. We also provide multiple formats (spreadsheet, markdown) at [https://anonymous.4open.science/r/ai-safety-benchmark/](https://anonymous.4open.science/r/ai-safety-benchmark/) for adoption and adaptation by researchers and practitioners.

### D.1 Checklist for Safety Benchmark Design

Table 2: Checklist for safety benchmark design, aligned with Recommendations R1–R10.

<table><thead><tr><th>Module</th><th>Recommendation</th><th>Checklist Item</th></tr></thead><tbody><tr><td rowspan="3">Construct Coverage</td><td>R1. Documenting Known Blind Spots</td><td>a. State which risk types are evaluated (e.g., toxicity, bias, jailbreaks, misinformation) and how each is measured. b. Document excluded risks and deployment assumptions (e.g., single-turn only, English text only, no tool-use or multi-agent scenarios). c. Acknowledge that passing the benchmark does not guarantee safety against untested or emergent risks. d. Compare coverage against prior benchmarks and document differences in risk categories or evaluation methods.</td></tr><tr><td>R2. Expanding Known Boundaries</td><td>a. Describe mechanisms for discovering novel risks (e.g., fuzzing, red-teaming, LM-generated evaluation). b. Include infrastructure for community contribution (e.g., submission portals with versioned integration and contributor credit). c. Describe update mechanisms: how and when new risks will be incorporated (e.g., annual taxonomy review, continuous calibration). d. Incorporate multi-agent or interactive evaluation where emergent risks may arise through interaction.</td></tr><tr><td>R3. Reframing ML Phenomena as Safety Concerns</td><td>a. Address distribution shift as a safety-critical issue, not merely a performance limitation. b. Document potential annotation bias (annotator selection, disagreement patterns, demographic skew). c. Implement contamination detection and track temporal validity of evaluation sets.</td></tr><tr><td rowspan="3">Risk Quantification</td><td>R4. Calibrating Benchmark Frequencies to Exposure Estimates</td><td>a. Report results as “observed rate” or “failure frequency”; reserve “probability” for calibrated estimates. b. Calibrate benchmark rates against in-the-wild prevalence to support risk-relevant interpretation. c. Specify factors limiting generalization (e.g., limited prompt diversity, synthetic scenarios, missing user context).</td></tr><tr><td>R5. Grounding Severity in Principled Frameworks</td><td>a. Justify severity scales by citing sources (e.g., prior research, regulatory standards, domain-specific frameworks). b. Clarify scale semantics: equal intervals, power-law relationships, or catastrophic thresholds. c. Reference established practices where applicable.</td></tr><tr><td>R6. Accounting for Uncertainty Quantification</td><td>a. Report confidence intervals, standard errors, or worst-case bounds for main metrics. b. Report inter-rater reliability (e.g., Cohen’s <math><semantics><mi>κ</mi> <annotation>\kappa</annotation></semantics></math>) for human or LLM-as-judge evaluation. c. Test robustness: report score variance across random seeds, prompt rephrasings, and evaluator versions. d. Apply explicit safety margins when extrapolating to deployment risk; note that real-world risk depends on user behavior, system safeguards, and context.</td></tr><tr><td rowspan="4">Measurement Validity</td><td>R7. Standardizing Safety Constructs with Transparency</td><td>a. Specify harm constructs targeted (e.g., toxicity, bias, manipulation) and provide operational definitions for each. b. State whose values inform judgments of harm (expert assessments, policy frameworks, affected communities). c. Acknowledge contested normative choices in construct definitions. d. Articulate the relationship between measured proxies and real-world safety concerns.</td></tr><tr><td>R8. Locking and Versioning for Reproducibility</td><td>a. Record model access details: interface (API or UI), access date, inference parameters (temperature, top-p), system prompt. b. Fix and report random seeds for data sampling, model inference, and evaluation. c. Version all evaluation components: LLM judge model, scoring rubric, annotation guidelines. d. Provide documentation (e.g., code repository, README) to enable independent replication.</td></tr><tr><td>R9. Anchoring Proxies in Deployment Contexts</td><td>a. State prompt sources: real user logs, researcher-designed, LLM-generated, or crowdsourced. Report validation if synthetic. b. Justify why test scenarios represent real-world use; if abstract or synthetic, state limitations. c. Include multi-turn evaluation if risks emerge over extended interaction (e.g., manipulation, trust exploitation). d. Document trade-offs when in-the-wild collection is constrained by privacy or curation opacity.</td></tr><tr><td>R10. Iterative Refinement via Community Input</td><td>a. Treat benchmarks as evolving instruments with risk-sensitive update cycles. b. Involve affected communities to assess whether scenarios reflect harms they experience. c. State whether the benchmark evaluates the model alone or within system context (user interaction, interface, safeguards). d. Acknowledge model-level scores <math><semantics><mo>≠</mo> <annotation>\neq</annotation></semantics></math> system-level safety; identify additional evaluation needed for deployment (e.g., user studies, sandbox simulations, post-deployment monitoring).</td></tr></tbody></table>

### D.2 Worked Example: AIR 2024 Checklist Assessment

We next apply the checklist as a worked example by auditing AIR 2024 [^272].

##### Assessment criteria.

✓(addressed) indicates the benchmark explicitly and fully implements the checklist item with clear documentation; $\circ$ (partially addressed) indicates the item is mentioned or implemented incompletely, without full specification or justification; ✗(not addressed) indicates no evidence the item was considered in the benchmark design or documentation.

Table 3: Checklist assessment for AIR 2024, aligned with Recommendations R1–R10. Status indicators: ✓ = addressed, $\circ$ = partially addressed, ✗ = not addressed.

<table><thead><tr><th>Module</th><th>Recommendation</th><th>Checklist Item</th><th>Status</th></tr></thead><tbody><tr><td rowspan="11">Construct Coverage</td><td rowspan="4">R1. Documenting Known Blind Spots</td><td>a. State which risk types are evaluated and how each is measured.</td><td>✓</td></tr><tr><td>b. Document excluded risks and deployment assumptions.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>c. Acknowledge that passing does not guarantee safety against untested risks.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Compare coverage against prior benchmarks.</td><td>✓</td></tr><tr><td rowspan="4">R2. Expanding Known Boundaries</td><td>a. Describe mechanisms for discovering novel risks.</td><td>✗</td></tr><tr><td>b. Include infrastructure for community contribution.</td><td>✗</td></tr><tr><td>c. Describe update mechanisms for incorporating new risks.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Incorporate multi-agent or interactive evaluation.</td><td>✗</td></tr><tr><td rowspan="3">R3. Reframing ML Phenomena</td><td>a. Address distribution shift as safety-critical.</td><td>✗</td></tr><tr><td>b. Document potential annotation bias.</td><td>✗</td></tr><tr><td>c. Implement contamination detection and track temporal validity.</td><td>✗</td></tr><tr><td rowspan="10">Risk Quantification</td><td rowspan="3">R4. Calibrating Benchmark Frequencies to Exposure Estimates</td><td>a. Report results as “observed rate”; reserve “probability” for calibrated estimates.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>b. Calibrate benchmark rates against in-the-wild prevalence.</td><td>✗</td></tr><tr><td>c. Specify factors limiting generalization.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td rowspan="3">R5. Grounding Severity in Principled Frameworks</td><td>a. Justify severity scales by citing sources.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>b. Clarify scale semantics: intervals, power-law, or thresholds.</td><td>✗</td></tr><tr><td>c. Reference established practices.</td><td>✗</td></tr><tr><td rowspan="4">R6. Systematic Uncertainty Quantification</td><td>a. Report confidence intervals or standard errors.</td><td>✗</td></tr><tr><td>b. Report inter-rater reliability.</td><td>✓</td></tr><tr><td>c. Test robustness across seeds, prompts, evaluator versions.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Apply explicit safety margins when extrapolating to deployment.</td><td>✗</td></tr><tr><td rowspan="16">Measurement Validity</td><td rowspan="4">R7. Standardizing Safety Constructs with Transparency</td><td>a. Specify harm constructs and provide operational definitions.</td><td>✓</td></tr><tr><td>b. State whose values inform judgments of harm.</td><td>✓</td></tr><tr><td>c. Acknowledge contested normative choices.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Articulate relationship between proxies and real-world safety.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td rowspan="4">R8. Locking and Versioning for Reproducibility</td><td>a. Record model access details and inference parameters.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>b. Fix and report random seeds.</td><td>✗</td></tr><tr><td>c. Version all evaluation components.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Provide documentation for independent replication.</td><td>✓</td></tr><tr><td rowspan="4">R9. Anchoring Proxies in Deployment</td><td>a. State prompt sources and report validation if synthetic.</td><td>✓</td></tr><tr><td>b. Justify why scenarios represent real-world use.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>c. Include multi-turn evaluation for extended interaction risks.</td><td>✗</td></tr><tr><td>d. Document trade-offs for in-the-wild collection constraints.</td><td>✗</td></tr><tr><td rowspan="4">R10. Iterative Refinement via Community</td><td>a. Treat benchmarks as evolving instruments.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>b. Involve affected communities in assessment.</td><td>✗</td></tr><tr><td>c. State whether benchmark evaluates model alone or within system context.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr><tr><td>d. Acknowledge model-level <math><semantics><mo>≠</mo> <annotation>\neq</annotation></semantics></math> system-level safety.</td><td><math><semantics><mo>∘</mo> <annotation>\circ</annotation></semantics></math></td></tr></tbody></table>

##### Summary

Of the 37 checklist items, AIR 2024 fully addresses 7 (✓), partially addresses 15 ($\circ$), and does not address 15 (✗). The benchmark demonstrates strength in construct coverage documentation (R1) and value specification (R7), but shows gaps in dynamic risk discovery (R2), ML phenomena as safety concerns (R3), uncertainty quantification (R6), and community engagement (R10).

## Appendix E Coding Details

##### Coding Dimensions

We coded all surveyed benchmarks along multiple dimensions, including their assignment to Rumsfeld-style risk categories, whether benchmarks explicitly specify the risks not covered in their work, their reliance on fixed versus dynamic data, the use of binary outcome metrics, distinctions between harm severity levels and whether such distinctions are theoretically grounded, explicit treatment of uncertainty, grounding of proxies in external standards or regulations, and whether evaluations are limited to single-turn interactions. Coding protocol provided in additional file.

Table 4: Coding results for all surveyed benchmarks. One author performed initial coding; a second author reviewed all assignments, with disagreements resolved through discussion. Column definitions: Rumsfeld: Rumsfeld category assignment (KK = Known knowns, KU = Known unknowns, UK = Unknown knowns, UU = Unknown unknowns). Uncovered Doc.: Whether the benchmark explicitly specifies the risks it uncovers, including unexpected, unknown, or unforeseen risks. Fixed Data: Whether the benchmark relies on a fixed, static dataset. Binary Metric: Whether the benchmark reduces evaluation to binary outcome proportions (e.g., harmful/safe, reject/not reject, biased/unbiased, attack success/failure) as the primary metric. Sev. Level: Whether the benchmark distinguishes between different levels of harm severity (e.g., low/medium/high or Level 1–5). Sev. Grd.: If severity levels are distinguished, whether they are grounded in an explicit theoretical framework or external standard (e.g., regulatory guidance or established harm taxonomies). Uncert.: Whether the benchmark explicitly identifies sources of uncertainty or variation (e.g., model sensitivity, response stochasticity, sampling variation, or evaluator disagreement). Proxy Grd.: Whether benchmark definitions or evaluation proxies are explicitly grounded in established frameworks, regulations, policies, or societal standards. Single-turn: Whether the benchmark evaluates models in isolation via a single question-answer interaction, without contextual information or multiple trials. Notation. ✓ denotes yes, $\circ$ denotes partial or mixed support, ✗ denotes no, and NA indicates not applicable.

|  | Rumsfeld | Uncovered Doc. | Fixed Data | Binary Metric | Sev. Level | Sev. Grd. | Uncert. | Proxy Grd. | Single-turn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark |  |  |  |  |  |  |  |  |  |
| CATQA [^16] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| HOLISTICBIAS [^217] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| SAFETEXT [^131] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| WALLEDEVAL [^74] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| TOXIGEN [^83] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ |
| JADE [^278] | KU | $\circ$ | ✗ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✓ |
| PROSOCIALDIALOG [^116] | KK | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| StrongREJECT [^220] | KK | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ |
| XSTEST [^198] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| Cognitive Biases [^155] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| Non-Discrimination [^277] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| Societal Bias VLMs [^207] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| AART [^190] | KU | ✓ | ✗ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| AAVENUE [^73] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| Ego-View Accident [^56] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| Adversarial VQA [^135] | KU | ✗ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| Adversarial GLUE [^246] | UK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| SAFETY-TUNED LLAMAS [^19] | KK | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | $\circ$ | ✓ |
| AgentDojo [^45] | KU | ✓ | ✗ | ✓ | ✗ | NA | $\circ$ | ✗ | ✗ |
| AILUMINATE [^66] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| AIR-BENCH 2024 [^272] | KK | $\circ$ | ✓ | $\circ$ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ALERT [^231] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| QA-LIGN [^49] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✓ |
| [^249] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| [^219] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ |
| [^4] | KK | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | NA |
| C2SaferRust [^175] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✗ |
| [^89] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| [^245] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| ArtPrompt [^104] | KU | ✓ | ✗ | $\circ$ | ✓ | ✓ | $\circ$ | ✓ | ✓ |
| WildTeaming [^105] | KU | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| [^92] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| Athena [^202] | KK | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ |
| BackdoorLLM [^141] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| BBG [^109] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| BBQ [^181] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| BeaverTails [^103] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| KOFFVQA [^118] | KK | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ |
| [^248] | KU | ✗ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| Flames [^91] | KK | ✗ | ✓ | $\circ$ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [^144] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| [^238] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| [^126] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| SAFE [^268] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^120] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| BOLD [^47] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^265] | KK | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ |
| [^102] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| [^48] | KU | ✗ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| [^20] | KK | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | NA |
| CALM [^75] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| [^37] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✗ |
| RuLES [^164] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| CARNOVEL [^59] | UK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✗ |
| [^96] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | NA |
| OccuGender [^36] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✗ |
| CDEval [^251] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| CHBias [^284] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✗ |
| CHiSafetyBench [^279] | KK | ✗ | ✓ | $\circ$ | ✓ | ✓ | ✓ | ✓ | ✗ |
| CIF-Bench [^142] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| CBBQ [^94] | KK | ✗ | ✓ | ✓ | ✓ | NA | ✓ | ✓ | ✓ |
| OW-DFA [^287] | KU | ✓ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| CPO [^72] | KK | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ |
| CoSafe [^267] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| CrowS-Pairs [^168] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| CVE-Bench [^247] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| Cybench [^274] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | $\circ$ | ✓ | ✗ |
| [^205] | KK | $\circ$ | ✗ | ✗ | ✗ | NA | ✓ | ✓ | ✗ |
| DELPHI [^222] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| DICES [^9] | KK | $\circ$ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✗ |
| [^183] | UU | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| discrim-eval [^229] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| [^77] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| DiversityMedQA [^193] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| JailbreakHub [^212] | KU | $\circ$ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Do-Not-Answer [^252] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✓ |
| MACHIAVELLI [^180] | KU | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| [^151] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| ConfAIde [^161] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✗ | ✓ | ✗ |
| LabellessFace [^177] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| ePiC [^65] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| GenMO [^11] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| RealToxicityPrompts [^64] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| Tri-HE [^259] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| [^143] | KU | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^119] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| AdvMark [^260] | KU | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| FACET [^76] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| FairLex [^31] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| [^216] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✗ | ✓ | ✓ |
| FFT [^43] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✓ |
| Filipino [^62] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| FLEX [^112] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| FLAIR [^218] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| FrenchCrowS-Pairs [^172] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| FrenchToxicityPrompts [^23] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✓ |
| Z’eroe [^53] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| WinoBias [^285] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| GeoNet [^113] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| CPAD [^150] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| GPTFuzz [^269] | KU | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| CoP [^262] | KU | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | $\circ$ | ✗ |
| SafeWatch-Bench [^38] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✗ |
| HarmBench [^159] | KU | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| HRS-Bench [^12] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| FVQA2.0 [^148] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| HypoTermQA [^235] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| IHEval [^281] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | $\circ$ | ✓ | ✗ |
| IndiBias [^203] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✓ |
| UNQOVER [^139] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| InjecAgent [^273] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| ADVQA [^226] | KU | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| JailbreakBench [^32] | KK | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| [^3] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| JailBreakV-28K [^153] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✗ | ✓ | ✓ |
| JobFair [^253] | KK | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✗ |
| KoBBQ [^110] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| KorNAT [^127] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| LatentJailbreak [^189] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| CCLR [^69] | UK | ✗ | ✓ | ✗ | ✗ | NA | ✗ | ✗ | NA |
| [^101] | KK | $\circ$ | ✗ | ✗ | ✓ | ✓ | ✓ | $\circ$ | ✗ |
| LLMArena [^34] | UU | $\circ$ | ✗ | ✗ | ✗ | NA | ✓ | ✗ | ✗ |
| SAD [^125] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| MedHALT [^179] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| MEDFAIR [^291] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| MedSafetyBench [^78] | KK | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [^2] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| MLeVLM [^264] | KK | $\circ$ | ✓ | $\circ$ | ✓ | NA | ✓ | $\circ$ | ✗ |
| MMEvalPro [^90] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| ModSCAN [^106] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| MultiRobustBench [^44] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^199] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| OKTest [^215] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| CLCA [^149] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✗ |
| [^210] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| [^223] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| [^237] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| CAMeL-2 [^169] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| [^33] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| OR-Bench [^42] | KU | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| PAPILLON [^138] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| PERSONA [^28] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| PLUE [^39] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| Poser [^40] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| PrivLM-Bench [^132] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| PROMPTEVALS [^241] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| MLLMU-Bench [^152] | KK | ✓ | ✓ | $\circ$ | ✓ | NA | ✗ | ✓ | ✓ |
| RADDLE [^182] | KU | ✗ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| RAGTruth [^176] | KK | $\circ$ | ✓ | ✓ | ✓ | NA | ✓ | ✗ | ✗ |
| [^18] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| MDIT-Bench [^108] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| REAP [^86] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| [^63] | KK | ✓ | NA | $\circ$ | ✓ | NA | ✓ | $\circ$ | ✗ |
| RED-EVAL [^17] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| RedditBias [^13] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✗ |
| DeMET [^130] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| TLDR [^60] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✓ |
| ROBBIE [^54] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| Robo3D [^122] | KK | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ | $\circ$ | ✓ |
| GQA-OOD [^115] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| S-Eval [^271] | KK | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| LaMaSafe [^254] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✗ |
| SafeBench [^263] | KU | ✗ | ✗ | $\circ$ | ✗ | NA | $\circ$ | ✓ | ✗ |
| [^224] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| SafetyBench [^280] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| SALAD-Bench [^134] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✗ |
| [^225] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| SG-Bench [^163] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✗ |
| SimpleSafetyTests [^240] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| SoFa [^156] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| [^201] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | $\circ$ | ✓ |
| SORRY-Bench [^261] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| StereoSet [^166] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| BenchPress [^162] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✗ |
| TensorTrust [^233] | KU | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| COCONOT [^22] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| [^1] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| SwedishWinogender [^79] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| WMDP [^136] | KK | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| [^213] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| [^15] | UK | ✓ | NA | ✗ | ✗ | NA | ✗ | ✗ | NA |
| TheGreatestGood [^157] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| TAB [^187] | KU | $\circ$ | ✓ | $\circ$ | ✓ | ✓ | ✓ | ✓ | NA |
| EmpatheticDialogues [^192] | KK | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ |
| [^288] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| MMHB [^230] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✗ | $\circ$ | ✓ |
| [^145] | KK | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✗ |
| [^137] | KK | ✗ | ✓ | ✗ | ✗ | NA | ✓ | ✗ | ✓ |
| [^206] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^10] | KK | ✓ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✗ |
| TrustLLM [^93] | KK | ✗ | ✓ | $\circ$ | ✓ | ✓ | ✓ | ✓ | ✗ |
| TruthfulQA [^147] | KK | $\circ$ | ✓ | $\circ$ | ✓ | ✗ | ✓ | $\circ$ | ✓ |
| [^188] | KU | ✓ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✓ | ✓ |
| CII-Bench [^275] | KK | $\circ$ | ✓ | $\circ$ | ✓ | ✗ | ✓ | ✗ | ✓ |
| UNQOVER [^140] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^283] | KK | ✓ | ✓ | ✗ | ✗ | NA | ✓ | ✓ | ✓ |
| MHaluBench [^35] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| AdvBench [^292] | KU | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| [^124] | KU | $\circ$ | ✓ | ✗ | ✗ | NA | ✓ | $\circ$ | ✓ |
| LMMs-Eval [^276] | UK | $\circ$ | ✗ | ✗ | ✗ | NA | ✓ | ✓ | ✗ |
| VALUE [^289] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| MixCuBe [^117] | KK | ✗ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| B-score [^242] | KK | ✗ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✗ |
| WinoQueer [^57] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✓ | ✓ |
| SeqAR [^266] | KU | $\circ$ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| [^250] | KU | $\circ$ | ✗ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| GEST [^186] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | ✓ | ✓ |
| TiEBe [^6] | KK | ✓ | ✓ | ✓ | ✗ | NA | ✓ | ✗ | ✓ |
| WorldCuisines [^257] | KK | $\circ$ | ✓ | $\circ$ | ✗ | NA | ✓ | ✗ | ✓ |
| VITAL [^214] | KK | ✓ | ✓ | $\circ$ | ✗ | NA | ✓ | $\circ$ | ✓ |

[^1]: The multilingual alignment prism: aligning global and local preferences to reduce harm. In EMNLP, pp. 12027–12049. Cited by: Table 1, Table 4.

[^2]: Mitigating language-dependent ethnic bias in BERT. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, M. Moens, X. Huang, L. Specia, and S. W. Yih (Eds.), Online and Punta Cana, Dominican Republic, pp. 533–549. External Links: [Link](https://aclanthology.org/2021.emnlp-main.42/), [Document](https://dx.doi.org/10.18653/v1/2021.emnlp-main.42) Cited by: Table 4.

[^3]: Jailbreaking LLMs with Arabic transliteration and Arabizi. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 18584–18600. External Links: [Link](https://aclanthology.org/2024.emnlp-main.1034/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.1034) Cited by: Table 4.

[^4]: On the threat of npm vulnerable dependencies in node. js applications. arXiv preprint arXiv:2009.09019. Cited by: Table 4.

[^5]: Operationalizing pluralistic values in large language model alignment reveals trade-offs in safety, inclusivity, and model behavior. arXiv preprint arXiv:2511.14476. Cited by: §C.3, §7.

[^6]: TiEBe: A benchmark for assessing the current knowledge of large language models. CoRR abs/2501.07482. External Links: [Link](https://doi.org/10.48550/arXiv.2501.07482), [Document](https://dx.doi.org/10.48550/ARXIV.2501.07482), 2501.07482 Cited by: Table 4.

[^7]: Concrete problems in AI safety. arXiv preprint arXiv:1606.06565. Cited by: §1, §3.

[^8]: How useful is quantitative risk assessment?. Risk Analysis: An International Journal 24 (3), pp. 515–520. Cited by: §C.2.

[^9]: DICES dataset: diversity in conversational ai evaluation for safety. In Proceedings of the 37th International Conference on Neural Information Processing Systems, NIPS ’23, Red Hook, NY, USA. Cited by: Table 4.

[^10]: Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv preprint arXiv:2204.05862. Cited by: Table 4.

[^11]: Evaluating gender bias of LLMs in making morality judgements. In Findings of the Association for Computational Linguistics: EMNLP 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 15804–15818. External Links: [Link](https://aclanthology.org/2024.findings-emnlp.928/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.928) Cited by: Table 4.

[^12]: HRS-bench: holistic, reliable and scalable benchmark for text-to-image models. External Links: 2304.05390, [Link](https://arxiv.org/abs/2304.05390) Cited by: Table 4.

[^13]: RedditBias: a real-world resource for bias evaluation and debiasing of conversational language models. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), C. Zong, F. Xia, W. Li, and R. Navigli (Eds.), Online, pp. 1941–1955. External Links: [Link](https://aclanthology.org/2021.acl-long.151/), [Document](https://dx.doi.org/10.18653/v1/2021.acl-long.151) Cited by: Table 4.

[^14]: Measuring what matters: construct validity in large language model benchmarks. In NeurIPS 2025 Datasets and Benchmarks Track, Note: OpenReview id: mdA5lVvNcU Cited by: §3, §7.

[^15]: Children and the data cycle: rights and ethics in a big data world. CoRR abs/1710.06881. External Links: [Link](http://arxiv.org/abs/1710.06881), 1710.06881 Cited by: Table 4, §5.

[^16]: Language models are homer simpson! safety re-alignment of fine-tuned language models through task arithmetic. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 14138–14149. Cited by: Table 4.

[^17]: Red-teaming large language models using chain of utterances for safety-alignment. External Links: 2308.09662, [Link](https://arxiv.org/abs/2308.09662) Cited by: Table 4.

[^18]: Re-contextualizing fairness in NLP: the case of India. In Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), Y. He, H. Ji, S. Li, Y. Liu, and C. Chang (Eds.), Online only, pp. 727–740. External Links: [Link](https://aclanthology.org/2022.aacl-main.55/), [Document](https://dx.doi.org/10.18653/v1/2022.aacl-main.55) Cited by: Table 4.

[^19]: Safety-tuned llamas: lessons from improving the safety of large language models that follow instructions. arXiv preprint arXiv:2309.07875. Cited by: Table 4, §6, §6.

[^20]: Cake, death, and trolleys: dilemmas as benchmarks of ethical decision-making. AIES ’18, New York, NY, USA, pp. 23–29. External Links: ISBN 9781450360128, [Link](https://doi.org/10.1145/3278721.3278767), [Document](https://dx.doi.org/10.1145/3278721.3278767) Cited by: Table 4.

[^21]: Cited by: §C.2.

[^22]: The art of saying no: contextual noncompliance in language models. In NeurIPS, Cited by: Table 4.

[^23]: FrenchToxicityPrompts: a large benchmark for evaluating and mitigating toxicity in French texts. In Proceedings of the Fourth Workshop on Threat, Aggression & Cyberbullying @ LREC-COLING-2024, R. Kumar, A. Kr. Ojha, S. Malmasi, B. R. Chakravarthi, B. Lahiri, S. Singh, and S. Ratan (Eds.), Torino, Italia, pp. 105–114. External Links: [Link](https://aclanthology.org/2024.trac-1.12/) Cited by: Table 4.

[^24]: The malicious use of artificial intelligence: forecasting, prevention, and mitigation. Note: arXiv:1802.07228 External Links: [Link](https://arxiv.org/abs/1802.07228) Cited by: §1.

[^25]: Gender shades: intersectional accuracy disparities in commercial gender classification. In Proceedings of the 1st Conference on Fairness, Accountability and Transparency (FAccT), Proceedings of Machine Learning Research, Vol. 81, pp. 77–91. Cited by: §1, §2.

[^26]: Assessing the impact of planned social change. Evaluation and Program Planning 2, pp. 67–90. Cited by: §3.

[^27]: Extracting training data from large language models. In 30th USENIX Security Symposium, External Links: [Link](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting) Cited by: §1.

[^28]: PERSONA: a reproducible testbed for pluralistic alignment. In Proceedings of the 31st International Conference on Computational Linguistics, O. Rambow, L. Wanner, M. Apidianaki, H. Al-Khalifa, B. D. Eugenio, and S. Schockaert (Eds.), Abu Dhabi, UAE, pp. 11348–11368. External Links: [Link](https://aclanthology.org/2025.coling-main.752/) Cited by: Table 4.

[^29]: SafeBench winners. Note: [https://www.mlsafety.org/safebench/winners](https://www.mlsafety.org/safebench/winners) Accessed: 2025-10-16 Cited by: §1, §2.

[^30]: Development of an automated decision-making tool for supervisory control system. Technical report Oak Ridge National Lab.(ORNL), Oak Ridge, TN (United States). Cited by: §C.2.

[^31]: FairLex: a multilingual benchmark for evaluating fairness in legal text processing. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), S. Muresan, P. Nakov, and A. Villavicencio (Eds.), Dublin, Ireland, pp. 4389–4406. External Links: [Link](https://aclanthology.org/2022.acl-long.301/), [Document](https://dx.doi.org/10.18653/v1/2022.acl-long.301) Cited by: Table 4.

[^32]: JailbreakBench: an open robustness benchmark for jailbreaking large language models. In NeurIPS, Cited by: Table 4.

[^33]: On the robustness of language guidance for low-level vision tasks: findings from depth estimation. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2024, Seattle, WA, USA, June 16-22, 2024, pp. 2794–2803. External Links: [Link](https://doi.org/10.1109/CVPR52733.2024.00270), [Document](https://dx.doi.org/10.1109/CVPR52733.2024.00270) Cited by: Table 4.

[^34]: LLMArena: assessing capabilities of large language models in dynamic multi-agent environments. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 13055–13077. External Links: [Link](https://aclanthology.org/2024.acl-long.705/), [Document](https://dx.doi.org/10.18653/v1/2024.acl-long.705) Cited by: Table 1, Table 4, §5, §5.

[^35]: Unified hallucination detection for multimodal large language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), pp. 3235–3252. External Links: [Link](https://doi.org/10.18653/v1/2024.acl-long.178), [Document](https://dx.doi.org/10.18653/V1/2024.ACL-LONG.178) Cited by: Table 4.

[^36]: Causally testing gender bias in LLMs: a case study on occupational bias. In Findings of the Association for Computational Linguistics: NAACL 2025, L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 4984–5004. External Links: [Link](https://aclanthology.org/2025.findings-naacl.281/), [Document](https://dx.doi.org/10.18653/v1/2025.findings-naacl.281), ISBN 979-8-89176-195-7 Cited by: Table 4.

[^37]: Can large language models provide security & privacy advice? measuring the ability of llms to refute misconceptions. In Proceedings of the 39th Annual Computer Security Applications Conference, ACSAC ’23, New York, NY, USA, pp. 366–378. External Links: ISBN 9798400708862, [Link](https://doi.org/10.1145/3627106.3627196), [Document](https://dx.doi.org/10.1145/3627106.3627196) Cited by: Table 4.

[^38]: SafeWatch: an efficient safety-policy following video guardrail model with transparent explanations. External Links: 2412.06878, [Link](https://arxiv.org/abs/2412.06878) Cited by: Table 4.

[^39]: PLUE: language understanding evaluation benchmark for privacy policies in English. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.), Toronto, Canada, pp. 352–365. External Links: [Link](https://aclanthology.org/2023.acl-short.31/), [Document](https://dx.doi.org/10.18653/v1/2023.acl-short.31) Cited by: Table 4.

[^40]: Poser: unmasking alignment faking llms by manipulating their internals. CoRR abs/2405.05466. External Links: [Link](https://doi.org/10.48550/arXiv.2405.05466), [Document](https://dx.doi.org/10.48550/ARXIV.2405.05466), 2405.05466 Cited by: Table 4.

[^41]: AIR-bench leaderboard, holistic evaluation of language models (helm). Center for Research on Foundation Models (CRFM), Stanford University. Note: [https://crfm.stanford.edu/helm/air-bench/latest/](https://crfm.stanford.edu/helm/air-bench/latest/) Accessed: 2025-12-27 Cited by: Figure 4, Figure 4.

[^42]: OR-bench: an over-refusal benchmark for large language models. External Links: 2405.20947, [Link](https://arxiv.org/abs/2405.20947) Cited by: Table 4.

[^43]: FFT: towards harmlessness evaluation and analysis for llms with factuality, fairness, toxicity. CoRR abs/2311.18580. External Links: [Link](https://doi.org/10.48550/arXiv.2311.18580), [Document](https://dx.doi.org/10.48550/ARXIV.2311.18580), 2311.18580 Cited by: Table 4.

[^44]: MultiRobustBench: benchmarking robustness against multiple attacks. External Links: 2302.10980, [Link](https://arxiv.org/abs/2302.10980) Cited by: Table 4.

[^45]: Agentdojo: a dynamic environment to evaluate prompt injection attacks and defenses for llm agents. Advances in Neural Information Processing Systems 37, pp. 82895–82920. Cited by: Table 4.

[^46]: NASA risk management handbook. Technical report Cited by: §3.

[^47]: BOLD: dataset and metrics for measuring biases in open-ended language generation. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, FAccT ’21, New York, NY, USA, pp. 862–872. External Links: ISBN 9781450383097, [Link](https://doi.org/10.1145/3442188.3445924), [Document](https://dx.doi.org/10.1145/3442188.3445924) Cited by: Table 4, §6.

[^48]: Build it break it fix it for dialogue safety: robustness from adversarial human attack. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), K. Inui, J. Jiang, V. Ng, and X. Wan (Eds.), Hong Kong, China, pp. 4537–4546. External Links: [Link](https://aclanthology.org/D19-1461/), [Document](https://dx.doi.org/10.18653/v1/D19-1461) Cited by: Table 4.

[^49]: QA-lign: aligning llms through constitutionally decomposed qa. arXiv preprint arXiv:2506.08123. Cited by: Table 4, §6.

[^50]: System safety and artificial intelligence. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency, pp. 1584–1584. Cited by: §C.2, §2, §7.

[^51]: Regulatory history and experimental support of uncertainty (safety) factors. Regulatory toxicology and pharmacology 3 (3), pp. 224–238. Cited by: §6.

[^52]: International ai safety report 2025. Department for Science, Innovation & Technology, United Kingdom. Note: GOV.UK External Links: [Link](https://www.gov.uk/government/publications/international-ai-safety-report-2025) Cited by: §3.

[^53]: From hero to zéroe: a benchmark of low-level adversarial attacks. In Proceedings of the 1st Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing, K. Wong, K. Knight, and H. Wu (Eds.), Suzhou, China, pp. 786–803. External Links: [Link](https://aclanthology.org/2020.aacl-main.79/), [Document](https://dx.doi.org/10.18653/v1/2020.aacl-main.79) Cited by: Table 4.

[^54]: ROBBIE: robust bias evaluation of large generative language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, H. Bouamor, J. Pino, and K. Bali (Eds.), Singapore, pp. 3764–3814. External Links: [Link](https://aclanthology.org/2023.emnlp-main.230/), [Document](https://dx.doi.org/10.18653/v1/2023.emnlp-main.230) Cited by: Table 4.

[^55]: Final report – risk acceptance criteria for technical systems and operational procedures. Technical Report European Union Agency for Railways. Note: Accessed: 2026-01-05 External Links: [Link](https://www.era.europa.eu/system/files?file=2022-11/risk-acceptance-criteria-for-technical-systems_en.pdf) Cited by: §3.

[^56]: Abductive ego-view accident video understanding for safe driving perception. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 22030–22040. Cited by: Table 4.

[^57]: WinoQueer: A community-in-the-loop benchmark for anti-lgbtq+ bias in large language models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14, 2023, A. Rogers, J. L. Boyd-Graber, and N. Okazaki (Eds.), pp. 9126–9140. External Links: [Link](https://doi.org/10.18653/v1/2023.acl-long.507), [Document](https://dx.doi.org/10.18653/V1/2023.ACL-LONG.507) Cited by: Table 4.

[^58]: My observations during the explosion at trinity on july 16, 1945. Technical report Los Alamos National Laboratory. Cited by: §C.2, §6.

[^59]: Can autonomous vehicles identify, recover from, and adapt to distribution shifts?. External Links: 2006.14911, [Link](https://arxiv.org/abs/2006.14911) Cited by: Table 1, Table 4, §5, §5.

[^60]: TLDR: token-level detective reward model for large vision language models. In ICLR, Cited by: Table 4.

[^61]: Cited by: §1, §3.

[^62]: Filipino benchmarks for measuring sexist and homophobic bias in multilingual language models from Southeast Asia. In Proceedings of the First Workshop on Language Models for Low-Resource Languages, H. Hettiarachchi, T. Ranasinghe, P. Rayson, R. Mitkov, M. Gaber, D. Premasiri, F. A. Tan, and L. Uyangodage (Eds.), Abu Dhabi, United Arab Emirates, pp. 123–134. External Links: [Link](https://aclanthology.org/2025.loreslm-1.9/) Cited by: Table 4.

[^63]: Red teaming language models to reduce harms: methods, scaling behaviors, and lessons learned. External Links: 2209.07858, [Link](https://arxiv.org/abs/2209.07858) Cited by: Table 4.

[^64]: RealToxicityPrompts: evaluating neural toxic degeneration in language models. In Findings of the Association for Computational Linguistics: EMNLP 2020, T. Cohn, Y. He, and Y. Liu (Eds.), Online, pp. 3356–3369. External Links: [Link](https://aclanthology.org/2020.findings-emnlp.301/), [Document](https://dx.doi.org/10.18653/v1/2020.findings-emnlp.301) Cited by: Table 4, §1, §7.

[^65]: EPiC: employing proverbs in context as a benchmark for abstract language understanding. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), S. Muresan, P. Nakov, and A. Villavicencio (Eds.), Dublin, Ireland, pp. 3989–4004. External Links: [Link](https://aclanthology.org/2022.acl-long.276/), [Document](https://dx.doi.org/10.18653/v1/2022.acl-long.276) Cited by: Table 4.

[^66]: Ailuminate: introducing v1. 0 of the ai risk and reliability benchmark from mlcommons. arXiv preprint arXiv:2503.05731. Cited by: Table 4, §6, §6, §7.

[^67]: Discovery of grounded theory: strategies for qualitative research. Routledge. Cited by: §A.2.

[^68]: Problems of monetary management: the uk experience. In Papers in Monetary Economics, Cited by: §3.

[^69]: Likelihood-based out-of-distribution detection with denoising diffusion probabilistic models. External Links: 2310.17432, [Link](https://arxiv.org/abs/2310.17432) Cited by: Table 4, §5.

[^70]: Gemini 3 pro frontier safety framework (fsf) report. Technical report Google DeepMind. Note: Gemini 3 Pro Frontier Safety Framework Report External Links: [Link](https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf) Cited by: §5.

[^71]: How many interviews are enough? an experiment with data saturation and variability. Field methods 18 (1), pp. 59–82. Cited by: §A.2.

[^72]: Controllable preference optimization: toward controllable multi-objective alignment. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 1437–1454. External Links: [Link](https://aclanthology.org/2024.emnlp-main.85/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.85) Cited by: Table 4.

[^73]: Aavenue: detecting llm biases on nlu tasks in aave via a novel benchmark. arXiv preprint arXiv:2408.14845. Cited by: Table 4.

[^74]: Walledeval: a comprehensive safety evaluation toolkit for large language models. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pp. 397–407. Cited by: Table 4.

[^75]: CALM: a multi-task benchmark for comprehensive assessment of language model bias. External Links: 2308.12539, [Link](https://arxiv.org/abs/2308.12539) Cited by: Table 4, §5.

[^76]: FACET: fairness in computer vision evaluation benchmark. In 2023 IEEE/CVF International Conference on Computer Vision (ICCV), Vol., pp. 20313–20325. External Links: [Document](https://dx.doi.org/10.1109/ICCV51070.2023.01863) Cited by: Table 4.

[^77]: Vision-language models performing zero-shot tasks exhibit disparities between gender groups. In 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW), Vol., pp. 2770–2777. External Links: [Document](https://dx.doi.org/10.1109/ICCVW60793.2023.00294) Cited by: Table 4, §6.

[^78]: MedSafetyBench: evaluating and improving the medical safety of large language models. In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track, External Links: [Link](https://openreview.net/forum?id=cFyagd2Yh4) Cited by: Table 4, §6.

[^79]: The swedish winogender dataset. In NoDaLiDa, pp. 452–459. Cited by: Table 4.

[^80]: What is ai safety? what do we want it to be?. Philosophical Studies, pp. 1–24. Cited by: §1, §4.

[^81]: What is ai safety? what do we want it to be?. Philosophical Studies 182, pp. 1495–1518. External Links: [Document](https://dx.doi.org/10.1007/s11098-025-02367-z) Cited by: §A.1.

[^82]: Patterns, predictions, and actions: a story about machine learning. arXiv preprint arXiv:2102.05242. Cited by: §2.

[^83]: Toxigen: a large-scale machine-generated dataset for adversarial and implicit hate speech detection. arXiv preprint arXiv:2203.09509. Cited by: Table 1, Table 4.

[^84]: Sample sizes for saturation in qualitative research: a systematic review of empirical tests. Social science & medicine 292, pp. 114523. Cited by: §A.2.

[^85]: Modelling and simulation of complex sociotechnical systems: envisioning and analysing work environments. Ergonomics 58 (4), pp. 600–614. Cited by: §C.2.

[^86]: REAP: A large-scale realistic adversarial patch benchmark. In IEEE/CVF International Conference on Computer Vision, ICCV 2023, Paris, France, October 1-6, 2023, pp. 4617–4628. External Links: [Link](https://doi.org/10.1109/ICCV51070.2023.00428), [Document](https://dx.doi.org/10.1109/ICCV51070.2023.00428) Cited by: Table 4.

[^87]: European commission stakeholder dialogue on article 17 – written statement (lumen). Note: [https://communia-association.org/wp-content/uploads/2019/12/stakholderdiagogue4\_Lumen.pdf](https://communia-association.org/wp-content/uploads/2019/12/stakholderdiagogue4_Lumen.pdf) As of Dec. 2019, Lumen database contains approximately 12 million takedown notices, majority DMCA (copyright) notices External Links: [Link](https://communia-association.org/wp-content/uploads/2019/12/stakholderdiagogue4_Lumen.pdf) Cited by: §C.2.

[^88]: Safety-i and safety-ii: the past and future of safety management. CRC Press. External Links: [Document](https://dx.doi.org/10.1201/9781315607511) Cited by: §1.

[^89]: Are large pre-trained language models leaking your personal information?. arXiv preprint arXiv:2205.12628. Cited by: Table 4.

[^90]: MMEvalPro: calibrating multimodal benchmarks towards trustworthy and efficient evaluation. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 4805–4822. External Links: [Link](https://aclanthology.org/2025.naacl-long.247/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.247), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^91]: Flames: benchmarking value alignment of llms in chinese. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 4551–4591. Cited by: Table 4.

[^92]: Catastrophic jailbreak of open-source llms via exploiting generation. arXiv preprint arXiv:2310.06987. Cited by: Table 4.

[^93]: Position: trustllm: trustworthiness in large language models. In International Conference on Machine Learning, pp. 20166–20270. Cited by: Table 4.

[^94]: CBBQ: a Chinese bias benchmark dataset curated with human-AI collaboration for large language models. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), N. Calzolari, M. Kan, V. Hoste, A. Lenci, S. Sakti, and N. Xue (Eds.), Torino, Italia, pp. 2917–2929. External Links: [Link](https://aclanthology.org/2024.lrec-main.260/) Cited by: Table 4, §6.

[^95]: Managing the risks of extreme events and disasters to advance climate change adaptation (srex). Technical report Cambridge University Press, Intergovernmental Panel on Climate Change. External Links: [Link](https://www.ipcc.ch/report/srex/) Cited by: §3.

[^96]: Can we obtain fairness for free?. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society, AIES ’21, New York, NY, USA, pp. 586–596. External Links: ISBN 9781450384735, [Link](https://doi.org/10.1145/3461702.3462614), [Document](https://dx.doi.org/10.1145/3461702.3462614) Cited by: Table 4.

[^97]: Medical devices — application of risk management to medical devices. Standard Technical Report ISO 14971:2019, International Organization for Standardization, Geneva, CH. Cited by: §3.

[^98]: Cited by: §1.

[^99]: Cited by: §1.

[^100]: Measurement and fairness. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT), pp. 375–385. External Links: [Document](https://dx.doi.org/10.1145/3442188.3445901) Cited by: §3.

[^101]: Interacting large language model agents. interpretable models and social learning. External Links: 2411.01271, [Link](https://arxiv.org/abs/2411.01271) Cited by: Table 4.

[^102]: Breaking the global north stereotype: a global south-centric benchmark dataset for auditing and mitigating biases in facial recognition systems. External Links: 2407.15810, [Link](https://arxiv.org/abs/2407.15810) Cited by: Table 4.

[^103]: Beavertails: towards improved safety alignment of llm via a human-preference dataset. Advances in Neural Information Processing Systems 36, pp. 24678–24704. Cited by: Table 4.

[^104]: Artprompt: ascii art-based jailbreak attacks against aligned llms. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 15157–15173. Cited by: Table 4, §6.

[^105]: Wildteaming at scale: from in-the-wild jailbreaks to (adversarially) safer language models. Advances in Neural Information Processing Systems 37, pp. 47094–47165. Cited by: Table 4, §5, §7, §8.

[^106]: ModSCAN: Measuring stereotypical bias in large vision-language models from vision and language modalities. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 12814–12845. External Links: [Link](https://aclanthology.org/2024.emnlp-main.713/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.713) Cited by: Table 4.

[^107]: Swe-bench: can language models resolve real-world github issues?. arXiv preprint arXiv:2310.06770. Cited by: §7.

[^108]: MDIT-bench: evaluating the dual-implicit toxicity in large multimodal models. External Links: 2505.17144, [Link](https://arxiv.org/abs/2505.17144) Cited by: Table 4.

[^109]: Social bias benchmark for generation: a comparison of generation and qa-based evaluations. arXiv preprint arXiv:2503.06987. Cited by: Table 4.

[^110]: KoBBQ: Korean bias benchmark for question answering. Transactions of the Association for Computational Linguistics 12, pp. 507–524. External Links: [Link](https://aclanthology.org/2024.tacl-1.28/), [Document](https://dx.doi.org/10.1162/tacl%5Fa%5F00661) Cited by: Table 4.

[^111]: Developing and applying scenarios. Climate Change 2001: Impacts, Adaptation, and Vulnerability: Contribution of Working Group II to the Third Assessment Report of the Intergovernmental Panel on Climate Change 2, pp. 145. Cited by: §C.2.

[^112]: FLEX: a benchmark for evaluating robustness of fairness in large language models. In Findings of the Association for Computational Linguistics: NAACL 2025, L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 3606–3620. External Links: [Link](https://aclanthology.org/2025.findings-naacl.199/), [Document](https://dx.doi.org/10.18653/v1/2025.findings-naacl.199), ISBN 979-8-89176-195-7 Cited by: Table 4.

[^113]: GeoNet: benchmarking unsupervised adaptation across geographies. External Links: 2303.15443, [Link](https://arxiv.org/abs/2303.15443) Cited by: Table 4.

[^114]: On the quantitative definition of risk. Risk Analysis 1 (1), pp. 11–27. Cited by: §C.2.

[^115]: Roses are red, violets are blue… but should VQA expect them to?. In CVPR, pp. 2776–2785. Cited by: Table 4.

[^116]: Prosocialdialog: a prosocial backbone for conversational agents. arXiv preprint arXiv:2205.12688. Cited by: Table 4, §6.

[^117]: When tom eats kimchi: evaluating cultural bias of multimodal large language models in cultural mixture contexts. CoRR abs/2503.16826. External Links: [Link](https://doi.org/10.48550/arXiv.2503.16826), [Document](https://dx.doi.org/10.48550/ARXIV.2503.16826), 2503.16826 Cited by: Table 4.

[^118]: KOFFVQA: an objectively evaluated free-form vqa benchmark for large vision-language models in the korean language. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 575–585. Cited by: Table 4.

[^119]: Examining gender and race bias in two hundred sentiment analysis systems. In Proceedings of the Seventh Joint Conference on Lexical and Computational Semantics, M. Nissim, J. Berant, and A. Lenci (Eds.), New Orleans, Louisiana, pp. 43–53. External Links: [Link](https://aclanthology.org/S18-2005/), [Document](https://dx.doi.org/10.18653/v1/S18-2005) Cited by: Table 4.

[^120]: Bias out-of-the-box: an empirical analysis of intersectional occupational biases in popular generative language models. External Links: 2102.04130, [Link](https://arxiv.org/abs/2102.04130) Cited by: Table 4.

[^121]: WILDS: a benchmark of in-the-wild distribution shifts. In Proceedings of the 38th International Conference on Machine Learning (ICML), Proceedings of Machine Learning Research, Vol. 139. External Links: [Link](https://proceedings.mlr.press/v139/koh21a.html) Cited by: §1.

[^122]: Robo3D: towards robust and reliable 3d perception against corruptions. In ICCV, pp. 19937–19949. Cited by: Table 4.

[^123]: Methods of future and scenario analysis: overview, assessment, and selection criteria. Vol. 39, DEU. Cited by: §C.2.

[^124]: Unveiling safety vulnerabilities of large language models. CoRR abs/2311.04124. External Links: [Link](https://doi.org/10.48550/arXiv.2311.04124), [Document](https://dx.doi.org/10.48550/ARXIV.2311.04124), 2311.04124 Cited by: Table 4.

[^125]: Me, myself, and ai: the situational awareness dataset (sad) for llms. Advances in Neural Information Processing Systems 37, pp. 64010–64118. Cited by: Table 4.

[^126]: Benchmarking the fairness of image upsampling methods. In The 2024 ACM Conference on Fairness, Accountability, and Transparency, FAccT 2024, Rio de Janeiro, Brazil, June 3-6, 2024, pp. 489–517. External Links: [Link](https://doi.org/10.1145/3630106.3658921), [Document](https://dx.doi.org/10.1145/3630106.3658921) Cited by: Table 4, §5.

[^127]: KorNAT: LLM alignment benchmark for Korean social values and common knowledge. In Findings of the Association for Computational Linguistics: ACL 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 11177–11213. External Links: [Link](https://aclanthology.org/2024.findings-acl.666/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-acl.666) Cited by: Table 4.

[^128]: Engineering a safer world: systems thinking applied to safety. MIT Press, Cambridge, MA. Cited by: §3, §3.

[^129]: Engineering a safer world: systems thinking applied to safety. MIT Press, Cambridge, MA. External Links: [Link](https://sunnyday.mit.edu/safer-world.pdf) Cited by: §1.

[^130]: Gender bias in decision-making with large language models: a study of relationship conflicts. In Findings of the Association for Computational Linguistics: EMNLP 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 5777–5800. External Links: [Link](https://aclanthology.org/2024.findings-emnlp.331/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.331) Cited by: Table 4.

[^131]: Safetext: a benchmark for exploring physical safety in language models. arXiv preprint arXiv:2210.10045. Cited by: Table 4.

[^132]: PrivLM-bench: a multi-level privacy evaluation benchmark for language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 54–73. External Links: [Link](https://aclanthology.org/2024.acl-long.4/), [Document](https://dx.doi.org/10.18653/v1/2024.acl-long.4) Cited by: Table 4.

[^133]: FMEA-ai: ai fairness impact assessment using failure mode and effects analysis. AI and Ethics 2 (4), pp. 837–850. Cited by: §C.2.

[^134]: SALAD-Bench: a hierarchical and comprehensive safety benchmark for large language models. In Findings of the Association for Computational Linguistics (ACL), Cited by: Table 4, §6.

[^135]: Adversarial vqa: a new benchmark for evaluating the robustness of vqa models. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 2042–2051. Cited by: Table 4.

[^136]: The wmdp benchmark: measuring and reducing malicious use with unlearning. In International Conference on Machine Learning, pp. 28525–28550. Cited by: Table 4.

[^137]: Towards benchmarking and assessing visual naturalness of physical world adversarial attacks. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-24, 2023, pp. 12324–12333. External Links: [Link](https://doi.org/10.1109/CVPR52729.2023.01186), [Document](https://dx.doi.org/10.1109/CVPR52729.2023.01186) Cited by: Table 4.

[^138]: PAPILLON: privacy preservation from Internet-based and local language model ensembles. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 3371–3390. External Links: [Link](https://aclanthology.org/2025.naacl-long.173/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.173), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^139]: UNQOVERing stereotyping biases via underspecified questions. In Findings of the Association for Computational Linguistics: EMNLP 2020, T. Cohn, Y. He, and Y. Liu (Eds.), Online, pp. 3475–3489. External Links: [Link](https://aclanthology.org/2020.findings-emnlp.311/), [Document](https://dx.doi.org/10.18653/v1/2020.findings-emnlp.311) Cited by: Table 4.

[^140]: UnQovering stereotyping biases via underspecified questions. CoRR abs/2010.02428. External Links: [Link](https://arxiv.org/abs/2010.02428), 2010.02428 Cited by: Table 4.

[^141]: BackdoorLLM: a comprehensive benchmark for backdoor attacks and defenses on large language models. arXiv preprint arXiv:2408.12798. Cited by: Table 4.

[^142]: CIF-bench: a Chinese instruction-following benchmark for evaluating the generalizability of large language models. In Findings of the Association for Computational Linguistics: ACL 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 12431–12446. External Links: [Link](https://aclanthology.org/2024.findings-acl.739/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-acl.739) Cited by: Table 4.

[^143]: Evaluating the instruction-following robustness of large language models to prompt injection. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 557–568. External Links: [Link](https://aclanthology.org/2024.emnlp-main.33/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.33) Cited by: Table 4.

[^144]: Benchmarking algorithmic bias in face recognition: an experimental approach using synthetic faces and human evaluation. In 2023 IEEE/CVF International Conference on Computer Vision (ICCV), Vol., pp. 4954–4964. External Links: [Document](https://dx.doi.org/10.1109/ICCV51070.2023.00459) Cited by: Table 4.

[^145]: Towards understanding and mitigating social biases in language models. In Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event, M. Meila and T. Zhang (Eds.), Proceedings of Machine Learning Research, Vol. 139, pp. 6565–6576. External Links: [Link](http://proceedings.mlr.press/v139/liang21a.html) Cited by: Table 4.

[^146]: Holistic evaluation of language models. arXiv preprint arXiv:2211.09110. External Links: [Link](https://arxiv.org/abs/2211.09110) Cited by: §1, §3.

[^147]: TruthfulQA: measuring how models mimic human falsehoods. pp. 3214–3252. Cited by: Table 4, §3.

[^148]: FVQA 2.0: introducing adversarial samples into fact-based visual question answering. In Findings of the Association for Computational Linguistics: EACL 2023, A. Vlachos and I. Augenstein (Eds.), Dubrovnik, Croatia, pp. 149–157. External Links: [Link](https://aclanthology.org/2023.findings-eacl.11/), [Document](https://dx.doi.org/10.18653/v1/2023.findings-eacl.11) Cited by: Table 4.

[^149]: Cultural learning-based culture adaptation of language models. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 3114–3134. External Links: [Link](https://aclanthology.org/2025.acl-long.156/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.156), ISBN 979-8-89176-251-0 Cited by: Table 4.

[^150]: Goal-oriented prompt attack and safety evaluation for llms. External Links: 2309.11830, [Link](https://arxiv.org/abs/2309.11830) Cited by: Table 4.

[^151]: Does gender matter? towards fairness in dialogue systems. In Proceedings of the 28th International Conference on Computational Linguistics, D. Scott, N. Bel, and C. Zong (Eds.), Barcelona, Spain (Online), pp. 4403–4416. External Links: [Link](https://aclanthology.org/2020.coling-main.390/), [Document](https://dx.doi.org/10.18653/v1/2020.coling-main.390) Cited by: Table 4.

[^152]: Protecting privacy in multimodal large language models with MLLMU-bench. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 4105–4135. External Links: [Link](https://aclanthology.org/2025.naacl-long.207/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.207), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^153]: JailBreakV: a benchmark for assessing the robustness of multimodal large language models against jailbreak attacks. In First Conference on Language Modeling, External Links: [Link](https://openreview.net/forum?id=GC4mXVfquq) Cited by: Table 4, §6.

[^154]: Street-fighting mathematics: the art of educated guessing and opportunistic problem solving. MIT Press. Cited by: §C.2.

[^155]: A comprehensive evaluation of cognitive biases in llms. arXiv preprint arXiv:2410.15413. Cited by: Table 4.

[^156]: Social bias probing: fairness benchmarking for language models. In EMNLP, pp. 14653–14671. Cited by: Table 4.

[^157]: The greatest good benchmark: measuring llms’ alignment with utilitarian moral dilemmas. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, EMNLP 2024, Miami, FL, USA, November 12-16, 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), pp. 21950–21959. External Links: [Link](https://doi.org/10.18653/v1/2024.emnlp-main.1224), [Document](https://dx.doi.org/10.18653/V1/2024.EMNLP-MAIN.1224) Cited by: Table 4.

[^158]: MLPerf training benchmark. In Proceedings of Machine Learning and Systems (MLSys), Vol. 2, pp. 336–349. External Links: [Link](https://proceedings.mlsys.org/paper_files/paper/2020/hash/411e39b117e885341f25efb8912945f7-Abstract.html) Cited by: §1.

[^159]: HarmBench: a standardized evaluation framework for automated red teaming and robust refusal. arXiv preprint arXiv:2402.04249. Cited by: §C.2, Table 4, §3, §6, §7.

[^160]: Risk management for mitigating benchmark failure modes: benchrisk. arXiv preprint arXiv:2510.21460. Cited by: §C.2.

[^161]: Can llms keep a secret? testing privacy implications of language models via contextual integrity theory. External Links: 2310.17884, [Link](https://arxiv.org/abs/2310.17884) Cited by: Table 4.

[^162]: BenchPress: analyzing android app vulnerability benchmark suites. In ASE Workshops, pp. 13–18. Cited by: Table 4.

[^163]: SG-bench: evaluating LLM safety generalization across diverse tasks and prompt types. In NeurIPS, Cited by: Table 4.

[^164]: Can llms follow simple rules?. External Links: 2311.04235, [Link](https://arxiv.org/abs/2311.04235) Cited by: Table 4.

[^165]: Systematic hazard analysis for frontier ai using stpa. arXiv preprint arXiv:2506.01782. Cited by: §C.2.

[^166]: StereoSet: measuring stereotypical bias in pretrained language models. In ACL/IJCNLP (1), pp. 5356–5371. Cited by: Table 4.

[^167]: Demystification and actualisation of data saturation in qualitative research through thematic analysis. International Journal of Qualitative Methods 23, pp. 16094069241229777. Cited by: §A.2.

[^168]: CrowS-Pairs: a challenge dataset for measuring social biases in masked language models. In Proceedings of EMNLP, Cited by: Table 4, §6.

[^169]: On the origin of cultural biases in language models: from pre-training data to linguistic phenomena. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 6423–6443. External Links: [Link](https://aclanthology.org/2025.naacl-long.326/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.326), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^170]: What if algorithmic fairness is a category error?. In Contemporary Debates in the Ethics of Artificial Intelligence, S. Nyholm, A. Kasirzadeh, and J. Zerilli (Eds.), pp. 77–96. External Links: ISBN 9781394258819 Cited by: §7, §9.

[^171]: ChatGPT statistics 2025: 800m+ users, revenue, and key insights. Note: [https://nerdynav.com/chatgpt-statistics/](https://nerdynav.com/chatgpt-statistics/) Accessed: January 2026 Cited by: §C.2.

[^172]: French CrowS-pairs: extending a challenge dataset for measuring social bias in masked language models to a language other than English. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), S. Muresan, P. Nakov, and A. Villavicencio (Eds.), Dublin, Ireland, pp. 8521–8531. External Links: [Link](https://aclanthology.org/2022.acl-long.583/), [Document](https://dx.doi.org/10.18653/v1/2022.acl-long.583) Cited by: Table 4.

[^173]: Use of probabilistic safety assessment (psa) for nuclear installations. Safety science 40 (1-4), pp. 153–176. Cited by: §C.2.

[^174]: Artificial intelligence risk management framework (ai rmf 1.0). Technical report Technical Report NIST AI 100-1, National Institute of Standards and Technology, Gaithersburg, MD. External Links: [Document](https://dx.doi.org/10.6028/NIST.AI.100-1), [Link](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) Cited by: §1, §3, §3, §6.

[^175]: C2saferrust: transforming c projects into safer rust with neurosymbolic techniques. arXiv preprint arXiv:2501.14257. Cited by: Table 4.

[^176]: RAGTruth: a hallucination corpus for developing trustworthy retrieval-augmented language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 10862–10878. External Links: [Link](https://aclanthology.org/2024.acl-long.585/), [Document](https://dx.doi.org/10.18653/v1/2024.acl-long.585) Cited by: Table 4.

[^177]: LabellessFace: fair metric learning for face recognition without attribute labels. External Links: 2409.09274, [Link](https://arxiv.org/abs/2409.09274) Cited by: Table 4.

[^178]: AI as a sport: on the competitive epistemologies of benchmarking. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency, pp. 1875–1884. Cited by: §2.

[^179]: Med-HALT: medical domain hallucination test for large language models. In Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL), J. Jiang, D. Reitter, and S. Deng (Eds.), Singapore, pp. 314–334. External Links: [Link](https://aclanthology.org/2023.conll-1.21/), [Document](https://dx.doi.org/10.18653/v1/2023.conll-1.21) Cited by: Table 4, §6.

[^180]: Do the rewards justify the means? measuring trade-offs between rewards and ethical behavior in the machiavelli benchmark. In Proceedings of the 40th International Conference on Machine Learning, ICML’23. Cited by: Table 4, §3.

[^181]: BBQ: a hand-built bias benchmark for question answering. arXiv preprint arXiv:2110.08193. Cited by: §B.3.1, Table 4, §6.

[^182]: RADDLE: an evaluation benchmark and analysis platform for robust task-oriented dialog systems. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), C. Zong, F. Xia, W. Li, and R. Navigli (Eds.), Online, pp. 4418–4429. External Links: [Link](https://aclanthology.org/2021.acl-long.341/), [Document](https://dx.doi.org/10.18653/v1/2021.acl-long.341) Cited by: Table 4, §7.

[^183]: Discovering language model behaviors with model-written evaluations. In Findings of the association for computational linguistics: ACL 2023, pp. 13387–13434. Cited by: Table 1, Table 4, §5, §5.

[^184]: Proof or bluff? evaluating llms on 2025 usa math olympiad. arXiv preprint arXiv:2503.21934. Cited by: §7.

[^185]: Humanity’s last exam. arXiv preprint arXiv:2501.14249. Cited by: §9.

[^186]: Women are beautiful, men are leaders: gender stereotypes in machine translation and language modeling. In Findings of the Association for Computational Linguistics: EMNLP 2024, Miami, Florida, USA, November 12-16, 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), pp. 3060–3083. External Links: [Link](https://doi.org/10.18653/v1/2024.findings-emnlp.173), [Document](https://dx.doi.org/10.18653/V1/2024.FINDINGS-EMNLP.173) Cited by: Table 4.

[^187]: The text anonymization benchmark (TAB): A dedicated corpus and evaluation framework for text anonymization. Comput. Linguistics 48 (4), pp. 1053–1101. External Links: [Link](https://doi.org/10.1162/coli%5C_a%5C_00458), [Document](https://dx.doi.org/10.1162/COLI%5FA%5F00458) Cited by: Table 4.

[^188]: Fine-tuning aligned language models compromises safety, even when users do not intend to!. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024, External Links: [Link](https://openreview.net/forum?id=hTEGyKf0dZ) Cited by: Table 1, Table 4.

[^189]: Latent jailbreak: a benchmark for evaluating text safety and output robustness of large language models. External Links: 2307.08487, [Link](https://arxiv.org/abs/2307.08487) Cited by: Table 4.

[^190]: Aart: ai-assisted red-teaming with diverse data generation for new llm-powered applications. arXiv preprint arXiv:2311.08592. Cited by: Table 4.

[^191]: AI and the everything in the whole wide world benchmark. arXiv preprint arXiv:2111.15366. Cited by: §2.

[^192]: Towards empathetic open-domain conversation models: A new benchmark and dataset. In Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers, A. Korhonen, D. R. Traum, and L. Màrquez (Eds.), pp. 5370–5381. External Links: [Link](https://doi.org/10.18653/v1/p19-1534), [Document](https://dx.doi.org/10.18653/V1/P19-1534) Cited by: Table 4.

[^193]: DiversityMedQA: a benchmark for assessing demographic biases in medical diagnosis using large language models. In Proceedings of the Third Workshop on NLP for Positive Impact, D. Dementieva, O. Ignat, Z. Jin, R. Mihalcea, G. Piatti, J. Tetreault, S. Wilson, and J. Zhao (Eds.), Miami, Florida, USA, pp. 334–348. External Links: [Link](https://aclanthology.org/2024.nlp4pi-1.29/), [Document](https://dx.doi.org/10.18653/v1/2024.nlp4pi-1.29) Cited by: Table 4.

[^194]: Safetywashing: do ai safety benchmarks actually measure safety progress?. Advances in Neural Information Processing Systems 37, pp. 68559–68594. Cited by: §B.3.1.

[^195]: Beyond accuracy: behavioral testing of nlp models with checklist. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 4902–4912. External Links: [Document](https://dx.doi.org/10.18653/v1/2020.acl-main.442), [Link](https://aclanthology.org/2020.acl-main.442/) Cited by: §1.

[^196]: Cited by: §3.

[^197]: Measuring what matters: connecting ai ethics evaluations to system attributes, hazards, and harms. Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society 8 (3), pp. 2199–2213. External Links: [Document](https://dx.doi.org/10.1609/aies.v8i3.36706), [Link](https://ojs.aaai.org/index.php/AIES/article/view/36706) Cited by: §7.

[^198]: Xstest: a test suite for identifying exaggerated safety behaviours in large language models. arXiv preprint arXiv:2308.01263. Cited by: Table 4.

[^199]: Gender bias in coreference resolution. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers), M. Walker, H. Ji, and A. Stent (Eds.), New Orleans, Louisiana, pp. 8–14. External Links: [Link](https://aclanthology.org/N18-2002/), [Document](https://dx.doi.org/10.18653/v1/N18-2002) Cited by: Table 4.

[^200]: ImageNet large scale visual recognition challenge. International Journal of Computer Vision 115 (3), pp. 211–252. External Links: [Document](https://dx.doi.org/10.1007/s11263-015-0816-y) Cited by: §1.

[^201]: Social bias in large language models for bangla: an empirical study on gender and religious bias. In COLING Workshops, pp. 204–218. Cited by: Table 4.

[^202]: Athena: safe autonomous agents with verbal contrastive learning. arXiv preprint arXiv:2408.11021. Cited by: Table 4.

[^203]: IndiBias: a benchmark dataset to measure social biases in language models for Indian context. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), K. Duh, H. Gomez, and S. Bethard (Eds.), Mexico City, Mexico, pp. 8786–8806. External Links: [Link](https://aclanthology.org/2024.naacl-long.487/), [Document](https://dx.doi.org/10.18653/v1/2024.naacl-long.487) Cited by: Table 4.

[^204]: Measurement to meaning: a validity-centered framework for ai evaluation. arXiv preprint arXiv:2505.10573. Cited by: §7.

[^205]: Re-imagining algorithmic fairness in india and beyond. FAccT ’21, New York, NY, USA, pp. 315–328. External Links: ISBN 9781450383097, [Link](https://doi.org/10.1145/3442188.3445896), [Document](https://dx.doi.org/10.1145/3442188.3445896) Cited by: Table 4.

[^206]: Towards explainability and fairness in swiss judgement prediction: benchmarking on a multilingual dataset. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation, LREC/COLING 2024, 20-25 May, 2024, Torino, Italy, N. Calzolari, M. Kan, V. Hoste, A. Lenci, S. Sakti, and N. Xue (Eds.), pp. 16500–16513. External Links: [Link](https://aclanthology.org/2024.lrec-main.1434) Cited by: Table 4.

[^207]: A unified framework and dataset for assessing societal bias in vision-language models. arXiv preprint arXiv:2402.13636. Cited by: Table 4.

[^208]: Saturation in qualitative research: exploring its conceptualization and operationalization. Quality & quantity 52 (4), pp. 1893–1907. Cited by: §A.2.

[^209]: Fairness and abstraction in sociotechnical systems. In Proceedings of the conference on fairness, accountability, and transparency, pp. 59–68. Cited by: §B.3.1, §7.

[^210]: On second thought, let’s not think step by step! bias and toxicity in zero-shot reasoning. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.), Toronto, Canada, pp. 4454–4470. External Links: [Link](https://aclanthology.org/2023.acl-long.244/), [Document](https://dx.doi.org/10.18653/v1/2023.acl-long.244) Cited by: Table 4.

[^211]: " Do anything now": characterizing and evaluating in-the-wild jailbreak prompts on large language models. In Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security, pp. 1671–1685. Cited by: §C.2.

[^212]: "Do anything now": characterizing and evaluating in-the-wild jailbreak prompts on large language models. In Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security, CCS ’24, New York, NY, USA, pp. 1671–1685. External Links: ISBN 9798400706363, [Link](https://doi.org/10.1145/3658644.3670388), [Document](https://dx.doi.org/10.1145/3658644.3670388) Cited by: Table 4, §6.

[^213]: The woman worked as a babysitter: on biases in language generation. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing, EMNLP-IJCNLP 2019, Hong Kong, China, November 3-7, 2019, K. Inui, J. Jiang, V. Ng, and X. Wan (Eds.), pp. 3405–3410. External Links: [Link](https://doi.org/10.18653/v1/D19-1339), [Document](https://dx.doi.org/10.18653/V1/D19-1339) Cited by: Table 4.

[^214]: VITAL: A new dataset for benchmarking pluralistic alignment in healthcare. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), pp. 22954–22974. External Links: [Link](https://aclanthology.org/2025.acl-long.1119/) Cited by: Table 4.

[^215]: Navigating the overkill in large language models. External Links: 2401.17633, [Link](https://arxiv.org/abs/2401.17633) Cited by: Table 4.

[^216]: An examination of bias of facial analysis based bmi prediction models. External Links: 2204.10262, [Link](https://arxiv.org/abs/2204.10262) Cited by: Table 4.

[^217]: " I’m sorry to hear that": finding new biases in language models with a holistic descriptor dataset. arXiv preprint arXiv:2205.09209. Cited by: Table 4.

[^218]: FLAIR: federated learning annotated image repository. External Links: 2207.08869, [Link](https://arxiv.org/abs/2207.08869) Cited by: Table 4.

[^219]: Analyzing stereotypes in generative text inference tasks. In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, pp. 4052–4065. Cited by: Table 4.

[^220]: A strongreject for empty jailbreaks. Advances in Neural Information Processing Systems 37, pp. 125416–125440. Cited by: Table 4, §5, §6, §6.

[^221]: SPEC cpu® 2017 benchmark. Note: [https://www.spec.org/cpu2017/](https://www.spec.org/cpu2017/) Accessed 2025-10-09 Cited by: §1.

[^222]: DELPHI: data for evaluating LLMs’ performance in handling controversial issues. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track, M. Wang and I. Zitouni (Eds.), Singapore, pp. 820–827. External Links: [Link](https://aclanthology.org/2023.emnlp-industry.76/), [Document](https://dx.doi.org/10.18653/v1/2023.emnlp-industry.76) Cited by: Table 4.

[^223]: On the safety of conversational models: taxonomy, dataset, and benchmark. In Findings of the Association for Computational Linguistics: ACL 2022, S. Muresan, P. Nakov, and A. Villavicencio (Eds.), Dublin, Ireland, pp. 3906–3923. External Links: [Link](https://aclanthology.org/2022.findings-acl.308/), [Document](https://dx.doi.org/10.18653/v1/2022.findings-acl.308) Cited by: Table 4.

[^224]: Safety assessment of chinese large language models. CoRR abs/2304.10436. Cited by: Table 4.

[^225]: Scaling behavior of machine translation with large language models under prompt injection attacks. In Proceedings of the First edition of the Workshop on the Scaling Behavior of Large Language Models (SCALE-LLM 2024), A. V. Miceli-Barone, F. Barez, S. Cohen, E. Voita, U. Germann, and M. Lukasik (Eds.), St. Julian’s, Malta, pp. 9–23. External Links: [Link](https://aclanthology.org/2024.scalellm-1.2/) Cited by: Table 4.

[^226]: Is your benchmark truly adversarial? AdvScore: evaluating human-grounded adversarialness. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 623–642. External Links: [Link](https://aclanthology.org/2025.naacl-long.27/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.27), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^227]: Measurement in Science. In The Stanford Encyclopedia of Philosophy, E. N. Zalta (Ed.), Note: [https://plato.stanford.edu/archives/fall2020/entries/measurement-science/](https://plato.stanford.edu/archives/fall2020/entries/measurement-science/) Cited by: §7, §7.

[^228]: The black swan: the impact of the highly improbable. Random House, New York. External Links: ISBN 978-1400063512 Cited by: §5.

[^229]: Evaluating and mitigating discrimination in language model decisions. External Links: 2312.03689, [Link](https://arxiv.org/abs/2312.03689) Cited by: Table 4.

[^230]: Towards massive multilingual holistic bias. CoRR abs/2407.00486. External Links: [Link](https://doi.org/10.48550/arXiv.2407.00486), [Document](https://dx.doi.org/10.48550/ARXIV.2407.00486), 2407.00486 Cited by: Table 4.

[^231]: ALERT: a comprehensive benchmark for assessing large language models’ safety through red teaming. arXiv preprint arXiv:2404.08676. Cited by: Table 4.

[^232]: The role of risk modeling in advanced ai risk management. arXiv preprint arXiv:2512.08723. Cited by: §C.2.

[^233]: Tensor trust: interpretable prompt injection attacks from an online game. In ICLR, Cited by: Table 4.

[^234]: Copyright infringement litigation fell 22 percent in fy 2016. Note: [https://tracreports.org/whatsnew/email.161121.html](https://tracreports.org/whatsnew/email.161121.html) Report noting 3,944 new federal copyright infringement cases filed in FY 2016 External Links: [Link](https://tracreports.org/whatsnew/email.161121.html) Cited by: §C.2.

[^235]: HypoTermQA: hypothetical terms dataset for benchmarking hallucination tendency of LLMs. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Student Research Workshop, N. Falk, S. Papi, and M. Zhang (Eds.), St. Julian’s, Malta, pp. 95–136. External Links: [Link](https://aclanthology.org/2024.eacl-srw.9/), [Document](https://dx.doi.org/10.18653/v1/2024.eacl-srw.9) Cited by: Table 4.

[^236]: Dual use of artificial-intelligence-powered drug discovery. Nature Machine Intelligence 4 (3), pp. 189–191. External Links: [Document](https://dx.doi.org/10.1038/s42256-022-00465-9) Cited by: §1.

[^237]: On evaluating and mitigating gender biases in multilingual settings. In Findings of the Association for Computational Linguistics: ACL 2023, A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.), Toronto, Canada, pp. 307–318. External Links: [Link](https://aclanthology.org/2023.findings-acl.21/), [Document](https://dx.doi.org/10.18653/v1/2023.findings-acl.21) Cited by: Table 4.

[^238]: The hidden space of safety: understanding preference-tuned llms in multilingual context. arXiv preprint arXiv:2504.02708. Cited by: Table 4.

[^239]: Introducing v0. 5 of the ai safety benchmark from mlcommons. arXiv preprint arXiv:2404.12241. Cited by: §1.

[^240]: SimpleSafetyTests: a test suite for identifying critical safety risks in large language models. CoRR abs/2311.08370. Cited by: Table 4.

[^241]: PROMPTEVALS: a dataset of assertions and guardrails for custom production large language model pipelines. External Links: 2504.14738, [Link](https://arxiv.org/abs/2504.14738) Cited by: Table 4.

[^242]: B-score: detecting biases in large language models using response history. In Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, External Links: [Link](https://openreview.net/forum?id=kl7SbPfBsB) Cited by: Table 4.

[^243]: The fermi solution: essays on science. Random House. Cited by: §C.2.

[^244]: Position: evaluating generative ai systems is a social science measurement challenge. arXiv preprint arXiv:2502.00561. Cited by: §7.

[^245]: Are personalized stochastic parrots more dangerous? evaluating persona biases in dialogue systems. arXiv preprint arXiv:2310.05280. Cited by: Table 4.

[^246]: Adversarial glue: a multi-task benchmark for robustness evaluation of language models. arXiv preprint arXiv:2111.02840. Cited by: Table 4, §6.

[^247]: CVE-bench: benchmarking LLM-based software engineering agent’s ability to repair real-world CVE vulnerabilities. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 4207–4224. External Links: [Link](https://aclanthology.org/2025.naacl-long.212/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.212), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^248]: Benchmark self-evolving: a multi-agent framework for dynamic llm evaluation. In Proceedings of the 31st international conference on computational linguistics, pp. 3310–3328. Cited by: Table 4, §5, §6.

[^249]: All languages matter: on the multilingual safety of llms. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 5865–5877. Cited by: Table 4.

[^250]: Testing and evaluation of large language models: correctness, non-toxicity, and fairness. CoRR abs/2409.00551. External Links: [Link](https://doi.org/10.48550/arXiv.2409.00551), [Document](https://dx.doi.org/10.48550/ARXIV.2409.00551), 2409.00551 Cited by: Table 4.

[^251]: CDEval: a benchmark for measuring the cultural dimensions of large language models. In Proceedings of the 2nd Workshop on Cross-Cultural Considerations in NLP, V. Prabhakaran, S. Dev, L. Benotti, D. Hershcovich, L. Cabello, Y. Cao, I. Adebara, and L. Zhou (Eds.), Bangkok, Thailand, pp. 1–16. External Links: [Link](https://aclanthology.org/2024.c3nlp-1.1/), [Document](https://dx.doi.org/10.18653/v1/2024.c3nlp-1.1) Cited by: Table 4.

[^252]: Do-not-answer: evaluating safeguards in LLMs. In Findings of the Association for Computational Linguistics: EACL 2024, Y. Graham and M. Purver (Eds.), St. Julian’s, Malta, pp. 896–911. External Links: [Link](https://aclanthology.org/2024.findings-eacl.61/) Cited by: Table 4.

[^253]: JobFair: a framework for benchmarking gender hiring bias in large language models. In Findings of the Association for Computational Linguistics: EMNLP 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 3227–3246. External Links: [Link](https://aclanthology.org/2024.findings-emnlp.184/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.184) Cited by: Table 4.

[^254]: Safe multi-agent reinforcement learning with natural language constraints. CoRR abs/2405.20018. Cited by: Table 4.

[^255]: Taxonomy of risks posed by language models. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT), External Links: [Document](https://dx.doi.org/10.1145/3531146.3533088), [Link](https://dl.acm.org/doi/10.1145/3531146.3533088) Cited by: §1, §3.

[^256]: Guesstimation: solving the world’s problems on the back of a cocktail napkin. Princeton University Press. Cited by: §C.2.

[^257]: Worldcuisines: a massive-scale benchmark for multilingual and multicultural visual question answering on global cuisines. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 3242–3264. Cited by: Table 4.

[^258]: Adapting probabilistic risk assessment for ai. arXiv preprint arXiv:2504.18536. Cited by: §B.1, Table 1, Table 1, §C.2, §5.

[^259]: Unified triplet-level hallucination evaluation for large vision-language models. External Links: 2410.23114, [Link](https://arxiv.org/abs/2410.23114) Cited by: Table 4.

[^260]: Are watermarks bugs for deepfake detectors? rethinking proactive forensics. In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, Cited by: Table 4.

[^261]: SORRY-bench: systematically evaluating large language model safety refusal. In ICLR, Cited by: Table 4.

[^262]: CoP: agentic red-teaming for large language models using composition of principles. External Links: 2506.00781, [Link](https://arxiv.org/abs/2506.00781) Cited by: Table 4.

[^263]: SafeBench: A benchmarking platform for safety evaluation of autonomous vehicles. In NeurIPS, Cited by: Table 4.

[^264]: MLeVLM: improve multi-level progressive capabilities based on multimodal large language model for medical visual question answering. In Findings of the Association for Computational Linguistics: ACL 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 4977–4997. External Links: [Link](https://aclanthology.org/2024.findings-acl.296/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-acl.296) Cited by: Table 4.

[^265]: Bot-adversarial dialogue for safe conversational agents. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, K. Toutanova, A. Rumshisky, L. Zettlemoyer, D. Hakkani-Tur, I. Beltagy, S. Bethard, R. Cotterell, T. Chakraborty, and Y. Zhou (Eds.), Online, pp. 2950–2968. External Links: [Link](https://aclanthology.org/2021.naacl-main.235/), [Document](https://dx.doi.org/10.18653/v1/2021.naacl-main.235) Cited by: Table 4.

[^266]: SeqAR: jailbreak llms with sequential auto-generated characters. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL 2025 - Volume 1: Long Papers, Albuquerque, New Mexico, USA, April 29 - May 4, 2025, L. Chiruzzo, A. Ritter, and L. Wang (Eds.), pp. 912–931. External Links: [Link](https://doi.org/10.18653/v1/2025.naacl-long.42), [Document](https://dx.doi.org/10.18653/V1/2025.NAACL-LONG.42) Cited by: Table 4.

[^267]: CoSafe: evaluating large language model safety in multi-turn dialogue coreference. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 17494–17508. External Links: [Link](https://aclanthology.org/2024.emnlp-main.968/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.968) Cited by: Table 4, §5.

[^268]: Beyond binary classification: A fine-grained safety dataset for large language models. IEEE Access 12, pp. 64717–64726. External Links: [Link](https://doi.org/10.1109/ACCESS.2024.3393245), [Document](https://dx.doi.org/10.1109/ACCESS.2024.3393245) Cited by: Table 4.

[^269]: GPTFUZZER: red teaming large language models with auto-generated jailbreak prompts. External Links: 2309.10253, [Link](https://arxiv.org/abs/2309.10253) Cited by: Table 4, §5, §6.

[^270]: R-judge: benchmarking safety risk awareness for llm agents. arXiv preprint arXiv:2401.10019. Cited by: §5.

[^271]: S-eval: towards automated and comprehensive safety evaluation for large language models. Proc. ACM Softw. Eng. 2 (ISSTA), pp. 2136–2157. Cited by: Table 4.

[^272]: Air-bench 2024: a safety benchmark based on risk categories from regulations and policies. arXiv preprint arXiv:2407.17436. Cited by: Figure 4, Figure 4, §C.1, §D.2, Table 4, §6, §8.

[^273]: InjecAgent: benchmarking indirect prompt injections in tool-integrated large language model agents. In Findings of the Association for Computational Linguistics: ACL 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 10471–10506. External Links: [Link](https://aclanthology.org/2024.findings-acl.624/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-acl.624) Cited by: Table 4.

[^274]: Cybench: a framework for evaluating cybersecurity capabilities and risks of language models. External Links: 2408.08926, [Link](https://arxiv.org/abs/2408.08926) Cited by: Table 4.

[^275]: Can mllms understand the deep implication behind chinese images?. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), pp. 14369–14402. External Links: [Link](https://aclanthology.org/2025.acl-long.700/) Cited by: Table 4.

[^276]: LMMs-eval: reality check on the evaluation of large multimodal models. In NAACL (Findings), pp. 881–916. Cited by: Table 1, Table 4, §5, §7.

[^277]: Achieving non-discrimination in prediction. External Links: 1703.00060, [Link](https://arxiv.org/abs/1703.00060) Cited by: Table 4, §6.

[^278]: Jade: a linguistics-based safety evaluation platform for large language models. arXiv preprint arXiv:2311.00286. Cited by: Table 1, Table 4, §5, §6.

[^279]: CHiSafetyBench: a chinese hierarchical safety benchmark for large language models. External Links: 2406.10311, [Link](https://arxiv.org/abs/2406.10311) Cited by: Table 4.

[^280]: SafetyBench: evaluating the safety of large language models. pp. 15537–15553. Cited by: Table 4.

[^281]: IHEval: evaluating language models on following the instruction hierarchy. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 8374–8398. External Links: [Link](https://aclanthology.org/2025.naacl-long.425/), [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.425), ISBN 979-8-89176-189-6 Cited by: Table 4.

[^282]: Position: measure dataset diversity, don’t just claim it. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024, External Links: [Link](https://openreview.net/forum?id=jsKr6RVDDs) Cited by: §3.

[^283]: Understanding and evaluating racial biases in image captioning. In 2021 IEEE/CVF International Conference on Computer Vision, ICCV 2021, Montreal, QC, Canada, October 10-17, 2021, pp. 14810–14820. External Links: [Link](https://doi.org/10.1109/ICCV48922.2021.01456), [Document](https://dx.doi.org/10.1109/ICCV48922.2021.01456) Cited by: Table 4.

[^284]: CHBias: bias evaluation and mitigation of Chinese conversational language models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.), Toronto, Canada, pp. 13538–13556. External Links: [Link](https://aclanthology.org/2023.acl-long.757/), [Document](https://dx.doi.org/10.18653/v1/2023.acl-long.757) Cited by: Table 4, §6.

[^285]: Gender bias in coreference resolution: evaluation and debiasing methods. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers), M. Walker, H. Ji, and A. Stent (Eds.), New Orleans, Louisiana, pp. 15–20. External Links: [Link](https://aclanthology.org/N18-2003/), [Document](https://dx.doi.org/10.18653/v1/N18-2003) Cited by: Table 4.

[^286]: WildChat: 1m chatgpt interaction logs in the wild. In Proceedings of the 12th International Conference on Learning Representations (ICLR), Cited by: Figure 4, Figure 4, §C.1, §C.2.

[^287]: Open-world deepfake attribution via confidence-aware asymmetric learning. External Links: 2512.12667, [Link](https://arxiv.org/abs/2512.12667) Cited by: Table 4.

[^288]: Towards identifying social bias in dialog systems: framework, dataset, and benchmark. In Findings of the Association for Computational Linguistics: EMNLP 2022, Abu Dhabi, United Arab Emirates, December 7-11, 2022, Y. Goldberg, Z. Kozareva, and Y. Zhang (Eds.), pp. 3576–3591. External Links: [Link](https://doi.org/10.18653/v1/2022.findings-emnlp.262), [Document](https://dx.doi.org/10.18653/V1/2022.FINDINGS-EMNLP.262) Cited by: Table 4.

[^289]: VALUE: understanding dialect disparity in NLU. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2022, Dublin, Ireland, May 22-27, 2022, S. Muresan, P. Nakov, and A. Villavicencio (Eds.), pp. 3701–3720. External Links: [Link](https://doi.org/10.18653/v1/2022.acl-long.258), [Document](https://dx.doi.org/10.18653/V1/2022.ACL-LONG.258) Cited by: Table 4.

[^290]: Reliability engineering: old problems and new challenges. Reliability engineering & system safety 94 (2), pp. 125–141. Cited by: §C.2, §C.2.

[^291]: MEDFAIR: benchmarking fairness for medical imaging. In International Conference on Learning Representations (ICLR), Cited by: Table 4, §7.

[^292]: Universal and transferable adversarial attacks on aligned language models. CoRR abs/2307.15043. External Links: [Link](https://doi.org/10.48550/arXiv.2307.15043), [Document](https://dx.doi.org/10.48550/ARXIV.2307.15043), 2307.15043 Cited by: Table 4, §1.