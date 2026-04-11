# What Is An Evaluation, And Why This Definition Matters

- **Тип источника:** extra
- **Неделя:** week-01
- **Raw:** [clipped `.md`](<../../raw/week-01/extra/What is an evaluation, and why this definition matters — AI Alignment Forum.md>)
- **Оригинал:** [AI Alignment Forum](https://www.alignmentforum.org/posts/E9fvqHEDzfLDJTGyq/what-is-an-evaluation-and-why-this-definition-matters)
- **Полнота raw:** полный текст поста в clipped Markdown

## Ключевая мысль
> **Проблема “evaluation awareness” начинается раньше, чем кажется: сначала нужно вообще понять, что именно считать evaluation и какие признаки этого реально доступны модели.**

## Зачем источник в базе
Этот текст нужен, чтобы не обращаться со словом `evaluation` слишком свободно. Он полезен как точка, где неделя перестает быть только про benchmarks и начинает обсуждать, **что именно модель может распознавать в eval-like context**.

## Краткое содержание
Текст построен как последовательный разбор нескольких интуитивных определений слова `evaluation`. Сначала Иванов рассматривает идею “evaluation — это взаимодействие, в котором мы хотим что-то узнать о модели”, затем более узкую версию через **primary intent**, а потом еще одну линию через **consequences** для модели или разработчиков. Для каждого варианта автор показывает, почему он плохо работает как operational definition: люди и в deployment тоже обновляют beliefs о моделях, `intent` смешан и плохо читается из prompt, а последствия могут радикально различаться при одном и том же surface interaction. На этом фоне пост предлагает более полезное разложение проблемы на несколько осей — `intent`, `benchmark-likeness` и `consequences` — и отдельно различает `evaluation awareness` и `consequence awareness`. Итоговый вывод специально сделан приземленным: современные модели, вероятно, распознают не абстрактную “сущность оценки”, а набор surface features, historically correlated with benchmark-like or unusual environments.

## Что здесь особенно важно
- **Определение влияет на исследование.** Пока неясно, что такое evaluation, трудно и говорить об `evaluation awareness`.
- **`Intent`, `benchmark-likeness` и `consequences` — разные оси.** Их полезно не смешивать.
- **Модель не обязана читать человеческие намерения.** Ей может хватать более простых статистических признаков среды.
- **Нужно различать `evaluation awareness` и `consequence awareness`.** Это один из самых полезных anchors текста.
- **Текст очищает терминологию.** Он полезен не за счет нового benchmark, а за счет того, что делает разговор про awareness более точным.

## Что это добавляет к теме недели
Этот источник превращает общий скепсис недели в более конкретный механизм ошибки. После него “behavior on eval may be misleading” уже не звучит мистически: становится понятно, что модель может реагировать на узнаваемый формат, а не на реальную safety-critical суть ситуации. В этом смысле текст очень хорошо связывает Hubinger, Barnett и prompt-level failure modes.

## Что стоит запомнить при повторении
- **Evaluation** — не простой наблюдаемый примитив.
- **Benchmark-likeness** часто practically detectable лучше, чем `intent` или реальные `consequences`.
- **Awareness problems** начинаются не с большой философии, а с неправильно выбранной operational definition.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Какие именно prompt features сильнее всего коррелируют с ощущением “это eval”?
- Можно ли строить evals, которые минимизируют evaluation awareness без потери измерительной полезности?
- Где проходит практическая граница между `benchmark-likeness` и `consequence awareness` для frontier models?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
