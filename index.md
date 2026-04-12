# Индекс базы знаний

## Главный вход
- [wiki/home](wiki/home.md) — входная страница по сценариям использования базы
- [log](log.md) — append-only журнал ingest, framing, cleanup и policy-изменений

## Как читать этот индекс
- Это content-oriented каталог wiki, а не только набор маршрутов.
- Здесь перечислены основные страницы базы по категориям и даны короткие summaries.
- Для быстрого старта удобно сначала открыть [wiki/home](wiki/home.md), а потом уже использовать этот файл как карту всего содержимого.

## Быстрые маршруты
- Если нужен **весь курс в одном тексте**, начинай с [wiki/syntheses/course-arc-from-evals-to-reliable-safety](wiki/syntheses/course-arc-from-evals-to-reliable-safety.md).
- Если нужен **вход в методологию evals как общекурсовую тему**, смотри [wiki/syntheses/eval-methodology-in-ai-safety](wiki/syntheses/eval-methodology-in-ai-safety.md), [wiki/concepts/eval-methodology](wiki/concepts/eval-methodology.md) и три shared-лекции Славы Меритона.
- Если нужен **вход в limits of evals**, смотри [wiki/weeks/week-01](wiki/weeks/week-01.md), [wiki/concepts/evals](wiki/concepts/evals.md) и [wiki/syntheses/evals-scope-and-limits](wiki/syntheses/evals-scope-and-limits.md).
- Если нужен **вход в benchmarking и статистическую интерпретацию**, открывай [wiki/weeks/week-02](wiki/weeks/week-02.md), [wiki/concepts/statistical-rigor-in-evals](wiki/concepts/statistical-rigor-in-evals.md) и [wiki/syntheses/benchmarking-beyond-single-scores](wiki/syntheses/benchmarking-beyond-single-scores.md).
- Если нужен **вход в benchmark design и validity**, переходи к [wiki/weeks/week-03](wiki/weeks/week-03.md), [wiki/concepts/benchmark-design](wiki/concepts/benchmark-design.md) и [wiki/syntheses/benchmark-design-evidence-and-incentives](wiki/syntheses/benchmark-design-evidence-and-incentives.md).
- Если нужен **вход в agent evaluation**, открывай [wiki/weeks/week-04](wiki/weeks/week-04.md), [wiki/concepts/agent-evaluation](wiki/concepts/agent-evaluation.md) и [wiki/syntheses/agent-evals-beyond-task-success](wiki/syntheses/agent-evals-beyond-task-success.md).
- Если нужен **вход в reliable AI safety evals**, переходи к [wiki/weeks/week-05](wiki/weeks/week-05.md), [wiki/concepts/ai-safety-benchmarks](wiki/concepts/ai-safety-benchmarks.md) и [wiki/syntheses/reliable-ai-safety-evals](wiki/syntheses/reliable-ai-safety-evals.md).
- Если нужен **практический слой**, смотри [wiki/concepts/inspect-ai](wiki/concepts/inspect-ai.md) и notebook source pages первых четырех недель.

## Покрытие
- В базе сейчас 5 week hub-pages, 41 source pages, 32 concept page и 7 syntheses.
- Все внутренние Markdown-ссылки резолвятся; orphan pages в `wiki/` сейчас нет.
- `raw/` и `wiki/` уже разведены по ролям: `raw` хранит исходники, `wiki` хранит compounding knowledge layer.

## Страницы недель
- [wiki/weeks/week-01](wiki/weeks/week-01.md) — ввод в природу evals, limits of behavioral evidence и failure modes уверенного чтения тестов.
- [wiki/weeks/week-02](wiki/weeks/week-02.md) — benchmarking, evaluation strategy и статистическая дисциплина чтения результатов.
- [wiki/weeks/week-03](wiki/weeks/week-03.md) — benchmark design, evidence claims, validity и benchmark ecosystem.
- [wiki/weeks/week-04](wiki/weeks/week-04.md) — agent evaluation, reliability, elicitation, autonomy и практический ReAct / Inspect AI слой.
- [wiki/weeks/week-05](wiki/weeks/week-05.md) — reliable AI safety evals, science of evals и research taste как финальный слой курса.

