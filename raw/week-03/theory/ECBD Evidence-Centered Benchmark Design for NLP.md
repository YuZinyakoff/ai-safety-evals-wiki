---
type: raw
source_kind: theory
capture_method: web-clipper
title: ECBD: Evidence-Centered Benchmark Design for NLP
author: 
site: arxiv.org
published: 
url: https://arxiv.org/html/2406.08723v1
captured: 2026-04-12T13:43:10+03:00
status: unprocessed
---

# ECBD: Evidence-Centered Benchmark Design for NLP

Источник: https://arxiv.org/html/2406.08723v1

## Краткая справка
- Автор: 
- Сайт: arxiv.org
- Дата публикации: 

## Текст
Yu Lu Liu <sup>1,2</sup> Su Lin Blodgett <sup>3</sup> Jackie Chi Kit Cheung <sup>1,2,4</sup>  
Q. Vera Liao <sup>3</sup> Alexandra Olteanu <sup>3</sup> Ziang Xiao <sup>3,5</sup>  
<sup>1</sup> Mila – Quebec Artificial Intelligence Institute   <sup>2</sup> McGill University  
<sup>3</sup> Microsoft Research, Montréal, Canada   <sup>4</sup> Canada CIFAR AI Chair   <sup>5</sup> Johns Hopkins University  
yu.l.liu@mail.mcgill.ca jackie.cheung@mcgill.ca  
{sulin.blodgett,veraliao,alexandra.olteanu}@microsoft.com  
ziang.xiao@jhu.edu

###### Abstract

Benchmarking is seen as critical to assessing progress in NLP. However, creating a benchmark involves many design decisions (e.g., which datasets to include, which metrics to use) that often rely on tacit, untested assumptions about what the benchmark is intended to measure or is actually measuring. There is currently no principled way of analyzing these decisions and how they impact the validity of the benchmark’s measurements. To address this gap, we draw on evidence-centered design in educational assessments and propose Evidence-Centered Benchmark Design (ECBD), a framework which formalizes the benchmark design process into five modules. ECBD specifies the role each module plays in helping practitioners collect evidence about capabilities of interest. Specifically, each module requires benchmark designers to describe, justify, and support benchmark design choices—e.g., clearly specifying the capabilities the benchmark aims to measure or how evidence about those capabilities is collected from model responses. To demonstrate the use of ECBD, we conduct case studies with three benchmarks: BoolQ, SuperGLUE, and HELM. Our analysis reveals common trends in benchmark design and documentation that could threaten the validity of benchmarks’ measurements.

## 1 Introduction

While benchmarking has long been seen as critical to gauging progress in natural language processing (NLP) and guiding model selection for downstream applications, assessing the quality of a benchmark remains a persistent challenge. Do benchmark measurements—most often in the form of numerical scores—provide meaningful insights about the evaluated models and their capabilities? How valid are these measurements? For what purposes are they useful? The field of NLP lacks a systematic way of reflecting on these important questions.

![Refer to caption](https://arxiv.org/html/2406.08723v1/x1.png)

Figure 1: Simplified schema of the Evidence-Centered Benchmark Design ( ECBD ) framework. Solid line arrows indicate the process of designing a benchmark (e.g., designers should decide on the intended uses of the benchmark before deciding what capabilities are of interest). The dotted line arrows indicate the process wherein the benchmark gathers necessary evidence.

At the same time, as NLP models are increasingly believed to be more performant and to exhibit a wider range of capabilities, evaluation in NLP has shifted from measuring model performance on a specific dataset for a single task to using large benchmarks that cover multiple tasks (e.g., GLUE [^34], SuperGLUE [^33], BIG-Bench [^31], HELM [^21]). These benchmarks are increasingly larger and more ambitious (e.g., HELM aims to “assess language models in their totality”), covering ever-growing numbers of tasks, datasets, and metrics aimed at measuring an increasing number of capabilities—i.e., abilities or behaviors that researchers believe the models exhibit or might exhibit. This trend further increases the complexity of assessing benchmark quality.

Such issues with assessing measurement quality do not only concern NLP practitioners. Researchers and practitioners in educational testing often face similar questions: do students’ exam results provide meaningful insights about their ability in, for example, reading comprehension? Can these results be used to determine whether a student needs remedial classes?

In this work, we take inspiration from the Evidence-Centered Design (ECD) framework in educational testing [^25]. ECD views testing as the process of gathering evidence about students’ abilities, and provides guidance on the creation, documentation, and validation of educational tests. We draw an analogy between educational tests and NLP benchmarks and propose the Evidence-Centered Benchmark Design (ECBD) framework, in which we view benchmarking as the process of gathering evidence from objects of evaluation (e.g., language models) about whether or to what degree they have some capabilities of interest.

ECBD unpacks and formalizes benchmark design decisions into five modules, each having a specific role in supporting the process of collecting necessary evidence (see Figure 1). For each module, we provide guiding questions that help benchmark creators document, justify, and validate their design choices. These same questions can also guide benchmark users in analyzing and documenting existing benchmarks to better understand their limitations and how to appropriately use them: what are the design decisions shaping the benchmark? Why did its creators make these decisions? And what evidence do they provide to support their decisions? By doing so, ECBD also supports added transparency about what benchmarks measure, and when and how they can be used. In turn, this transparency can also help our community contest and mitigate issues with current benchmarks.

To illustrate ECBD’s usage for benchmark analysis, we organize these questions into a worksheet (Appendix A) and apply it to three different benchmarks: BoolQ [^11], SuperGLUE [^33], and HELM [^21].<sup>1</sup> Through this exercise, we uncover common issues, such as poor conceptualization of capabilities, that threaten the validity of these benchmarks’ measurements. In general, we find that these benchmarks lack justification and validation, as well as appropriate documentation of the many of their design choices made during their creation.

## 2 Background & Related Work

##### Benchmarking in NLP

At a time when most NLP models were built for a single specific task, [^34] introduced the General Language Understanding Evaluation (GLUE) benchmark with the goal of helping the research community develop models with better general language understanding abilities. It includes a collection of nine English language understanding tasks, covering question answering, sentiment analysis, and textual entailment. Soon after, prompted by the belief that many models were already surpassing the performance of non-expert humans on GLUE, [^33] proposed SuperGLUE.

This trend of evaluating models across an increasing number of datasets and tasks continues, with recent benchmarks such as GEM [^14] [^15], covering 40 language generation tasks. Collaborative and evolving benchmarks such as BIG-Bench [^31], now counting more than 200 tasks in its repository,<sup>2</sup> call on the research community to contribute new tasks.

We designed ECBD to encourage more critical analyses of these increasingly complex benchmarks and a deeper reflection on how benchmark design decisions might affect the validity of benchmark measurements.

##### Critiques and Meta-Analyses

Prior work has also surveyed and critiqued both NLP and machine learning (ML) evaluation more generally. [^10] outline a list of criteria they argue that useful benchmarks for natural language understanding (NLU) should meet, including validity. Similarly, [^32] highlights the disconnect between benchmark results and real world impacts—e.g., does a given increase on the benchmark actually lead to positive impact in the tested domain of application?—while [^22] argue for centering language models’ evaluation on how models will be used in practice. Analyses of benchmarks in NLP evaluation have raised concerns about annotation artifacts [^17], threats to validity [^9], lack of justification surrounding design choices [^16], inconsistent results from benchmarks aimed at measuring similar things [^1], and benchmarks’ lack of robustness [^2].

##### NLP and ML Documentation

Various documentation guidelines have been proposed for NLP and ML datasets, models, and systems [^6] [^4] [^26] [^13] [^7]. Datasheets for Datasets [^13] provides a standardized process for documenting ML datasets, formulated as a list of questions (e.g., “Does the dataset contain data that might be considered confidential?”). In NLP, Data Statements for NLP [^6] contains guidelines more specific to speech and text data, asking practitioners to document details about how data is curated, such as the demographics of the speakers included. Similarly, Model Cards [^26] and FactSheets [^4] have been proposed to support better model and AI service documentation.

Our work contributes to these efforts by providing a set of guidelines for documenting NLP benchmark design choices. Our focus, however, is on design choices that affect how benchmarks are used to gather the necessary evidence about whether, or to what degree, an evaluated model has some capabilities of interest. Our framework also guides the process of gathering the required validity evidence for benchmark measurements.

##### Measurement Theory

In the social sciences, hypothesized theoretical entities known as constructs (e.g., a person’s creativity, attitude towards a social issue) cannot be directly measured [^19]. Instead, the measurement is indirect, relying on samples of observable behaviors obtained through tests. Measurement theory is the study of test development, aiming to minimize measurement error so to produce the best measurements of the desired constructs [^5]. Educational testing is rooted in measurement theory, aiming to produce the best measurements of students’ abilities.

The quality of tests depends on their validity, which refers to “the degree to which evidence and theory support the interpretations of test scores for proposed uses of tests” [^3]. [^5] argues that it is the most important quality of a test as it concerns the fundamental issue of what measurement instruments (i.e., tests) are really measuring.

These concepts are relevant to NLP, as many desirable model capabilities (e.g., language understanding) cannot be directly measured; they are unobservable constructs, and NLP benchmarks can be seen as tests that use observable model behaviors (e.g., LM-generated text) to measure these constructs [^35]. This raises key concerns about the validity of the performance measurements obtained with various NLP benchmarks [^9] [^10] [^12].

##### Evidence-Centered Design (ECD) in Education

is a framework introduced in the field of education with the goal of guiding the design, evaluation, and interpretation of educational tests [^25]. Our main source of inspiration to create Evidence-Centered Benchmark Design (ECBD) comes from the conceptual assessment framework (CAF), a vital component of ECD consisting of five models:

1. Student model: specifies the constructs that characterize the students and that the test aims to measure. This model connects the test to its intended uses (e.g., if a test is to determine whether students need remedial language classes, should their reading comprehension skill be measured?).
2. Task model: builds a pool of tasks (i.e., test items) that draw out responses from students. Since the test relies on these responses to measure the constructs of interest, the tasks should elicit evidence about those constructs.
3. Presentation model: specifies how a given test item or task is presented to students (e.g., font size, instructions given by teachers). The goal is to avoid introducing measurement error (e.g., due to differences in the readability of the test using inconsistent font sizes).
4. Assembly model: specifies how tasks are selected from the available pool to be presented to students (e.g., when there are 100 exam questions but students can only answer 20, how should the test select these 20 questions?). This model also specifies and helps assess the amount of evidence that will be collected (e.g., are the selected 20 questions sufficient to measure reading comprehension?)
5. Evidence model: specifies how to measure constructs specified in the student model by observing students’ performance on the presented test items. It consists of two components: one specifies item-level scoring (i.e., extracting evidence from students’ performance on a single test item) and the other specifies test-level scoring (i.e., accumulating extracted evidence across all presented test items).

In summary, each CAF model has specific roles to fulfill, and together they roadmap the process of educational testing. We adapt CAF models to NLP benchmarking, proposing a framework for benchmark design that similarly centers evidence in measurement.

## 3 Evidence-Centered Benchmark Design

![Refer to caption](https://arxiv.org/html/2406.08723v1/x2.png)

Figure 2: The Evidence-Centered Benchmark Design framework. Solid line arrows indicate the process of designing a benchmark (e.g., designers decide on the intended uses of the benchmark before deciding what capabilities are of interest). The dotted line arrows indicate the process of the benchmark gathering necessary capability evidence.

We consider benchmarking as the process of gathering *capability evidence* from objects of evaluation (e.g., LMs)—i.e., evidence about whether or to what degree those objects have some capabilities of interest. Evidence-Centered Benchmark Design (ECBD) structures this process into five modules,<sup>3</sup> each of which has a specific role in helping collect the necessary capability evidence: the capability module (§3.1), the content module (§3.2), the adaptation module (§3.3), the assembly module (§3.4), and the evidence module (§3.5). See Figure 2 for an overview of ECBD.

For each module, ECBD breaks down the design process into three required actions. To guide benchmark creation, ECBD requires benchmark creators to i) describe their design choices; ii) justify these choices, forming hypotheses about how they ensure that the module accomplishes its role; and iii) provide support for these hypotheses, which requires gathering either evidence showing that underlying constructs are well-defined and well-grounded, or validity evidence—i.e., evidence about how benchmark design choices might support or threaten the validity of the resulting benchmark measurements. Such evidence can be theoretical (e.g., work conceptualizing a capability) or empirical (e.g., experiments correlating benchmark measurements with some ground truth).

