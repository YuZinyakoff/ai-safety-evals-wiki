# AI Safety Evaluations: An Explainer

- **Тип источника:** theory
- **Неделя:** week-02
- **Raw:** [web clip](<../../raw/week-02/theory/AI Safety Evaluations An Explainer.md>)
- **Оригинал:** [CSET](https://cset.georgetown.edu/article/ai-safety-evaluations-an-explainer/)
- **Полнота raw:** полный web clip статьи

## Ключевая мысль
> **Не все safety evals отвечают на один и тот же вопрос.** Прежде чем обсуждать score, полезно сначала понять, оцениваем ли мы outputs модели или ее real-world usefulness / impact in context.

## Зачем источник в базе
Это лучший входной текст недели, если нужно быстро восстановить базовую taxonomy AI safety evaluations. Он нужен как страница, которая разводит разные типы evaluation-задач и помогает не смешивать измерение `model outputs` с измерением `downstream impact`.

## Краткое содержание
Explainer устроен как аккуратное введение в design logic safety evaluations. Сначала он делит оценки на две большие группы: **model safety evaluations**, которые спрашивают в первую очередь про свойства outputs модели, и **contextual safety evaluations**, которые пытаются понять влияние доступа к модели на реальные действия и outcomes. Затем текст вводит простую, но полезную рамку проектирования: сначала решить **что именно измерять**, потом **как это измерять**, а затем отдельно разобрать, **что полученный результат вообще означает**. Внутри этой рамки explainer обсуждает capability testing, benchmarking, red-teaming и uplift studies, а в конце отдельно подчеркивает ограничения proxy metrics и риск переинтерпретации результатов.

## Что здесь особенно важно
- **Taxonomy before metrics.** Источник полезен тем, что заставляет сначала различить объект оценки, а не сразу спорить о score.
- **`What / how / what it means`** — очень удачная design frame для всей недели.
- **Model-side и contextual protocols несут разный тип evidence.**
- **Proxy nature результатов** проговаривается прямо: performance on a task не равна прямому измерению реального риска.
- **Human-heavy contextual setups** труднее стандартизировать и интерпретировать, чем model-side benchmarks.

## Что это добавляет к теме недели
CSET делает week-02 более структурной. После week-01 уже понятно, что evals ограничены; этот текст уточняет следующий шаг: **ограничены разные evals по-разному, потому что измеряют разные объекты**. Благодаря этому потом проще читать и Miller, и survey beyond benchmarks, и notebook как части одного разговора, а не как случайный набор материалов.

## Что стоит запомнить при повторении
- Сначала полезно спросить: **мы меряем модель или контекст ее использования?**
- Хороший evaluation design начинается раньше benchmark run: с выбора правильного объекта измерения.
- Даже аккуратный результат почти всегда остается **proxy evidence**, а не прямым ответом на risk question.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/model-safety-evals](../concepts/model-safety-evals.md)
- [concepts/contextual-safety-evals](../concepts/contextual-safety-evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Где проходит практическая граница между `model safety` и `contextual safety evaluations` в гибридных протоколах?
- Какие proxy outcomes достаточно хороши, чтобы на их основе принимать policy или deployment decisions?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
