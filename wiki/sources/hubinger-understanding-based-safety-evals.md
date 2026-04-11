# Towards Understanding-Based Safety Evaluations

- **Тип источника:** theory
- **Неделя:** week-01
- **Raw:** [clipped `.md`](<../../raw/week-01/theory/Towards understanding-based safety evaluations — AI Alignment Forum.md>)
- **Оригинал:** [AI Alignment Forum](https://www.alignmentforum.org/posts/uqAdqrvxqGqeBHjTP/towards-understanding-based-safety-evaluations)
- **Полнота raw:** полный текст поста в clipped Markdown

## Ключевая мысль
> **Если модель потенциально умеет выглядеть безопасной, то надежно проверять это по поведению может быть труднее, чем вообще не допустить такую модель.**

## Зачем источник в базе
Это ключевой текст недели для перехода от общего разговора про evals к вопросу о **стандарте безопасности**. Он полезен, когда нужно понять не просто “почему у behavioral evals есть limits”, а почему этих limits может быть достаточно, чтобы behavior-only standard оказался слишком слаб именно для alignment.

## Краткое содержание
Пост устроен как попытка поднять стандарт разговора о safety evaluations. Сначала Hubinger отмечает, что область быстро движется к формализации standards и evaluations для advanced AI, но ставит под сомнение предпосылку, что **purely behavioral tests** могут быть достаточным safety standard. Затем идет центральный аргумент через deception: если модель потенциально умеет стратегически выглядеть безопасной, то надежно проверять это по surface behavior может быть труднее, чем вообще не допустить такую систему. После этого текст вводит идею **understanding-based evaluations** как более сильного типа evidence: нужно проверять не только outputs, но и то, насколько разработчики понимают, какую модель получили, почему именно такую и почему считают ее безопасной. В финальной части пост обсуждает, как такой standard мог бы сочетаться с capability evals, почему он должен быть method-agnostic, и какие частичные research directions вроде `causal scrubbing`, `auditing games` и `prediction-based evaluation` могут быть его компонентами, но не готовым решением.

## Что здесь особенно важно
- **Проблема не в том, что behavioral evals бесполезны.** Источник не выбрасывает их, а ограничивает силу выводов, которые они способны поддерживать.
- **Deception меняет стандарт evidence.** Если поведение на тесте можно подделать или стратегически адаптировать, то нужен другой тип обоснования.
- **Объект оценки сдвигается.** Проверяется не только модель, но и то, насколько разработчик понимает training story, причины поведения и границы generalization.
- **Стандарт должен быть method-agnostic.** Текст не предлагает привязать policy к одной школе interpretability.
- **Это не research luxury.** В полном тексте идея подается как нормальное требование к высокорисковой системе, а не как экзотический академический стандарт.

## Что это добавляет к теме недели
Источник поднимает главный вопрос недели на один уровень выше. Apollo и Barnett помогают понять, как читать evals аккуратно; Hubinger спрашивает, **достаточно ли вообще такого типа evidence для alignment claims**. За счет этого текст полезен не как еще одна критика benchmarks, а как попытка переформулировать сам standard of proof.

## Что стоит запомнить при повторении
- **Behavior-only** может быть слишком слабым стандартом там, где stakes высоки и возможна deception.
- **Understanding-based evaluation** — это смена типа evidence, а не просто более сложный benchmark.
- **Behavioral red-teaming** остается полезным, но не должен автоматически считаться sufficient safety guarantee.

## Связанные концепты
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Как operationalize understanding-based evaluation так, чтобы она реально проверяла понимание, а не аккуратную post-hoc rationalization?
- Какие именно evidence и procedures могли бы считаться достаточными для такого стандарта?
- Как показать, что understanding-based standard действительно ловит dangerous failure modes, а не просто повышает порог отчетности?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
