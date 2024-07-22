# Salary

### Краткое описание
Проект подсчёта месячной зарплаты и аванса

### Работа с зависимостями
```bash
pip install -r requirements.txt
```

#### Добавление зависимости проекта:
* Добавляем новую зависимость в список `project.dependencies` в `pyproject.toml`
* Генерируем обновленный `requirements.txt`

```bash
pip-compile -o requirements.txt pyproject.toml
```
