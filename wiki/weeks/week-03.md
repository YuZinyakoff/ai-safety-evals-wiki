# Неделя 03

## Ключевая мысль
> **Week-03 смещает фокус с модели на сам benchmark.** После нее уже трудно смотреть на benchmark result как на прямое окно в способности модели: все время приходится спрашивать, какое evidence вообще собирает этот benchmark и какие выводы он по-настоящему поддерживает.

## Зачем открывать эту страницу
Это hub-page третьей недели. Она нужна как мост между разговором о `evaluation strategy` из week-02 и более предметным разговором о том, как benchmark design сам формирует результат оценки. Эту страницу полезно читать как карту того, почему выбор benchmark'а, метрик, coverage и формата агрегирования влияет на вывод не меньше, чем сама модель.

## Замысел недели от организаторов
В `raw/` теперь сохранена отдельная organizer note: [course-framing-week-03.md](../../raw/week-03/extra/course-framing-week-03.md). Она полезна не как еще один theory-source, а как рамка перехода от общей стратегии evals к вопросу о том, как проектируются benchmark'и и какие claims они вообще позволяют делать.

Если сжать эту рамку до одного абзаца, получится так: week-02 уже показала, что benchmark score нельзя интерпретировать наивно, а week-03 делает следующий шаг и спрашивает, откуда вообще берется сам score. Ответ недели такой: benchmark — это содержательная конструкция, в которой заранее зашиты выбор задач, метрик, способов адаптации и представление о том, какое evidence считать достаточным.

## Главные вопросы недели
- **Что именно benchmark считает свидетельством о свойстве модели?** Здесь особенно важна граница между `what to measure` и `how to measure it`.
- **Как дизайн benchmark'а влияет на выводы о модели?** На этой неделе в центр выходят `coverage`, `multi-metric evaluation`, `construct validity`, `aggregate scores` и `benchmark ecosystem`.
- **Как benchmark встроен в более широкую evaluation strategy?** Неделя помогает не просто читать готовые benchmark'и, а думать о том, когда их достаточно, а когда нужен другой evaluation frame.
- **Как это проявляется в реальных evaluation pipelines?** Дополнительные материалы и ноутбук связывают benchmark design с bias analysis, toxicity evaluation и `LLM-as-a-judge`.

## Вопросы перед чтением и повторением
Эти вопросы полезны и до чтения, и после него: сначала они помогают увидеть свои интуитивные границы, а потом проверить, насколько они изменились.

- Где проходит граница между `what we measure` и `how to measure it`?
- Что должно быть истинно, чтобы из того, как модель показала себя на benchmark'е, можно было делать вывод о способностях модели?

## Если нужно быстро вспомнить неделю
- Если нужен **мульти-метрический и coverage-oriented frame**, начни с [HELM](../sources/holistic-evaluation-language-models.md) и [holistic evaluation](../concepts/holistic-evaluation.md).
- Если нужен **строгий язык про evidence и validity benchmark design**, смотри [ECBD](../sources/evidence-centered-benchmark-design-nlp.md), [evidence-centered benchmark design](../concepts/evidence-centered-benchmark-design.md) и [construct validity](../concepts/construct-validity.md).
- Если нужен **взгляд на benchmark как на силу, которая формирует само поле**, переходи к [The Benchmark Lottery](../sources/benchmark-lottery.md), [Hardt](../sources/hardt-emerging-science-ml-benchmarks.md) и [benchmark lottery](../concepts/benchmark-lottery.md).
- Если нужен **прикладной хвост недели**, смотри [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-03.md), [Jigsaw bias paper](../sources/jigsaw-unintended-bias-text-classification.md), [RealToxicityPrompts](../sources/realtoxicityprompts-toxic-degeneration.md) и [LLM-as-a-judge](../concepts/llm-as-a-judge.md).

