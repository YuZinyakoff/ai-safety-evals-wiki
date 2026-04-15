# Towards A Science Of AI Agent Reliability

- **Тип источника:** theory
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/theory/Towards a Science of AI Agent Reliability.md>), [PDF](<../../raw/week-04/theory/2602.16666v1.pdf>), [TeX source](<../../raw/week-04/theory/arXiv-2602.16666v1.tar.gz>)
- **Оригинал:** [arXiv HTML](https://arxiv.org/html/2602.16666v1)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **У агента может расти capability, но не расти reliability.** Mean success score скрывает то, что для deployment часто важнее: consistency, robustness, predictability и bounded failure severity.

## Зачем источник в базе
Это главный текст недели про то, почему agent evaluation нельзя сжимать до одного success metric. Он нужен как опорная страница, когда нужно восстановить не просто тезис "accuracy недостаточна", а более строгую рамку: какие именно свойства теряются при таком сжатии и как их можно измерять отдельно.

## Эпистемический статус и как на него смотреть
Это framework-plus-empirics paper about reliability, а не just another benchmark leaderboard. Его полезно читать как попытку отделить `capability` from `reliability` and give the latter its own measurement language.

## На какие вопросы источник помогает отвечать
- Почему mean success score плохо описывает deployment-relevant behavior агента?
- Какие four reliability dimensions authors выделяют и зачем?
- Какые metrics нужны, чтобы измерять consistency, robustness, predictability and safety separately?
- Что authors empirically показывают о разрыве между capability gains and reliability gains?

## Краткое содержание
Статья начинается с постановки проблемы через реальные agent failures и через contrast с safety-critical engineering: в авиации, атомной энергетике и других высокорисковых областях надежность давно понимается как многомерное свойство, а agent evals все еще часто сводятся к mean task success. Затем paper вводит четыре reliability dimensions — `consistency`, `robustness`, `predictability`, `safety` — и подробно объясняет, почему каждое из них operationally важно. После этого авторы предлагают 12 concrete metrics: от outcome/trajectory/resource consistency и prompt/environment/fault robustness до calibration, discrimination и consequence-aware safety scores. В экспериментальной части работа применяет этот framework к 14 agentic models на двух benchmark families и показывает ключевой empirical result: capability gains заметно опережают reliability gains. Финал текста важен тем, что он предлагает смотреть на reliability как на отдельный профиль, а не как на украшение вокруг accuracy.

## Как читать источник быстро
- Если нужен conceptual shift, читай motivation versus safety-critical engineering and the four reliability dimensions.
- Если вопрос про measurement, переходи к the 12 proposed metrics and what each dimension is supposed to capture.
- Если нужен empirical punchline, смотри experiments showing capability versus reliability divergence.

## Что источник утверждает прямо
- Capability and reliability are distinct properties and should not be collapsed into one mean success score.
- Reliability for agents is multi-dimensional, including at least consistency, robustness, predictability and safety.
- Tail-risk-like failure properties matter in ways that average performance metrics often obscure.
- In the reported experiments, capability improvements outpace reliability improvements across evaluated agent families.

## Что здесь особенно важно
- **Reliability disentangled from capability.** Это центральный methodological move текста.
- **Tail risks нельзя усреднять.** Safety metrics надо читать иначе, чем обычные performance metrics.
- **Predictability** вводит слой calibrated uncertainty, который редко попадает в обычные agent leaderboards.
- **Trajectory consistency** полезно помнить как отличие agent evaluation от simple answer evaluation.

## Интерпретация для курса
Для курса этот paper делает agent evaluation deployment-shaped rather than leaderboard-shaped. Он показывает, что вопрос “насколько агент хорош?” слишком грубый; нужно отдельно спрашивать, насколько он стабилен, предсказуем и безопасен across contexts and trajectories.

## Что это добавляет к теме недели
Princeton paper делает week-04 существенно строже. После него разговор об agent evals перестает быть просто разговором о richer benchmarking и становится разговором о deployment-relevant properties, которые требуют отдельного measurement language.

## Что стоит запомнить при повторении
- **Accuracy и reliability — не одно и то же.**
- **Хороший агент может быть ненадежным, а менее сильный агент может быть надежным в узком envelope.**
- **Если failure severity важна, average score почти наверняка недостаточен.**

## Связанные концепты
- [concepts/agent-reliability](../concepts/agent-reliability.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-autonomy](../concepts/agent-autonomy.md)

## Что осталось неясным / спорным
- Насколько предложенные metrics practical вне лабораторных benchmark settings?
- Как соотносится этот reliability profile с более threat-model-specific safety evaluation?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/evaluation-benchmarking-llm-agents-survey](evaluation-benchmarking-llm-agents-survey.md)
- [sources/metr-guidelines-capability-elicitation](metr-guidelines-capability-elicitation.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
