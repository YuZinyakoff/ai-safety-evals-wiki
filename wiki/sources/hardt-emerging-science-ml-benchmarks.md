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

## Эпистемический статус и как на него смотреть
Это short meta-essay, а не empirical survey or benchmark paper. Его полезно читать как исторически informed commentary про то, какой scientific export benchmarks реально давали раньше и почему этот механизм ломается в LLM era.

## На какие вопросы источник помогает отвечать
- Почему старые benchmark regimes вообще работали достаточно хорошо для науки?
- Почему `rankings`, а не raw scores, были их главным epistemic output?
- Что в LLM era ломает ranking stability and contamination control?
- Почему автор говорит о необходимости `science of benchmarks`, а не просто о смерти benchmark'ов?

## Краткое содержание
Hardt начинает с очевидной критики benchmark'ов: narrow objectives, gaming, overfitting, weak transfer и ethical problems. Затем он задает более непривычный вопрос — в чем вообще был scientific case for benchmarks — и отвечает на него историческим наблюдением: такие benchmarks, как CIFAR-10 и ImageNet, долго давали surprisingly stable model rankings, а именно rankings, а не absolute scores, и были их главным scientific export. После этого текст переходит к LLM era и показывает, почему старая стабильность исчезает: training data uncontrollable, multitask aggregation нестабильна из-за social-choice-like trade-offs, а `LLM-as-a-judge` не снимает проблему на evaluation frontier. В финале автор призывает не выбрасывать benchmark'и, а строить более зрелую science of benchmarks.

## Как читать источник быстро
- Если нужен one-shot takeaway, читай historical argument about why benchmarks once worked and the contrast with the LLM era.
- Если интересует failure mode, концентрируйся на ranking stability, contamination and multitask aggregation.
- Если нужен broader relevance, не пропускай closing call for a more mature science of benchmarks.

## Что источник утверждает прямо
- Историческая usefulness benchmark'ов частично объяснялась тем, что они долго давали относительно стабильные model rankings, even when absolute scores were less meaningful.
- В LLM era эта ranking stability ломается из-за contamination, weak control over training data и нестабильного multi-task aggregation.
- `LLM-as-a-judge` не устраняет автоматически проблему evaluation at the frontier, потому что сам judge встроен в ту же нестабильную среду.
- Автор призывает не выбрасывать benchmark'и, а строить более зрелую `science of benchmarks`.

## Что здесь особенно важно
- **Rankings**, а не raw scores, были реальным экспортом старых benchmark regimes.
- **Data contamination** подрывает validity model comparisons.
- **Multi-task aggregation** в LLM era создает новые structural instabilities.
- **Judge-based evaluation** не решает frontier problem.

## Интерпретация для курса
Для курса этот текст важен как исторический corrective. Он помогает читать кризис benchmark'ов не как внезапную моду на критику, а как изменение того, какой эпистемический продукт benchmark вообще когда-то давал и почему этот продукт хуже переносится в LLM era.

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