In addition to helping benchmark creators reflect on their design choices, ECBD can also support benchmark analysis by benchmark users or third parties by drawing attention to whether and how benchmark creators describe and justify their design decisions, and to what extent there is validity evidence supporting these decisions.

We also organize ECBD in a worksheet of 20 questions to facilitate its use (Appendix A). Benchmark creators can use this worksheet while constructing a benchmark, with each question meant to encourage them to reflect on their decisions and make their assumptions explicit. When analyzing existing benchmarks, the worksheet can be completed by referring to available documentation of the benchmark under analysis (e.g., papers, blog posts).

##### Benchmark Intended Use

While establishing the intended use of a benchmark is not a ECBD module per se, it is a critical step that should precede benchmark design or analysis using ECBD modules. This first step is important as the validity of the resulting benchmark measurements often concerns whether the benchmark can be used as intended. Articulating a benchmark’s intended use requires specifying: i) What are the intended objects of evaluation (analogously, “test takers”)? ii) Who are the intended users of the benchmark? and iii) How should they interpret and use the benchmark results?

A benchmark’s design choices should be assessed with respect to its intended use. This intended use might be closely connected to the use context of the evaluated model (e.g., aiming to inform deployment decisions of automatic summarizers for medical records), or it might not be directly connected to any downstream applications (e.g., aiming to compare language models’ and humans’ linguistic abilities).

If the intended use is not clearly stated, benchmark creators risk making choices simply because they are convenient or common practices, likely resulting in a benchmark that does not serve any particular purpose. Furthermore, if the intended use is not clearly communicated to potential users, they could unintentionally misuse the benchmark (e.g., use it to evaluate other objects than those intended), or misinterpret the resulting measurements.

### 3.1 Capability Module

The capability module specifies the capabilities—constructs that the objects of evaluation are thought to exhibit or possess—that the benchmark aims to measure. For NLP models, such capabilities might encompass a wide range of model characteristics and properties, such as reasoning, multilingual understanding, stereotyping, or toxicity. What capabilities we might want to measure, however, depends on the benchmark’s intended use. Thus, this module is also intended to capture the connection between the benchmark and its intended use. To do so, it requires benchmark creators to define the capabilities of interest, justify the aforementioned connection, and provide appropriate grounding for how these capabilities are defined. This process encourages reflection on the definitions of the capabilities of interest, to ensure that they are i) well-matched to the benchmark’s intended use, and ii) well-grounded, as capabilities may be contested and context-dependent (e.g., who are the users of an evaluated model, and what are their needs?).

Theoretical work conceptualizing capabilities, as well as empirical work seeking to understand contexts of use and capabilities relevant to those contexts, could provide evidence that the choices of capabilities and accompanying definitions are well-grounded. For example, [^23] conduct survey studies with topical experts and end users to understand what evaluation criteria are important for explainable AI algorithms.

### 3.2 Content Module

The content module specifies the pool of available test items that the benchmark could require objects of evaluation to perform or respond to. These test items should help elicit evidence about the capabilities of interest, so that this evidence can be later extracted from the responses and accumulated to produce measurements of those capabilities (§3.5). Note that it is not necessary for each test item to target all capabilities of interest, as items can be used in combination (see §3.4).

Through the characteristics of the test items, benchmark creators should justify how each test item elicits evidence about the capabilities it targets. Gathering validity evidence for this module—evidence about how the test items help us elicit useful signals about the capabilities of interest—could involve research studies or experts assessing whether test items capture the capabilities of interest.<sup>4</sup> The research study by [^9] is such an example, as it examines whether NLP benchmarks meant to measure stereotyping actually measure stereotyping. They identify, for instance, test items that contain true facts instead of harmful stereotypes (e.g., “Afghanistan shares a border with Pakistan. Most people there are Muslim.” [^27]). An evaluated model favoring such items is likely not indicative of the model producing harmful stereotypes. Consequently, the prevalence of such test items threatens the validity of these benchmarks.

