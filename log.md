# Журнал изменений

## 2026-04-12 | ingest | week-03
- Разобраны материалы `raw/week-03/` по theory, notebook и extra-слоям, включая organizer framing и fallback sidecar только для PDF-only материалов
- Созданы 12 source pages, 8 новых concept pages и 1 synthesis про benchmark design, evidence claims и benchmark ecosystem
- `wiki/weeks/week-03.md` собрана как полноценная hub-page недели, а `wiki/home.md` и `index.md` обновлены под текущее покрытие первых трех недель

## 2026-04-12 | framing | week-03 organizer note
- В `raw/week-03/extra/` добавлена organizer note `course-framing-week-03.md` как педагогическая рамка третьей недели
- `wiki/weeks/week-03.md` переписана из стартового шаблона в pre-ingest hub-page с замыслом недели, предварительными вопросами, картиной недели и ссылками на raw-материалы
- Для week-03 зафиксирован переход от `evaluation strategy` к benchmark design, evidence claims и benchmark ecosystem

## 2026-04-12 | framing | week-02 organizer note
- В `raw/week-02/extra/` добавлена organizer note `course-framing-week-02.md` как отдельный слой педагогической рамки недели
- `wiki/weeks/week-02.md` дополнена замыслом недели, предварительными вопросами и вопросами для обсуждения на основе organizer note
- Организаторская рамка встроена в week-02 как переход от ограничений evals к вопросу о strategy, benchmark choice и честной интерпретации результата

## 2026-04-12 | framing | week-01 organizer note
- В `raw/week-01/extra/` добавлена organizer note `course-framing-week-01.md` как отдельный слой педагогической рамки недели
- В `AGENTS.md` и `README.md` зафиксировано, что такие `course framing`-заметки живут в `extra/`, усиливают week pages и не подменяют предметные source pages
- `wiki/weeks/week-01.md` дополнена замыслом недели, предварительными вопросами и вопросами для обсуждения на основе organizer note

## 2026-04-11 | cleanup | top-level nav and barnett raw
- `wiki/home.md` и `index.md` усилены как верхнеуровневые точки входа: добавлены более полезные маршруты по задачам, а не только каталог страниц
- Для Barnett-Thiergart добавлены clipped HTML raw и `TeX Source`, поэтому source page и `week-01` больше не зависят от fallback-sidecar
- Старый `pdf.md` fallback для Barnett удален из `raw/` как больше не нужный вспомогательный артефакт

## 2026-04-11 | refactor | week-02 wiki roles
- `wiki/weeks/week-02.md` переписана как более сильная hub-page про evaluation frame, uncertainty и bounded benchmark coverage
- Source pages week-02 усилены: добавлены более явные `Ключевая мысль`, структурные summaries и прямые ссылки на лучшие raw-источники
- Concept pages week-02 стали более объясняющими и лучше различают объект оценки, механизм ошибки и тип путаницы
- `wiki/syntheses/benchmarking-beyond-single-scores.md` переписан как более настоящий межисточниковый synthesis, а не просто recap benchmark-темы
- Source page survey про generalizable evaluation обновлена под новый raw-набор: clipped Markdown, PDF и `TeX Source`

## 2026-04-11 | refactor | week-01 wiki roles
- `wiki/weeks/week-01.md` переписана как более сильная hub-page для повторения курса, а provenance/raw-статус сдвинут ниже
- Source pages week-01 усилены не только summary-блоками, но и более явным ответом на вопрос, почему каждый текст важен и что из него стоит запомнить
- Concept pages week-01 сделаны более объясняющими: теперь они лучше различают механизм, тип ошибки и частые путаницы
- `wiki/syntheses/evals-scope-and-limits.md` переписан как более настоящий межисточниковый synthesis, а не просто общий recap недели
- В source pages добавлены явные ссылки на raw-источники, чтобы wiki было удобнее читать как рядом с summary, так и рядом с полными текстами
- Для source pages уточнен стандарт `Краткого содержания`: теперь он должен лучше отражать структуру текста, paper или notebook, а не только общий тезис

