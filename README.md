# LandingCars

### Краткое описание
Проект c регистрацией

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

### TODO
- [ ] **Документация**: описание сервиса
- [ ] **Документация**: основные абстракции и их базовые реализации (doc-string).
- [ ] **Тесты**
- [ ] **CI/CD Job**: pre-commit
- [ ] **CI/CD Job**: test