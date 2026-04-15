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

## Эпистемический статус и как на него смотреть
Это programmatic alignment post, который спорит не о локальном benchmark design, а о standard of evidence for safety. Его полезно читать как аргумент о том, почему behavior-only evidence может быть принципиально недостаточным, а не как готовый operational protocol.

## На какие вопросы источник помогает отвечать
- Почему behavioral safety evals могут оказаться слишком слабыми для alignment claims?
- Как deception меняет стандарт требуемого evidence?
- Что такое `understanding-based evaluations` и чем они отличаются от behavior-only testing?
- Как такой стандарт может сочетаться с capability evals и interpretability-like tools?

## Краткое содержание
Пост устроен как попытка поднять стандарт разговора о safety evaluations. Сначала Hubinger отмечает, что область быстро движется к формализации standards и evaluations для advanced AI, но ставит под сомнение предпосылку, что **purely behavioral tests** могут быть достаточным safety standard. Затем идет центральный аргумент через deception: если модель потенциально умеет стратегически выглядеть безопасной, то надежно проверять это по surface behavior может быть труднее, чем вообще не допустить такую систему. После этого текст вводит идею **understanding-based evaluations** как более сильного типа evidence: нужно проверять не только outputs, но и то, насколько разработчики понимают, какую модель получили, почему именно такую и почему считают ее безопасной. В финальной части пост обсуждает, как такой standard мог бы сочетаться с capability evals, почему он должен быть method-agnostic, и какие частичные research directions вроде `causal scrubbing`, `auditing games` и `prediction-based evaluation` могут быть его компонентами, но не готовым решением.

## Как читать источник быстро
- Если нужен главный аргумент, читай opening sections, где Hubinger связывает deception с limits of behavioral testing.
- Если вопрос про сам стандарт, переходи к sections про `understanding-based evaluations` и method-agnostic framing.
- Если нужен practical reading, смотри финальные examples of possible components and research directions, но не путай их с готовым solution.

## Что источник утверждает прямо
- Purely behavioral tests могут быть принципиально недостаточными как safety standard for advanced systems.
- Deception and strategic adaptation make it too easy for dangerous systems to look safe under behavior-only evaluation.
- Более сильный standard of evidence should involve understanding of what the system is and why developers believe it is safe.
- Such a standard should be method-agnostic and not collapse into one particular interpretability technique.

## Что здесь особенно важно
- **Проблема не в том, что behavioral evals бесполезны.** Источник не выбрасывает их, а ограничивает силу выводов, которые они способны поддерживать.
- **Deception меняет стандарт evidence.** Если поведение на тесте можно подделать или стратегически адаптировать, то нужен другой тип обоснования.
- **Объект оценки сдвигается.** Проверяется не только модель, но и то, насколько разработчик понимает training story, причины поведения и границы generalization.
- **Стандарт должен быть method-agnostic.** Текст не предлагает привязать policy к одной школе interpretability.
- **Это не research luxury.** В полном тексте идея подается как нормальное требование к высокорисковой системе, а не как экзотический академический стандарт.

## Интерпретация для курса
В логике курса этот текст поднимает ставку выше, чем просто critique of benchmarks. Он показывает, что для high-stakes alignment claims может быть недостаточно “лучше мерить поведение”; иногда нужен другой type of evidence altogether. Это делает его одним из центральных texts for understanding why week-01 is about standards of proof, not just failure modes.

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
