# Clone repository
git clone https://github.com/GFRXHJ/final-project.git
cd final-project

# Create virtual environment
`python -m venv venv`
`source venv/bin/activate`  # Linux/Mac
`venv\Scripts\activate`     # Windows

# Install dependencies
`pip install -r requirements.txt`

# Run migrations
`python manage.py migrate`

# Create superuser
`python manage.py createsuperuser`

# Run server
`python manage.py runserver`


```bash

Testing with Swagger

Go to http://127.0.0.1:8000/swagger/
Register via /api/register/
Login via /api/login/ and copy access token
Click "Authorize" and enter: Bearer YOUR_TOKEN
Test protected endpoints
```
