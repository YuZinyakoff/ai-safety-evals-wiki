# Журнал изменений

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
