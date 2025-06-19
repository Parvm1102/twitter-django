# Twitter Django Project
A Django-based web application that replicates core Twitter functionality, allowing users to create accounts, post tweets, and search for content. Built with Python and Django framework for a complete social media experience.
## Setup Instructions

### Prerequisites
- Python 3.10+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Parvm1102/twitter-django.git
cd twitter_django
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

### Running the Project

Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Configuration

- Update `settings.py` with your database configuration
- Set environment variables for production deployment
- Configure static files for production

## Features

- User authentication
- Tweet functionality view,create,update and delete
- Search tweet by keyword
