# Measuring Mathematical Problem Solving With The MATH Dataset

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/Measuring Mathematical Problem Solving With the MATH Dataset.md>), [PDF](<../../raw/week-04/extra/2103.03874v2.pdf>), [TeX source](<../../raw/week-04/extra/arXiv-2103.03874v2.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2103.03874)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **MATH важен не только как сложный benchmark, но и как напоминание, что reasoning-heavy tasks требуют особого внимания к task construction и scoring.**

## Зачем источник в базе
Этот материал нужен как исторический и benchmark-level контекст для notebook. Он помогает не воспринимать `MATH-500` как просто "набор задач на математику", а видеть в нем конкретный benchmark slice со своей difficulty structure и limitations.

## Краткое содержание
Статья представляет `MATH` как benchmark для challenging mathematical reasoning, где ответы требуют не только знания фактов, но и многошагового решения. Авторы обсуждают construction dataset, diversity of topics и difficulty relative to competition-style math. Для week-04 текст полезен в первую очередь не детальной empirical частью, а тем, что он объясняет природу benchmark, который затем используется в notebook через subset `MATH-500`.

## Что здесь особенно важно
- **Math benchmark** не эквивалентен simple exact-answer QA.
- **Difficulty and subject mix** влияют на то, что именно model or agent должен уметь.
- **Subset usage** вроде `MATH-500` — это уже design choice, а не нейтральная данность.

## Что это добавляет к теме недели
Этот текст помогает лучше читать notebook: становится понятнее, что именно там происходит, почему выбираются tool-friendly subjects и почему even agent with tools сталкивается с содержательными ограничениями benchmark.

## Что стоит запомнить при повторении
- **Benchmark context matters even для учебного notebook.**
- **Subject mix влияет на полезность tools и scaffolding.**
- **Exact-match-like scoring не всегда передает трудность reasoning process.**

## Связанные концепты
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Насколько math benchmarks вообще representative для general-purpose agents?
- Какие выводы о reasoning можно делать из performance on MATH-like tasks без переобобщения?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/inspect-ai-tutorial-week-04](inspect-ai-tutorial-week-04.md)
- [sources/react-synergizing-reasoning-acting](react-synergizing-reasoning-acting.md)
