# trackpl
track profits and losses from daytrading or swingtrading

# Trading App

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dresendez/trackpl.git
   cd trackpl
   ```

2. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file with your actual values
   ```

3. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django python-dotenv
   # If you have a requirements.txt file:
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create admin account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Access the Application

- Main site: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin
- Calendar: http://127.0.0.1:8000/calendar

## Troubleshooting

- If you get any module import errors, make sure all required packages are installed
- If you get database errors, check your database settings in the `.env` file
- Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt)
- If the server won't start, check if another process is using port 8000. You can use a different port:
  ```bash
  python manage.py runserver 8001
  ```

## Environment Variables

The following environment variables need to be set in your `.env` file:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to True for development
- `DATABASE_NAME`: Your database name
- `DATABASE_USER`: Database user
- `DATABASE_PASSWORD`: Database password
- `DATABASE_HOST`: Database host (default: localhost)
- `DATABASE_PORT`: Database port (default: 5432)
