# TramplinADA — Stage 1 bootstrap

Минимальный старт проекта для этапа 1:
- backend на Django;
- базовый frontend через Django templates + static;
- API endpoint для проверки работы;
- PostgreSQL + Docker Compose для локального запуска всей инфраструктуры.

## Вариант 1: запуск в Docker (не забудьте установитьв всё)

```bash
cp .env.example .env
docker compose up --build
```

После запуска:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/health/

## Вариант 2: локально без Docker

По умолчанию используется SQLite, если `DB_ENGINE` не задан или равен `sqlite`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py runserver
```

### Локальный PostgreSQL (без Docker)

```bash
export DB_ENGINE=postgres
export POSTGRES_DB=tramplin_db
export POSTGRES_USER=tramplin_user
export POSTGRES_PASSWORD=tramplin_password
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
python backend/manage.py migrate
python backend/manage.py runserver
```