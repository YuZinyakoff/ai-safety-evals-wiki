# Индекс базы знаний

## Главный вход
- [wiki/home](wiki/home.md) — основная входная точка по базе
- [log](log.md) — краткая история изменений

## Как читать этот индекс
- Здесь собраны стабильные входы и полезные маршруты, а не полный инвентарь всех страниц.
- Внутренние ссылки ведутся в относительном Markdown-формате, чтобы одинаково открываться в Obsidian, VS Code и GitHub.
- Для полного понимания конкретной недели лучше идти через ее hub-page, а не пытаться читать wiki линейно из этого файла.

## Быстрые маршруты
- Если нужен **вход в limits of evals**, начинай с [wiki/weeks/week-01](wiki/weeks/week-01.md), [wiki/concepts/evals](wiki/concepts/evals.md) и [wiki/syntheses/evals-scope-and-limits](wiki/syntheses/evals-scope-and-limits.md).
- Если нужен **вход в benchmarking и статистическую интерпретацию**, открывай [wiki/weeks/week-02](wiki/weeks/week-02.md), [wiki/concepts/statistical-rigor-in-evals](wiki/concepts/statistical-rigor-in-evals.md) и [wiki/syntheses/benchmarking-beyond-single-scores](wiki/syntheses/benchmarking-beyond-single-scores.md).
- Если нужен **вход в benchmark design, validity и benchmark ecosystem**, переходи к [wiki/weeks/week-03](wiki/weeks/week-03.md), [wiki/concepts/benchmark-design](wiki/concepts/benchmark-design.md) и [wiki/syntheses/benchmark-design-evidence-and-incentives](wiki/syntheses/benchmark-design-evidence-and-incentives.md).
- Если нужен **вход в agent evaluation, reliability и elicitation**, открывай [wiki/weeks/week-04](wiki/weeks/week-04.md), [wiki/concepts/agent-evaluation](wiki/concepts/agent-evaluation.md) и [wiki/syntheses/agent-evals-beyond-task-success](wiki/syntheses/agent-evals-beyond-task-success.md).
- Если нужен **практический слой**, смотри [wiki/concepts/inspect-ai](wiki/concepts/inspect-ai.md), [wiki/sources/inspect-ai-tutorial-week-01](wiki/sources/inspect-ai-tutorial-week-01.md), [wiki/sources/inspect-ai-tutorial-week-02](wiki/sources/inspect-ai-tutorial-week-02.md), [wiki/sources/inspect-ai-tutorial-week-03](wiki/sources/inspect-ai-tutorial-week-03.md) и [wiki/sources/inspect-ai-tutorial-week-04](wiki/sources/inspect-ai-tutorial-week-04.md).

## Текущее покрытие
- `week-01` разобрана по theory, notebook и extra-материалам и дополнительно усилена clipped / normalized raw-текстами для ключевых источников.
- `week-02` тоже разобрана по theory, notebook и extra-материалам.
- `week-03` тоже разобрана по theory, notebook и extra-материалам.
- `week-04` тоже разобрана по theory, notebook и extra-материалам.
- Для ключевых arXiv-материалов первых двух недель теперь в основном есть более сильный raw: clipped Markdown, PDF и `TeX Source`.
- Для ключевых материалов третьей недели preferred raw тоже выбран: clipped Markdown там, где он был доступен, а PDF sidecar используется только как fallback.
- Для ключевых материалов четвертой недели preferred raw тоже в основном clipped-first, а PDF/TeX остаются backup-слоем.
- Для `week-01` есть 7 source pages, 7 concept pages и 1 synthesis.
- Для `week-02` есть 5 source pages, 5 новых concept pages и 1 synthesis.
- Для `week-03` есть 12 source pages, 8 новых concept pages и 1 synthesis.
- Для `week-04` есть 11 source pages, 6 новых concept pages и 1 synthesis.
- `week-05` пока остается стартовой страницей.

## Недели
- [wiki/weeks/week-01](wiki/weeks/week-01.md) — основная hub-page по первой неделе
- [wiki/weeks/week-02](wiki/weeks/week-02.md) — hub-page по benchmarking, statistical rigor и evaluation design
- [wiki/weeks/week-03](wiki/weeks/week-03.md) — hub-page по benchmark design, evidence claims и benchmark ecosystem
- [wiki/weeks/week-04](wiki/weeks/week-04.md) — hub-page по agent evaluation, reliability, elicitation и autonomy
- [wiki/weeks/week-05](wiki/weeks/week-05.md) — стартовая страница под будущий ingest

## Ключевые страницы week-01
- [wiki/sources/apollo-starter-guide-evals](wiki/sources/apollo-starter-guide-evals.md) — вводный словарь evals и роли evaluator
- [wiki/sources/barnett-thiergart-evals-catastrophic-risks](wiki/sources/barnett-thiergart-evals-catastrophic-risks.md) — самая системная страница про силу и пределы evals
- [wiki/sources/inspect-ai-tutorial-week-01](wiki/sources/inspect-ai-tutorial-week-01.md) — практический вход через notebook и `Inspect AI`
- [wiki/syntheses/evals-scope-and-limits](wiki/syntheses/evals-scope-and-limits.md) — межисточниковая сводка по тому, какие выводы evals реально поддерживают

