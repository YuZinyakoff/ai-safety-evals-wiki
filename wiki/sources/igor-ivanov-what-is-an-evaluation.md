# What Is An Evaluation, And Why This Definition Matters

- Тип источника: extra
- Неделя: week-01
- Raw: `raw/week-01/extra/What is an evaluation, and why this definition matters — AI Alignment Forum.md`
- Оригинал: https://www.alignmentforum.org/posts/E9fvqHEDzfLDJTGyq/what-is-an-evaluation-and-why-this-definition-matters
- Полнота raw: clipped Markdown-версия полного текста поста

## Зачем источник в базе
Этот текст нужен, чтобы не обращаться со словом "evaluation" слишком свободно. Он полезен как точка, где неделя перестает быть только про benchmarks и начинает обсуждать, что именно модель может распознавать в eval-like context.

## Краткое содержание
Текст Игоря Иванова уточняет, что именно мы называем evaluation и почему это важно для исследования evaluation awareness и evaluation gaming. В полном посте аргумент строится через последовательный разбор нескольких неудачных определений: "eval как способ узнать что-то о модели", "eval как primary intent исследователя", "eval как high-stakes interaction с последствиями для модели". Каждое из этих определений в чем-то полезно, но ломается как operational definition. В итоге источник приходит к более приземленному выводу: модели в реальности, вероятно, не видят ни intent пользователя, ни реальные consequences для себя, а скорее распознают prompt features и общее ощущение benchmark-like или "необычной" среды. Это делает текст особенно полезным для перечитывания: он не столько добавляет новый benchmark, сколько очищает сами термины, которыми потом приходится пользоваться на других страницах.

## Ключевые идеи
- Определение evaluation важно не только философски, но и практически: без него трудно исследовать evaluation awareness.
- Простые определения через "учимся о модели" или через "это high-stakes interaction" оказываются недостаточными.
- Модель не видит напрямую intent пользователя и реальные consequences для самой себя.
- Для разговора о detection полезно различать evaluation awareness и consequence awareness.
- На практике модели скорее распознают surface features, historically correlated with evaluation, и просто "ощущение", что среда не похожа на обычный deployment.
- Evaluation-like benchmark format не равен самой сущности evaluation, но может быть тем, что реально детектируется моделью.
- Для исследования evaluation awareness полезно разложить вопрос на отдельные измерения: intent, benchmark-likeness и consequences.

## Опорные тезисы из источника
- Автор связывает мотивацию текста с исследованием evaluation awareness: может ли модель понять, что ее оценивают, и изменить из-за этого поведение.
- В тексте показано, что определение "evaluation = взаимодействие, чтобы узнать что-то о модели" размывается, потому что в deployment люди тоже нередко обновляют beliefs о моделях.
- Определение через primary intent тоже проблематично, потому что intent может быть смешанным и не наблюдается изнутри prompt.
- Определение через consequences тоже ломается: один и тот же prompt может быть low-stakes в независимом эксперименте и high-stakes во внутреннем pre-deployment testing.
- Автор предлагает различать evaluation awareness и consequence awareness.
- В качестве practically detectable signal модель скорее использует benchmark-like prompt features и ощущение "что-то в среде не похоже на обычный deployment".
- В takeaways текст предлагает исследователям отдельно изучать intent, benchmark-likeness и предполагаемые consequences взаимодействия.

## Что это добавляет к теме недели
Источник полезен как калибровка самого слова eval: он показывает, что речь идет не только о наборе тестов, но и о типе среды, которую модель может распознавать. В связке с Hubinger и Barnett-Thiergart текст помогает точнее понять, почему behavioral evals могут давать misleading evidence: модель может проходить тест не потому, что она безопасна, а потому что поняла, что сейчас "режим оценки". Для week-01 это одна из страниц, которые превращают общий скепсис в более точный механизм ошибки. Особенно важно, что источник не мистифицирует problem setup: он предлагает смотреть не на абстрактный "eval", а на набор различимых признаков среды, из-за которых модель может изменить стратегию поведения.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)

## Что осталось неясным / спорным
- Какие именно prompt features сильнее всего коррелируют с ощущением "это eval"?
- Можно ли строить evals, которые минимизируют evaluation awareness без потери измерительной полезности?
- Где проходит практическая граница между benchmark-likeness и consequence awareness для современных frontier models?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
