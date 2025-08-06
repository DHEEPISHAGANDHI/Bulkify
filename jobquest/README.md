# Job Quest - Professional Job Board

A modern, professional job board web application built with Django, featuring a clean and responsive user interface for browsing and searching job opportunities.

## 🌟 Features

- **Professional Interface**: Clean, light-themed design with responsive layout
- **Job Listings**: Browse job opportunities with detailed information
- **Advanced Search**: Search jobs by keywords, company, or description
- **Location Filtering**: Filter jobs by location
- **Pagination**: Efficient pagination for large job datasets
- **Detailed Job Views**: Comprehensive job detail pages with application information
- **Admin Interface**: Full Django admin integration for job management
- **Database Integration**: SQLite for development, MySQL-ready for production
- **Comprehensive Testing**: Complete test suite with unit and integration tests

## 🚀 Technologies Used

- **Backend**: Python 3.13, Django 5.2.5
- **Database**: SQLite (development), MySQL-ready
- **Frontend**: HTML5, CSS3 (Vanilla CSS, no frameworks)
- **Icons**: Font Awesome 6.0
- **Fonts**: Inter (Google Fonts)
- **Testing**: Django TestCase, unittest

## 📋 Requirements

- Python 3.8+
- Django 5.2.5
- mysqlclient 2.2.7 (for MySQL support)

## 🛠️ Installation & Setup

### 1. Clone or Download the Project

```bash
# Navigate to the project directory
cd jobquest
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv job_quest_env

# Activate virtual environment
# On Linux/Mac:
source job_quest_env/bin/activate
# On Windows:
# job_quest_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

The application uses SQLite by default for development. For production with MySQL, update the database configuration in `jobquest/settings.py`.

```bash
# Run migrations
python manage.py migrate

# Load sample data (optional)
python manage.py load_sample_data
```

### 5. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 📁 Project Structure

```
jobquest/
├── jobquest/
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
├── jobs/                   # Main application
│   ├── migrations/         # Database migrations
│   ├── management/
│   │   └── commands/
│   │       └── load_sample_data.py  # Sample data loader
│   ├── templates/jobs/     # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── home.html       # Home page
│   │   ├── job_list.html   # Job listings
│   │   └── job_detail.html # Job detail view
│   ├── admin.py           # Admin configuration
│   ├── models.py          # Job model
│   ├── views.py           # Views and logic
│   ├── urls.py            # App URL patterns
│   └── tests.py           # Comprehensive test suite
├── static/css/
│   └── style.css          # Professional CSS styling
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## 🎨 Design Features

### Professional Light Theme
- Clean, modern interface with subtle shadows and gradients
- Professional color palette with blue primary colors
- Responsive design that works on desktop, tablet, and mobile
- Inter font family for excellent readability

### User Experience
- Intuitive navigation with sticky header
- Search and filter functionality
- Pagination for large datasets
- Breadcrumb navigation
- Empty states and loading indicators
- Professional job cards with hover effects

### Responsive Design
- Mobile-first approach
- Flexible grid layouts
- Scalable typography
- Touch-friendly interface elements

## 🧪 Testing

The application includes a comprehensive test suite with 26+ tests covering:

### Unit Tests
- Model creation and validation
- Field constraints and defaults
- Model methods functionality
- String representations

### Integration Tests
- View responses and context
- Template rendering
- Search and filter functionality
- Pagination
- Complete user workflows
- Database queries

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific test class
python manage.py test jobs.tests.JobModelTest

# Run with verbose output
python manage.py test --verbosity=2
```

## 📊 Database Schema

### Job Model
- `title` (CharField, max 200): Job title
- `company_name` (CharField, max 150): Company name
- `description` (TextField): Detailed job description
- `location` (CharField, max 150): Job location
- `posting_date` (DateTimeField): When job was posted
- `created_at` (DateTimeField): Record creation timestamp
- `updated_at` (DateTimeField): Last update timestamp
- `is_active` (BooleanField): Whether job is currently active

## 🔧 Configuration

### MySQL Configuration

To use MySQL in production, update `jobquest/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobquest_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### Static Files

For production deployment, configure static files:

```python
STATIC_ROOT = '/path/to/static/files/'
```

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False` in settings
2. Configure proper database settings
3. Set up static file serving
4. Configure allowed hosts
5. Use environment variables for secrets
6. Set up proper logging
7. Configure web server (nginx, Apache)
8. Use WSGI server (gunicorn, uwsgi)

### Sample Production Settings

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

## 📱 API Endpoints

- `/` - Home page with featured jobs
- `/jobs/` - Job listings with search and pagination
- `/jobs/<id>/` - Individual job detail page
- `/admin/` - Django admin interface

## 🤝 Contributing

1. Follow Django best practices
2. Write tests for new features
3. Use meaningful commit messages
4. Update documentation as needed
5. Ensure responsive design compatibility

## 📄 License

This project is built for educational and demonstration purposes.

## 🔍 Key Features Demonstrated

### Django Best Practices
- MVT (Model-View-Template) architecture
- Proper URL routing
- Template inheritance
- Static file management
- Admin interface customization
- Management commands

### Web Development
- Responsive CSS without frameworks
- Professional UI/UX design
- Search and filtering
- Pagination
- Form handling
- Database optimization

### Testing
- Unit tests for models
- Integration tests for views
- Template testing
- Complete workflow testing
- Database query testing

## 📞 Support

For questions or issues, please refer to the Django documentation or create an issue in the project repository.

---

**Built with ❤️ using Django and vanilla CSS for a professional job board experience.**