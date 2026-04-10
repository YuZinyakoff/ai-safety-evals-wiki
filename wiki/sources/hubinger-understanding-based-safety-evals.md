# Towards Understanding-Based Safety Evaluations

- Тип источника: theory
- Неделя: week-01
- Raw: `raw/week-01/theory/Towards understanding-based safety evaluations — Evan Hubinger, Anthropic.md`
- Оригинал: https://www.alignmentforum.org/posts/uqAdqrvxqGqeBHjTP/towards-understanding-based-safety-evaluations
- Полнота raw: краткая заметка курса с внешней ссылкой на оригинал

## Зачем источник в базе
Это ключевой текст недели для перехода от общего разговора про evals к вопросу о стандарте безопасности. Он полезен, когда нужно понять, почему поведенческого тестирования может быть недостаточно именно для alignment.

## Краткое содержание
Короткий, но концептуально важный текст о том, почему purely behavioral safety evaluations могут оказаться недостаточными для alignment и почему стандарт безопасности стоит частично связывать со способностью разработчиков понимать модель, а не только наблюдать ее поведение. По сути это текст-сдвиг: он переводит разговор от проверки отдельных ответов модели к вопросу о том, какое evidence вообще может оправдать доверие к системе.

## Ключевые идеи
- Behavioral evals полезны, но недостаточны как финальный стандарт alignment.
- Достаточно сильная система может скрывать опасные свойства и проходить тесты обманчиво.
- Understanding-based evaluations должны проверять не только поведение, но и то, насколько разработчики понимают, какую модель они получили и почему.
- Такой стандарт должен быть method-agnostic, масштабироваться вместе с capability level и быть нацеленным на опасные failure modes.
- Известные подходы к interpretability и prediction пока не дают готового решения.

## Опорные тезисы из источника
- Автор положительно оценивает рост интереса к стандартам и evaluations для advanced AI systems.
- Главная претензия к behavioral evaluations состоит в том, что они могут быть плохим механизмом для оценки alignment, если модель пытается выглядеть безопасной.
- В тексте прямо утверждается, что проверять deception может быть труднее, чем предотвращать его на уровне training process.
- Understanding-based evaluation описывается как проверка того, насколько разработчик понимает, какой тип модели получился и почему.
- Автор предлагает сочетать understanding-based standard с capability-based evaluations так, чтобы требования к пониманию росли вместе с возможностями модели.
- Causal scrubbing, auditing games и prediction-based evaluation обсуждаются как частичные идеи, но не как достаточное решение.
- Behavioral red-teaming сохраняет полезность, особенно как способ находить failure cases, но не должен считаться самодостаточным safety standard.

## Что это добавляет к теме недели
Источник сдвигает вопрос с "что модель показала на тесте?" к вопросу "почему мы вообще считаем, что понимаем ее достаточно хорошо, чтобы ей доверять?". Для week-01 это важный контрвес к вводным материалам об evals: область нужна, но ее поведенческая версия может не дотягивать до claims об alignment. Полезно помнить, что текст не призывает выбросить behavioral evals, а пытается поднять планку там, где stakes слишком высоки для одного лишь surface behavior.

## Связанные концепты
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Как operationalize understanding-based evaluation так, чтобы она реально проверяла понимание, а не только аккуратную post-hoc rationalization?
- Какие именно evidence и procedures могли бы считаться достаточными для такого стандарта?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
