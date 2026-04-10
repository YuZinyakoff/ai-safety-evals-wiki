# Inspect AI

## Суть
Inspect AI — это framework для построения и запуска evaluations через явную структуру `Task`, в которой отдельно задаются dataset, solver и scorer.

## Факты из источников
- [[sources/inspect-ai-tutorial-week-01]] использует `Task`, `Sample`, solver pipeline и scorer как базовые сущности.
- [[sources/inspect-ai-tutorial-week-01]] показывает built-in components вроде `system_message`, `prompt_template`, `chain_of_thought`, `multiple_choice`, `match`, `exact`, `pattern` и `choice`.
- [[sources/inspect-ai-tutorial-week-01]] отдельно вводит `inspect view` как UI для анализа логов evaluations.
- [[sources/apollo-starter-guide-evals]] подчеркивает важность tooling и engineering skillset для evaluators.

## Рабочая интерпретация
- В этой wiki Inspect AI полезен как concrete implementation layer для идей из недели: как из разговора про elicitation и benchmarking перейти к воспроизводимым tasks.
- Framework также делает видимыми места, где возникают measurement choices: prompt templates, solver chains, scoring rules, metadata и analysis workflows.

## Открытые вопросы
- Какие abstractions Inspect AI особенно полезны для safety evals, а какие больше подходят для учебных benchmarks?
- Как лучше связывать Inspect AI workflows с threat modeling и richer failure analysis?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/inspect-ai-tutorial-week-01]]
- [[concepts/evals]]
- [[concepts/prompt-sensitivity]]
- [[syntheses/evals-scope-and-limits]]