## 2026-04-11 | policy | raw hierarchy refined
- После сравнения PDF, clipped HTML и TeX source для arXiv-статей week-01 и week-02 уточнен приоритет raw-форматов
- Зафиксировано, что `pdf.md` sidecar из MarkItDown полезен как fallback-extract и поисковый слой, но не как автоматически preferred raw
- Для arXiv предпочтение отдано связке `HTML-clipped .md` для ingest + PDF как visual ground truth + `TeX Source` как backup для формул и таблиц
- В `AGENTS.md` и `README.md` добавлено правило выбирать лучшее локальное представление источника, а не любой найденный текстовый sidecar
- Добавлено правило не хранить sidecar из PDF, если уже есть более качественный clipped/HTML/TeX raw

## 2026-04-11 | refresh | week-01 raw fidelity
- Для `week-01` добавлены и учтены новые clipped raw-версии Apollo, Hubinger и Ivanov
- Для двух PDF week-01 созданы нормализованные `pdf.md` sidecar-файлы рядом с оригиналами
- Source pages, `wiki/weeks/week-01.md`, связанные concept pages и synthesis обновлены под более полный локальный raw
- Исправлена ссылка на raw-файл у страницы про specification gaming

## 2026-04-10 | policy | raw normalization
- Зафиксирована policy, что ingest по возможности опирается на локально доступный текст источника, а не только на URL или бинарный файл
- Для `raw/` утвержден приоритет: clipped `.md` -> sidecar `filename.ext.md` -> URL-only как временно неполное состояние
- В `README.md` и `AGENTS.md` добавлен явный шаг `normalize` перед ingest

## 2026-04-10 | ingest | week-02
- Разобраны все текущие материалы `raw/week-02/`: 3 theory, 1 notebook и 1 extra
- Созданы 5 source pages, 5 новых concept pages и 1 synthesis
- `wiki/weeks/week-02.md` собрана как hub-page по benchmarking, statistical rigor и evaluation design
- Обновлены `wiki/home.md`, `index.md`, `log.md`, а также общие concept pages `evals` и `inspect-ai`

## 2026-04-10 | polish | week-01 wiki
- `wiki/weeks/week-01.md` дополнена пояснением, как читать набор источников и где raw полон, а где это только note-with-link
- Source pages week-01 получили явную пометку о полноте raw-артефакта
- Concept pages week-01 дополнены секциями про частые путаницы
- Внутренние wiki-ссылки переведены на относительный Markdown-формат
- `index.md` сделан более каталоговым и удобным для навигации вне Obsidian

## 2026-04-10 | content-pass | week-01 wiki
- `wiki/weeks/week-01.md` усилена как hub-page для повторения недели
- Все source pages week-01 приведены к более единообразному и подробному формату
- Concept pages, связанные с week-01, переведены из телеграфного режима в более объясняющий
- Точечно обновлен `index.md`

## 2026-04-10 | enrichment | week-01 wiki
- Week-01 страницы переписаны в менее телеграфном и более учебном режиме
- Source pages усилены короткими объяснениями о том, почему каждый источник важен
- Concept pages дополнены пояснениями для повторного чтения спустя время
- Обновлен synthesis `wiki/syntheses/evals-scope-and-limits.md`

## 2026-04-10 | ingest | week-01
- Разобраны все текущие материалы `raw/week-01/`: 3 theory, 1 notebook и 3 extra
- Созданы 7 source pages, 7 concept pages и 1 synthesis
- Обновлены `wiki/weeks/week-01.md`, `wiki/home.md`, `index.md` и `log.md`
- Проверены ссылки и cross-links вокруг `week-01`; битых ссылок и orphan pages в wiki не найдено

## 2026-04-10 | scaffold | wiki
- Уточнена `wiki/home.md`: добавлены навигация, текущее покрытие и краткие правила записи
- Страницы `wiki/weeks/week-01..week-05.md` усилены как стартовые шаблоны для ingest
- Обновлен `index.md` под текущее состояние базы

## 2026-04-09 | init | repo
- Создан git-репозиторий
- Создана базовая структура `raw/` и `wiki/`
- Добавлены стартовые файлы `README.md`, `AGENTS.md`, `index.md`, `log.md`
- Созданы страницы недель