## Если у тебя конкретный вопрос
- Если вопрос звучит как **“какую общую рамку benchmark evaluation authors предлагают?”**, начни с [HELM](../sources/holistic-evaluation-language-models.md).
- Если вопрос звучит как **“как связать capability claim, task design и evidence chain более строго?”**, иди в [ECBD](../sources/evidence-centered-benchmark-design-nlp.md) и затем в [Construct validity paper](../sources/construct-validity-nomological-networks.md).
- Если вопрос звучит как **“почему benchmark влияет не только на score, но и на траекторию всего поля?”**, читай [The Benchmark Lottery](../sources/benchmark-lottery.md) вместе с [Hardt](../sources/hardt-emerging-science-ml-benchmarks.md).
- Если вопрос звучит как **“как documentation and reporting влияют на корректное использование benchmark?”**, открой [BenchmarkCards](../sources/benchmarkcards-llm-benchmarks.md).
- Если вопрос звучит как **“когда `LLM-as-a-judge` реально помогает, а где у него жесткие limits?”**, пройди связку [MT-Bench / Chatbot Arena](../sources/llm-as-a-judge-mt-bench-chatbot-arena.md), [Limits at the frontier](../sources/limits-scalable-evaluation-frontier.md) и [No Free Labels](../sources/no-free-labels-llm-as-a-judge.md).
- Если вопрос звучит как **“как benchmark design проявляется в toxicity and harm evaluation?”**, смотри [Jigsaw bias paper](../sources/jigsaw-unintended-bias-text-classification.md), [RealToxicityPrompts](../sources/realtoxicityprompts-toxic-degeneration.md) и [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-03.md).

## Картина недели
Если собрать week-03 в одну линию, получится такой ход. Сначала HELM показывает benchmark не как один тест, а как систему standardized comparison по многим сценариям и метрикам. Затем ECBD делает эту систему более строгой и спрашивает, за счет каких именно design decisions benchmark вообще собирает evidence о нужной способности. После этого The Benchmark Lottery добавляет еще один уровень критики: benchmark влияет не только на локальный вывод о модели, но и на то, что сообщество вообще начинает считать прогрессом. Дополнительные материалы и notebook переводят этот разговор в более прикладной слой, где видно, что те же вопросы всплывают в bias evaluation, toxicity evaluation, `LLM-as-a-judge` и benchmark documentation.

## Как материалы собираются в одну линию
- **HELM** задает широкий frame: benchmark должен покрывать несколько сценариев использования, несколько метрик и прозрачные условия сравнения.
- **ECBD** повышает строгость и требует явно связывать capability claim, content, adaptation, assembly и evidence.
- **The Benchmark Lottery** показывает, что benchmark design влияет не только на отдельный эксперимент, но и на траекторию всего research ecosystem.
- **Hardt** помещает этот спор в более длинную историю ML benchmarking и показывает, почему ranking stability и benchmark science сегодня становятся центральной темой.
- **Тексты про toxicity, judge pipelines и benchmark documentation** заземляют критику и показывают, что те же design questions всплывают в прикладных eval workflows.
- **Текст про construct validity** добавляет последний слой: benchmark score еще не автоматически оправдывает capability language, которым его описывают.

## Что нужно уметь объяснить своими словами
- **Почему benchmark design влияет на вывод не меньше, чем сама модель.** Потому что benchmark заранее определяет, какие задачи, метрики и формы evidence вообще попадут в поле зрения.
- **Почему coverage и validity не одно и то же.** Широкий benchmark может оставаться плохо обоснованным, а строго аргументированный benchmark может оставаться слишком узким.
- **Почему aggregate score опасен без разреза по сценариям и свойствам.** Он может скрывать реальные trade-offs между методами и режимами использования.
- **Почему benchmark — это часть evaluation strategy, а не вся стратегия.** Даже хороший benchmark не снимает вопрос о task fit, limits of transfer и том, что осталось вне теста.
- **Почему benchmark ecosystem влияет на само направление прогресса.** Сообщество оптимизирует то, что benchmark позволяет увидеть и награждает.

## Практический слой
В week-03 практика особенно важна как контрпример против слишком абстрактного разговора о benchmark design. Ноутбук и дополнительные материалы полезны здесь не сами по себе, а как место, где методологические вопросы становятся инженерными:
- как benchmark для toxicity может систематически давать перекос по отдельным группам примеров;
- как генеративная evaluation setup меняет сам смысл токсичности и вреда;
- как `LLM-as-a-judge` обещает масштабируемость, но вводит новые failure modes;
- как documentation benchmark'а помогает не потерять assumptions, limits и intended use.

## Источники недели
### Theory
- [HELM](../sources/holistic-evaluation-language-models.md) — multi-metric, coverage-oriented и standardized benchmark frame
- [ECBD](../sources/evidence-centered-benchmark-design-nlp.md) — пять модулей benchmark design и язык capability evidence
- [The Benchmark Lottery](../sources/benchmark-lottery.md) — benchmark ecosystem, task selection bias и research priorities

