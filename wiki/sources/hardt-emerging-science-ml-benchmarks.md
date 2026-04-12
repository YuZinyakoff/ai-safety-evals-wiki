# The Emerging Science Of Machine Learning Benchmarks

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/The Emerging Science of Machine Learning Benchmarks.md>)
- **Оригинал:** [SIAM News](https://www.siam.org/publications/siam-news/articles/the-emerging-science-of-machine-learning-benchmarks/)
- **Полнота raw:** clipped Markdown

## Ключевая мысль
> **Исторически benchmarks работали не потому, что были безупречны как measurement devices, а потому, что долго сохраняли полезный порядок моделей.** В LLM era именно эта опора начинает ломаться.

## Зачем источник в базе
Это короткий, но очень полезный meta-text к обязательной части недели. Он нужен, чтобы вывести разговор из режима “benchmark'и плохие” в более интересный режим: “почему они вообще когда-то работали и что именно перестает работать сейчас”.

## Краткое содержание
Hardt начинает с очевидной критики benchmark'ов: narrow objectives, gaming, overfitting, weak transfer и ethical problems. Затем он задает более непривычный вопрос — в чем вообще был scientific case for benchmarks — и отвечает на него историческим наблюдением: такие benchmarks, как CIFAR-10 и ImageNet, долго давали surprisingly stable model rankings, а именно rankings, а не absolute scores, и были их главным scientific export. После этого текст переходит к LLM era и показывает, почему старая стабильность исчезает: training data uncontrollable, multitask aggregation нестабильна из-за social-choice-like trade-offs, а `LLM-as-a-judge` не снимает проблему на evaluation frontier. В финале автор призывает не выбрасывать benchmark'и, а строить более зрелую science of benchmarks.

## Что здесь особенно важно
- **Rankings**, а не raw scores, были реальным экспортом старых benchmark regimes.
- **Data contamination** подрывает validity model comparisons.
- **Multi-task aggregation** в LLM era создает новые structural instabilities.
- **Judge-based evaluation** не решает frontier problem.

## Что это добавляет к теме недели
Этот текст связывает week-03 с более широкой историей ML benchmarking. Он помогает увидеть, что текущие проблемы benchmark design не случайны и не сводятся к одной области: меняется сама природа benchmark evidence в эпоху large models.

## Что стоит запомнить при повторении
- **Benchmarks “worked” исторически, но не так, как часто рассказывают.**
- **LLM era бьет именно по ranking stability, contamination control и evaluation frontier.**
- **Нужна не отмена benchmark'ов, а более сильная benchmark science.**

## Связанные концепты
- [concepts/benchmark-lottery](../concepts/benchmark-lottery.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Можно ли найти новый источник ranking stability в LLM era или нужно пересобирать идею benchmark'а радикальнее?
- Какие benchmark properties реально стоит считать фундаментальными для “науки benchmark'ов”, а какие зависят от конкретной технологической эпохи?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/benchmark-lottery](benchmark-lottery.md)
- [sources/limits-scalable-evaluation-frontier](limits-scalable-evaluation-frontier.md)