### 3.3 Adaptation Module

The adaptation module specifies how test conditions are constructed, and how objects of evaluation are instructed (e.g., students) or adapted (e.g., models) for each test item. For example, benchmarks for evaluating models might employ methods that add examples in few-shot prompting, or adapt models by fine-tuning with examples. These methods and the data they involve are specified in the adaptation module and should be chosen carefully so as to not confound benchmark measurements. The adaptation module should ensure that test conditions and adapted test items are well-suited to all objects of evaluation and not disadvantage some objects.

For example, if a benchmark employs prompting for LMs, some LMs might respond poorly to certain prompt formats [^30], thus confounding benchmark results; poor performance might be indicative of this sensitivity to prompt formatting instead of providing meaningful information about the capabilities of interest.

### 3.4 Assembly Module

The pool of available test items specified by the content module (§3.2) is what the benchmark has available to use. The assembly module specifies which items from this pool are actually used by the benchmark for evaluation, and whether this subset enables practitioners to use the benchmark to gather sufficient evidence for all capabilities of interest.

The simplest assembly method would be to use all available items. When there are resource constraints (e.g., computational, financial, or time), it may become necessary to consider more sophisticated assembly methods to make sure the benchmark measurements remain valid and useful. For instance, using a smaller set of test items should not introduce an unacceptable amount of measurement error.

### 3.5 Evidence Module

The evidence module specifies how capability evidence is extracted from responses obtained from objects of evaluation (evidence extraction), and how this evidence is accumulated to produce benchmark measurements that capture the capabilities of interest (evidence accumulation).

##### Evidence Extraction

For each presented test item, objects of evaluation produce observable responses (e.g., LM-generated text, token probabilities). Evidence extraction involves specifying what type of responses are elicited from the objects of evaluation and the capability evidence we can infer from these responses.

This process necessarily involves representing the evidence via some observable variables such as numerical scores (e.g., 1/0 to indicate that a LM-generated text is “fluent”/“disfluent,” representing a piece of evidence about the LM’s ability to generate fluent text). Benchmark creators therefore need to justify and show that these variables actually capture the target capabilities. For example, experiments examining the correlation between automatic metrics and human annotations (presumed ground truth) could in some cases provide validity evidence for this component of the module.

##### Evidence Accumulation

Benchmarks involving multiple test items often need to accumulate multiple pieces of extracted evidence to produce measurements of the capabilities of interest to be interpreted and used. This component of the module thus connects observable variables used for evidence extraction to the capability module (Section 3.1): the accumulated evidence should capture the capabilities of interest. For example, the benchmark measurements might be computed as the average of item-level responses, if the distribution of those responses is assumed to follow a normal distribution. Gathering validity evidence could involve testing this assumption about the distribution.

## 4 Case Studies

To illustrate how our framework guides benchmark analysis and helps foreground possible validity concerns, we apply the ECBD worksheet to analyze HELM [^21], SuperGLUE [^33], and BoolQ [^11].

### 4.1 Analyzed Benchmarks

SuperGLUE aims to be “a more rigorous test of language understanding” than its predecessor GLUE [^34]. It includes 8 pre-existing datasets, each corresponding to a “language understanding task.” HELM, the most recent benchmark of the three, is meant to be a “living benchmark” that is continuously updated. When its accompanying paper was first published, HELM included 15 existing datasets.<sup>5</sup> BoolQ includes a dataset of real user yes/no queries, which is re-used in both SuperGLUE and HELM.

These benchmarks are different in many ways: they are from different points in time and of various sizes, aim to capture different capabilities, and are constructed differently (e.g., BoolQ introduces a novel dataset while SuperGLUE and HELM re-purposes existing datasets). Due to its flexibility, ECBD can be applied to all these benchmarks.

### 4.2 Method

