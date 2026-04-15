# Неделя 02

## Ключевая мысль
> **Week-02 делает benchmark culture взрослее.** После нее score полезно читать не как почти готовый verdict, а как результат внутри evaluation frame, статистических предпосылок и ограниченного coverage.

## Зачем открывать эту страницу
Это hub-page второй недели. Ее лучше читать как карту вопросов, которые появляются сразу после первой недели. Если week-01 калибровала ожидания от behavioral evidence, то week-02 делает следующий шаг: спрашивает, **что именно мы меряем**, **как честно интерпретировать число**, и **насколько далеко вообще можно переносить benchmark result**.

## Замысел недели от организаторов
В `raw/` теперь сохранена отдельная organizer note: [course-framing-week-02.md](../../raw/week-02/extra/course-framing-week-02.md). Она полезна не как еще один theory-source, а как рамка перехода от week-01 к вопросу о стратегии evals.

Если сжать эту рамку до одного абзаца, получится так: week-01 показала, что evals ограничены и не дают гарантий, а week-02 спрашивает, что делать после этого вывода. Ответ недели такой: нужно яснее различать типы evaluation-задач, аккуратнее выбирать benchmark под конкретный вопрос и честнее обращаться с неопределенностью, статистической мощностью и границами обобщения.

## Главные вопросы недели
- **Какой тип evaluation мы вообще проводим?** Неделя начинает с различия между `model safety evaluations` и `contextual safety evaluations`.
- **Что означает benchmark score?** Здесь в центр входят `confidence intervals`, `paired analysis`, `power` и `minimum detectable effect`.
- **Где кончается полезность benchmark?** Появляются `contamination`, `static benchmark limits`, `bounded evaluation pipelines` и `evaluation generalization`.
- **Как это operationalize на практике?** Notebook по `Inspect AI` показывает полный путь от benchmark run до statistical analysis.

## Вопросы перед чтением и повторением
Эти вопросы полезны как до чтения, так и после него: сначала они вскрывают неясности, а потом помогают проверить, насколько точнее стала картина.

- Если evals не дают общей гарантии безопасности, то какие свойства модели вообще имеет смысл пытаться измерять и зачем?
- Когда мы говорим, что модель "хорошо работает", что именно мы имеем в виду: высокий benchmark score, надежность в контексте, низкий риск вреда или что-то еще?
- Если evals не дают гарантий, то что может делать один eval более надежным, чем другой: лучший task fit, более честная статистика, более широкий coverage или что-то еще?

## Если нужно быстро вспомнить неделю
- Если нужен **taxonomy / design frame**, начни с [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md), [model safety evals](../concepts/model-safety-evals.md) и [contextual safety evals](../concepts/contextual-safety-evals.md).
- Если нужен **statistical core**, смотри [Miller](../sources/miller-adding-error-bars-to-evals.md), [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-02.md) и [statistical rigor in evals](../concepts/statistical-rigor-in-evals.md).
- Если нужен **взгляд beyond benchmarks**, открывай [survey](../sources/cao-generalizable-evaluation-llm-era.md), [benchmarking](../concepts/benchmarking.md), [evaluation generalization](../concepts/evaluation-generalization.md) и [synthesis](../syntheses/benchmarking-beyond-single-scores.md).
- Если нужен **landscape-wide каталог**, переходи к [Awesome LLM Eval](../sources/awesome-llm-eval.md).

## Если у тебя конкретный вопрос
- Если вопрос звучит как **“что именно я вообще пытаюсь измерить: model property или contextual harm/usefulness?”**, начни с [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md).
- Если вопрос звучит как **“как честно читать benchmark score, uncertainty и difference between models?”**, сначала иди в [Miller](../sources/miller-adding-error-bars-to-evals.md), потом в [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-02.md).
- Если вопрос звучит как **“почему даже аккуратный benchmark может плохо generalize beyond its suite?”**, читай [Generalizable Evaluation survey](../sources/cao-generalizable-evaluation-llm-era.md).
- Если вопрос звучит как **“где быстро посмотреть landscape benchmarks и tools, но не спутать это с готовым judgment?”**, используй [Awesome LLM Eval](../sources/awesome-llm-eval.md) как карту, а не как финальный ответ.

## Картина недели
Если собрать week-02 в одну линию, получится такой ход. Сначала материалы уточняют, что разные evaluation setups отвечают на разные вопросы: одно дело — измерять outputs самой модели, другое — оценивать downstream usefulness или harm in context. Затем неделя делает benchmark result статистически “тяжелее”: score перестает быть просто числом и становится estimate с uncertainty, paired structure, power limits и design assumptions. Наконец, survey beyond benchmarks показывает, что даже аккуратно посчитанный benchmark result не снимает проблемы coverage, contamination и bounded evaluation practice. Notebook по `Inspect AI` нужен здесь затем, чтобы все эти принципы превратились в конкретный workflow, а не остались на уровне красивых формулировок.

