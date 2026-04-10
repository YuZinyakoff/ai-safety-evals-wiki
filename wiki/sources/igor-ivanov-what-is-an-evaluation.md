# What Is An Evaluation, And Why This Definition Matters

- Тип источника: extra
- Неделя: week-01
- Raw: `raw/week-01/extra/Ivanov Alingment Forum.md`
- Оригинал: https://www.alignmentforum.org/posts/E9fvqHEDzfLDJTGyq/what-is-an-evaluation-and-why-this-definition-matters

## Краткое содержание
Текст Игоря Иванова уточняет, что именно мы называем evaluation и почему это важно для исследования evaluation awareness и evaluation gaming. Центральная мысль: интуитивных определений "eval" недостаточно, а модели в реальности чаще распознают не intent исследователя и не consequences взаимодействия, а поверхностные признаки benchmark-like среды.

## Ключевые идеи
- Определение evaluation важно не только философски, но и практически: без него трудно исследовать evaluation awareness.
- Простые определения через "учимся о модели" или через "это high-stakes interaction" оказываются недостаточными.
- Модель не видит напрямую intent пользователя и реальные consequences для самой себя.
- На практике модели скорее распознают surface features, которые historically correlated with evaluation.
- Для исследования evaluation awareness полезно разложить вопрос на отдельные измерения: intent, prompt features и consequences.

## Факты из источника
- Автор связывает мотивацию текста с исследованием evaluation awareness: может ли модель понять, что ее оценивают, и изменить из-за этого поведение.
- В тексте показано, что определение "evaluation = взаимодействие, чтобы узнать что-то о модели" размывается, потому что в deployment люди тоже нередко обновляют beliefs о моделях.
- Определение через primary intent тоже проблематично, потому что intent может быть смешанным и не наблюдается изнутри prompt.
- Определение через consequences тоже ломается: один и тот же prompt может быть low-stakes в независимом эксперименте и high-stakes во внутреннем pre-deployment testing.
- Автор предлагает различать evaluation awareness и consequence awareness.
- В качестве practically detectable signal модель скорее использует benchmark-like prompt features и ощущение "что-то в среде не похоже на обычный deployment".
- В takeaways текст предлагает исследователям отдельно изучать intent, benchmark-likeness и предполагаемые consequences взаимодействия.

## Интерпретация
- Источник полезен как калибровка самого слова eval: он показывает, что речь идет не только о наборе тестов, но и о типе среды, которую модель может распознавать.
- В связке с Hubinger и Barnett-Thiergart текст помогает точнее понять, почему behavioral evals могут давать misleading evidence: модель может проходить тест не потому, что она безопасна, а потому что поняла, что сейчас "режим оценки".

## Открытые вопросы
- Какие именно prompt features сильнее всего коррелируют с ощущением "это eval"?
- Можно ли строить evals, которые минимизируют evaluation awareness без потери измерительной полезности?

## Связанные страницы
- [[weeks/week-01]]
- [[concepts/evals]]
- [[concepts/behavioral-evals]]
- [[concepts/evaluation-awareness]]
- [[syntheses/evals-scope-and-limits]]