The ECBD worksheet for each benchmark was completed by two to three authors of this paper, where one author first read the paper introducing that benchmark, and then re-read it while completing the worksheet. At least two other authors then examined the completed worksheets while reading the paper. We discussed and resolved any ambiguities and inconsistencies that arose during this process both in the phrasing of the worksheet questions and in how to use the information provided in the benchmark papers to answer the questions. The completed worksheets can be found at [https://github.com/isle-dev/ECBD](https://github.com/isle-dev/ECBD).

### 4.3 Observations

We overview key concerns with the design of existing benchmarks that ECBD’s modules helped us foreground.

##### Intended use: Benchmarks’ intended uses are vaguely specified.

Specifying a benchmark’s intended uses is a crucial first step in ECBD. In examining how the three benchmarks discuss their intended uses, we found little description of who their intended users are and how they should interpret and use the resulting measurements. HELM explicitly states that the use and interpretation of benchmark measurements is up to the users to decide for themselves.<sup>6</sup> Since validity involves whether benchmark measurements can be used as intended, this lack of information makes the analysis and validation of these benchmarks difficult—in particular, assessing whether measured capabilities are relevant to benchmarks’ intended uses.

##### Capability module: When evaluating complex capabilities, benchmarks seem to break down capabilities of interest into intermediate capabilities that are perhaps easier to measure, but this process is sometimes not explicitly described.

![Refer to caption](https://arxiv.org/html/2406.08723v1/x3.png)

Figure 3: Different levels of capabilities and their connection, in HELM and SuperGLUE. In SuperGLUE, the connection between sub-capabilities (e.g., “causal reasoning” ) and “general-purpose language understanding” is not explained. It is thus denoted by the dotted lines and the question mark.

ECBD’s capability module draws attention towards what capabilities the benchmarks measure and how they are conceptualized. For SuperGLUE, which aims to measure “general language understanding” (GLU), we found that the benchmark seems to consider intermediate capabilities of interest that contribute to measuring GLU (see Figure 3). The paper’s descriptions of datasets introduce constructs such as “causal reasoning,” <sup>7</sup> treating them as though they are self-evidently relevant to GLU. However, these additional constructs are not defined, and their connection to GLU is left implied. This lack of clarity about capabilities of interest makes it difficult to analyze whether a benchmark properly operationalizes them. HELM provides more descriptions of choices and definitions of capabilities: it draws an explicit connection between the overall capability under measurement—“practical utility”—and the seven intermediate capabilities of interest—e.g., “accuracy,” “calibration”—which are selected as they are believed to reflect what “it mean\[s\] for a system to be useful” [^21]. The relationships between these overall and intermediate capabilities, however, might need further interrogation.

##### Capability module: The capabilities the benchmarks are purportedly measuring are often poorly and/or inconsistently conceptualized.

ECBD requires benchmark creators not only to say what they want to measure but also to justify why they want to measure it. This helps us foreground inconsistencies in how these capabilities are defined and justified. For example, some of the analyzed benchmarks collapse the constructs they are designed to measure with the measurement of those constructs. Specifically, HELM describes e.g., “accuracy” (the construct) as an “umbrella term for the standard accuracy-like metric” [^21] (possible measurements of the construct). This makes it difficult to even know what capability the resulting measurements actually measure.

Furthermore, constructs sometimes lack appropriate grounding; for example, HELM conceptualizes constructs like “fairness,” “bias,” and “toxicity” as measurable without requiring ‘‘knowledge about the broader social context” [^21]. We know from prior work, however, that more often than not, such constructs are contested and depend on the context in which they are applied [^8] [^19]. While such inconsistencies are not necessarily problematic, they can give rise to validity concerns if the benchmark’s conceptualizations are not well-justified.

##### Content module: For benchmarks re-purposing data, we found little justification connecting the data to capabilities of interest.

Pre-existing data that is re-purposed by a benchmark may not be fit for measuring the capabilities that benchmark aims to measure. By requiring benchmark creators to justify their choice of data, ECBD’s content module helps highlight potential disconnects between capabilities of interest and the re-purposed data. For instance, the BoolQ dataset was re-purposed by HELM to measure “(social) bias,” among other capabilities. Since this dataset was not designed to elicit evidence about “bias,” ECBD requires HELM to justify and validate the re-use of this data to capture this capability. We found no such justification or validation, which raises doubts about whether the resulting measurement is meaningful.

##### Adaptation module: Some benchmarks do not prescribe adaptation methods.

ECBD’s adaptation module draws attention to the suitability of adaptation methods. Among the benchmarks we inspected, only HELM prescribed an adaptation strategy: few-shot prompting with 5 in-context examples. Once chosen for a given dataset, these examples and the prompt template (e.g., instructions) stay fixed across all test items from that dataset, as well as across all evaluated models. BoolQ and SuperGLUE do not specify whether or how evaluated models need to be adapted. As benchmark users are free to decide for themselves what methods to employ, it might be difficult to meaningfully interpret benchmark measurements when users adopt different adaptation methods for the same benchmark. We recommend that users report what adaptation methods they employ, if such methods are not prescribed by the benchmark.

##### Assembly module: The choices surrounding assembly methods are often taken as self-evidently appropriate.

We find that the benchmarks we examined do not fully describe or justify the choices of assembly methods. For BoolQ, we only found brief mentions that test items are split into training, development, and test sets, without further elaboration about why and how items are selected to be part of the test set. SuperGLUE uses existing train/dev/test splits from the datasets it re-purposes, but does not describe how these splits were originally constructed or justify the continued use of those splits. For HELM, a maximum of 1,000 test items per dataset are selected for evaluation, but we found no description about the exact selection process. This lack of attention to assembly methods could hinder benchmark creators from considering alternative methods (e.g., selecting test items based on their difficulty [^24]) and reflecting about possible trade-offs different methods might help them make, such as balancing resource constraints with possible threats to validity.

##### Evidence module: The way evidence is being extracted and accumulated is often only justified by a desire to follow similar practices as prior work.

All three benchmarks use automatic metrics to extract evidence, such as exact-match for classification tasks and ROUGE-2 for summarization. These metric scores are then accumulated through functions like F1-score or by averaging. ECBD’s evidence module requires benchmark creators to justify these choices, particularly with respect to the role they play in extracting and accumulating capability evidence. However, we found that when such choices are justified, the explanations often do not focus on whether or how these methods help capture the capabilities of interest. Instead, benchmark creators only briefly mention that the metrics they use are “standard” or “default” for a certain task [^21], or that they are “follow\[ing\] prior work” [^33] when choosing metrics or aggregation functions.

We encourage benchmark creators to more carefully consider their choices in the evidence module, including questioning methodology used in prior work, so as not to risk perpetuating the use of currently popular yet potentially unsuitable methodology. Even where methods may be well-justified in prior work, they may not always be well-suited to other contexts (e.g., with differently defined capabilities under measurement), and their appropriateness to new contexts should always be justified.

##### Evidence module: Even when new evaluation methods are introduced, we still find little justification for how the methods capture the capabilities of interest.

For example, HELM introduces new automatic metrics to measure “(social) bias” through demographic representation. The metric first counts occurrences of words related to each considered demographic group (e.g., “gomez,” “martinez,” for the group “Hispanic”) in model outputs. It then compares the word counts to the uniform distribution (i.e., where every demographic group is equally represented). Some design choices, such as the demographic groups under consideration and their corresponding word lists, are well-described. However, we found little justification for them—for example, why does the benchmark use the demographic groups “White,” “Hispanic,” and “Asian” to measure racial bias? Why is the uniform distribution a suitable reference distribution? Under ECBD, the creators of HELM would need to justify how these design decisions enable the new metric to capture “(social) bias.”

##### The benchmarks rarely gather validity evidence to support their design choices.

All modules in ECBD require collecting validity evidence to support benchmark design choices. The benchmarks we examined either do not describe collecting such evidence, or acknowledge the need for it but leave gathering it to future work. We encourage benchmark creators to identify and use validity evidence that may already exist, and plan future experiments to gather necessary validity evidence. For existing benchmarks, identifying and developing this evidence may require efforts from other researchers, benchmark users, or other practitioners. Appropriate incentives from the community could encourage future efforts on gathering validity evidence and on examining how to integrate this evidence into the use of existing benchmarks (e.g., how might a benchmark that includes a metric which is found to be unsuitable be used?). For future benchmarks, we strongly encourage benchmark creators to gather and report validity evidence supporting their design choices during the process of benchmark design.

## 5 Conclusion

To guide NLP benchmark creation and analysis, we take inspiration from the evidence-centered design framework from the field of educational testing to propose ECBD (Evidence-Centered Benchmark Design). Our framework formalizes the benchmark design process into five modules that each play a critical role in gathering valid and useful capability evidence—i.e., evidence about whether or to what degree objects of evaluation have some capabilities of interest.

We demonstrated its utility by using it to analyze BoolQ, SuperGLUE, and HELM, finding common practices that threaten the validity of their measurements. For example, for these benchmarks we found more of a focus on describing design choices (e.g., which dataset/metric is used), and less on justifying them and their role in the benchmark. Gathering validity evidence is also rare.

Future directions include further analyses of our framework’s utility in guiding the creation of benchmarks. It is also important to understand how ECBD helps increase transparency and supports practitioners in achieving a greater understanding of benchmark results and their limitations. Future work might also examine this, for example through user studies with benchmark creators and users. As ECBD does not constrain the model inputs and outputs to be textual, we also see it to be applicable or adaptable to multi-modal NLP benchmarks, or to other areas in ML and AI.

## Limitations

### Framework and Worksheet

While we have developed ECBD and the accompanying worksheet to guide practitioners through the essential components of the benchmark design process, the questions for each module are not exhaustive, and it is possible that practitioners will identify additional questions particularly relevant to their own benchmark creation or analysis processes.

We also note that assessing a benchmark should involve many criteria beyond validity, such as the provenance of test items (did those who created the data consent to its use?) [^29], privacy (do test items reveal sensitive or personally identifying information?) [^18], and the reliability of the measurements (can they be repeated?) [^19].

### Case Studies

The choice of benchmarks to analyze (i.e., BoolQ, SuperGLUE, and HELM) likely also limits our findings. Although there are many differences between them, these benchmarks are unlikely to cover the wide space of possibilities in benchmark design. We have not analyzed, for instance, dynamic benchmarks that create test items instead of relying on existing data [^20].

Furthermore, our analysis relied only on the papers introducing each of the three benchmarks, namely the work of [^11], of [^33], and of [^21]. We have not used other sources of information on the benchmarks, such as their official websites and code repositories, which could limit our analysis. On the other hand, only relying on the papers allows us to examine the benchmark creators’ reporting practices.

Finally, the case studies are subject to our reading. We could have missed or misinterpreted passages from the analyzed papers.

## Ethical Considerations

NLP benchmarks not only influence the development and use of specific NLP models—e.g., how performant is a specific model believed to be?—but also help to construct the field’s priorities and norms—e.g., what capabilities are researchers developing models towards, and what is seen as evidence of success? Well-documented and more valid benchmarks run less risk of misguiding benchmark users and stakeholders of evaluated models—potentially avoiding e.g., the costs of optimizing models towards the wrong goal or deploying models with undetected issues, causing harms to users.

By proposing a more principled way of designing and analyzing NLP benchmarks, we hope to encourage the construction of well-documented and more valid benchmarks. However, our work could potentially have the unintended, opposite impact of discouraging future work in benchmark design. Although we believe that the benefits of following ECBD outweigh its costs, extensive documentation in following ECBD, as well as conducting experiments to gather validity evidence, could be expensive and time-consuming. Finally, although we intend for ECBD to encourage meaningful reflection during the benchmark design process, as with all documentation there is a risk that it will instead be treated as a checklist.

## Acknowledgements

We would like to thank Susu Zhang for their helpful discussions and feedback. This work is supported by a joint Microsoft Research–Mila grant. Yu Lu Liu is supported by a Fonds de Recherche du Québec Nature et Technologies master research scholarship (File #330991). Jackie C.K. Cheung is a consulting researcher at Microsoft Research Montréal. Finally, we thank the anonymous reviewers for their valuable feedback.

## References

## Appendix A Worksheet Template

### Introduction

Evidence-Centered Benchmark Design (ECBD) is a framework that formalizes the benchmark design process. It requires first specifying the intended use of the benchmark (including specifying the objects of evaluation). The process is then broken down into five modules:

1. Capability module: capabilities that the benchmark aims to measure.
2. Content module: pool of test items that draw out responses from the objects.
3. Adaptation module: adapting or instructing the objects to complete the tasks.
4. Assembly module: selecting from the pool of test items to build the set used for evaluation.
5. Evidence module: extracting and accumulating evidence about the capabilities of interest from responses produced by the objects.

This worksheet provides guidance on how to create a new benchmark or analyze an existing benchmark following ECBD. It can be completed from different perspectives: as the creator of a new benchmark, as the custodian or the user of an existing benchmark, or as a third-party analyzing benchmarks, etc. Each module contains three questions:

1. Describe: What design decisions did the benchmark creators make for this module?
2. Justify: Why did the benchmark creators make these decisions? This involves forming a hypothesis that the decisions allow the module to accomplish its role in the process of gathering necessary capability evidence.
3. Support: What validity evidence do the benchmark creators have to support the above hypothesis? In other words, what shows that the module indeed accomplishes its role?

This worksheet is not a checklist, and it is not required to answer each question perfectly. These questions are meant to encourage reflection and validation of benchmark design decisions, as well as to guide benchmark documentation.

### Benchmark Name and Reference(s)

The references are the source of information used to complete this worksheet. For example, a third-party analyzing an existing benchmark may choose to use the academic publication introducing said benchmark as their source of information. Other sources of information could be blog posts, official websites, or code repositories accompanying the benchmark.

\[ANSWER HERE\]

### Who is filing the worksheet?

From what perspective is this worksheet completed? In other words, what is the relation between the person(s) completing this worksheet and the benchmark that is the focus of this worksheet?

\[ANSWER HERE\]

### A.1 Intended Use

Q1 - Who/What are the intended objects of evaluation? Elaboration on the objects of evaluation (e.g., their assumed capabilities, demographic information for human objects of evaluation, etc.) helps us better understand whether the benchmark is suitable for all intended objects of evaluation.

\[ANSWER HERE\]

##### Q2 - What is the intended use of the benchmark? Who are the intended users of the benchmark?

Benchmark results aim to provide insights about the objects of evaluation: how are users meant to use these insights?

\[ANSWER HERE\]

### A.2 Capability Module

The capability module specifies the capabilities that the benchmark aims to evaluate. The term “capability” refers to a construct (e.g., quality criteria, skill, etc.) that the objects of evaluation are thought to exhibit or possess. Capabilities often cannot be directly observed or directly measured, thus requiring the benchmark to indirectly measure them by gathering necessary evidence about said capabilities.  

Q3 - DESCRIBE: i) What are the capabilities of interest? ii) How is each one defined, and under what context is each one defined?

\[ANSWER HERE\]

Additional recommended questions to consider so to further clarify and contextualize the definitions (in benchmark analysis: as presented by the benchmark):

- How does the definition used by the benchmark differ from other existing definitions of this capability?  
	\[ANSWER HERE\]
- How does this capability differ from other similarly defined capabilities?  
	\[ANSWER HERE\]

##### Q4 - JUSTIFY: How are the capabilities of interest connected to the intended use of the benchmark (specified in Q2)? Are the capabilities theoretically attainable by the objects to be evaluated?

Explain the interest in measuring the capabilities in Q3 and question whether it may be impossible for the objects of evaluation to have said capabilities.

\[ANSWER HERE\]  

Q5 - SUPPORT: What validity evidence do the benchmark creators offer to support the choice and definition of capabilities of interest?

\[ANSWER HERE\]

### A.3 Content Module

The content module specifies test items that the benchmark could require objects of evaluation to perform or to respond to. The test items should elicit evidence about some capability of interest, so that said capability evidence can be later extracted from the responses and aggregated to produce a measurement of said capability.

##### Q6 - DESCRIBE:

i) Characterize the test items. Most often, NLP evaluation relies on input data, so this step could involve describing the data that is available to the benchmark to use, how the data is obtained, etc. ii) Which capabilities of interest does each test item aim to capture? Each item can aim to capture one or several capabilities amongst those listed in Q3.