## Ключевые страницы week-02
- [wiki/sources/cset-ai-safety-evaluations-explainer](wiki/sources/cset-ai-safety-evaluations-explainer.md) — taxonomy safety evaluations и design frame недели
- [wiki/sources/miller-adding-error-bars-to-evals](wiki/sources/miller-adding-error-bars-to-evals.md) — главная страница про uncertainty, CI и power в evals
- [wiki/sources/cao-generalizable-evaluation-llm-era](wiki/sources/cao-generalizable-evaluation-llm-era.md) — survey про limits of static benchmarks и evaluation generalization
- [wiki/sources/inspect-ai-tutorial-week-02](wiki/sources/inspect-ai-tutorial-week-02.md) — практический MMLU notebook с statistical analysis
- [wiki/syntheses/benchmarking-beyond-single-scores](wiki/syntheses/benchmarking-beyond-single-scores.md) — сводка недели о том, почему benchmark score не равен хорошему выводу

## Ключевые страницы week-03
- [wiki/sources/holistic-evaluation-language-models](wiki/sources/holistic-evaluation-language-models.md) — HELM как широкий frame для benchmark design
- [wiki/sources/evidence-centered-benchmark-design-nlp](wiki/sources/evidence-centered-benchmark-design-nlp.md) — самый строгий текст про evidence chain benchmark'а
- [wiki/sources/benchmark-lottery](wiki/sources/benchmark-lottery.md) — benchmark ecosystem как сила, которая формирует прогресс
- [wiki/sources/inspect-ai-tutorial-week-03](wiki/sources/inspect-ai-tutorial-week-03.md) — judge-based toxicity pipeline в `Inspect AI`
- [wiki/syntheses/benchmark-design-evidence-and-incentives](wiki/syntheses/benchmark-design-evidence-and-incentives.md) — сводка недели о том, как benchmark design формирует evidence и incentives

## Ключевые страницы week-04
- [wiki/sources/evaluation-benchmarking-llm-agents-survey](wiki/sources/evaluation-benchmarking-llm-agents-survey.md) — карта области agent evaluation по осям `what` и `how`
- [wiki/sources/science-ai-agent-reliability](wiki/sources/science-ai-agent-reliability.md) — reliability profile beyond mean success
- [wiki/sources/metr-guidelines-capability-elicitation](wiki/sources/metr-guidelines-capability-elicitation.md) — главный текст недели про elicitation и underestimation
- [wiki/sources/inspect-ai-tutorial-week-04](wiki/sources/inspect-ai-tutorial-week-04.md) — ReAct agent, tools и dev/test elicitation loop
- [wiki/syntheses/agent-evals-beyond-task-success](wiki/syntheses/agent-evals-beyond-task-success.md) — сводка недели о capability, reliability и measurement procedure

## Ключевые концепты week-01
- [wiki/concepts/evals](wiki/concepts/evals.md) — базовая карта области
- [wiki/concepts/behavioral-evals](wiki/concepts/behavioral-evals.md) — что именно измеряет observed behavior
- [wiki/concepts/understanding-based-evals](wiki/concepts/understanding-based-evals.md) — зачем нужен более сильный standard, чем behavior-only testing
- [wiki/concepts/evaluation-awareness](wiki/concepts/evaluation-awareness.md) — почему eval-like context может искажать поведение
- [wiki/concepts/prompt-sensitivity](wiki/concepts/prompt-sensitivity.md) — как phrasing prompt влияет на measurement
- [wiki/concepts/specification-gaming](wiki/concepts/specification-gaming.md) — как proxy objective расходится с intended outcome
- [wiki/concepts/inspect-ai](wiki/concepts/inspect-ai.md) — tooling layer первой недели

## Ключевые концепты week-02
- [wiki/concepts/benchmarking](wiki/concepts/benchmarking.md) — benchmarking как controlled slice, а не финальный verdict
- [wiki/concepts/model-safety-evals](wiki/concepts/model-safety-evals.md) — evaluation outputs самой модели
- [wiki/concepts/contextual-safety-evals](wiki/concepts/contextual-safety-evals.md) — evaluation downstream impact и task context
- [wiki/concepts/statistical-rigor-in-evals](wiki/concepts/statistical-rigor-in-evals.md) — CI, paired tests, power и MDE
- [wiki/concepts/evaluation-generalization](wiki/concepts/evaluation-generalization.md) — bounded evaluation pipeline vs growing model capacity

## Ключевые концепты week-03
- [wiki/concepts/benchmark-design](wiki/concepts/benchmark-design.md) — benchmark как содержательная конструкция, а не нейтральный тест
- [wiki/concepts/holistic-evaluation](wiki/concepts/holistic-evaluation.md) — coverage, multi-metric evaluation и standardized comparison
- [wiki/concepts/evidence-centered-benchmark-design](wiki/concepts/evidence-centered-benchmark-design.md) — benchmark как evidence chain из пяти модулей
- [wiki/concepts/benchmark-lottery](wiki/concepts/benchmark-lottery.md) — benchmark ecosystem искажающий narrative о прогрессе
- [wiki/concepts/llm-as-a-judge](wiki/concepts/llm-as-a-judge.md) — judge model как новый measurement device со своими limits
- [wiki/concepts/construct-validity](wiki/concepts/construct-validity.md) — почему capability words требуют более строгой validity рамки

## Ключевые концепты week-04
- [wiki/concepts/agent-evaluation](wiki/concepts/agent-evaluation.md) — почему оценка агентов шире обычного benchmarking
- [wiki/concepts/agent-reliability](wiki/concepts/agent-reliability.md) — consistency, robustness, predictability и safety как отдельный профиль
- [wiki/concepts/capability-elicitation](wiki/concepts/capability-elicitation.md) — как не занижать reachable performance
- [wiki/concepts/agent-scaffolding](wiki/concepts/agent-scaffolding.md) — prompts, tools, loops и limits как часть measurement
- [wiki/concepts/agent-autonomy](wiki/concepts/agent-autonomy.md) — autonomy как свойство не только модели, но и продукта/oversight
- [wiki/concepts/react-agents](wiki/concepts/react-agents.md) — think-act-observe loop как минимальный agent pattern
