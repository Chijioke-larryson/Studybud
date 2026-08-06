# Studybud

Studybud is a Django web application for discovering and organising study rooms around shared topics. It is an early-stage learning project that provides a simple foundation for a study-community platform.

Users can browse rooms, filter them by topic or keyword, and manage room records through the web interface or Django admin.

## Current features

- Browse all available study rooms
- Browse rooms by topic
- Search room names, topics, and descriptions
- Create, edit, and delete rooms
- View individual room pages
- Manage users, rooms, and topics from the Django admin site
- Basic login page and chat route placeholders for future development

## Built with

- Python
- Django 6.0.7
- SQLite (the default development database)
- Django templates and plain HTML

## Project structure

```text
Studybud/
├── manage.py                 # Django command-line entry point
├── Studybud/                 # Project configuration and root URLs
├── Insta/                    # Study-room application
│   ├── models.py             # Topic, Room, and Message models
│   ├── views.py              # Page and room-management views
│   ├── urls.py               # Application routes
│   ├── forms.py              # Room form
│   ├── migrations/           # Database schema migrations
│   └── templates/Insta/      # Application templates
├── templates/                # Shared templates (navbar)
└── db.sqlite3                # Local SQLite database
```

## Getting started

### Prerequisites

- Python 3.12 or later
- `pip`

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Studybud
```

### 2. Create and activate a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install "Django==6.0.7"
```

> Django 6.0 requires Python 3.12 or later. If you are using an earlier Python version, install a compatible Django release or upgrade Python first.

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin account (optional)

Use this account to add topics, rooms, and users at `/admin/`.

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Home page with room list, topics, and search |
| `/room/<id>/` | Individual room page |
| `/create-room/` | Create a room |
| `/update-room/<id>/` | Edit a room |
| `/delete-room/<id>/` | Delete a room |
| `/login/` | Login page UI |
| `/admin/` | Django administration site |

## Data model

- **Topic** — a study category, such as Python or Mathematics.
- **Room** — a study space with a name, host, topic, optional description, and timestamps.
- **Message** — a message associated with a room and user. The model is in place for future chat functionality.

## Development notes

- Authentication is not yet connected to the login form.
- Room actions are not yet restricted to authenticated owners.
- The room-detail and chat experiences are currently placeholders.
- The committed SQLite database is intended for local development only.
- Before deployment, set `DEBUG = False`, move `SECRET_KEY` to environment variables, configure `ALLOWED_HOSTS`, and use a production-ready database and static-file setup.

## Useful Django commands

```bash
# Create migrations after changing models
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run the test suite
python manage.py test
```

## License

No license has been specified yet. Add one before distributing or reusing this project publicly.
