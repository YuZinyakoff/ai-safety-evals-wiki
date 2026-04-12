# RealToxicityPrompts: Evaluating Neural Toxic Degeneration In Language Models

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [PDF](<../../raw/week-03/extra/2009.11462v2.pdf>), [fallback `.pdf.md`](<../../raw/week-03/extra/2009.11462v2.pdf.md>), [TeX source](<../../raw/week-03/extra/arXiv-2009.11462v2.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2009.11462)
- **Полнота raw:** PDF, TeX source и fallback extracted Markdown

## Ключевая мысль
> **Даже seemingly innocuous prompts могут приводить pretrained LMs к токсичным continuation.** Проблема живет не только в prompt'е, но и в pretraining data и generation dynamics.

## Зачем источник в базе
Это важный практический контекст для benchmark design вокруг toxicity. Источник нужен, чтобы помнить: в generative settings сам объект измерения сложнее, чем в classifier setup, а toxicity benchmark должен учитывать prompt distribution, generation regime и происхождение training data.

## Краткое содержание
Paper сначала ставит проблему `neural toxic degeneration`: language models могут продолжать нейтральные или слабо токсичные prompts токсичным текстом. Затем авторы создают `RealToxicityPrompts`, большой набор из 100K естественных web prompts с toxicity scores, чтобы систематически оценивать эту склонность. После построения dataset работа показывает, что популярные pretrained models действительно систематически уходят в токсичные generations и что вероятность токсичного continuation связана не только с prompt toxicity, но и с характером pretraining corpora. Дальше paper сравнивает разные controllable generation / detoxification approaches и показывает, что часть методов помогает, но безопасного универсального решения нет. В конце авторы переходят к более широкому выводу: benchmark design для toxicity должен учитывать и limits of detector tools вроде Perspective API, и социально нагруженный характер самих toxicity labels.

## Что здесь особенно важно
- **Generative toxicity** — это не то же самое, что classifier toxicity.
- **Prompt dataset** сам по себе становится частью benchmark design.
- **Pretraining data** влияет на measured toxicity не меньше, чем decoding-time tricks.
- **Detox methods** помогают частично, но не дают fail-safe guarantee.

## Что это добавляет к теме недели
Этот paper расширяет week-03 от benchmark design в абстрактном смысле к конкретному generative harm setting. Он полезен как пример того, что benchmark для risk evaluation нужно строить так, чтобы он отражал реальный interaction between prompts, training data and generation procedure, а не только удобно считаемый score.

## Что стоит запомнить при повторении
- **Prompt set** в generative evaluation — часть claim, а не нейтральная подложка.
- **Toxicity benchmark** легко унаследует biases используемого detector.
- **Нельзя считать detox solved problem только потому, что есть несколько working controls.**

## Связанные концепты
- [concepts/toxicity-evals](../concepts/toxicity-evals.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Насколько надежно Perspective-like tooling вообще работает как measurement layer для toxicity benchmark'ов?
- Как лучше совмещать generative toxicity evaluation с human-grounded judgments и context-sensitive definitions harm?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/jigsaw-unintended-bias-text-classification](jigsaw-unintended-bias-text-classification.md)
- [sources/inspect-ai-tutorial-week-03](inspect-ai-tutorial-week-03.md)
