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

## Эпистемический статус и как на него смотреть
Это benchmark-quality-control and verification note, а не simply a new leaderboard announcement. Его полезно читать как example of how human review can change what a benchmark is actually claiming to measure.

## На какие вопросы источник помогает отвечать
- Как benchmark artifacts в SWE-bench занижают apparent model capability?
- Что именно проверяли human annotators и зачем нужен `Verified` subset?
- Чем quality filtering отличается от artificial difficulty reduction?
- Почему benchmark verification itself becomes part of evaluation methodology?

## Краткое содержание
OpenAI разбирает `SWE-bench` как важный benchmark для model autonomy, а затем показывает, где он может недооценивать capabilities. Текст выделяет три класса проблем: overly specific or misaligned unit tests, underspecified issue descriptions и unreliable environment setup. Затем описывается human annotation campaign, где профессиональные разработчики вручную проверяли quality samples, и на этой основе выделяется `SWE-bench Verified` — subset из 500 более надежных задач. Важный смысл работы не в новом score как таковом, а в methodological claim: если benchmark construction плох, то benchmark systematically distorts what we think the models can do.

## Как читать источник быстро
- Если нужен main correction, читай the three artifact classes: tests, issue descriptions and environment instability.
- Если интересует method, переходи к human annotation / verification process and how the subset was formed.
- Если нужен broader takeaway, держи фокус на claim that benchmark quality control can materially change capability conclusions.

## Что источник утверждает прямо
- Original `SWE-bench` содержит artifacts вроде overly specific tests, underspecified issue descriptions and unstable environments.
- Human review and filtering can carve out a `Verified` subset with more reliable task specifications.
- Quality filtering can materially change the apparent capability picture without being mere artificial difficulty reduction.
- Benchmark verification itself is part of methodology when conclusions depend on benchmark cleanliness.

## Что здесь особенно важно
- **Benchmark verification** может заметно менять perceived capability level.
- **Difficulty shift** и **quality filtering** — не одно и то же.
- **Evaluation harness quality** сама по себе влияет на вывод о модели.

## Интерпретация для курса
Для курса этот текст полезен как reminder that underestimation comes not only from weak elicitation. Иногда benchmark itself is noisy, unfair or underspecified, и тогда улучшать нужно не агента, а сам evaluation substrate.

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
