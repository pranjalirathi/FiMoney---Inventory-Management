# 🏦 FiMoney - Inventory Management System

**A modern, full-stack inventory management system built with FastAPI backend and React frontend, featuring JWT authentication, product management, and responsive UI design.**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## ⚙️ POSTMAN API Documentation Link:

https://www.postman.com/grey-crescent-113665/workspace/fimoney-backend-apis/collection/36707787-41b8e109-c347-407d-b53d-812d131672be?action=share&source=copy-link&creator=36707787


## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Installation & Setup](#-installation--setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Frontend Features](#-frontend-features)
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

### 🎨 Frontend Features
- **Responsive React UI** with modern design patterns
- **Interactive Login/Register Forms** with real-time validation
- **Product Dashboard** with grid layout and search functionality
- **JWT Token Management** with automatic authentication handling
- **Custom Green/Gold Theme** for professional financial appearance
- **Error Handling** with user-friendly messages
- **Mobile-First Design** optimized for all screen sizes
- **Component-Based Architecture** for maintainability

## 🚀 Tech Stack

### Frontend Framework
- **[React 18](https://reactjs.org/)** - Modern JavaScript library for building user interfaces
- **[Vite](https://vitejs.dev/)** - Next-generation frontend build tool with HMR
- **[JavaScript ES6+](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Modern JavaScript features
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Styling with custom themes and responsive design

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
- **[Node.js](https://nodejs.org/)** - JavaScript runtime for frontend development
- **[npm](https://www.npmjs.com/)** - Package manager for JavaScript

### Frontend HTTP Client
- **[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)** - Modern HTTP client for API communication

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
├── frontend/
│   ├── public/
│   │   ├── index.html           # HTML template
│   │   └── vite.svg             # Vite logo
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.jsx        # Login/Register component
│   │   │   ├── Login.css        # Login component styles
│   │   │   ├── Dashboard.jsx    # Main dashboard component
│   │   │   └── Dashboard.css    # Dashboard component styles
│   │   ├── App.jsx              # Main React component
│   │   ├── App.css              # Global application styles
│   │   └── main.jsx             # React entry point
│   ├── package.json             # Frontend dependencies
│   ├── package-lock.json        # Locked dependency versions
│   ├── vite.config.js           # Vite configuration
│   └── .gitignore               # Frontend git ignore rules
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
- **Node.js 16 or higher**
- **npm** (Node package manager)
- **Git** (for cloning the repository)

### 1. Clone the Repository
```bash
git clone https://github.com/pranjalirathi/FiMoney---Inventory-Management.git
cd FiMoney---Inventory-Management
```

## Backend Setup

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

### 4. Install Backend Dependencies
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

## Frontend Setup

### 6. Navigate to Frontend Directory
```bash
# Open a new terminal or navigate back to root
cd ../frontend
```

### 7. Install Frontend Dependencies
```bash
npm install
```

### 8. Configure Frontend API URL
The frontend is pre-configured to connect to the backend at `http://localhost:8000`. If you need to change this, update the API URLs in the React components.

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

### 1. Start the Backend Server
```bash
# Make sure you're in the backend directory and virtual environment is activated
cd backend
python main.py
```

### 2. Alternative: Using Uvicorn Directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start the Frontend Development Server
```bash
# Open a new terminal and navigate to frontend directory
cd frontend
npm run dev
```

### 4. Application URLs
- **Frontend Application**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

### 5. Development Workflow
1. Start the backend server first (runs on port 8000)
2. Start the frontend development server (runs on port 5173)
3. The frontend will automatically connect to the backend API
4. Any changes to frontend code will trigger hot reload
5. Backend changes require server restart

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

## 🎨 Frontend Features

### User Interface Components
- **Login/Register Form**: Unified authentication component with toggle functionality
- **Dashboard**: Product management interface with responsive grid layout
- **Navigation**: Clean header with user info and logout functionality
- **Error Handling**: User-friendly error messages and loading states

### Design & Styling
- **Custom Green/Gold Theme**: Professional financial color scheme
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox
- **Smooth Animations**: Hover effects and transitions for better UX
- **Modern UI Elements**: Rounded corners, shadows, and gradients

### Authentication Flow
- **JWT Token Management**: Automatic token storage and validation
- **Protected Routes**: Conditional rendering based on authentication state
- **Session Persistence**: Login state maintained across browser sessions
- **Automatic Logout**: Token expiration handling

### Frontend Development Features
- **Hot Module Replacement**: Instant updates during development
- **Component Architecture**: Reusable React components
- **Modern JavaScript**: ES6+ features and async/await patterns
- **CSS Modules**: Scoped styling for component isolation

### Frontend Commands
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

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

### Frontend Testing
To test the full application:

1. **Start both servers** (backend on :8000, frontend on :5173)
2. **Navigate to** http://localhost:5173
3. **Test user registration** with unique username
4. **Test login functionality** with created credentials
5. **Verify dashboard** displays products correctly
6. **Test logout functionality** clears authentication state

### Manual Testing Checklist
- [ ] Registration with new username
- [ ] Login with valid credentials
- [ ] Dashboard loads product data
- [ ] Responsive design on mobile/tablet
- [ ] Error handling for invalid credentials
- [ ] Token persistence across browser refresh
- [ ] Logout functionality works correctly

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
- **Backend Models**: SQLAlchemy database models
- **Backend Schemas**: Pydantic request/response models
- **Backend Routes**: FastAPI endpoint definitions
- **Backend Core**: Utility functions (auth, etc.)
- **Frontend Components**: React functional components
- **Frontend Styles**: Component-specific CSS files
- **Frontend Utils**: Helper functions and API calls

## 🚀 Deployment

### Backend Production Setup
1. **Use PostgreSQL** instead of SQLite
2. **Set Environment Variables** securely
3. **Use HTTPS** with SSL certificates
4. **Configure CORS** for frontend integration
5. **Set up proper logging**
6. **Use production ASGI server** (Gunicorn + Uvicorn)

### Frontend Production Setup
1. **Build the application**: `npm run build`
2. **Serve static files** with Nginx or CDN
3. **Configure API endpoints** for production URLs
4. **Enable HTTPS** for secure authentication
5. **Set up proper caching** headers

### Environment Variables for Production
```env
# Backend
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
CORS_ORIGINS=https://yourdomain.com

# Frontend (if needed)
VITE_API_URL=https://api.yourdomain.com
```

### Deployment Options

#### Frontend Deployment
- **Vercel**: `npm run build` → Deploy dist folder
- **Netlify**: Connect GitHub repo → Auto-deploy
- **AWS S3 + CloudFront**: Static hosting with CDN
- **Docker**: Multi-stage build with Nginx

#### Backend Deployment
- **Railway**: Direct GitHub integration
- **Heroku**: Git-based deployment
- **DigitalOcean App Platform**: Container deployment
- **AWS EC2**: Manual server setup
- **Docker**: Containerized deployment

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m 'Add feature'`
4. **Push to branch**: `git push origin feature-name`
5. **Submit pull request**

### Development Guidelines
- **Backend**: Follow PEP 8 style guidelines
- **Frontend**: Use ESLint and Prettier for code formatting
- **Components**: Keep React components small and focused
- **Styling**: Use component-specific CSS files
- **API Integration**: Use consistent error handling patterns
- **Documentation**: Add docstrings and comments
- **Testing**: Write tests for new features
- **Git**: Use descriptive commit messages

### Frontend Development Guidelines
- Use functional components with hooks
- Implement proper error boundaries
- Follow React best practices
- Maintain consistent component structure
- Use semantic HTML elements
- Ensure accessibility compliance
- Optimize for performance

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Pranjali Rathi** - [GitHub Profile](https://github.com/pranjalirathi)

## 🙏 Acknowledgments

- **Backend Technologies**:
  - FastAPI documentation and community
  - SQLAlchemy ORM framework
  - JWT authentication standards
  - Python security best practices

- **Frontend Technologies**:
  - React.js community and documentation
  - Vite build tool and development server
  - Modern CSS techniques and responsive design
  - JavaScript ES6+ features and best practices


## 🙏 AI USAGE
 AI tools were used to help in the creation of the README file for this repository with the tree structure. However it is being validated and edited after it. It was also used in getting some parts of the creation of the frontend design and for getting the approach for backend pagination api. 


**⭐ Star this repository if you found it helpful!**
