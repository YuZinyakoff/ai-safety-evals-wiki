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

## Эпистемический статус и как на него смотреть
Это benchmark-introduction paper for mathematical reasoning, а не agent paper. Его полезно читать как source of benchmark context: что именно измеряет MATH, почему он сложен и какие assumptions baked into its task construction.

## На какие вопросы источник помогает отвечать
- Что именно benchmark `MATH` пытается измерять?
- Почему competition-style math tasks отличаются от ordinary QA?
- Как topic mix and difficulty profile влияют на usefulness tools and scaffolding?
- Что меняется, когда из `MATH` берут subsets вроде `MATH-500`?

## Краткое содержание
Статья представляет `MATH` как benchmark для challenging mathematical reasoning, где ответы требуют не только знания фактов, но и многошагового решения. Авторы обсуждают construction dataset, diversity of topics и difficulty relative to competition-style math. Для week-04 текст полезен в первую очередь не детальной empirical частью, а тем, что он объясняет природу benchmark, который затем используется в notebook через subset `MATH-500`.

## Как читать источник быстро
- Если нужен benchmark context only, читай dataset motivation plus discussion of topic diversity and difficulty.
- Если вопрос про relevance to agents, смотри, почему exact-answer math tasks still demand multi-step reasoning.
- Если нужен bridge to the notebook, держи в фокусе how subset choice changes what the eval is really measuring.

## Что источник утверждает прямо
- `MATH` benchmark ориентирован на competition-style multi-step mathematical reasoning, а не на ordinary fact lookup or short-form QA.
- Topic mix and difficulty structure matter for what exactly the benchmark reveals about a model or agent.
- Exact-answer scoring упрощает verification, but does not capture the full reasoning process.
- Subset choice вроде `MATH-500` already changes the distribution of tasks and therefore the scope of the claim.

## Что здесь особенно важно
- **Math benchmark** не эквивалентен simple exact-answer QA.
- **Difficulty and subject mix** влияют на то, что именно model or agent должен уметь.
- **Subset usage** вроде `MATH-500` — это уже design choice, а не нейтральная данность.

## Интерпретация для курса
Для курса эта страница полезна как benchmark-context layer под notebook. Она напоминает, что даже когда practical exercise выглядит “просто как agent solves math”, под ним уже лежит конкретная benchmark construction with its own subject mix, scoring assumptions and subset choices.

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
