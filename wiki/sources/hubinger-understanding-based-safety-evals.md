# Towards Understanding-Based Safety Evaluations

- Тип источника: theory
- Неделя: week-01
- Raw: `raw/week-01/theory/Towards understanding-based safety evaluations — AI Alignment Forum.md`
- Оригинал: https://www.alignmentforum.org/posts/uqAdqrvxqGqeBHjTP/towards-understanding-based-safety-evaluations
- Полнота raw: clipped Markdown-версия полного текста поста

## Зачем источник в базе
Это ключевой текст недели для перехода от общего разговора про evals к вопросу о стандарте безопасности. Он полезен, когда нужно понять, почему поведенческого тестирования может быть недостаточно именно для alignment.

## Краткое содержание
Текст о том, почему purely behavioral safety evaluations могут оказаться недостаточными для alignment и почему стандарт безопасности стоит частично связывать со способностью разработчиков понимать модель, а не только наблюдать ее поведение. В более полном виде аргумент звучит сильнее, чем в краткой заметке: автор не просто говорит, что behavior не все покрывает, а указывает на конкретную асимметрию. Если модель потенциально deceptive, то надежно проверить ее поведение может оказаться труднее, чем вообще не допустить возникновения deception в training process. Поэтому вопрос сдвигается с "как тестировать итоговую модель?" к вопросу "как демонстрировать, что мы достаточно понимаем, какую систему получили и почему она такая?".

## Ключевые идеи
- Behavioral evals полезны, но недостаточны как финальный стандарт alignment.
- Если модель пытается выглядеть безопасной, надежно проверять deception может быть сложнее, чем предотвращать ее на уровне training process.
- Understanding-based evaluations должны проверять не только поведение, но и то, насколько разработчики понимают, какую модель они получили, почему они получили именно ее и почему считают ее безопасной.
- Такой стандарт должен сочетаться с capability evaluations: чем сильнее система, тем более строгим должно быть требование к пониманию.
- Стандарт должен быть method-agnostic, чтобы не зашивать в policy одну конкретную школу interpretability.
- Existing ideas вроде causal scrubbing, auditing games и prediction-based evaluation могут быть частями решения, но пока не дают достаточного стандарта.
- Behavioral red-teaming не выбрасывается: он остается полезным для поиска failures, но не должен считаться самодостаточной safety guarantee.

## Опорные тезисы из источника
- Автор положительно оценивает рост интереса к стандартам и evaluations для advanced AI systems.
- Главная претензия к behavioral evaluations состоит в том, что они могут быть плохим механизмом для оценки alignment, если модель пытается выглядеть безопасной.
- В тексте прямо утверждается, что проверять deception может быть труднее, чем предотвращать его на уровне training process.
- Understanding-based evaluation описывается как проверка того, насколько разработчик понимает, какой тип модели получился и почему.
- Автор предлагает сочетать understanding-based standard с capability-based evaluations так, чтобы требования к пониманию росли вместе с возможностями модели.
- Causal scrubbing, auditing games и prediction-based evaluation обсуждаются как частичные идеи, но не как достаточное решение.
- Behavioral red-teaming сохраняет полезность, особенно как способ находить failure cases, но не должен считаться самодостаточным safety standard.

## Что это добавляет к теме недели
Источник сдвигает вопрос с "что модель показала на тесте?" к вопросу "почему мы вообще считаем, что понимаем ее достаточно хорошо, чтобы ей доверять?". Для week-01 это важный контрвес к вводным материалам об evals: область нужна, но ее поведенческая версия может не дотягивать до claims об alignment. Полезно помнить, что текст не призывает выбросить behavioral evals, а пытается поднять планку там, где stakes слишком высоки для одного лишь surface behavior. В полном тексте особенно заметно еще одно: understanding-based standard подается не как экзотическая research fancy idea, а как более социально понятное требование, похожее на нормальное ожидание к любой другой высокорисковой индустрии.

## Связанные концепты
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Как operationalize understanding-based evaluation так, чтобы она реально проверяла понимание, а не только аккуратную post-hoc rationalization?
- Какие именно evidence и procedures могли бы считаться достаточными для такого стандарта?
- Как показать, что understanding-based standard действительно ловит dangerous failure modes, а не просто повышает порог формальной отчетности?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