## Syntheses
- [wiki/syntheses/course-arc-from-evals-to-reliable-safety](wiki/syntheses/course-arc-from-evals-to-reliable-safety.md) — capstone synthesis по всей дуге `week-01..05`.
- [wiki/syntheses/eval-methodology-in-ai-safety](wiki/syntheses/eval-methodology-in-ai-safety.md) — shared synthesis про методологию evals как AI safety bottleneck и research direction.
- [wiki/syntheses/evals-scope-and-limits](wiki/syntheses/evals-scope-and-limits.md) — week-01 synthesis про силу и пределы eval claims.
- [wiki/syntheses/benchmarking-beyond-single-scores](wiki/syntheses/benchmarking-beyond-single-scores.md) — week-02 synthesis про benchmarking, statistical rigor и bounded coverage.
- [wiki/syntheses/benchmark-design-evidence-and-incentives](wiki/syntheses/benchmark-design-evidence-and-incentives.md) — week-03 synthesis про benchmark design, evidence chain и incentives.
- [wiki/syntheses/agent-evals-beyond-task-success](wiki/syntheses/agent-evals-beyond-task-success.md) — week-04 synthesis про capability, reliability и procedure in agent evals.
- [wiki/syntheses/reliable-ai-safety-evals](wiki/syntheses/reliable-ai-safety-evals.md) — week-05 synthesis про safety benchmarks, science of evals и research taste.

## Concept Pages

### Базовый слой evals
- [wiki/concepts/evals](wiki/concepts/evals.md) — центральная карта области evals и ее главных distinctions.
- [wiki/concepts/behavioral-evals](wiki/concepts/behavioral-evals.md) — behavioral evidence, lower bounds и limits of behavior-only reading.
- [wiki/concepts/understanding-based-evals](wiki/concepts/understanding-based-evals.md) — более сильный standard, чем behavior-only testing.
- [wiki/concepts/evaluation-awareness](wiki/concepts/evaluation-awareness.md) — как модель может распознавать benchmark-like context.
- [wiki/concepts/prompt-sensitivity](wiki/concepts/prompt-sensitivity.md) — хрупкость measurement к phrasing и surface formatting.
- [wiki/concepts/specification-gaming](wiki/concepts/specification-gaming.md) — как proxy objective расходится с intended outcome.
- [wiki/concepts/inspect-ai](wiki/concepts/inspect-ai.md) — Inspect AI как главный practical tooling layer курса.

### Benchmarking и interpretation
- [wiki/concepts/benchmarking](wiki/concepts/benchmarking.md) — benchmarking как controlled slice, а не финальный verdict.
- [wiki/concepts/model-safety-evals](wiki/concepts/model-safety-evals.md) — оценки, работающие на уровне outputs и model-side properties.
- [wiki/concepts/contextual-safety-evals](wiki/concepts/contextual-safety-evals.md) — оценки, учитывающие context, deployment и downstream impact.
- [wiki/concepts/statistical-rigor-in-evals](wiki/concepts/statistical-rigor-in-evals.md) — confidence intervals, paired tests, power и MDE.
- [wiki/concepts/evaluation-generalization](wiki/concepts/evaluation-generalization.md) — limits of static benchmarks и bounded transfer of results.

### Benchmark design и validity
- [wiki/concepts/benchmark-design](wiki/concepts/benchmark-design.md) — benchmark как содержательная конструкция, а не нейтральный прибор.
- [wiki/concepts/holistic-evaluation](wiki/concepts/holistic-evaluation.md) — HELM-style coverage, multi-metric evaluation и standardized comparison.
- [wiki/concepts/evidence-centered-benchmark-design](wiki/concepts/evidence-centered-benchmark-design.md) — benchmark как evidence chain из capability, content, adaptation, assembly и evidence.
- [wiki/concepts/benchmark-lottery](wiki/concepts/benchmark-lottery.md) — как benchmark ecosystem формирует narrative о прогрессе.
- [wiki/concepts/construct-validity](wiki/concepts/construct-validity.md) — насколько benchmark действительно измеряет заявленный capability concept.
- [wiki/concepts/benchmark-documentation](wiki/concepts/benchmark-documentation.md) — documentation layer для benchmark transparency и reuse.
- [wiki/concepts/llm-as-a-judge](wiki/concepts/llm-as-a-judge.md) — judge model как отдельный measurement device со своими biases и limits.
- [wiki/concepts/toxicity-evals](wiki/concepts/toxicity-evals.md) — toxicity measurement как пример benchmark design и bias-sensitive evaluation.