\[ANSWER HERE\]  

Q7 - JUSTIFY: How does each test item elicit evidence about its target capabilities? Justify via the characteristics of the test items (Q6).

\[ANSWER HERE\]

##### Q8 - SUPPORT: What evidence do the benchmark creators offer to support content validity of the test items?

In other words, we question whether the test items captures capabilities of interest. Content validity is often based on analysis by external experts or benchmark users.

\[ANSWER HERE\]

### A.4 Adaptation Module

When evaluating humans, the benchmark might instruct them to perform a task by providing instructions, training exercises, demonstrations, etc. When evaluating models/systems, there are also myriad methods that i) modify the models/systems (e.g., fine-tuning), or ii) format or add onto the input (e.g., adding examples in few-shot prompting). These adaptation methods should be chosen carefully so as to not confound evaluation results.  

Q9 - DESCRIBE: Given an input, how are the objects of evaluation adapted or instructed to provide the output?

\[ANSWER HERE\]  

Q10 - JUSTIFY: Elaborate on the suitability of the adaptation methods for all intended objects of evaluation.

\[ANSWER HERE\]  

Q11 - SUPPORT: What validity evidence do benchmark designers offer that supports the choice of the adaptation methods?

\[ANSWER HERE\]

### A.5 Assembly Module

Test items specified by the content module are what the benchmark could use. The assembly module concerns what items from that pool will actually be used by the benchmark for evaluation, and whether this set allows the benchmark to gather sufficient evidence.  

Q12 - DESCRIBE: How many test items are chosen to assemble the subset used for evaluation? What factors inform this selection?

\[ANSWER HERE\]  

Q13 - JUSTIFY: How does the described assembly method ensure that the produced subset elicits sufficient evidence for all capabilities of interest?

\[ANSWER HERE\]  

Q14 - SUPPORT: What validity evidence do the benchmark creators offer to support the choice of assembly methods?

\[ANSWER HERE\]

### A.6 Evidence Module

#### A.6.1 Evidence Extraction Component

In response to each presented test item, objects of evaluation produce observable behaviors (referred to as “responses”) which are captured by the benchmark. From these responses, the benchmark extracts evidence about capabilities of interest that said test item targets (referred to as “salient evidence”).

##### Q15 - DESCRIBE: For each test item,

i) What responses are captured and used for evidence extraction? When evaluating humans, many types of responses can be captured: selection in multiple-choice questions, long-form answers, response time, etc. Similarly, the benchmark can use the generated text (decoded in a certain way), token probabilities, running time, etc. ii) How is evidence extracted and represented?

\[ANSWER HERE\]  

Q16 - JUSTIFY: How does the extracted evidence capture the capabilities of interest?

\[ANSWER HERE\]  

Q17 - SUPPORT: What validity evidence do the benchmark creators offer to support the choice of evidence extraction method?

\[ANSWER HERE\]  

#### A.6.2 Evidence Accumulation Component

Q18 - DESCRIBE: How is the evidence accumulated to draw insights about the objects of evaluation in terms of capabilities of interest?

\[ANSWER HERE\]  

Q19 - JUSTIFY: How does the method of accumulating evidence capture capabilities of interest?

\[ANSWER HERE\]  

Q20 - SUPPORT: What validity evidence do the benchmark creators offer to support the choice of evidence accumulation method?

\[ANSWER HERE\]  

## Appendix B Glossary

We compile terminology used in the present paper and in the ECBD worksheet in Table 1.

