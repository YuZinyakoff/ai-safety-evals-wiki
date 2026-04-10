# What Is An Evaluation, And Why This Definition Matters

- Тип источника: extra
- Неделя: week-01
- Raw: `raw/week-01/extra/Ivanov Alingment Forum.md`
- Оригинал: https://www.alignmentforum.org/posts/E9fvqHEDzfLDJTGyq/what-is-an-evaluation-and-why-this-definition-matters
- Полнота raw: краткая заметка курса с внешней ссылкой на оригинал

## Зачем источник в базе
Этот текст нужен, чтобы не обращаться со словом "evaluation" слишком свободно. Он полезен как точка, где неделя перестает быть только про benchmarks и начинает обсуждать, что именно модель может распознавать в eval-like context.

## Краткое содержание
Текст Игоря Иванова уточняет, что именно мы называем evaluation и почему это важно для исследования evaluation awareness и evaluation gaming. Центральная мысль: интуитивных определений "eval" недостаточно, а модели в реальности чаще распознают не intent исследователя и не consequences взаимодействия, а поверхностные признаки benchmark-like среды. Это делает текст особенно полезным для перечитывания: он не столько добавляет новый benchmark, сколько очищает сами термины, которыми потом приходится пользоваться на других страницах.

## Ключевые идеи
- Определение evaluation важно не только философски, но и практически: без него трудно исследовать evaluation awareness.
- Простые определения через "учимся о модели" или через "это high-stakes interaction" оказываются недостаточными.
- Модель не видит напрямую intent пользователя и реальные consequences для самой себя.
- На практике модели скорее распознают surface features, которые historically correlated with evaluation.
- Для исследования evaluation awareness полезно разложить вопрос на отдельные измерения: intent, prompt features и consequences.

## Опорные тезисы из источника
- Автор связывает мотивацию текста с исследованием evaluation awareness: может ли модель понять, что ее оценивают, и изменить из-за этого поведение.
- В тексте показано, что определение "evaluation = взаимодействие, чтобы узнать что-то о модели" размывается, потому что в deployment люди тоже нередко обновляют beliefs о моделях.
- Определение через primary intent тоже проблематично, потому что intent может быть смешанным и не наблюдается изнутри prompt.
- Определение через consequences тоже ломается: один и тот же prompt может быть low-stakes в независимом эксперименте и high-stakes во внутреннем pre-deployment testing.
- Автор предлагает различать evaluation awareness и consequence awareness.
- В качестве practically detectable signal модель скорее использует benchmark-like prompt features и ощущение "что-то в среде не похоже на обычный deployment".
- В takeaways текст предлагает исследователям отдельно изучать intent, benchmark-likeness и предполагаемые consequences взаимодействия.

## Что это добавляет к теме недели
Источник полезен как калибровка самого слова eval: он показывает, что речь идет не только о наборе тестов, но и о типе среды, которую модель может распознавать. В связке с Hubinger и Barnett-Thiergart текст помогает точнее понять, почему behavioral evals могут давать misleading evidence: модель может проходить тест не потому, что она безопасна, а потому что поняла, что сейчас "режим оценки". Для week-01 это одна из страниц, которые превращают общий скепсис в более точный механизм ошибки.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Какие именно prompt features сильнее всего коррелируют с ощущением "это eval"?
- Можно ли строить evals, которые минимизируют evaluation awareness без потери измерительной полезности?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
