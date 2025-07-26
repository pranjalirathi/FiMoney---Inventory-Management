from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
import math

from database import get_db
from core.auth import get_current_user
from models.user import User
from models.product import Product
from schemas.product import ProductCreate, ProductCreateResponse, ProductQuantityUpdate, ProductResponse, ProductListResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductCreateResponse)
async def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        db_product = Product(
            name=product.name,
            type=product.type,
            sku=product.sku,
            image_url=product.image_url,
            description=product.description,
            quantity=product.quantity,
            price=product.price,
            created_by=current_user.id
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        
        return ProductCreateResponse(
            product_id=db_product.id,
            message=f"Product '{db_product.name}' created successfully"
        )
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Product creation failed")



@router.get("/", response_model=ProductListResponse)
async def get_products(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    offset = (page - 1) * size
    
    total = db.query(Product).count()
    products = db.query(Product).offset(offset).limit(size).all()
    total_pages = math.ceil(total / size)
    
    return ProductListResponse(
        products=products,
        total=total,
        page=page,
        size=size,
        total_pages=total_pages
    )

@router.put("/{product_id}/quantity", response_model=ProductResponse)
async def update_product_quantity(
    product_id: int,
    quantity_update: ProductQuantityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this product")
    product.quantity = quantity_update.quantity
    
    db.commit()
    db.refresh(product)
    return product


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this product")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