### Agent evaluation
- [wiki/concepts/agent-evaluation](wiki/concepts/agent-evaluation.md) — why agent eval is wider than ordinary model benchmarking.
- [wiki/concepts/agent-reliability](wiki/concepts/agent-reliability.md) — consistency, robustness, predictability и safety как отдельный reliability profile.
- [wiki/concepts/capability-elicitation](wiki/concepts/capability-elicitation.md) — как не занижать reachable performance слабым protocol.
- [wiki/concepts/agent-scaffolding](wiki/concepts/agent-scaffolding.md) — prompts, tools, loops и limits как часть measurement procedure.
- [wiki/concepts/agent-autonomy](wiki/concepts/agent-autonomy.md) — autonomy как свойство системы, а не только модели.
- [wiki/concepts/react-agents](wiki/concepts/react-agents.md) — think-act-observe loop как минимальный agent pattern.

### Reliable AI safety evals
- [wiki/concepts/ai-safety-benchmarks](wiki/concepts/ai-safety-benchmarks.md) — чем safety benchmark отличается от generic capability benchmark.
- [wiki/concepts/eval-methodology](wiki/concepts/eval-methodology.md) — качество самой практики построения, проверки и интерпретации evals.
- [wiki/concepts/science-of-evals](wiki/concepts/science-of-evals.md) — maturation evals от craft к более зрелой дисциплине.
- [wiki/concepts/measurement-validity](wiki/concepts/measurement-validity.md) — как proxy score связан с real-world property and harm.
- [wiki/concepts/risk-quantification](wiki/concepts/risk-quantification.md) — observed rate, severity, uncertainty и deployment risk.
- [wiki/concepts/research-taste](wiki/concepts/research-taste.md) — выбор действительно важных problems вместо convenient proxies.

## Source Pages

### Week-01
- [wiki/sources/apollo-starter-guide-evals](wiki/sources/apollo-starter-guide-evals.md) — вводный текст Apollo про смысл evals, навыки evaluator и практический цикл работы.
- [wiki/sources/hubinger-understanding-based-safety-evals](wiki/sources/hubinger-understanding-based-safety-evals.md) — аргумент за более сильный standard, чем поведенческая проверка.
- [wiki/sources/barnett-thiergart-evals-catastrophic-risks](wiki/sources/barnett-thiergart-evals-catastrophic-risks.md) — системная статья про lower bounds, upper bounds и пределы catastrophic-risk evals.
- [wiki/sources/igor-ivanov-what-is-an-evaluation](wiki/sources/igor-ivanov-what-is-an-evaluation.md) — разбор того, что вообще считать evaluation и почему это определение matters.
- [wiki/sources/deepmind-specification-gaming](wiki/sources/deepmind-specification-gaming.md) — canonical текст про proxy optimization и metric misspecification.
- [wiki/sources/prompt-sensitivity-benchmark](wiki/sources/prompt-sensitivity-benchmark.md) — paper про хрупкость benchmark results к изменению prompt wording.
- [wiki/sources/inspect-ai-tutorial-week-01](wiki/sources/inspect-ai-tutorial-week-01.md) — первый notebook-layer курса через Inspect AI.

### Week-02
- [wiki/sources/cset-ai-safety-evaluations-explainer](wiki/sources/cset-ai-safety-evaluations-explainer.md) — taxonomy safety evaluations и базовый frame `what / how / what it means`.
- [wiki/sources/miller-adding-error-bars-to-evals](wiki/sources/miller-adding-error-bars-to-evals.md) — главный текст про uncertainty, paired analysis, power и MDE.
- [wiki/sources/cao-generalizable-evaluation-llm-era](wiki/sources/cao-generalizable-evaluation-llm-era.md) — survey про limits of static benchmarks и beyond-benchmarks frame.
- [wiki/sources/inspect-ai-tutorial-week-02](wiki/sources/inspect-ai-tutorial-week-02.md) — практический notebook про MMLU и statistical reading of results.
- [wiki/sources/awesome-llm-eval](wiki/sources/awesome-llm-eval.md) — curated repo как карта benchmark landscape, но не замена evaluation judgment.

