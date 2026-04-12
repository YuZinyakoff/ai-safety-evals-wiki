# Introducing SWE-Bench Verified

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/Introducing SWE-bench Verified.md>)
- **Оригинал:** [OpenAI](https://openai.com/index/introducing-swe-bench-verified/)
- **Полнота raw:** хороший web-clipped Markdown

## Ключевая мысль
> **Даже сильный agent benchmark может систематически занижать способности моделей, если в нем есть плохо специфицированные задачи, unfair tests или unstable evaluation harness.**

## Зачем источник в базе
Этот текст нужен как week-04 extension к идее benchmark criticism. Он показывает, что проблема underestimation существует не только на уровне elicitation protocol, но и на уровне самого benchmark.

## Краткое содержание
OpenAI разбирает `SWE-bench` как важный benchmark для model autonomy, а затем показывает, где он может недооценивать capabilities. Текст выделяет три класса проблем: overly specific or misaligned unit tests, underspecified issue descriptions и unreliable environment setup. Затем описывается human annotation campaign, где профессиональные разработчики вручную проверяли quality samples, и на этой основе выделяется `SWE-bench Verified` — subset из 500 более надежных задач. Важный смысл работы не в новом score как таковом, а в methodological claim: если benchmark construction плох, то benchmark systematically distorts what we think the models can do.

## Что здесь особенно важно
- **Benchmark verification** может заметно менять perceived capability level.
- **Difficulty shift** и **quality filtering** — не одно и то же.
- **Evaluation harness quality** сама по себе влияет на вывод о модели.

## Что это добавляет к теме недели
Текст соединяет benchmark criticism из прошлой недели с agent evals текущей недели. Он хорошо показывает, что underestimation может возникать и из-за benchmark artifacts, и из-за weak elicitation, и эти источники ошибок нужно различать.

## Что стоит запомнить при повторении
- **Low score не всегда означает low capability.**
- **Human verification benchmark'а** иногда меняет картину сильнее, чем новая model release.
- **Benchmark quality control** — часть safety-relevant evaluation work.

## Связанные концепты
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)

## Что осталось неясным / спорным
- Насколько conservative filtering в SWE-bench Verified сам может увести benchmark distribution?
- Какие аналогичные verification passes нужны для других agent benchmarks?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/swe-bench-real-world-github-issues](swe-bench-real-world-github-issues.md)
- [sources/metr-guidelines-capability-elicitation](metr-guidelines-capability-elicitation.md)
