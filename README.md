# Family Cladding Backend - Django REST API

## 🏗️ Construction Management System Backend

A comprehensive Django REST API backend for Family Cladding construction company, providing complete content management, invoice system, and API endpoints for the frontend application.

## 🚀 Features

### **Core Functionality**
- ✅ **Django REST Framework**: Complete API endpoints
- ✅ **Invoice Management**: Create, send, and manage invoices
- ✅ **Content Management**: CRUD operations for all content types
- ✅ **Email Integration**: SMTP email sending for invoices
- ✅ **File Upload**: Image and document handling
- ✅ **Admin Interface**: Django admin for backend management

### **Security & Performance**
- ✅ **Production Security**: Hardened security settings
- ✅ **Caching**: Redis caching for performance
- ✅ **Input Validation**: Server-side validation
- ✅ **Authentication**: Secure API access
- ✅ **CORS Configuration**: Proper cross-origin setup

### **Database Models**
- ✅ **Information**: About Us, Carousel, Why Choose Us, Team
- ✅ **Projects**: Project management with images
- ✅ **Services**: Service catalog management
- ✅ **Testimonials**: Customer testimonials
- ✅ **Invoices**: Complete invoice system
- ✅ **Contacts**: Contact form submissions

## 🛠️ Technology Stack

- **Framework**: Django 4.2+ with REST Framework
- **Database**: PostgreSQL (configurable)
- **Caching**: Redis
- **Email**: SMTP integration
- **File Storage**: Local/Cloud storage
- **API**: RESTful API endpoints

## 📁 Project Structure

```
familycladding_back_end/
├── familycladding_back_end/          # Main project settings
│   ├── settings.py                   # Production-ready settings
│   ├── urls.py                       # URL configuration
│   └── wsgi.py                       # WSGI configuration
├── information/                      # Information app
│   ├── models.py                     # About Us, Carousel, etc.
│   ├── views.py                      # API views with caching
│   ├── serializers.py                # Data serialization
│   └── urls.py                       # URL patterns
├── projects/                         # Projects app
│   ├── models.py                     # Project models
│   ├── views.py                      # Project API views
│   └── serializers.py                # Project serializers
├── services/                         # Services app
│   ├── models.py                     # Service models
│   ├── views.py                      # Service API views
│   └── serializers.py                # Service serializers
├── invoices/                         # Invoice management
│   ├── models.py                     # Invoice and InvoiceItem models
│   ├── views.py                      # Invoice API views
│   ├── serializers.py                # Invoice serializers
│   ├── admin.py                      # Admin interface
│   └── urls.py                       # Invoice URLs
├── testimonials/                     # Testimonials app
└── requirements.txt                  # Python dependencies
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- PostgreSQL (optional, SQLite for development)
- Redis (optional, for caching)

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/ludmil/familycladding-backend.git
cd familycladding-backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment setup**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Database setup**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

## 🔧 Configuration

### **Environment Variables**
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,localhost
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379/0
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
```

### **Database Configuration**
- **Development**: SQLite (default)
- **Production**: PostgreSQL recommended
- **Caching**: Redis for performance

## 📊 API Endpoints

### **Information Endpoints**
- `GET /info/aboutus/` - About Us information
- `GET /info/carousels/` - Carousel images
- `GET /info/why_choose_us/` - Why Choose Us content
- `GET /info/team/` - Team members

### **Projects Endpoints**
- `GET /projects/projects/` - List all projects
- `POST /projects/projects/` - Create new project
- `GET /projects/projects/{id}/` - Get specific project
- `PUT /projects/projects/{id}/` - Update project
- `DELETE /projects/projects/{id}/` - Delete project

### **Services Endpoints**
- `GET /services/services/` - List all services
- `POST /services/services/` - Create new service
- `GET /services/services/{id}/` - Get specific service
- `PUT /services/services/{id}/` - Update service
- `DELETE /services/services/{id}/` - Delete service

### **Invoice Endpoints**
- `GET /invoice/invoices/` - List all invoices
- `POST /invoice/invoices/` - Create new invoice
- `GET /invoice/invoices/{id}/` - Get specific invoice
- `PUT /invoice/invoices/{id}/` - Update invoice
- `DELETE /invoice/invoices/{id}/` - Delete invoice
- `POST /invoice/invoices/{id}/send/` - Send invoice via email
- `POST /invoice/invoices/{id}/mark-paid/` - Mark invoice as paid

### **Testimonials Endpoints**
- `GET /testimonials/testimonials/` - List all testimonials
- `POST /testimonials/testimonials/` - Create new testimonial

## 🎯 Invoice System

### **Features**
- **Professional Templates**: Branded invoice design
- **Email Integration**: Send invoices directly to clients
- **Status Tracking**: Draft, Sent, Paid, Overdue, Cancelled
- **Automatic Calculations**: Tax and total calculations
- **Line Items**: Multiple items per invoice
- **Client Management**: Complete client information

### **Invoice Model**
```python
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    client_address = models.TextField()
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # ... more fields
```

## 🔒 Security Features

### **Production Security**
- **SECRET_KEY**: Environment variable configuration
- **DEBUG**: Disabled in production
- **ALLOWED_HOSTS**: Restricted host access
- **HTTPS**: SSL/TLS enforcement
- **CSRF Protection**: Cross-site request forgery protection
- **XSS Protection**: Cross-site scripting prevention

### **Authentication**
- **Django Admin**: Secure admin access
- **API Authentication**: Token-based authentication
- **CORS Configuration**: Proper cross-origin setup
- **Session Security**: Secure session configuration

## 📈 Performance Optimization

### **Caching Strategy**
- **Database Queries**: Query optimization with select_related
- **API Responses**: Redis caching for frequently accessed data
- **Static Files**: CDN-ready static file serving
- **Database Connection**: Connection pooling

### **Database Optimization**
- **Indexing**: Proper database indexes
- **Query Optimization**: Efficient database queries
- **Pagination**: API response pagination
- **Prefetch Related**: Optimized related object loading

## 🚀 Deployment

### **Production Deployment**
1. **Environment Setup**: Configure production environment variables
2. **Database Migration**: Run database migrations
3. **Static Files**: Collect static files
4. **WSGI Configuration**: Configure WSGI server
5. **Reverse Proxy**: Nginx configuration
6. **SSL Certificate**: HTTPS configuration

### **Docker Deployment**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "familycladding_back_end.wsgi:application"]
```

## 📊 Monitoring & Logging

### **Logging Configuration**
- **Debug Logging**: Development debugging
- **Error Logging**: Production error tracking
- **Access Logging**: Request/response logging
- **Performance Logging**: Performance monitoring

### **Health Checks**
- **Database Health**: Database connection monitoring
- **Cache Health**: Redis connection monitoring
- **Email Health**: SMTP connection monitoring
- **API Health**: Endpoint availability monitoring

## 🔧 Development

### **Code Quality**
- **PEP 8**: Python style guide compliance
- **Type Hints**: Type annotation support
- **Documentation**: Comprehensive code documentation
- **Testing**: Unit and integration tests

### **API Documentation**
- **Swagger/OpenAPI**: Interactive API documentation
- **Postman Collection**: API testing collection
- **Response Examples**: Detailed response examples
- **Error Handling**: Comprehensive error responses

## 📞 Support

For technical support or questions about the backend system:

- **Email**: support@familycladding.co.za
- **Documentation**: Check the API documentation
- **Issues**: Report issues on GitHub
- **Development**: Contact the development team

## 📄 License

This project is proprietary software developed for Family Cladding construction company.

---

**Family Cladding Backend** - Robust, scalable, and secure API for construction management! 🏗️