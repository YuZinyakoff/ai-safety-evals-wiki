# Неделя 04

## Ключевая мысль
> **Week-04 переводит разговор с benchmark design на agent evaluation как на оценку поведения во времени.** После нее уже трудно довольствоваться одним `task success`: приходится отдельно думать про достижимые capabilities, reliability profile, autonomy, scaffolding и о том, что именно score вообще говорит об агенте.

## Зачем открывать эту страницу
Это hub-page четвертой недели. Она нужна как мост между benchmark-centric разговором week-03 и более сложным разговором о том, как оценивать системы, которые планируют, используют инструменты, взаимодействуют со средой и накапливают ошибки по ходу траектории. Эту страницу полезно читать как карту перехода от model evals к agent evals.

## Замысел недели от организаторов
В `raw/` теперь сохранена отдельная organizer note: [course-framing-week-04.md](../../raw/week-04/extra/course-framing-week-04.md). Она полезна как рамка перехода от benchmark design к оценке агентских систем.

Если сжать эту рамку до одного абзаца, получится так: week-03 уже показала, что benchmark не является нейтральным прибором, а week-04 делает следующий шаг и показывает, что в случае агентов сама единица оценки становится сложнее. Агент не просто отвечает на вопрос, а идет по траектории действий, пользуется инструментами, сталкивается с промежуточными сбоями и по-разному ведет себя при повторных запусках. Поэтому и вывод о нем нельзя сжимать до одного score без больших потерь.

## Главные вопросы недели
- **Что именно оценивать у агента помимо task success?** В центр выходят `behavior`, `capabilities`, `reliability`, `safety` и `autonomy`.
- **Как agent evaluation меняет рамку `what to measure / how to measure / what the result means`?** Для агентов важны trajectories, tools, environments, repeated runs и scaffolding.
- **Как не занижать capabilities плохой процедурой оценки?** Здесь ключевым становится `capability elicitation`.
- **Что считать meaningful result для агента?** Нужно отдельно различать score, reachable performance, reliability profile и deployment-relevant failure modes.

## Вопросы перед чтением и повторением
Эти вопросы полезны и до чтения, и после него: сначала они помогают заметить свои интуитивные пробелы, а потом проверить, насколько они изменились.

- Какие свойства агентской системы вообще труднее всего измерять корректно?
- Как рамка `evaluation strategy` переносится на оценку агентов и что в ней меняется из-за агентской специфики?

## Если нужно быстро вспомнить неделю
- Если нужна **карта всей области agent evaluation**, начни с [LLM Agents Survey](../sources/evaluation-benchmarking-llm-agents-survey.md) и [agent evaluation](../concepts/agent-evaluation.md).
- Если нужен **строгий язык про reliability beyond accuracy**, смотри [AI Agent Reliability](../sources/science-ai-agent-reliability.md) и [agent reliability](../concepts/agent-reliability.md).
- Если нужен **методический взгляд на reachable capabilities и на риск underestimation**, переходи к [METR elicitation guidelines](../sources/metr-guidelines-capability-elicitation.md) и [capability elicitation](../concepts/capability-elicitation.md).
- Если нужен **практический слой недели**, смотри [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-04.md), [ReAct](../sources/react-synergizing-reasoning-acting.md), [SWE-bench](../sources/swe-bench-real-world-github-issues.md) и [Measuring AI agent autonomy in practice](../sources/measuring-ai-agent-autonomy-practice.md).

## Картина недели
Если собрать week-04 в одну линию, получится такой ход. Сначала survey от SAP раскладывает область agent evaluation на `what to evaluate` и `how to evaluate`, показывая, что у агентов измерять нужно не только поведение, но и capabilities, reliability и safety. Затем Princeton-текст делает следующий шаг и показывает, почему single success metric скрывает свойства, важные для deployment: consistency, robustness, predictability и safety. После этого METR добавляет еще один уровень критики: даже если метрика выбрана осмысленно, плохая процедура оценки может сильно занизить реальные capabilities агента. Дополнительные материалы и notebook заземляют этот разговор: ReAct показывает, как scaffolding меняет agent behavior, SWE-bench и SWE-bench Verified показывают сложность agentic benchmark design, а Anthropic и METR дают более практический взгляд на autonomy evals и post-deployment monitoring.

## Как материалы собираются в одну линию
- **Survey про LLM agents** задает карту поля и делает видимым, что у agent evaluation больше измерений, чем у model evaluation.
- **Reliability paper** показывает, что capability growth не равна reliability growth, и что meaningful profile требует нескольких осей оценки.
- **METR elicitation guidelines** переводят разговор от "что мерить" к "как не испортить measurement procedure" и "как не занизить reachable capability".
- **ReAct и notebook** заземляют это в concrete scaffolding choices: prompts, tools, loop structure, limits, dev/test split.
- **SWE-bench и SWE-bench Verified** показывают, что agent benchmark сам по себе тоже нуждается в критической проверке и что underestimation / unfairness может исходить от benchmark design.
- **Anthropic autonomy post** добавляет deployment layer: pre-deployment evals недостаточны без наблюдения за тем, как autonomy и oversight реально устроены в использовании.

