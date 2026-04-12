---
type: raw
source_kind: theory
capture_method: web-clipper
title: Introducing SWE-bench Verified
author: 
site: openai.com
published: 
url: https://openai.com/index/introducing-swe-bench-verified/
captured: 2026-04-12T14:37:30+03:00
status: unprocessed
---

# Introducing SWE-bench Verified

Источник: https://openai.com/index/introducing-swe-bench-verified/

## Краткая справка
- Автор: 
- Сайт: openai.com
- Дата публикации: 

## Текст
We’re releasing a human-validated subset of SWE-bench that more reliably evaluates AI models’ ability to solve real-world software issues.

As part of our [Preparedness Framework ⁠](https://openai.com/preparedness/), OpenAI develops a range of metrics to track, evaluate, and forecast models’ abilities to act autonomously. The ability to autonomously complete software engineering tasks is a key component of our Medium risk level in the Model Autonomy risk category. Evaluating these capabilities is challenging due to the complexity of software engineering tasks, the difficulty of accurately assessing generated code, and the challenge of simulating real-world development scenarios. Therefore, our approach to Preparedness must also involve careful examination of evaluations themselves, to reduce the potential for underestimating or overestimating performance in important risk categories.

One of the most popular evaluation suites for software engineering is [SWE-bench ⁠](https://www.swebench.com/) [^1] —a benchmark for evaluating large language models’ (LLMs’) abilities to solve real-world software issues sourced from GitHub. The benchmark involves giving agents a code repository and issue description, and challenging them to generate a patch that resolves the problem described by the issue. Coding agents have made impressive progress on SWE-bench, with top scoring agents scoring 20% on SWE-bench and 43% on SWE-bench Lite according to the [SWE-bench leaderboard ⁠](https://www.swebench.com/) as of August 5, 2024.

Our testing identified some SWE-bench tasks which may be hard or impossible to solve, leading to SWE-bench systematically underestimating models’ autonomous software engineering capabilities. We’ve collaborated with the authors of SWE-bench to address those issues in a new release of the benchmark that should provide more accurate evaluations.

## Background on SWE-bench

Each sample in the SWE-bench test set is created from a resolved GitHub issue in one of 12 open-source Python repositories on GitHub. Each sample has an associated pull request (PR), which includes both the solution code and unit tests to verify code correctness. These unit tests fail before the solution code in the PR is added, but pass afterwards, and are therefore called `*FAIL_TO_PASS*` *tests*. Each sample also has associated `*PASS_TO_PASS*` *tests*, which pass both before and after the PR is merged, and are used to check that existing unrelated functionality in the codebase has not been broken by the PR.

For each sample in SWE-bench, agents are provided with the original text from the GitHub issue, known as the *problem statement*, and are given access to the codebase. Given these, agents must edit the files in the codebase to resolve the issue. The tests are not shown to the agent.

A proposed edit is evaluated by running both the `FAIL_TO_PASS` and `PASS_TO_PASS` tests. If the `FAIL_TO_PASS` tests pass, this means the edit solves the issue. If the `PASS_TO_PASS` tests pass, then the edit has not inadvertently broken unrelated sections of the codebase. Both sets of tests are required to pass for the edit to fully resolve the original GitHub issue.

## Adapting SWE-bench as a Preparedness Evaluation

Given the potential relevance of SWE-bench for the Preparedness Framework, we aimed to find ways in which we could improve the robustness and reliability of the benchmark. We identified three major areas for improvement [^2]:

1. The unit tests used to evaluate the correctness of a solution are often overly specific, and in some cases are even unrelated to the issue. This potentially causes correct solutions to be rejected.
2. Many samples have an issue description that is underspecified, leading to ambiguity on what the problem is and how it should be solved.
3. It is sometimes difficult to reliably set up the SWE-bench development environments for the agents, inadvertently causing unit tests to fail regardless of the solution. In such cases, perfectly valid solutions might be graded as incorrect.

Here is an example illustrating the first of these issues.

SWE-bench sample `scikit-learn__scikit-learn-14520` tasks an agent with solving [an issue in the scikit-learn repository ⁠](https://github.com/scikit-learn/scikit-learn/issues/14501). This problem statement reports that a function’s `copy` argument could be specified by a user, but is ignored by the library (the behavior is instead hardcoded inside the function):

#### Plain Text

```
Copy param ignored in TfidfVectorizer
I was playing with vectorizers and I found this:

https://github.com/scikit-learn/scikit-learn/blob/ae16319626e2ca6ca0e54d4a5b83f73f817232aa/sklearn/feature_extraction/text.py#L1669

However that parameter is not used later in the method.

Here \`copy=False\` is used:

https://github.com/scikit-learn/scikit-learn/blob/ae16319626e2ca6ca0e54d4a5b83f73f817232aa/sklearn/feature_extraction/text.py#L1692

Is there anything I am missing?
```

An agent approaching the above issue would first have to deal with the ambiguity in whether the function’s behavior is intended or a bug, then make changes to the codebase to resolve the issue. Per the SWE-bench setup, any solution the agent proposes then needs to pass the following test, extracted from [the PR that originally resolved the issue ⁠](https://github.com/scikit-learn/scikit-learn/pull/14520):

#### Python

```
def test_tfidf_vectorizer_deprecationwarning():
    msg = ("'copy' param is unused and has been deprecated since "
           "version 0.22. Backward compatibility for 'copy' will "
           "be removed in 0.24.")
    with pytest.warns(DeprecationWarning, match=msg):
        tv = TfidfVectorizer()
        train_data = JUNK_FOOD_DOCS
        tv.fit(train_data)
        tv.transform(train_data, copy=True)
```

This test explicitly checks that the solution must raise a DeprecationWarning whenever the `copy` parameter is used, although the original problem statement in the issue text above does not convey this requirement. Furthermore, even if the agent realized that a DeprecationWarning should be raised, the test also requires the agent to exactly match the deprecation message, which was only arrived at after some discussion in the PR which the agent has no access to.

Note that the agent is only given the problem description from the main issue text, and does not have visibility into the tests that it needs to pass. Given this setup, it would be nearly impossible for an agent to solve this sample in SWE-bench.

## SWE-bench Verified

To address these issues, we launched a human annotation campaign with professional software developers to screen each sample of the SWE-bench test set for appropriately scoped unit tests and well-specified issue descriptions.

Together with the authors of SWE-bench, we are releasing SWE-bench Verified: a subset of the original test set from SWE-bench, consisting of 500 samples verified to be non-problematic by our human annotators. This version supersedes the original SWE-bench and SWE-bench Lite test sets. Additionally, we are releasing our human annotations for all SWE-bench test samples. These annotations enable slicing the dataset by difficulty. The 'easy' subset is composed of 196 <15-minute fix tasks, while the 'hard' subset is composed of 45 >1-hour tasks.

We also collaborated with the SWE-bench authors to [develop a new evaluation harness for SWE-bench ⁠](https://github.com/princeton-nlp/SWE-bench/tree/main/docs/20240627_docker) which uses containerized Docker environments to make evaluating on SWE-bench easier and more reliable.

On SWE-bench Verified, GPT‑4o resolves 33.2% of samples [^3], with the best performing open-source scaffold, Agentless, doubling its previous score of 16% on SWE-bench.

## Our Approach

We worked with 93 software developers experienced in Python to manually screen SWE-bench samples for quality. We annotated 1,699 random samples from the SWE-bench test set to produce SWE-bench Verified. The following analysis is based on the 1,699 samples.

We annotate samples to capture:

- Whether we consider the issue description to be underspecified and hence unfair to be testing on.
- Whether the `FAIL_TO_PASS` unit tests filter out valid solutions.

Each annotation criterion has a label ranging \[0, 1, 2, 3\] in increasing severity. Labels 0 and 1 are minor; labels 2 and 3 are severe and indicate that the sample is inadequate in some way and should be discarded. We choose to annotate across four ordinal categories rather than a single binary label of severe/not severe to capture more granular detail.

Additionally, we rate the difficulty of each sample by having annotators estimate how long it would take for a developer to decide upon and implement the solution, assuming the sample is non-problematic. Finally, we provide a freeform input option to flag any other major issues with the sample (for example, if the `FAIL_TO_PASS` unit tests are easily gamed, this could lead to an invalid solution being marked as correct).

Our team of engineers first hand-labeled 50 samples to a high degree of confidence for use in annotator onboarding tests. To take part in the annotation campaign, each prospective annotator had to pass our onboarding tests. We provided detailed feedback to each annotator throughout onboarding to better train them for the task. Annotators were not necessarily prior experts in the codebases relevant to SWE-bench, but were given time to familiarize themselves with each codebase they worked with.

To ensure a high-quality dataset, each sample is labeled 3 times by separate annotators. It is easy to accidentally miss potential issues, and issues themselves can be ambiguous, so we conservatively ensemble annotations by taking the highest-severity label amongst the 3 annotators.

The full text of our annotation rubric can be found [here ⁠](https://cdn.openai.com/introducing-swe-bench-verified/swe-b-annotation-instructions.pdf).  

### Annotation Criteria

Evaluated models are expected to generate a patch given the *problem statement* and codebase. If the *problem statement* is poorly specified, it can be significantly harder, or in some cases impossible, to generate a patch that solves the problem.

We label the problem statement with these 4 possible labels:

- 0: The issue is well-specified and it is clear what is required for a successful solution.
- 1: There are some blanks to fill in about the issue, but there is a sensible interpretation of what is required for a successful solution.
- 2: The issue is vague and there is room for ambiguity. It is unclear what a successful solution would look like.
- 3: It is almost impossible to understand what you are being asked to do without further information.

### Dataset construction

To construct SWE-bench Verified, we filter out any sample from the original test set where either the problem statement or the `FAIL_TO_PASS` unit tests have an ensemble label of 2 or above in severity. We also filter out all samples that have other major issues flagged. Given our ensembling method, this is equivalent to filtering out samples where any single annotator of three has flagged an issue with the sample. This approach leads to a higher false-positive rate in removing samples, but helps increase our confidence in sample quality for the final dataset.

We include as many samples with difficulty 1-4 hours and >4 hours as possible, and then we randomly sample the remainder to arrive at the 500 samples that constitute SWE-bench Verified.

## Annotation Results

The results of our annotations are below:

##### Is the problem statement underspecified?

<svg width="917.328125" height="400"><g transform="translate(60, 10)"><g transform="translate(0, 0)"><path d="M101.61830357142861,256.945 h36 a2,2 0 0 1 2,2 v74.055 v2h-2 h-36 h-2v-2 v-74.055 a2,2 0 0 1 2,-2z" fill="#84e086" stroke="transparent"></path></g><g transform="translate(0, 0)"><path d="M300.9821428571429,206.35999999999999 h36 a2,2 0 0 1 2,2 v124.64000000000001 v2h-2 h-36 h-2v-2 v-124.64000000000001 a2,2 0 0 1 2,-2z" fill="#adebad" stroke="transparent"></path></g><g transform="translate(0, 0)"><path d="M500.34598214285717,228.13500000000002 h36 a2,2 0 0 1 2,2 v102.86499999999998 v2h-2 h-36 h-2v-2 v-102.86499999999998 a2,2 0 0 1 2,-2z" fill="#ffd481" stroke="transparent"></path></g><g transform="translate(0, 0)"><path d="M699.7098214285716,313.56 h36 a2,2 0 0 1 2,2 v17.439999999999998 v2h-2 h-36 h-2v-2 v-17.439999999999998 a2,2 0 0 1 2,-2z" fill="#ff9a33" stroke="transparent"></path></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><g transform="translate(-8, 329)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 262)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 195)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 128)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 60.999999999999986)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, -6)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><svg x="0" y="0" font-size="inherit" style="overflow:visible"><text transform="rotate(-90)" x="-167.5" y="-40" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="-167.5" dy="0em">% of Samples</tspan></text></svg></g> <g transform="translate(0, 335)"><g transform="translate(0, 0)"><g transform="translate(119.61830357142861, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(318.9821428571429, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(518.3459821428571, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(717.7098214285716, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><line x1="0.5" y1="0" x2="837.828125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><svg x="0" y="24" font-size="inherit" style="overflow:visible"><text x="418.6640625" y="26" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="418.6640625" dy="0em">Severity</tspan></text></svg></g></g></svg>

We see that 38.3% of samples were flagged for underspecified problem statements, and 61.1% were flagged for unit tests that may unfairly mark valid solutions as incorrect. Overall, our annotation process resulted in 68.3% of SWE-bench samples being filtered out due to underspecification, unfair unit tests, or other issues. As discussed previously, this filtering process is likely to be overzealous but allows us to have high confidence in the feasibility of the unfiltered samples.

We present a few examples of samples and their annotations below, cherry-picked to illustrate the diversity in sample quality:

Select sample:

Commentary

This is an example of a good sample which has been verified by annotators for the SWE-bench Verified dataset. The problem statement gives a short but clear demonstration of a bug, and the `FAIL_TO_PASS` tests directly assert that the example given in the problem statement has been resolved.

Problem statement

`Unset  kernS: 'kern' referenced before assignment    from sympy.core.sympify import kernS       text = "(2*x)/(x-1)"   expr = kernS(text)   // hit = kern in s   // UnboundLocalError: local variable 'kern' referenced beforeassignment  `

Are the tasks well-specified? (Raw annotation)

Severity: 0 - The issue is well-specified and it is clear what is required for a successful solution.

It is clear that kernS is throwing exception for (2\*x)/(x-1)  
It provides example input for which the error is occurring which can make it easy to reproduce the issue.

`FAIL_TO_PASS` test (Only showing lines added during the original PR for brevity)

`Python   def test_kernS():       ...       assert kernS("(2*x)/(x-1)") == 2*x/(x-1)   `

How valid are the evaluation criteria? (Raw annotation)

Severity: 0 - The tests perfectly cover all possible solutions.

The test case is exactly for kernS("(2\*x)/(x-1)") for which the issue was occurring in issue description.  
It will cover all possible solutions.

The chart below compares the difficulty distributions of the original SWE-bench datasets and our new SWE-bench Verified dataset. We estimate the difficulty distribution of SWE-bench based on our random subset of 1699 samples. Note that while these results provide estimates of the effort necessary to implement a solution (refer to our annotation instructions for the precise wording), they assume a software engineer who is able to figure out the solution. In practice, we expect the baseline solve rate of a typical human software engineer to be lower than 100%.

We observe that most (77.8%) of the samples in the original SWE-bench dataset were estimated to take less than an hour for an experienced software engineer to complete. Both SWE-bench Lite and our new SWE-bench Verified dataset skews this further, leaving fewer than 10% of issues estimated to take longer than an hour. However, the mechanism underlying this shift is importantly different: SWE-bench Lite subsampled the original dataset to make the benchmark easier, whereas SWE-bench Verified attempts to remove infeasible samples from the dataset. We further explore this effect in the next section.

##### Distribution of Difficulty Labels

<svg width="917.328125" height="400"><g transform="translate(60, 40)"><g transform="translate(0, 0)"><line x1="0" y1="290" x2="857.328125" y2="290" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="265.8333333333333" x2="857.328125" y2="265.8333333333333" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="241.66666666666669" x2="857.328125" y2="241.66666666666669" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="217.5" x2="857.328125" y2="217.5" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="193.33333333333334" x2="857.328125" y2="193.33333333333334" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="169.16666666666666" x2="857.328125" y2="169.16666666666666" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="145" x2="857.328125" y2="145" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="120.83333333333333" x2="857.328125" y2="120.83333333333333" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="96.66666666666667" x2="857.328125" y2="96.66666666666667" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="72.5" x2="857.328125" y2="72.5" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="48.33333333333332" x2="857.328125" y2="48.33333333333332" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="24.16666666666668" x2="857.328125" y2="24.16666666666668" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="0" x2="857.328125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line></g><g transform="translate(0, 0)"><path d="M62,171.58333333333334 h36 a2,2 0 0 1 2,2 v114.41666666666666 v2h-2 h-36 h-2v-2 v-114.41666666666666 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M104,107.78333333333332 h36 a2,2 0 0 1 2,2 v178.2166666666667 v2h-2 h-36 h-2v-2 v-178.2166666666667 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M146,102.46666666666668 h36 a2,2 0 0 1 2,2 v183.5333333333333 v2h-2 h-36 h-2v-2 v-183.5333333333333 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M266,32.38333333333334 h36 a2,2 0 0 1 2,2 v253.61666666666667 v2h-2 h-36 h-2v-2 v-253.61666666666667 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M308,17.88333333333336 h36 a2,2 0 0 1 2,2 v268.1166666666666 v2h-2 h-36 h-2v-2 v-268.1166666666666 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M350,37.7 h36 a2,2 0 0 1 2,2 v248.3 v2h-2 h-36 h-2v-2 v-248.3 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M470,196.23333333333335 h36 a2,2 0 0 1 2,2 v89.76666666666665 v2h-2 h-36 h-2v-2 v-89.76666666666665 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M512,260.51666666666665 h36 a2,2 0 0 1 2,2 v25.48333333333335 v2h-2 h-36 h-2v-2 v-25.48333333333335 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M554,249.4 h36 a2,2 0 0 1 2,2 v36.599999999999994 v2h-2 h-36 h-2v-2 v-36.599999999999994 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M674,276.4666666666667 h36 a2,2 0 0 1 2,2 v9.533333333333303 v2h-2 h-36 h-2v-2 v-9.533333333333303 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M715,290 h38 a1,1 0 0 1 1,1 v-2 v1h-1 h-38 h-1v-1 v2 a1,1 0 0 1 1,-1z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M757.45,287.1 h37.10000000000002 a1.4499999999999886,1.4499999999999886 0 0 1 1.4499999999999886,1.4499999999999886 v0 v1.4499999999999886h-1.4499999999999886 h-37.10000000000002 h-1.4499999999999886v-1.4499999999999886 v0 a1.4499999999999886,1.4499999999999886 0 0 1 1.4499999999999886,-1.4499999999999886z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><g transform="translate(-8, 284)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 235.66666666666669)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 187.33333333333334)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 139)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 90.66666666666667)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 42.33333333333332)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, -6)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><svg x="0" y="0" font-size="inherit" style="overflow:visible"><text transform="rotate(-90)" x="-145" y="-40" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="-145" dy="0em">Difficulty Categories</tspan></text></svg></g> <g transform="translate(0, 290)"><g transform="translate(0, 0)"><g transform="translate(123, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(327, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(531, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(735, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><line x1="0.5" y1="0" x2="857.828125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><svg x="0" y="40" font-size="inherit" style="overflow:visible"><text x="428.6640625" y="26" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="428.6640625" dy="0em">% of Samples</tspan></text></svg></g></g></svg>

## Performance on SWE-bench Verified

With our new SWE-bench Verified dataset, we tested GPT‑4o’s performance using several open-source scaffolds that performed well on the original SWE-bench leaderboards [^4].

We found that GPT‑4o’s performance on the best-performing scaffold reaches 33.2% on SWE-bench Verified, more than doubling its score of 16% on the original SWE-bench. In general, this validates our initial suspicion that the original SWE-bench dataset underestimates agent abilities. Note that the jump from SWE-bench Lite to SWE-bench Verified is not as significant, because SWE-bench Lite was already [filtered in a way that makes it easier ⁠](https://www.swebench.com/lite.html) than the full dataset, though that process would not fully capture the same issues as our filtering procedure.  

##### Performance of open-source scaffolds on SWE-bench subsets

<svg width="917.328125" height="400"><g transform="translate(60, 40)"><g transform="translate(0, 0)"><line x1="0" y1="290" x2="857.328125" y2="290" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="261" x2="857.328125" y2="261" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="232" x2="857.328125" y2="232" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="203" x2="857.328125" y2="203" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="174" x2="857.328125" y2="174" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="145" x2="857.328125" y2="145" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="116" x2="857.328125" y2="116" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="87.00000000000001" x2="857.328125" y2="87.00000000000001" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="57.999999999999986" x2="857.328125" y2="57.999999999999986" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="28.999999999999993" x2="857.328125" y2="28.999999999999993" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="0" x2="857.328125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line></g><g transform="translate(0, 0)"><path d="M39.5,243.6 h36 a2,2 0 0 1 2,2 v42.400000000000006 v2h-2 h-36 h-2v-2 v-42.400000000000006 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M81.5,219.53 h36 a2,2 0 0 1 2,2 v66.47 v2h-2 h-36 h-2v-2 v-66.47 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M123.5,193.71999999999997 h36 a2,2 0 0 1 2,2 v92.28000000000003 v2h-2 h-36 h-2v-2 v-92.28000000000003 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M203.5,248.24 h36 a2,2 0 0 1 2,2 v37.75999999999999 v2h-2 h-36 h-2v-2 v-37.75999999999999 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M245.5,224.17000000000002 h36 a2,2 0 0 1 2,2 v61.829999999999984 v2h-2 h-36 h-2v-2 v-61.829999999999984 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M287.5,206.48 h36 a2,2 0 0 1 2,2 v79.52000000000001 v2h-2 h-36 h-2v-2 v-79.52000000000001 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M367.5,245.63 h36 a2,2 0 0 1 2,2 v40.370000000000005 v2h-2 h-36 h-2v-2 v-40.370000000000005 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M409.5,232.87 h36 a2,2 0 0 1 2,2 v53.129999999999995 v2h-2 h-36 h-2v-2 v-53.129999999999995 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M451.5,202.42 h36 a2,2 0 0 1 2,2 v83.58000000000001 v2h-2 h-36 h-2v-2 v-83.58000000000001 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M531.5,245.92 h36 a2,2 0 0 1 2,2 v40.08000000000001 v2h-2 h-36 h-2v-2 v-40.08000000000001 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M573.5,231.12999999999997 h36 a2,2 0 0 1 2,2 v54.87000000000003 v2h-2 h-36 h-2v-2 v-54.87000000000003 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M615.5,207.64 h36 a2,2 0 0 1 2,2 v78.36000000000001 v2h-2 h-36 h-2v-2 v-78.36000000000001 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M695.5,255.49 h36 a2,2 0 0 1 2,2 v30.50999999999999 v2h-2 h-36 h-2v-2 v-30.50999999999999 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M737.5,236.92999999999998 h36 a2,2 0 0 1 2,2 v49.07000000000002 v2h-2 h-36 h-2v-2 v-49.07000000000002 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M779.5,223.3 h36 a2,2 0 0 1 2,2 v62.69999999999999 v2h-2 h-36 h-2v-2 v-62.69999999999999 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><g transform="translate(-8, 284)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 226)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 168)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 110)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 51.999999999999986)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, -6)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><svg x="0" y="0" font-size="inherit" style="overflow:visible"><text transform="rotate(-90)" x="-145" y="-40" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="-145" dy="0em">Scaffolds</tspan></text></svg></g> <g transform="translate(0, 290)"><g transform="translate(0, 0)"><g transform="translate(101, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(265, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(429, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(593, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(757, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><line x1="0.5" y1="0" x2="857.828125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><svg x="0" y="40" font-size="inherit" style="overflow:visible"><text x="428.6640625" y="26" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="428.6640625" dy="0em">% Resolved</tspan></text></svg></g></g></svg>

The increase in performance when evaluating on SWE-bench Verified may partly be explained by shifting the distribution toward easier samples (as shown in earlier analyses). However, our goal is not to inflate benchmark scores, but to make sure that the benchmark faithfully represents model capability at any given difficulty level.

We investigate this by plotting performance stratified by difficulty. If our new dataset merely shifted the difficulty distribution to contain more easy samples, the stratified performance within each category would not change, as appears to be the case going from the original SWE-bench to SWE-bench Lite. We instead observe that performance increases *within* individual difficulty categories when moving to SWE-bench Verified, which is consistent with the intended effect of removing impossible samples from all categories instead of removing difficult samples. The effect is clearest in the easiest two buckets of difficulty, where we have the most samples.

##### Averaged performance of all scaffolds stratified by difficulty

<svg width="917.328125" height="400"><g transform="translate(60, 40)"><g transform="translate(0, 0)"><line x1="0" y1="290" x2="857.328125" y2="290" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="261" x2="857.328125" y2="261" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="232" x2="857.328125" y2="232" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="203" x2="857.328125" y2="203" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="174" x2="857.328125" y2="174" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="145" x2="857.328125" y2="145" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="116" x2="857.328125" y2="116" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="87.00000000000001" x2="857.328125" y2="87.00000000000001" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="57.999999999999986" x2="857.328125" y2="57.999999999999986" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="28.999999999999993" x2="857.328125" y2="28.999999999999993" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><line x1="0" y1="0" x2="857.328125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line></g><g transform="translate(0, 0)"><path d="M62,193.71999999999997 h36 a2,2 0 0 1 2,2 v92.28000000000003 v2h-2 h-36 h-2v-2 v-92.28000000000003 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M104,189.37 h36 a2,2 0 0 1 2,2 v96.63 v2h-2 h-36 h-2v-2 v-96.63 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M146,159.20999999999998 h36 a2,2 0 0 1 2,2 v126.79000000000002 v2h-2 h-36 h-2v-2 v-126.79000000000002 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M266,252.59 h36 a2,2 0 0 1 2,2 v33.41 v2h-2 h-36 h-2v-2 v-33.41 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M308,245.34 h36 a2,2 0 0 1 2,2 v40.66 v2h-2 h-36 h-2v-2 v-40.66 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M350,229.68 h36 a2,2 0 0 1 2,2 v56.31999999999999 v2h-2 h-36 h-2v-2 v-56.31999999999999 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M470,283.90999999999997 h36 a2,2 0 0 1 2,2 v2.090000000000032 v2h-2 h-36 h-2v-2 v-2.090000000000032 a2,2 0 0 1 2,-2z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M512,265.06 h36 a2,2 0 0 1 2,2 v20.939999999999998 v2h-2 h-36 h-2v-2 v-20.939999999999998 a2,2 0 0 1 2,-2z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M554,276.08 h36 a2,2 0 0 1 2,2 v9.920000000000016 v2h-2 h-36 h-2v-2 v-9.920000000000016 a2,2 0 0 1 2,-2z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><path d="M673,290 h38 a1,1 0 0 1 1,1 v-2 v1h-1 h-38 h-1v-1 v2 a1,1 0 0 1 1,-1z" fill="#2078b3"></path></g><g transform="translate(0, 0)"><path d="M715,290 h38 a1,1 0 0 1 1,1 v-2 v1h-1 h-38 h-1v-1 v2 a1,1 0 0 1 1,-1z" fill="#a6cee3"></path></g><g transform="translate(0, 0)"><path d="M757,290 h38 a1,1 0 0 1 1,1 v-2 v1h-1 h-38 h-1v-1 v2 a1,1 0 0 1 1,-1z" fill="#b2e08a"></path></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><g transform="translate(-8, 284)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 226)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 168)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 110)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, 51.999999999999986)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(-8, -6)"><svg x="0" y="0.25" font-size="inherit" style="overflow: visible;"></svg></g></g><svg x="0" y="0" font-size="inherit" style="overflow:visible"><text transform="rotate(-90)" x="-145" y="-40" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="-145" dy="0em">Difficulty Buckets</tspan></text></svg></g> <g transform="translate(0, 290)"><g transform="translate(0, 0)"><g transform="translate(123, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(327, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(531, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><g transform="translate(0, 0)"><g transform="translate(735, 18)"><svg x="0" y="-2" font-size="inherit" style="overflow: visible;"></svg></g></g><line x1="0.5" y1="0" x2="857.828125" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="1"></line><svg x="0" y="40" font-size="inherit" style="overflow:visible"><text x="428.6640625" y="26" font-family="inherit" font-size="inherit" fill="currentColor" font-weight="inherit" text-anchor="middle"><tspan x="428.6640625" dy="0em">% Resolved</tspan></text></svg></g></g></svg>

We use SWE-bench as one of several evaluations tracking the Medium risk level of the Model Autonomy risk category in our Preparedness Framework. Tracking catastrophic risk levels via evaluations relies on ensuring that we can trust evaluation results and are calibrated about what the scores entail.

Our experiences suggest that we should:

**Invest in deeply understanding our benchmarks.** Although SWE-bench was designed thoughtfully, it underestimates model capabilities due to the issues mentioned in this blogpost. As our systems get closer to AGI, we need to evaluate them on increasingly more challenging tasks. This also elevates the level of expertise and care needed to curate and verify benchmarks to ensure that they are sufficiently challenging and robust (a case where work like [CriticGPT ⁠](https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/), which explores ways in which AI can assist with annotation pipelines, may be helpful).

**Account for progress in the ecosystem.** Community-led progress in agent scaffolding highlights the need to consider potential external enhancements to a model when assessing risk. Looking at the difference between the worst- and best-performing scaffolds for a given model on the [SWE-bench leaderboards ⁠](https://www.swebench.com/), we can see that, for example, GPT‑4’s performance on SWE-bench Lite varies between 2.7% using an early RAG-based scaffold and 28.3% using CodeR. Thus the Preparedness Framework calls for evaluations to be run continually and as often as needed to identify any non-trivial capability change; which includes before, during, and even after training, where models can be enhanced via integration with external systems. Furthermore, curating evaluations is an ecosystem-wide effort, and we hope to continue collaborating with researchers on building trustworthy, high-quality evaluations.

**Be cognizant of limitations.** Evaluations based on static datasets are inherently limited, and SWE-bench is no exception. Given that the benchmark is composed of scrapes of public GitHub repos, large foundation models that are pre-trained on internet text are likely to be contaminated on the tasks. Furthermore, SWE-bench only covers a narrow distribution of the Medium risk level for model autonomy and so must be supplemented with other evaluations.

We believe in an empirical and scientific approach to tracking and protecting against catastrophic risk. Building and continually improving evaluations is a key element of this work. There remains much to be done, and we’re eager to see more work from the community in contributing valuable benchmarks like SWE-bench.

## Data downloads

SWE-bench Verified is available for download [here⁠](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified); the full set of our annotations is [here⁠](https://cdn.openai.com/introducing-swe-bench-verified/swe-bench-annotation-results.zip), and our annotation rubric is [here⁠](https://cdn.openai.com/introducing-swe-bench-verified/swe-b-annotation-instructions.pdf).

## Authors

Neil Chowdhury, James Aung, Chan Jun Shern, Oliver Jaffe, Dane Sherburn, Giulio Starace, Evan Mays, Rachel Dias, Marwan Aljubeh, Mia Glaese, Carlos E. Jimenez, John Yang, Leyton Ho, Tejal Patwardhan, Kevin Liu, Aleksander Madry

*NC, JA, CJS, OJ, DS, GS contributed equally.*

## Acknowledgements

We’re grateful to Carlos Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan for developing the original SWE-bench benchmark; the Preparedness team for supporting this work; Tao Lin, who initially pointed out many of these issues; Ian Kivlichan and Sarah Schwettmann for feedback on an earlier version of this manuscript; and the many human annotators who helped create SWE-bench Verified.

[^1]: 1

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2024). SWE-bench: Can Language Models Resolve Real-World GitHub Issues? arXiv preprint arXiv:2310.06770.

[^2]: 2

Concurrent work with Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based Software Engineering Agents. arXiv preprint arXiv:2407.01489

[^3]: 3

`gpt-4o-2024-05-13`

[^4]: 4

We ran a single seed using closest-documented or default hyperparameters for each scaffold, so results may differ from what is reported in the official leaderboards.