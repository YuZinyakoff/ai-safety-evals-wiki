# The Benchmark Lottery

- **Тип источника:** theory
- **Неделя:** week-03
- **Raw:** [PDF](<../../raw/week-03/theory/2107.07002v1.pdf>), [fallback `.pdf.md`](<../../raw/week-03/theory/2107.07002v1.pdf.md>), [TeX source](<../../raw/week-03/theory/arXiv-2107.07002v1.tar.gz>)
- **Оригинал:** [arXiv PDF](https://arxiv.org/pdf/2107.07002)
- **Полнота raw:** PDF, TeX source и fallback extracted Markdown

## Ключевая мысль
> **То, что метод выглядит лучшим на benchmark'е, еще не значит, что он фундаментально лучший.** Иногда он просто “выиграл лотерею” конкретного benchmark ecosystem.

## Зачем источник в базе
Это главный критический текст недели про benchmark ecosystem. Он нужен, чтобы увидеть: benchmark влияет не только на локальный evaluation result, но и на сами research incentives, на то, какие методы сообщество начнет считать прогрессом, и на то, что потом будут массово оптимизировать.

## Краткое содержание
Paper сначала вводит саму идею `benchmark lottery`: perceived superiority метода часто зависит не только от его “объективной” силы, но и от выбора задач, агрегации результатов и текущих норм benchmark ecosystem. Затем авторы проходят по основным источникам такой хрупкости. Сначала обсуждается `task selection bias` на case studies вроде SuperGLUE, VTAB, Long Range Arena и RL Unplugged: разные подмножества задач могут менять ranking моделей. После этого paper переходит к `community bias` и показывает, что benchmark'и направляют коллективное внимание и определяют, какие свойства вообще становятся заметными. Далее появляется идея stateful benchmarks: benchmark меняется вместе с сообществом, tooling и историей участия. В финале авторы обсуждают “rigging the lottery” и дают более практические рекомендации: guidelines, significance testing и living benchmarks как частичные ответы на хрупкость benchmark process.

## Что здесь особенно важно
- **Task selection** уже сама по себе может менять ranking и narrative о “лучшем методе”.
- **Aggregate score** часто скрывает важные различия между методами.
- **Benchmark community** влияет на то, что вообще считается значимым улучшением.
- **Statefulness** означает, что benchmark нельзя считать нейтральным и неизменным арбитром.
- **Living benchmark** — не магическое решение, но более честный ответ, чем вера в static leaderboard.

## Что это добавляет к теме недели
Если HELM и ECBD говорят о том, как benchmark можно строить лучше, то `The Benchmark Lottery` показывает, почему benchmark process в принципе хрупок и socially loaded. Это важный контрвес против слишком спокойного отношения к benchmark leaderboards и “общепринятым” evaluation suites.

## Что стоит запомнить при повторении
- **Лучший на benchmark'е** не всегда значит **лучший по существу**.
- **Benchmark design и benchmark ecosystem** вместе формируют направление прогресса.
- **Ранжирование моделей** часто устойчивее абсолютных scores, но и эта устойчивость в LLM era уже ломается.

## Связанные концепты
- [concepts/benchmark-lottery](../concepts/benchmark-lottery.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/holistic-evaluation](../concepts/holistic-evaluation.md)

## Что осталось неясным / спорным
- Насколько realistic переход к benchmark ecosystems, которые меньше искажают incentives, а не просто делают эти искажения явнее?
- Когда living benchmarks действительно улучшают ситуацию, а когда просто переносят старые проблемы в более динамичную форму?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/holistic-evaluation-language-models](holistic-evaluation-language-models.md)
- [sources/hardt-emerging-science-ml-benchmarks](hardt-emerging-science-ml-benchmarks.md)
- [syntheses/benchmark-design-evidence-and-incentives](../syntheses/benchmark-design-evidence-and-incentives.md)