### Week-03
- [wiki/sources/holistic-evaluation-language-models](wiki/sources/holistic-evaluation-language-models.md) — HELM как широкий multi-metric benchmark frame.
- [wiki/sources/evidence-centered-benchmark-design-nlp](wiki/sources/evidence-centered-benchmark-design-nlp.md) — ECBD как строгая evidence-centered рамка benchmark design.
- [wiki/sources/benchmark-lottery](wiki/sources/benchmark-lottery.md) — benchmark ecosystem как сила, формирующая progress narrative.
- [wiki/sources/jigsaw-unintended-bias-text-classification](wiki/sources/jigsaw-unintended-bias-text-classification.md) — unintended bias в toxicity classification.
- [wiki/sources/realtoxicityprompts-toxic-degeneration](wiki/sources/realtoxicityprompts-toxic-degeneration.md) — токсичность как свойство generative LM behavior и training data.
- [wiki/sources/llm-as-a-judge-mt-bench-chatbot-arena](wiki/sources/llm-as-a-judge-mt-bench-chatbot-arena.md) — базовый paper про LLM-as-a-judge.
- [wiki/sources/limits-scalable-evaluation-frontier](wiki/sources/limits-scalable-evaluation-frontier.md) — limits of scalable eval at the frontier when judge quality saturates.
- [wiki/sources/no-free-labels-llm-as-a-judge](wiki/sources/no-free-labels-llm-as-a-judge.md) — ограничения judge without human grounding.
- [wiki/sources/hardt-emerging-science-ml-benchmarks](wiki/sources/hardt-emerging-science-ml-benchmarks.md) — более широкий benchmark-science взгляд на ranking stability и contamination.
- [wiki/sources/benchmarkcards-llm-benchmarks](wiki/sources/benchmarkcards-llm-benchmarks.md) — documentation standard для benchmark transparency.
- [wiki/sources/construct-validity-nomological-networks](wiki/sources/construct-validity-nomological-networks.md) — спорный, но полезный текст про construct validity и nomological networks.
- [wiki/sources/inspect-ai-tutorial-week-03](wiki/sources/inspect-ai-tutorial-week-03.md) — практический notebook с toxicity pipeline и LLM judge.

### Week-04
- [wiki/sources/evaluation-benchmarking-llm-agents-survey](wiki/sources/evaluation-benchmarking-llm-agents-survey.md) — survey-карта области agent evaluation по осям `what` и `how`.
- [wiki/sources/science-ai-agent-reliability](wiki/sources/science-ai-agent-reliability.md) — reliability profile beyond success rate.
- [wiki/sources/metr-guidelines-capability-elicitation](wiki/sources/metr-guidelines-capability-elicitation.md) — METR protocol про elicitation и underestimation.
- [wiki/sources/inspect-ai-tutorial-week-04](wiki/sources/inspect-ai-tutorial-week-04.md) — ReAct agent, MATH-500 и dev/test elicitation loop.
- [wiki/sources/react-synergizing-reasoning-acting](wiki/sources/react-synergizing-reasoning-acting.md) — ReAct как baseline agent pattern.
- [wiki/sources/math-dataset](wiki/sources/math-dataset.md) — MATH dataset как benchmark context для notebook.
- [wiki/sources/llm-agent-survey-methodology-applications-challenges](wiki/sources/llm-agent-survey-methodology-applications-challenges.md) — широкий survey про design space самих агентов.
- [wiki/sources/measuring-ai-agent-autonomy-practice](wiki/sources/measuring-ai-agent-autonomy-practice.md) — deployment-side measurement of agent autonomy.
- [wiki/sources/swe-bench-real-world-github-issues](wiki/sources/swe-bench-real-world-github-issues.md) — canonical coding benchmark on real GitHub issues.
- [wiki/sources/swe-bench-verified](wiki/sources/swe-bench-verified.md) — benchmark quality control и verified subset для SWE-bench.
- [wiki/sources/metr-autonomy-evaluation-resources](wiki/sources/metr-autonomy-evaluation-resources.md) — index ресурсов METR по autonomy evaluation.

### Week-05
- [wiki/sources/how-should-ai-safety-benchmarks-benchmark-safety](wiki/sources/how-should-ai-safety-benchmarks-benchmark-safety.md) — самый строгий текст про standards and failure modes safety benchmarking.
- [wiki/sources/we-need-a-science-of-evals](wiki/sources/we-need-a-science-of-evals.md) — Apollo text про maturation evals в более зрелую discipline.
- [wiki/sources/you-and-your-research](wiki/sources/you-and-your-research.md) — финальный research-taste текст про important problems и long research trajectory.

### Shared
- [wiki/sources/slava-meriton-evals-methodology-lecture-01](wiki/sources/slava-meriton-evals-methodology-lecture-01.md) — why eval methodology is AI safety-relevant at the level of field context and leverage.
- [wiki/sources/slava-meriton-evals-methodology-lecture-02](wiki/sources/slava-meriton-evals-methodology-lecture-02.md) — evals as an empirical tool under weak theory and imperfect checks.
- [wiki/sources/slava-meriton-evals-methodology-lecture-03](wiki/sources/slava-meriton-evals-methodology-lecture-03.md) — methodological turn toward operationalizing goals, ontology and measurable patterns.
