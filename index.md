# Индекс базы знаний

## Главный вход
- [wiki/home](wiki/home.md) — основная входная точка по базе
- [log](log.md) — краткая история изменений

## Как читать этот индекс
- Здесь собраны только стабильные входы, а не полный инвентарь всех страниц.
- Внутренние ссылки ведутся в относительном Markdown-формате, чтобы одинаково открываться в Obsidian, VS Code и GitHub.
- Для полной картины первой недели лучше идти через hub-page недели, а не через этот файл.

## Текущее покрытие
- `week-01` разобрана по theory, notebook и extra-материалам.
- `week-02` тоже разобрана по theory, notebook и extra-материалам.
- Для `week-01` есть 7 source pages, 7 concept pages и 1 synthesis.
- Для `week-02` есть 5 source pages, 5 новых concept pages и 1 synthesis.
- `week-03`..`week-05` пока остаются стартовыми страницами.

## Недели
- [wiki/weeks/week-01](wiki/weeks/week-01.md) — основная hub-page по первой неделе
- [wiki/weeks/week-02](wiki/weeks/week-02.md) — hub-page по benchmarking, statistical rigor и evaluation design
- [wiki/weeks/week-03](wiki/weeks/week-03.md) — стартовая страница под будущий ingest
- [wiki/weeks/week-04](wiki/weeks/week-04.md) — стартовая страница под будущий ingest
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
