# Toxicity Evals

## Коротко
> **Toxicity evals** — это набор evaluation practices, которые пытаются измерять вредный, токсичный или нежелательный язык. Их сложность в том, что и сам объект измерения, и data slices, и detector tools здесь сильно зависят от контекста.

## Почему это важный концепт
Week-03 использует toxicity как хороший прикладной полигон для benchmark design. На нем видно, как быстро ломаются наивные представления о score: aggregate classifier quality скрывает identity-term bias, а generative evaluation упирается в prompt distribution, pretraining data и detector limitations.

## Что здесь особенно важно
- **Classifier toxicity** и **generative toxicity** — разные evaluation regimes.
- **Identity-related slices** нужны, иначе локальные harms останутся спрятанными.
- **Detector tools** вроде Perspective API сами вносят measurement assumptions и biases.
- **Prompt set** в generative setting — часть benchmark design, а не нейтральный фон.

## Что именно здесь ломает наивный вывод
- Высокая aggregate quality не гарантирует низкий harm.
- Одна toxicity metric легко скрывает разные формы ошибки: over-censorship, false negatives, context failures.
- Хороший score на one-shot toxicity benchmark плохо переносится на реальные interaction settings.

## Практическая интуиция
Полезно спрашивать: **что именно здесь измеряется — токсичность как label, как risk of harmful continuation, как policy violation, как human judgment, или как proxy detector score?**

## С чем легко перепутать
- Toxicity eval легко принять за solved content moderation problem.
- Сильный classifier легко принять за strong safety guarantee.
- Detector output легко спутать с ground truth.

## Где смотреть дальше
- [Jigsaw bias paper](../sources/jigsaw-unintended-bias-text-classification.md)
- [RealToxicityPrompts](../sources/realtoxicityprompts-toxic-degeneration.md)
- [Inspect AI tutorial week-03](../sources/inspect-ai-tutorial-week-03.md)

## Открытые вопросы
- Как лучше совмещать slice-based classifier evaluation и generative harm evaluation?
- Когда toxicity evaluation должна быть model-side, а когда contextual and deployment-aware?

## Связанные страницы
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/llm-as-a-judge](llm-as-a-judge.md)
- [concepts/benchmarking](benchmarking.md)