| Term | Meaning |
| --- | --- |
| Objects of evaluation | Models, systems, people, etc. that are to be evaluated. |
| Capability | Quality criteria, ability, skill, etc. that characterizes the objects of evaluation. They are very often not observable nor directly measurable. |
| Capability evidence | Evidence indicating whether or to what degree an object of evaluation has the capability of interest. For example, a language model (object of evaluation) detecting the grammatical error in “their going to the mall.” can be a piece of evidence supporting the belief that the model has grammatical knowledge (capability of interest). |
| Benchmarking (verb); a benchmark (noun) | We view benchmarking as a process of gathering capability evidence from the objects of evaluation about the capabilities of interest. A benchmark is a collection of measurement instruments that supports the above process. |
| Benchmark results | The final product of benchmarking, often in the form of numerical scores (e.g., ratio), rankings, or categorization (e.g., detecting that an object of evaluation is “biased”). The results inform benchmark users about the objects of evaluation, about to whether or to what degree the object has the capabilities of interest. |
| Validity Evidence | Evidence supporting whether the benchmark results can be interpreted as it is originally intended to be interpreted, whether the benchmark can be used as it is originally intended to be used. In other words, it is evidence supporting that the capability evidence gathered is actually meaningful with respect to the intended uses of the benchmark. Validity evidence can be theoretical or empirical/ |
| Validity; validation | Validity is the degree to which all the accumulated validity evidence supports the intended interpretation of benchmark results for the intended use of the benchmark. Validation is thus the process of accumulating validity evidence |
| Test item | A single evaluation instance of the benchmark that objects of evaluation can be asked to perform or respond to in order to obtain outputs or behaviours from them. |
| Response | Outputs or behaviours from the objects of evaluation in response to a test item presented to them. These are expected to be observable. For example, a matrix of token probabilities can be a response from a language model. The decoded text that the model generated can also be a response. What response to capture is a benchmark design decision. |
| Context (in the capability module) | Where and how the objects of evaluation are intended to be used or intended to operate under. Context can involve the types of model/system users, other stakeholders, the domain of application, the linguistic phenomena the systems are meant to represent, etc. The definition of capabilities can greatly vary depending on context (e.g., informativeness of some texts varies for expert vs. non-expert readers) |

  
  

Table 1: Glossary