## Что нужно уметь объяснить своими словами
- **Почему agent evaluation нельзя сводить к одному success score.** Потому что агент может одинаково часто "успевать", но радикально различаться по consistency, robustness и failure severity.
- **Почему elicitation — это часть measurement, а не просто способ улучшить score.** Плохое scaffolding может измерять слабость процедуры, а не потолок возможностей модели.
- **Почему agent benchmark и deployment reality не совпадают.** В реальном использовании autonomy, oversight и user behavior совместно формируют итоговое поведение системы.
- **Почему reliability и capability нельзя смешивать.** Capability отвечает на вопрос "что агент может", а reliability — "насколько стабильно и предсказуемо он это делает".
- **Почему scaffolding choices epistemically важны.** Prompting, tools, context management и stopping criteria меняют саму траекторию агента и то, что мы считаем evidence о его способностях.

## Практический слой
Week-04 особенно полезна тем, что практический слой здесь не декоративный. Notebook делает агентскую оценку инженерной задачей:
- появляется явный `dev/test split`, чтобы не переобучать scaffolding под evaluation set;
- видно, что `ReAct` — это не просто модный паттерн, а конкретный способ организации траектории;
- становится заметно, что message limits, tool design и system prompt меняют не только score, но и тип failures;
- сама идея `elicitation` перестает быть абстракцией, потому что в notebook есть реальный цикл улучшения агента на dev set.

## Источники недели
### Theory
- [Evaluation and Benchmarking of LLM Agents: A Survey](../sources/evaluation-benchmarking-llm-agents-survey.md) — карта поля agent evaluation
- [Towards a Science of AI Agent Reliability](../sources/science-ai-agent-reliability.md) — reliability profile beyond success rate
- [METR: Guidelines for capability elicitation](../sources/metr-guidelines-capability-elicitation.md) — методика уменьшения underestimation

### Notebooks
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-04.md) — ReAct agent, MATH-500 и dev/test elicitation loop

### Extra
- [ReAct](../sources/react-synergizing-reasoning-acting.md) — reasoning + acting loop
- [MATH dataset](../sources/math-dataset.md) — benchmark context для notebook
- [LLM Agent Survey](../sources/llm-agent-survey-methodology-applications-challenges.md) — как устроен объект оценки
- [Measuring AI agent autonomy in practice](../sources/measuring-ai-agent-autonomy-practice.md) — deployment-side autonomy measurement
- [SWE-bench](../sources/swe-bench-real-world-github-issues.md) — canonical agentic coding benchmark
- [SWE-bench Verified](../sources/swe-bench-verified.md) — benchmark quality control и reduction of underestimation
- [METR Resources](../sources/metr-autonomy-evaluation-resources.md) — index автономных evaluation resources

## Куда идти дальше внутри wiki
- Если нужен **межисточниковый вывод недели**, смотри [Agent Evals Beyond Task Success](../syntheses/agent-evals-beyond-task-success.md).
- Если нужно быстро пройтись по **ключевым концептам**, открой [agent evaluation](../concepts/agent-evaluation.md), [agent reliability](../concepts/agent-reliability.md), [capability elicitation](../concepts/capability-elicitation.md), [agent scaffolding](../concepts/agent-scaffolding.md), [agent autonomy](../concepts/agent-autonomy.md) и [ReAct agents](../concepts/react-agents.md).

## Что повторить перед следующей неделей
- Держать в голове, что у агентов важен не только outcome, но и траектория.
- Отдельно различать capability, reliability и autonomy.
- Помнить, что elicitation может менять вывод о модели не меньше, чем сам benchmark.
- Не забывать, что post-deployment behavior и lab evaluation — это разные источники evidence.

## Примечание о raw
- Все три обязательных материала уже имеют сильный текстовый raw.
- Для week-04 extras raw тоже в основном сильный: почти везде есть clipped `.md`, а PDF/TeX остаются backup-слоем.
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-04.md) остается учебным notebook с `# YOUR CODE HERE`.

## Открытые вопросы
- Где проходит граница между честным elicitation и слишком сильной optimization под benchmark?
- Насколько realistic нужно делать agent eval, чтобы не потерять воспроизводимость и controllability?
- Какие reliability dimensions важнее всего в разных agent deployment contexts?
- Можно ли строить autonomy evals так, чтобы они были и threat-model-relevant, и practically runnable?

## Вопросы для обсуждения
- Должен ли хороший evaluation protocol пытаться мерить максимально достижимые возможности агента через elicitation, или полезнее держаться product-like setup?
- Как соотносятся `what to evaluate` и `how to evaluate` из survey с METR elicitation procedure и reliability dimensions из Princeton paper?
- Что в этой неделе относится к шагу `what the result means` и почему именно там появляется больше всего epistemic риска?

## Краткий вывод
Week-04 полезна тем, что ломает очень устойчивую интуицию: будто agent evaluation — это просто benchmark для чуть более сложной модели. После этой недели полезно помнить, что агентская оценка почти всегда включает вопрос о траектории, scaffolding, reliability и reachable performance. Поэтому и claims по ее результатам должны быть богаче, осторожнее и сильнее привязаны к самой процедуре измерения.
