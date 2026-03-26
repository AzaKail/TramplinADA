# TramplinADA — Stage 1 bootstrap

Минимальный старт проекта для этапа 1:
- backend на Django;
- базовый frontend через Django templates + static;
- API endpoint для проверки работы.

## Быстрый старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py runserver
```

Проверки:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/health/



python 3.11