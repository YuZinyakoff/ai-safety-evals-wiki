# Measuring And Mitigating Unintended Bias In Text Classification

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [PDF](<../../raw/week-03/extra/4578.pdf>), [fallback `.pdf.md`](<../../raw/week-03/extra/4578.pdf.md>)
- **Оригинал:** [Google Research](https://research.google/pubs/measuring-and-mitigating-unintended-bias-in-text-classification/)
- **Полнота raw:** PDF и fallback extracted Markdown

## Ключевая мысль
> **Классификатор может выглядеть сильным по общей метрике и одновременно систематически ошибаться на comments с определенными identity terms.**

## Зачем источник в базе
Это прямое дополнение к notebook недели. Источник нужен, чтобы разговор о toxicity evaluation не сводился к одной aggregate accuracy и чтобы было понятно, как именно возникают false positives и unwanted censorship effects на identity-related examples.

## Краткое содержание
Статья вводит понятие `unintended bias` в контексте text classification и сразу отделяет его от более широкой социальной проблемы fairness. Затем авторы разбирают конкретный кейс: toxicity classifier на Wikipedia Talk data начал переассоциировать отдельные identity terms вроде “gay” с toxicity, потому что в training data эти terms были непропорционально представлены в toxic comments. После постановки проблемы paper предлагает способ измерять bias на специальных slices и сравнивать поведение модели на identity-related examples с общим quality level. Далее работа показывает простой mitigation path через балансировку данных и добавление strategically chosen examples. В финале paper проверяет, что bias mitigation действительно уменьшает unintended bias without collapsing overall model quality.

## Что здесь особенно важно
- **Aggregate performance** может скрывать серьезные локальные failure modes.
- **Identity-term imbalance** в training data быстро превращается в false positive bias.
- **Mitigation** здесь понимается как изменение training distribution, а не только косметическая post-hoc correction.
- **Bias measurement** требует смотреть на специальные slices, а не только на весь test set целиком.

## Что это добавляет к теме недели
Этот текст связывает benchmark design с содержательной конструкцией test slices. Он показывает, что даже когда мы вроде бы “меряем токсичность”, benchmark choice все равно решает, какие harms станут видимыми, а какие останутся спрятанными за общей метрикой. Для week-03 это хороший прикладной пример того, как design benchmark'а влияет на смысл результата.

## Что стоит запомнить при повторении
- **Сильный classifier** не значит **равномерно надежный classifier**.
- **Bias slices** нужны не как бонус, а как часть осмысленного evaluation design.
- **Mitigation** без измерения локальных failure modes почти неизбежно слепа.

## Связанные концепты
- [concepts/toxicity-evals](../concepts/toxicity-evals.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Насколько методы такого bias mitigation переносятся с classifier settings на generative toxicity settings?
- Где проходит граница между model bias, dataset bias и mismatch between evaluation slice and deployment context?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/realtoxicityprompts-toxic-degeneration](realtoxicityprompts-toxic-degeneration.md)
- [sources/inspect-ai-tutorial-week-03](inspect-ai-tutorial-week-03.md)