### Notebooks
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-03.md) — classifier–judge toxicity pipeline и audit judge reliability

### Extra
- [Jigsaw bias paper](../sources/jigsaw-unintended-bias-text-classification.md) — unintended bias в toxicity classification и slice-based mitigation
- [RealToxicityPrompts](../sources/realtoxicityprompts-toxic-degeneration.md) — generative toxicity, prompt distributions и pretraining data
- [MT-Bench / Chatbot Arena](../sources/llm-as-a-judge-mt-bench-chatbot-arena.md) — judge-based preference evaluation
- [Limits at the frontier](../sources/limits-scalable-evaluation-frontier.md) — почему debiasing judge не решает frontier evaluation
- [No Free Labels](../sources/no-free-labels-llm-as-a-judge.md) — limits of judge without human grounding
- [Hardt](../sources/hardt-emerging-science-ml-benchmarks.md) — benchmark science и ranking stability
- [BenchmarkCards](../sources/benchmarkcards-llm-benchmarks.md) — documentation layer для benchmark ecosystems
- [Construct validity paper](../sources/construct-validity-nomological-networks.md) — nomological networks и язык capability claims

## Куда идти дальше внутри wiki
- Если нужен **межисточниковый вывод недели**, смотри [Benchmark Design, Evidence, And Incentives](../syntheses/benchmark-design-evidence-and-incentives.md).
- Если нужно быстро пройтись по **ключевым концептам**, открой [benchmark design](../concepts/benchmark-design.md), [holistic evaluation](../concepts/holistic-evaluation.md), [evidence-centered benchmark design](../concepts/evidence-centered-benchmark-design.md), [benchmark lottery](../concepts/benchmark-lottery.md), [LLM-as-a-judge](../concepts/llm-as-a-judge.md), [construct validity](../concepts/construct-validity.md), [benchmark documentation](../concepts/benchmark-documentation.md) и [toxicity evals](../concepts/toxicity-evals.md).

## Что повторить перед следующей неделей
- Понимать, что benchmark — это не нейтральный тест, а конструкция с собственными assumptions.
- Держать в голове напряжение между `coverage`, `standardization`, `validity` и `evidence`.
- Помнить, что benchmark design влияет и на локальный вывод о модели, и на то, что поле начинает считать прогрессом.
- Отдельно различать judge-based evaluation для preference settings и correctness-heavy settings.

## Примечание о raw
- [HELM](../sources/holistic-evaluation-language-models.md) и [ECBD](../sources/evidence-centered-benchmark-design-nlp.md) опираются на сильный raw-набор: clipped Markdown, PDF и `TeX Source`.
- [The Benchmark Lottery](../sources/benchmark-lottery.md) пока опирается на PDF, `TeX Source` и fallback extracted Markdown.
- Для week-03 extras raw неоднороден: часть материалов есть как clipped Markdown, часть как PDF + fallback sidecar, а часть еще и с `TeX Source`.
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-03.md) остается учебным notebook с `# YOUR CODE HERE`.

## Открытые вопросы
- Когда многообразие сценариев и метрик действительно улучшает benchmark, а когда превращает его в тяжеловесный каталог без ясного claim?
- Насколько реалистично требовать от benchmark'а strong evidence chain в духе ECBD в быстро меняющемся LLM field?
- Как practically совмещать multi-metric coverage из HELM с pressure на короткие aggregate leaderboards?
- Можно ли строить benchmark ecosystem так, чтобы он меньше искажал research incentives?

## Вопросы для обсуждения
- Как соотносятся три вопроса из стратегии evals (`what to measure`, `how to measure`, `what the result means`) с идеями из HELM, ECBD и The Benchmark Lottery?
- Что важнее для хорошего benchmark'а: широта покрытия, как в HELM, или строгость аргументации о том, почему benchmark вообще собирает нужное evidence, как в ECBD?
- Какой главный вывод о природе evals и benchmark design полезно вынести, если смотреть на эту неделю вместе с двумя предыдущими?

## Краткий вывод
Week-03 полезна тем, что ломает очень устойчивую интуицию: будто benchmark просто “считывает” свойства модели. После этой недели полезно помнить, что benchmark сначала сам конструирует, какие свойства станут видимыми, какие различия будут считаться важными и какие выводы вообще покажутся правдоподобными. Именно поэтому benchmark design — это не вспомогательная техника, а часть сущности evals.