## Как материалы собираются в одну линию
- **CSET explainer** задает taxonomy и design frame: `what to measure -> how to measure -> what the results mean`.
- **Miller** делает benchmark interpretation статистически честной и показывает, почему error bars, paired tests и power analysis — часть самого evaluation claim.
- **Survey beyond benchmarks** расширяет разговор: даже хороший benchmark может оставаться слишком узким, слишком статичным и слишком медленным по сравнению с ростом capabilities.
- **Inspect AI tutorial** переводит это в практику: `dataset -> Task -> EvalLog -> DataFrame -> CI / paired comparison / power`.
- **Awesome-LLM-Eval** служит полезной картой поля, но одновременно напоминает, что длинный каталог benchmarks не равен решенной проблеме оценки.

## Что нужно уметь объяснить своими словами
- **Почему важно различать model-side и contextual evaluations.** Один и тот же score не отвечает одинаково хорошо на вопрос о capability и на вопрос о real-world impact.
- **Почему один benchmark score почти всегда слишком слаб.** Нужны хотя бы uncertainty estimates и понимание design assumptions.
- **Почему paired comparison сильнее простого сравнения средних.** Если модели отвечают на одни и те же вопросы, структура данных сама дает более сильный тест.
- **Почему проблема benchmark не исчерпывается статистикой.** Даже честно посчитанный результат все равно может плохо generalize за пределы suite.
- **Почему catalog of benchmarks не заменяет evaluation judgment.** Наличие большого landscape не снимает вопрос о task fit, validity и интерпретации.

## Практический слой
Week-02 особенно сильна тем, что она не оставляет статистику в paper appendix. Ноутбук по `Inspect AI` показывает, как benchmark workflow на `MMLU` доводится до нормального анализа:
- как загрузить данные и собрать `Task`;
- как превратить `EvalLog` в табличный анализ;
- как считать `confidence intervals`;
- как сравнивать две модели через `paired test`;
- как думать про `power analysis` и `required sample size` до следующего дорогого запуска.

Это полезно помнить как контрвес популярной привычке “запустить benchmark и на этом остановиться”.

## Источники недели
### Theory
- [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md) — taxonomy AI safety evaluations и базовая рамка проектирования
- [Miller](../sources/miller-adding-error-bars-to-evals.md) — статистический взгляд на benchmark results и uncertainty
- [Generalizable Evaluation survey](../sources/cao-generalizable-evaluation-llm-era.md) — почему field движется beyond static benchmarks

### Notebooks
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-02.md) — MMLU, `EvalLog`, confidence intervals, paired tests и sample-size planning

### Extra
- [Awesome LLM Eval](../sources/awesome-llm-eval.md) — curated repo как карта benchmarks, tools и leaderboards

## Куда идти дальше внутри wiki
- Если нужен **межисточниковый вывод недели**, смотри [Benchmarking Beyond Single Scores](../syntheses/benchmarking-beyond-single-scores.md).
- Если нужно быстро пройтись по **ключевым концептам**, открой [benchmarking](../concepts/benchmarking.md), [model safety evals](../concepts/model-safety-evals.md), [contextual safety evals](../concepts/contextual-safety-evals.md), [statistical rigor in evals](../concepts/statistical-rigor-in-evals.md), [evaluation generalization](../concepts/evaluation-generalization.md) и [Inspect AI](../concepts/inspect-ai.md).

## Что повторить перед следующей неделей
- Уметь различать `model safety` и `contextual safety evaluations`.
- Понимать, почему benchmark score без uncertainty estimate слишком слаб как самостоятельный вывод.
- Держать в голове разницу между `n`, `K`, `paired comparison` и `minimum detectable effect`.
- Помнить, что проблема benchmarking не исчерпывается статистикой: `coverage`, `contamination` и `bounded evaluation practice` тоже критичны.

## Примечание о raw
- [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md) опирается на полный web clip.
- [Miller](../sources/miller-adding-error-bars-to-evals.md) теперь имеет сильный raw-набор: clipped HTML, PDF и `TeX Source`.
- [Generalizable Evaluation survey](../sources/cao-generalizable-evaluation-llm-era.md) теперь тоже опирается на более сильный raw-набор: clipped Markdown, PDF и `TeX Source`.
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-02.md) остается учебным notebook с `# YOUR CODE HERE`.
- [Awesome LLM Eval](../sources/awesome-llm-eval.md) остается note-with-link и служит скорее навигацией по полю, чем полным источником сам по себе.

## Открытые вопросы
- Какие benchmark designs сегодня лучше всего балансируют `reproducibility` и `real-world relevance`?
- Когда стоит переходить от model-side benchmarks к contextual protocols, а не просто улучшать existing benchmark suite?
- Насколько надежны `LLMs-as-a-judge` как долгосрочная альтернатива дорогой human evaluation?
- Как practically измерять `evaluation generalization`, а не только констатировать ее дефицит?

## Вопросы для обсуждения
- Какие концепции недели запомнились сильнее всего и почему: потому что они кажутся самыми важными, или потому что именно здесь были лучше всего объяснены?
- Если evals не дают гарантий, то что на практике делает один eval более надежным, чем другой?
- Как отвечать на вопрос "сколько вопросов нужно для хорошего eval" и что вообще должно определять достаточный размер теста?

## Краткий вывод
Week-02 полезна как калибровка против очень распространенной ошибки: смотреть на benchmark leaderboard как на почти готовый ответ. После этой недели полезно держать в голове, что score важен, но хороший evaluation начинается раньше него — в выборе frame и task — и заканчивается позже него — в статистической интерпретации и вопросе о том, что осталось вне теста.
