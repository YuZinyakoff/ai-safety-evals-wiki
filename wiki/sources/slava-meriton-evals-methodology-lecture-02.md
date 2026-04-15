# Проблема Методологии Evals в Контексте AI Safety — Лекция 2

- **Тип источника:** extra
- **Неделя:** shared
- **Raw:** [`.pptx`](<../../raw/shared/Проблемы методолгии в эвалс 2.pptx>), [sidecar `.md`](<../../raw/shared/Проблемы методолгии в эвалс 2.pptx.md>)
- **Полнота raw:** `.pptx` + generated Markdown sidecar; для слайдового формата структура в целом сохранена

## Ключевая мысль
> **Evals важны для AI safety не потому, что они дают гарантию безопасности, а потому, что в условиях слабой теории они остаются главным доступным эмпирическим инструментом для проверки, операционализации и накопления знания.**

## Зачем источник в базе
Эта лекция полезна как явная попытка поместить evals в эпистемическую архитектуру науки. Она не обсуждает только benchmark design или только statistical rigor, а спрашивает более жестко: что происходит, когда в поле нет хорошей проверки, плохие проверки, нет теории или плохие теории, и какую роль evals реально могут играть в такой ситуации.

## Эпистемический статус и как на него смотреть
Это methodological lecture and field-framing source, а не technical survey. Ее полезно читать как попытку встроить evals into a broader theory of empirical knowledge-making under weak theory.

## На какие вопросы источник помогает отвечать
- Что происходит с полем, когда эмпирика слабая, плохая или теории нет?
- Почему в AI safety недостаточно просто “иметь какие-то evals”?
- Какие роли evals играют beyond scorekeeping: operationalization, decision support and knowledge accumulation?
- Как критика evals меняется, если спросить “а что у нас остается без них?” 

## Краткое содержание
Лекция устроена в два больших блока. В первом блоке она строит почти философско-методологическую рамку через "рецепт науки": хорошие теории, проверка практикой и то, как поле ломается, когда любой из этих элементов отсутствует или работает плохо. Там же приводятся примеры плохой проверки и нехватки теории, чтобы показать, что сама по себе эмпирика не гарантирует полезного знания. Во втором блоке разговор возвращается к AI safety: вводится рамка угроз, затем перечисляется потенциал evals как инструмента операционализации, принятия решений и накопления знаний, и после этого разбираются типичные претензии к evals. Итоговая мысль лекции не в том, что evals достаточны, а в том, что без них поле почти лишается эмпирической опоры.

## Как читать источник быстро
- Если нужен conceptual frame, читай first block on science, theory and verification.
- Если важна AI-safety relevance, переходи к the second block on threats, roles of evals and common objections.
- Если нужен reusable takeaway, держи в фокусе difference between having evaluation and having good evaluation.

## Что источник утверждает прямо
- Научное поле ломается не только при отсутствии эмпирики, но и при наличии плохой эмпирики или плохой теории.
- В AI safety и evals уже можно увидеть все эти режимы провала: отсутствие проверки, слабые проверки и недостаток хороших объясняющих моделей.
- Evals играют как минимум три роли: помогают операционализировать свойства, поддерживают принятие решений и участвуют в накоплении знаний.
- Критика evals не отменяет того, что эмпирический подход остается необходимым этапом для более зрелого инженерного понимания AI systems.

## Что здесь особенно важно
- **Лекция различает наличие проверки и качество проверки.** Это хороший corrective против наивной идеи, что любой benchmark already means progress.
- **Evals подаются как empirical interface к слабой теории.** Это хорошо стыкуется и с week-01, и с week-05.
- **Потенциал evals описывается шире, чем benchmarking.** Они важны не только для scorekeeping, но и для operationalization и knowledge accumulation.
- **Претензии к evals не отбрасываются, а переворачиваются в вопрос о том, что делать без них.**

## Интерпретация для курса
Если week-01 и week-05 в основном обсуждают limits and standards, то эта лекция помогает удержать более базовую мысль: в AI safety эмпирический слой пока слишком слаб, чтобы отказаться от evals, и слишком важен, чтобы относиться к нему небрежно. В логике курса это один из лучших текстов для вопроса "почему методология evals важна еще до того, как мы спорим о конкретных benchmark protocols".

## Что стоит запомнить при повторении
- **Плохая проверка не лучше отсутствия проверки просто по определению; она тоже может систематически портить поле.**
- **Evals нужны как empirical tool, даже если они не решают всю задачу safety.**
- **Операционализация, decision support и knowledge accumulation — три полезные роли evals, которые стоит держать вместе.**

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/eval-methodology](../concepts/eval-methodology.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)

## Что осталось неясным / спорным
- Какая именно форма эмпирики в AI safety наиболее полезна: benchmarking, red-teaming, agent evals, interpretability-grounded tests или смешанные regimes?
- Можно ли говорить о evals как о "главном" эмпирическом инструменте, если часть наиболее сильных evidence-подходов может лежать на стыке с interpretability и auditing?

## Связанные страницы
- [syntheses/eval-methodology-in-ai-safety](../syntheses/eval-methodology-in-ai-safety.md)
- [sources/slava-meriton-evals-methodology-lecture-01](slava-meriton-evals-methodology-lecture-01.md)
- [sources/slava-meriton-evals-methodology-lecture-03](slava-meriton-evals-methodology-lecture-03.md)
- [sources/we-need-a-science-of-evals](we-need-a-science-of-evals.md)
