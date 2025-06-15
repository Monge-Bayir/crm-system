### 🧠 CRM-система на Django + Docker

Этот проект — полноценная CRM-платформа на Django, включающая:

- 📢 Рекламные кампании (Ads)
- 🧲 Потенциальные клиенты (Leads)
- 📞 Активные клиенты (Customers)
- 📑 Контракты (Contracts)
- 🎯 Продукты (Products)
- 📊 Автоматическая статистика (лиды, клиенты, ROI)

---

### 🚀 Быстрый старт (через Docker)

1. Клонировать репозиторий

```bash
git clone https://github.com/Monge-Bayir/crm-system.git
cd crm-system
```

2. Собрать Docker-образ

```bash
cd crm
docker build -t app .
```

3. Запустить контейнер
   
```bash
docker run -p 8000:8000 crm-system
```

4. Создать суперпользователя

```bash
docker exec -it <container_id> python manage.py createsuperuser
```

### ⚙️ Локальный запуск (без Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔐 Admin-панель

После запуска открой:
http://localhost:8000/admin/


### 📊 Статистика по кампаниям

http://localhost:8000/ads/statistics/
Показывает:
	•	Кол-во лидов
	•	Кол-во активных клиентов
	•	Прибыль по контрактам
	•	ROI (доход – бюджет)


### 🧾 Зависимости
	•	Python 3.11
	•	Django 4.2+
	•	Docker (опционально)
