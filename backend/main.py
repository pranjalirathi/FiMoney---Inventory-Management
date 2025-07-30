from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models.user import User
from models.product import Product

from routers import auth, users, products

User.metadata.create_all(bind=engine)
Product.metadata.create_all(bind=engine)

# Root app (serves only root or static if needed)
app = FastAPI(
    title="FiMoney Root",
    description="Handles root-level routes",
    version="1.0.0"
)

# Sub API app mounted at /api
api_app = FastAPI(
    title="FiMoney API",
    description="A Financial Money Management API with Authentication",
    version="1.0.0"
)

# CORS (for both frontend dev and production)
api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers in the API app
api_app.include_router(auth.router)
api_app.include_router(users.router)
api_app.include_router(products.router)

# Optional root endpoint for API
@api_app.get("/", tags=["API Root"])
def api_root():
    return {"message": "Welcome to the FiMoney API"}

# Mount the api app on /api
app.mount("/api", api_app)

# Optional root endpoint for the base app
@app.get("/", tags=["Root"])
def root():
    return {"message": "This is the base app. API is under /api"}
