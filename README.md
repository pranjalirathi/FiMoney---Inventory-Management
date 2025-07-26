# 🏦 FiMoney - Inventory Management System

**A modern, secure inventory management system built with FastAPI, featuring JWT authentication, product management, and RESTful APIs.**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Installation & Setup](#-installation--setup)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Postman Collection](#-postman-collection)
- [Security](#-security)
- [Contributing](#-contributing)

## ✨ Features

### 🔐 Authentication & Authorization
- **User Registration** with unique username validation
- **JWT Token-based Authentication** with secure password hashing
- **Protected Routes** requiring valid authentication
- **Dual Login Endpoints** (JSON & OAuth2 compatible)

### 📦 Product Management
- **Add Products** with unique SKU validation
- **Get Products** with pagination support
- **Update Product Quantity** with ownership validation
- **Product Details** retrieval
- **SKU Uniqueness** enforcement at database and application level

### 👥 User Management
- **Get Current User Info**
- **List All Users**
- **Get User by ID**
- **User Profile Management**

### 🛡️ Security Features
- **Bcrypt Password Hashing**
- **JWT Token Expiration**
- **Input Validation** with Pydantic
- **SQL Injection Protection** with SQLAlchemy ORM
- **Environment Variable Security**

## 🚀 Tech Stack

### Backend Framework
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server
- **[Python 3.8+](https://www.python.org/)** - Programming language

### Database & ORM
- **[SQLite](https://www.sqlite.org/)** - Lightweight, serverless database
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - Python SQL toolkit and ORM

### Authentication & Security
- **[PyJWT](https://pyjwt.readthedocs.io/)** - JSON Web Token implementation
- **[Passlib](https://passlib.readthedocs.io/)** - Password hashing library
- **[Bcrypt](https://github.com/pyca/bcrypt/)** - Password hashing algorithm

### Data Validation
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type annotations

### Development Tools
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management
- **[Python-multipart](https://github.com/andrew-d/python-multipart)** - Multipart form data parsing

## 📁 Project Structure

```
fimoney/
├── backend/
│   ├── core/
│   │   └── auth.py              # Authentication utilities
│   ├── models/
│   │   ├── user.py              # User database model
│   │   └── product.py           # Product database model
│   ├── routers/
│   │   ├── auth.py              # Authentication endpoints
│   │   ├── users.py             # User management endpoints
│   │   └── products.py          # Product management endpoints
│   ├── schemas/
│   │   ├── user.py              # User Pydantic schemas
│   │   └── product.py           # Product Pydantic schemas
│   ├── main.py                  # FastAPI application entry point
│   ├── database.py              # Database configuration
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables (not in repo)
│   ├── .env.example             # Environment template
│   └── test_product_api.py      # API test script
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore rules
```

## 🔗 API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/register` | Register new user | ❌ |
| POST | `/login` | Login with JSON payload | ❌ |
| POST | `/auth/login-oauth2` | OAuth2 compatible login | ❌ |

### User Management Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/users/me` | Get current user info | ✅ |
| GET | `/users/` | Get all users | ✅ |
| GET | `/users/{user_id}` | Get user by ID | ✅ |

### Product Management Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/products/` | Add new product | ✅ |
| GET | `/products/` | Get products (paginated) | ✅ |
| GET | `/products/{product_id}` | Get product details | ✅ |
| PUT | `/products/{product_id}/quantity` | Update product quantity | ✅ |

## 🔧 Installation & Setup

### Prerequisites
- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### 1. Clone the Repository
```bash
git clone https://github.com/pranjalirathi/FiMoney---Inventory-Management.git
cd FiMoney---Inventory-Management
```

### 2. Navigate to Backend Directory
```bash
cd backend
```

### 3. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Generate a secret key (run in Python)
python -c "import secrets; print(secrets.token_hex(32))"

# Edit .env file with your secret key
```

## 🔑 Environment Variables

Create a `.env` file in the `backend` directory with the following variables:

```env
# JWT Configuration
SECRET_KEY=your_secret_key_here_generate_with_secrets.token_hex(32)
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTE=30
```

### Generating a Secret Key
```python
import secrets
print(secrets.token_hex(32))
```

## ▶️ Running the Application

### 1. Start the Server
```bash
# Make sure you're in the backend directory and virtual environment is activated
python main.py
```

### 2. Alternative: Using Uvicorn Directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Server Information
- **Local URL**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 📚 API Documentation

FastAPI automatically generates interactive API documentation:

### Swagger UI (Recommended)
Visit: **http://localhost:8000/docs**
- Interactive API testing
- Request/response examples
- Authentication testing
- Schema documentation

### ReDoc
Visit: **http://localhost:8000/redoc**
- Clean, readable documentation
- Detailed schema information
- Code examples

## 🧪 Testing

### Manual Testing Script
Run the provided test script to verify all endpoints:

```bash
python test_product_api.py
```

### Test Coverage
The test script validates:
- ✅ User registration and login
- ✅ Product creation with unique SKUs
- ✅ Product listing with pagination
- ✅ Product quantity updates
- ✅ Duplicate SKU validation
- ✅ Authentication token handling

### Expected Test Output
```
Testing Product API Endpoints...
1. Testing Authentication...
User Registration: PASSED
Login Test: PASSED

2. Testing Add Product...
Add Product: PASSED

3. Testing Get Products...
Get Products: PASSED (Quantity = 15)

4. Testing Update Quantity...
Update Quantity: PASSED, Updated quantity: 15

5. Testing Duplicate SKU...
Duplicate SKU: PASSED (should fail)

API testing completed!
```

## 📮 Postman Collection

### Setting Up Postman

1. **Create New Collection**: "FiMoney API"

2. **Set Collection Variables**:
   ```
   base_url: http://localhost:8000
   token: (will be set automatically)
   ```

3. **Import Endpoints**: Create folders for Authentication, Users, and Products

4. **Authentication Flow**:
   - Signup → Login → Save Token → Use in other requests

### Key Postman Requests

**Authentication:**
- POST `/auth/signup` - Register user
- POST `/auth/login` - Get access token

**Products:**
- POST `/products/` - Create product
- GET `/products/?page=1&size=10` - List products
- PUT `/products/{id}/quantity` - Update quantity

**Users:**
- GET `/users/me` - Current user info
- GET `/users/` - All users

## 🔒 Security

### Security Features Implemented
- **Password Hashing**: Bcrypt with salt rounds
- **JWT Tokens**: Secure token-based authentication
- **Input Validation**: Pydantic schema validation
- **SQL Injection Protection**: SQLAlchemy ORM
- **Environment Variables**: Sensitive data protection

### Security Best Practices
- Never commit `.env` files
- Use strong secret keys (32+ characters)
- Implement token expiration
- Validate all user inputs
- Use HTTPS in production

### Production Security Recommendations
```python
# Use strong secret keys
SECRET_KEY = secrets.token_hex(32)

# Set appropriate token expiration
ACCESS_TOKEN_EXPIRE_MINUTE = 30

# Use environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
```

## 🛠️ Development

### Adding New Features
1. **Models**: Add database models in `models/`
2. **Schemas**: Define Pydantic schemas in `schemas/`
3. **Routes**: Create API endpoints in `routers/`
4. **Register**: Include router in `main.py`

### Database Migrations
```python
# Add to main.py after model creation
from models.your_model import YourModel
YourModel.metadata.create_all(bind=engine)
```

### Code Structure Guidelines
- **Models**: SQLAlchemy database models
- **Schemas**: Pydantic request/response models
- **Routes**: FastAPI endpoint definitions
- **Core**: Utility functions (auth, etc.)

## 🚀 Deployment

### Production Setup
1. **Use PostgreSQL** instead of SQLite
2. **Set Environment Variables** securely
3. **Use HTTPS** with SSL certificates
4. **Configure CORS** for frontend integration
5. **Set up proper logging**

### Environment Variables for Production
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m 'Add feature'`
4. **Push to branch**: `git push origin feature-name`
5. **Submit pull request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Write tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Pranjali Rathi** - [GitHub Profile](https://github.com/pranjalirathi)

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy ORM framework
- JWT authentication standards
- Python security best practices

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check the documentation**: http://localhost:8000/docs
2. **Run tests**: `python test_product_api.py`
3. **Check logs**: Server console output
4. **Create an issue**: GitHub repository issues

---

**⭐ Star this repository if you found it helpful!**
