# Twitter Django Project

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
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
- Tweet functionality
- User profiles
- Timeline views

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request