[^1]: Afra Feyza Akyürek, Muhammed Yusuf Kocyigit, Sejin Paik, and Derry Tanti Wijaya. 2022. [Challenges in measuring bias via open-ended language generation](https://doi.org/10.18653/v1/2022.gebnlp-1.9). In *Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing (GeBNLP)*, pages 76–76, Seattle, Washington. Association for Computational Linguistics.

[^2]: Norah Alzahrani, Hisham Abdullah Alyahya, Yazeed Alnumay, Sultan Alrashed, Shaykhah Alsubaie, Yusef Almushaykeh, Faisal Mirza, Nouf Alotaibi, Nora Altwairesh, Areeb Alowisheq, M Saiful Bari, and Haidar Khan. 2024. When benchmarks are targets: Revealing the sensitivity of large language model leaderboards. *arXiv preprint arXiv:2402.01781*.

[^3]: & National Council on Measurement in Education American Educational Research Association, American Psychological Association. 2014. *Standards for educational and psychological testing*. American Educational Research Association, Lanham, MD.

[^4]: M. Arnold, R. K. E. Bellamy, M. Hind, S. Houde, S. Mehta, A. Mojsilović, R. Nair, K. Natesan Ramamurthy, A. Olteanu, D. Piorkowski, D. Reimer, J. Richards, J. Tsay, and K. R. Varshney. 2019. FactSheets: Increasing trust in AI services through supplier’s declarations of conformity. *IBM Journal of Research and Development*, 63(4/5):6:1–6:13.

[^5]: Deborah L. Bandalos. 2018. *Measurement theory and applications for the social sciences*. The Guilford Press.

[^6]: Emily M. Bender and Batya Friedman. 2018. [Data statements for natural language processing: Toward mitigating system bias and enabling better science](https://doi.org/10.1162/tacl_a_00041). *Transactions of the Association for Computational Linguistics*, 6:587–604.

[^7]: Eshta Bhardwaj, Harshit Gujral, Siyi Wu, Ciara Zogheib, Tegan Maharaj, and Christoph Becker. 2024. Machine learning data practices through a data curation lens: An evaluation framework. *ACM Conference on Fairness, Accountability, and Transparency*.

[^8]: Su Lin Blodgett, Solon Barocas, Hal Daumé III, and Hanna Wallach. 2020. [Language (technology) is power: A critical survey of “bias” in NLP](https://doi.org/10.18653/v1/2020.acl-main.485). In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pages 5454–5476, Online. Association for Computational Linguistics.

[^9]: Su Lin Blodgett, Gilsinia Lopez, Alexandra Olteanu, Robert Sim, and Hanna Wallach. 2021. [Stereotyping Norwegian salmon: An inventory of pitfalls in fairness benchmark datasets](https://doi.org/10.18653/v1/2021.acl-long.81). In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 1004–1015, Online. Association for Computational Linguistics.

[^10]: Samuel R. Bowman and George Dahl. 2021. [What will it take to fix benchmarking in natural language understanding?](https://doi.org/10.18653/v1/2021.naacl-main.385) In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 4843–4855, Online. Association for Computational Linguistics.

[^11]: Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. 2019. [BoolQ: Exploring the surprising difficulty of natural yes/no questions](https://doi.org/10.18653/v1/N19-1300). In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 2924–2936, Minneapolis, Minnesota. Association for Computational Linguistics.

[^12]: Eve Fleisig, Aubrie Amstutz, Chad Atalla, Su Lin Blodgett, Hal Daumé III, Alexandra Olteanu, Emily Sheng, Dan Vann, and Hanna Wallach. 2023. [FairPrism: Evaluating fairness-related harms in text generation](https://doi.org/10.18653/v1/2023.acl-long.343). In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 6231–6251, Toronto, Canada. Association for Computational Linguistics.

[^13]: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. 2021. [Datasheets for datasets](https://doi.org/10.1145/3458723). *Commun. ACM*, 64(12):86–92.

[^14]: Sebastian Gehrmann, Tosin Adewumi, Karmanya Aggarwal, Pawan Sasanka Ammanamanchi, Anuoluwapo Aremu, Antoine Bosselut, Khyathi Raghavi Chandu, Miruna-Adriana Clinciu, Dipanjan Das, Kaustubh Dhole, Wanyu Du, Esin Durmus, Ondřej Dušek, Chris Chinenye Emezue, Varun Gangal, Cristina Garbacea, Tatsunori Hashimoto, Yufang Hou, Yacine Jernite, Harsh Jhamtani, Yangfeng Ji, Shailza Jolly, Mihir Kale, Dhruv Kumar, Faisal Ladhak, Aman Madaan, Mounica Maddela, Khyati Mahajan, Saad Mahamood, Bodhisattwa Prasad Majumder, Pedro Henrique Martins, Angelina McMillan-Major, Simon Mille, Emiel van Miltenburg, Moin Nadeem, Shashi Narayan, Vitaly Nikolaev, Andre Niyongabo Rubungo, Salomey Osei, Ankur Parikh, Laura Perez-Beltrachini, Niranjan Ramesh Rao, Vikas Raunak, Juan Diego Rodriguez, Sashank Santhanam, João Sedoc, Thibault Sellam, Samira Shaikh, Anastasia Shimorina, Marco Antonio Sobrevilla Cabezudo, Hendrik Strobelt, Nishant Subramani, Wei Xu, Diyi Yang, Akhila Yerukola, and Jiawei Zhou. 2021. [The GEM benchmark: Natural language generation, its evaluation and metrics](https://doi.org/10.18653/v1/2021.gem-1.10). In *Proceedings of the 1st Workshop on Natural Language Generation, Evaluation, and Metrics (GEM 2021)*, pages 96–120, Online. Association for Computational Linguistics.

[^15]: Sebastian Gehrmann, Abhik Bhattacharjee, Abinaya Mahendiran, Alex Wang, Alexandros Papangelis, Aman Madaan, Angelina McMillan-Major, Anna Shvets, Ashish Upadhyay, Bingsheng Yao, Bryan Wilie, Chandra Bhagavatula, Chaobin You, Craig Thomson, Cristina Garbacea, Dakuo Wang, Daniel Deutsch, Deyi Xiong, Di Jin, Dimitra Gkatzia, Dragomir Radev, Elizabeth Clark, Esin Durmus, Faisal Ladhak, Filip Ginter, Genta Indra Winata, Hendrik Strobelt, Hiroaki Hayashi, Jekaterina Novikova, Jenna Kanerva, Jenny Chim, Jiawei Zhou, Jordan Clive, Joshua Maynez, João Sedoc, Juraj Juraska, Kaustubh Dhole, Khyathi Raghavi Chandu, Laura Perez-Beltrachini, Leonardo F. R. Ribeiro, Lewis Tunstall, Li Zhang, Mahima Pushkarna, Mathias Creutz, Michael White, Mihir Sanjay Kale, Moussa Kamal Eddine, Nico Daheim, Nishant Subramani, Ondrej Dusek, Paul Pu Liang, Pawan Sasanka Ammanamanchi, Qi Zhu, Ratish Puduppully, Reno Kriz, Rifat Shahriyar, Ronald Cardenas, Saad Mahamood, Salomey Osei, Samuel Cahyawijaya, Sanja Štajner, Sebastien Montella, Shailza, Shailza Jolly, Simon Mille, Tahmid Hasan, Tianhao Shen, Tosin Adewumi, Vikas Raunak, Vipul Raheja, Vitaly Nikolaev, Vivian Tsai, Yacine Jernite, Ying Xu, Yisi Sang, Yixin Liu, and Yufang Hou. 2022. [Gemv2: Multilingual nlg benchmarking in a single line of code](http://arxiv.org/abs/2206.11249).

[^16]: Seraphina Goldfarb-Tarrant, Eddie Ungless, Esma Balkir, and Su Lin Blodgett. 2023. [This prompt is measuring <mask>: evaluating bias evaluation in language models](https://doi.org/10.18653/v1/2023.findings-acl.139). In *Findings of the Association for Computational Linguistics: ACL 2023*, pages 2209–2225, Toronto, Canada. Association for Computational Linguistics.

[^17]: Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A. Smith. 2018. [Annotation artifacts in natural language inference data](https://doi.org/10.18653/v1/N18-2017). In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 107–112, New Orleans, Louisiana. Association for Computational Linguistics.

[^18]: Yangsibo Huang, Samyak Gupta, Zexuan Zhong, Kai Li, and Danqi Chen. 2023. [Privacy implications of retrieval-based language models](https://doi.org/10.18653/v1/2023.emnlp-main.921). In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 14887–14902, Singapore. Association for Computational Linguistics.

[^19]: Abigail Z. Jacobs and Hanna Wallach. 2021. [Measurement and fairness](https://doi.org/10.1145/3442188.3445901). In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, FAccT ’21, page 375–385, New York, NY, USA. Association for Computing Machinery.

[^20]: Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp, Robin Jia, Mohit Bansal, Christopher Potts, and Adina Williams. 2021. [Dynabench: Rethinking benchmarking in NLP](https://doi.org/10.18653/v1/2021.naacl-main.324). In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 4110–4124, Online. Association for Computational Linguistics.

[^21]: Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. 2022. Holistic evaluation of language models. *arXiv preprint arXiv:2211.09110*.

[^22]: Q. Vera Liao and Ziang Xiao. 2023. Rethinking model evaluation as narrowing the socio-technical gap. *arXiv preprint arXiv:2306.03100*.

[^23]: Q Vera Liao, Yunfeng Zhang, Ronny Luss, Finale Doshi-Velez, and Amit Dhurandhar. 2022. Connecting Algorithmic Research and Usage Contexts: A Perspective of Contextualized Evaluation for Explainable AI. In *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing*, volume 10, pages 147–159.

[^24]: Swaroop Mishra and Anjana Arunkumar. 2021. [How robust are model rankings: A leaderboard customization approach for equitable evaluation](https://doi.org/10.1609/aaai.v35i15.17599). *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(15):13561–13569.

[^25]: Robert J Mislevy, Linda S Steinberg, and Russell G Almond. 2003. Focus article: On the structure of educational assessments. *Measurement: Interdisciplinary research and perspectives*, 1(1):3–62.

[^26]: Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. 2019. Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency*, pages 220–229.

[^27]: Nikita Nangia, Clara Vania, Rasika Bhalerao, and Samuel R. Bowman. 2020. [CrowS-pairs: A challenge dataset for measuring social biases in masked language models](https://doi.org/10.18653/v1/2020.emnlp-main.154). In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1953–1967, Online. Association for Computational Linguistics.

[^28]: Melissa Roemmele, Cosmin Adrian Bejan, and Andrew S Gordon. 2011. Choice of plausible alternatives: An evaluation of commonsense causal reasoning. In *2011 AAAI Spring Symposium Series*.

[^29]: Anna Rogers, Timothy Baldwin, and Kobi Leins. 2021. [‘just what do you think you’re doing, dave?’ a checklist for responsible data use in NLP](https://doi.org/10.18653/v1/2021.findings-emnlp.414). In *Findings of the Association for Computational Linguistics: EMNLP 2021*, pages 4821–4833, Punta Cana, Dominican Republic. Association for Computational Linguistics.

[^30]: Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2023. [Quantifying language models’ sensitivity to spurious features in prompt design or: How i learned to start worrying about prompt formatting](http://arxiv.org/abs/2310.11324).

[^31]: Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R. Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, Agnieszka Kluska, Aitor Lewkowycz, Akshat Agarwal, Alethea Power, Alex Ray, Alex Warstadt, Alexander W. Kocurek, Ali Safaya, Ali Tazarv, Alice Xiang, Alicia Parrish, Allen Nie, Aman Hussain, Amanda Askell, Amanda Dsouza, Ambrose Slone, Ameet Rahane, Anantharaman S. Iyer, Anders Andreassen, Andrea Madotto, Andrea Santilli, Andreas Stuhlmüller, Andrew Dai, Andrew La, Andrew Lampinen, Andy Zou, Angela Jiang, Angelica Chen, Anh Vuong, Animesh Gupta, Anna Gottardi, Antonio Norelli, Anu Venkatesh, Arash Gholamidavoodi, Arfa Tabassum, Arul Menezes, Arun Kirubarajan, Asher Mullokandov, Ashish Sabharwal, Austin Herrick, Avia Efrat, Aykut Erdem, Ayla Karakaş, B. Ryan Roberts, Bao Sheng Loe, Barret Zoph, Bartłomiej Bojanowski, Batuhan Özyurt, Behnam Hedayatnia, Behnam Neyshabur, Benjamin Inden, Benno Stein, Berk Ekmekci, Bill Yuchen Lin, Blake Howald, Cameron Diao, Cameron Dour, Catherine Stinson, Cedrick Argueta, César Ferri Ramírez, Chandan Singh, Charles Rathkopf, Chenlin Meng, Chitta Baral, Chiyu Wu, Chris Callison-Burch, Chris Waites, Christian Voigt, Christopher D. Manning, Christopher Potts, Cindy Ramirez, Clara E. Rivera, Clemencia Siro, Colin Raffel, Courtney Ashcraft, Cristina Garbacea, Damien Sileo, Dan Garrette, Dan Hendrycks, Dan Kilman, Dan Roth, Daniel Freeman, Daniel Khashabi, Daniel Levy, Daniel Moseguí González, Danielle Perszyk, Danny Hernandez, Danqi Chen, Daphne Ippolito, Dar Gilboa, David Dohan, David Drakard, David Jurgens, Debajyoti Datta, Deep Ganguli, Denis Emelin, Denis Kleyko, Deniz Yuret, Derek Chen, Derek Tam, Dieuwke Hupkes, Diganta Misra, Dilyar Buzan, Dimitri Coelho Mollo, Diyi Yang, Dong-Ho Lee, Ekaterina Shutova, Ekin Dogus Cubuk, Elad Segal, Eleanor Hagerman, Elizabeth Barnes, Elizabeth Donoway, Ellie Pavlick, Emanuele Rodola, Emma Lam, Eric Chu, Eric Tang, Erkut Erdem, Ernie Chang, Ethan A. Chi, Ethan Dyer, Ethan Jerzak, Ethan Kim, Eunice Engefu Manyasi, Evgenii Zheltonozhskii, Fanyue Xia, Fatemeh Siar, Fernando Martínez-Plumed, Francesca Happé, Francois Chollet, Frieda Rong, Gaurav Mishra, Genta Indra Winata, Gerard de Melo, Germán Kruszewski, Giambattista Parascandolo, Giorgio Mariani, Gloria Wang, Gonzalo Jaimovitch-López, Gregor Betz, Guy Gur-Ari, Hana Galijasevic, Hannah Kim, Hannah Rashkin, Hannaneh Hajishirzi, Harsh Mehta, Hayden Bogar, Henry Shevlin, Hinrich Schütze, Hiromu Yakura, Hongming Zhang, Hugh Mee Wong, Ian Ng, Isaac Noble, Jaap Jumelet, Jack Geissinger, Jackson Kernion, Jacob Hilton, Jaehoon Lee, Jaime Fernández Fisac, James B. Simon, James Koppel, James Zheng, James Zou, Jan Kocoń, Jana Thompson, Jared Kaplan, Jarema Radom, Jascha Sohl-Dickstein, Jason Phang, Jason Wei, Jason Yosinski, Jekaterina Novikova, Jelle Bosscher, Jennifer Marsh, Jeremy Kim, Jeroen Taal, Jesse Engel, Jesujoba Alabi, Jiacheng Xu, Jiaming Song, Jillian Tang, Joan Waweru, John Burden, John Miller, John U. Balis, Jonathan Berant, Jörg Frohberg, Jos Rozen, Jose Hernandez-Orallo, Joseph Boudeman, Joseph Jones, Joshua B. Tenenbaum, Joshua S. Rule, Joyce Chua, Kamil Kanclerz, Karen Livescu, Karl Krauth, Karthik Gopalakrishnan, Katerina Ignatyeva, Katja Markert, Kaustubh D. Dhole, Kevin Gimpel, Kevin Omondi, Kory Mathewson, Kristen Chiafullo, Ksenia Shkaruta, Kumar Shridhar, Kyle McDonell, Kyle Richardson, Laria Reynolds, Leo Gao, Li Zhang, Liam Dugan, Lianhui Qin, Lidia Contreras-Ochando, Louis-Philippe Morency, Luca Moschella, Lucas Lam, Lucy Noble, Ludwig Schmidt, Luheng He, Luis Oliveros Colón, Luke Metz, Lütfi Kerem Şenel, Maarten Bosma, Maarten Sap, Maartje ter Hoeve, Maheen Farooqi, Manaal Faruqui, Mantas Mazeika, Marco Baturan, Marco Marelli, Marco Maru, Maria Jose Ramírez Quintana, Marie Tolkiehn, Mario Giulianelli, Martha Lewis, Martin Potthast, Matthew L. Leavitt, Matthias Hagen, Mátyás Schubert, Medina Orduna Baitemirova, Melody Arnaud, Melvin McElrath, Michael A. Yee, Michael Cohen, Michael Gu, Michael Ivanitskiy, Michael Starritt, Michael Strube, Michał Swędrowski, Michele Bevilacqua, Michihiro Yasunaga, Mihir Kale, Mike Cain, Mimee Xu, Mirac Suzgun, Mo Tiwari, Mohit Bansal, Moin Aminnaseri, Mor Geva, Mozhdeh Gheini, Mukund Varma T, Nanyun Peng, Nathan Chi, Nayeon Lee, Neta Gur-Ari Krakover, Nicholas Cameron, Nicholas Roberts, Nick Doiron, Nikita Nangia, Niklas Deckers, Niklas Muennighoff, Nitish Shirish Keskar, Niveditha S. Iyer, Noah Constant, Noah Fiedel, Nuan Wen, Oliver Zhang, Omar Agha, Omar Elbaghdadi, Omer Levy, Owain Evans, Pablo Antonio Moreno Casares, Parth Doshi, Pascale Fung, Paul Pu Liang, Paul Vicol, Pegah Alipoormolabashi, Peiyuan Liao, Percy Liang, Peter Chang, Peter Eckersley, Phu Mon Htut, Pinyu Hwang, Piotr Miłkowski, Piyush Patil, Pouya Pezeshkpour, Priti Oli, Qiaozhu Mei, Qing Lyu, Qinlang Chen, Rabin Banjade, Rachel Etta Rudolph, Raefer Gabriel, Rahel Habacker, Ramón Risco Delgado, Raphaël Millière, Rhythm Garg, Richard Barnes, Rif A. Saurous, Riku Arakawa, Robbe Raymaekers, Robert Frank, Rohan Sikand, Roman Novak, Roman Sitelew, Ronan LeBras, Rosanne Liu, Rowan Jacobs, Rui Zhang, Ruslan Salakhutdinov, Ryan Chi, Ryan Lee, Ryan Stovall, Ryan Teehan, Rylan Yang, Sahib Singh, Saif M. Mohammad, Sajant Anand, Sam Dillavou, Sam Shleifer, Sam Wiseman, Samuel Gruetter, Samuel R. Bowman, Samuel S. Schoenholz, Sanghyun Han, Sanjeev Kwatra, Sarah A. Rous, Sarik Ghazarian, Sayan Ghosh, Sean Casey, Sebastian Bischoff, Sebastian Gehrmann, Sebastian Schuster, Sepideh Sadeghi, Shadi Hamdan, Sharon Zhou, Shashank Srivastava, Sherry Shi, Shikhar Singh, Shima Asaadi, Shixiang Shane Gu, Shubh Pachchigar, Shubham Toshniwal, Shyam Upadhyay, Shyamolima, Debnath, Siamak Shakeri, Simon Thormeyer, Simone Melzi, Siva Reddy, Sneha Priscilla Makini, Soo-Hwan Lee, Spencer Torene, Sriharsha Hatwar, Stanislas Dehaene, Stefan Divic, Stefano Ermon, Stella Biderman, Stephanie Lin, Stephen Prasad, Steven T. Piantadosi, Stuart M. Shieber, Summer Misherghi, Svetlana Kiritchenko, Swaroop Mishra, Tal Linzen, Tal Schuster, Tao Li, Tao Yu, Tariq Ali, Tatsu Hashimoto, Te-Lin Wu, Théo Desbordes, Theodore Rothschild, Thomas Phan, Tianle Wang, Tiberius Nkinyili, Timo Schick, Timofei Kornev, Timothy Telleen-Lawton, Titus Tunduny, Tobias Gerstenberg, Trenton Chang, Trishala Neeraj, Tushar Khot, Tyler Shultz, Uri Shaham, Vedant Misra, Vera Demberg, Victoria Nyamai, Vikas Raunak, Vinay Ramasesh, Vinay Uday Prabhu, Vishakh Padmakumar, Vivek Srikumar, William Fedus, William Saunders, William Zhang, Wout Vossen, Xiang Ren, Xiaoyu Tong, Xinran Zhao, Xinyi Wu, Xudong Shen, Yadollah Yaghoobzadeh, Yair Lakretz, Yangqiu Song, Yasaman Bahri, Yejin Choi, Yichi Yang, Yiding Hao, Yifu Chen, Yonatan Belinkov, Yu Hou, Yufang Hou, Yuntao Bai, Zachary Seid, Zhuoye Zhao, Zijian Wang, Zijie J. Wang, Zirui Wang, and Ziyi Wu. 2022. [Beyond the imitation game: Quantifying and extrapolating the capabilities of language models](http://arxiv.org/abs/2206.04615).

[^32]: Kiri L. Wagstaff. 2012. Machine learning that matters. In *Proceedings of the 29th International Coference on International Conference on Machine Learning*, ICML’12, page 1851–1856, Madison, WI, USA. Omnipress.

[^33]: Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2019. SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems. *Advances in neural information processing systems*, 32.

[^34]: Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2018. [GLUE: A multi-task benchmark and analysis platform for natural language understanding](https://doi.org/10.18653/v1/W18-5446). In *Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP*, pages 353–355, Brussels, Belgium. Association for Computational Linguistics.

[^35]: Ziang Xiao, Susu Zhang, Vivian Lai, and Q. Vera Liao. 2023. [Evaluating evaluation metrics: A framework for analyzing NLG evaluation metrics using measurement theory](https://doi.org/10.18653/v1/2023.emnlp-main.676). In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 10967–10982, Singapore. Association for Computational Linguistics.