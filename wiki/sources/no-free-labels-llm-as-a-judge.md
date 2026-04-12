# No Free Labels: Limitations Of LLM-As-A-Judge Without Human Grounding

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/No Free Labels Limitations of LLM-as-a-Judge Without Human Grounding.md>), [PDF](<../../raw/week-03/extra/2503.05061v2.pdf>), [TeX source](<../../raw/week-03/extra/arXiv-2503.05061v2.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2503.05061)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Judge model надежнее там, где она либо сама умеет решить задачу, либо получает корректную human-grounded reference.** Без этого agreement с экспертами быстро проседает.

## Зачем источник в базе
Это важное уточнение к более раннему optimism around `LLM-as-a-judge`. Источник нужен, чтобы добавить correctness-heavy perspective: preference-style agreement еще не гарантирует, что judge будет надежна там, где качество ответа зависит от domain knowledge и factual correctness.

## Краткое содержание
Paper строит собственную empirical base для проверки correctness-oriented judging. Сначала авторы создают `BFF-Bench` и `VERDICTS`: набор сложных business / finance вопросов, human-written references и expert judgments correctness. Затем работа сравнивает разные automated grading methods и отдельно исследует judge models в single и pairwise settings. Главный анализ идет через очень конкретный вопрос: что происходит с agreement judge'а, если у него нет правильной reference answer? Вывод paper в том, что judge сохраняет высокое agreement с экспертами главным образом там, где сам способен решить underlying question, а human-written reference сильно улучшает результат. Дальше работа показывает, что тип reference и ее correctness важнее, чем просто stylistic resemblance, и что human verification остается критичным даже при использовании сильных judge models.

## Что здесь особенно важно
- **Correctness-heavy evaluation** резко строже, чем preference-heavy judging.
- **Reference quality** влияет на judge сильнее, чем многие ожидают.
- **Judge competence on underlying task** — не второстепенный фактор, а почти главный.
- **Human grounding** остается необходимой частью trustworthy judging.

## Что это добавляет к теме недели
Источник хорошо закрывает week-03 со стороны limits of judge-based evaluation. Он показывает, что benchmark design для `LLM-as-a-judge` должен включать не только prompt and rubric choices, но и question of human grounding, reference correctness и domain fit judge model.

## Что стоит запомнить при повторении
- **LLM judge не производит “бесплатные метки” из воздуха.**
- **Correct reference часто важнее, чем просто более сильный judge model.**
- **Judge reliability зависит от underlying task competence.**

## Связанные концепты
- [concepts/llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [concepts/construct-validity](../concepts/construct-validity.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)

## Что осталось неясным / спорным
- Можно ли добиться достаточно надежного human grounding дешевле, чем через полноценные expert-written references?
- Как переносить эти выводы с high-stakes correctness domains на более open-ended evaluation regimes?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/llm-as-a-judge-mt-bench-chatbot-arena](llm-as-a-judge-mt-bench-chatbot-arena.md)
- [sources/limits-scalable-evaluation-frontier](limits-scalable-evaluation-frontier.md)
