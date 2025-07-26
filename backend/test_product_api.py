import requests
import json

# Base URL for your API
BASE_URL = "http://localhost:8000"

def test_signup_and_login():
    """Test user signup and login, return token"""
    # Signup
    signup_data = {
        "username": "testuser3",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
    print("Signup Response:", response.status_code, response.json())
    
    # Login
    login_data = {
        "username": "testuser3",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    print("Login Response:", response.status_code)
    if response.status_code == 200:
        return response.json()["access_token"]
    return None

def test_add_product(token):
    """Test adding a product"""
    headers = {"Authorization": f"Bearer {token}"}
    
    product_data = {
        "name": "Gaming Laptop",
        "type": "Electronics",
        "sku": "GLT-001",
        "image_url": "https://example.com/gaming-laptop.jpg",
        "description": "High-performance gaming laptop with RTX graphics",
        "quantity": 50,
        "price": 1299.99
    }
    
    response = requests.post(f"{BASE_URL}/products/", json=product_data, headers=headers)
    print("Add Product Response:", response.status_code, response.json())
    
    if response.status_code == 200:
        response_data = response.json()
        print(f"Product ID: {response_data['product_id']}")
        print(f"Message: {response_data['message']}")
        return response_data["product_id"]
    return None

def test_get_products(token):
    """Test getting products with pagination"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test pagination
    response = requests.get(f"{BASE_URL}/products/?page=1&size=5", headers=headers)
    print("Get Products Response:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(f"Total products: {data['total']}")
        print(f"Page: {data['page']}, Size: {data['size']}")
        print(f"Total pages: {data['total_pages']}")
        print(f"Products returned: {len(data['products'])}")
        
        # Print first product details if any
        if data['products']:
            product = data['products'][0]
            print(f"First product: {product['name']} (SKU: {product['sku']})")
    
    return response.status_code == 200

def test_update_product_quantity(token, product_id):
    """Test updating product quantity"""
    headers = {"Authorization": f"Bearer {token}"}
    
    quantity_data = {"quantity": 75}
    
    response = requests.put(f"{BASE_URL}/products/{product_id}/quantity", 
                          json=quantity_data, headers=headers)
    print("Update Quantity Response:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(f"Updated product quantity: {data['quantity']}")
    else:
        print("Error:", response.json())
    
    return response.status_code == 200

def test_duplicate_sku(token):
    """Test adding product with duplicate SKU"""
    headers = {"Authorization": f"Bearer {token}"}
    
    product_data = {
        "name": "Another Laptop",
        "type": "Electronics",
        "sku": "GLT-001",  # Same SKU as before
        "image_url": "https://example.com/another-laptop.jpg",
        "description": "Another laptop",
        "quantity": 10,
        "price": 999.99
    }
    
    response = requests.post(f"{BASE_URL}/products/", json=product_data, headers=headers)
    print("Duplicate SKU Response:", response.status_code, response.json())
    
    return response.status_code == 400  # Should fail

if __name__ == "__main__":
    print("Testing Product API Endpoints...")
    print("Make sure your FastAPI server is running on localhost:8000")
    
    # Get authentication token
    print("\n1. Testing Authentication...")
    token = test_signup_and_login()
    
    if token:
        print(f"\nAuthentication successful! Token: {token[:20]}...")
        
        # Test adding a product
        print("\n2. Testing Add Product...")
        product_id = test_add_product(token)
        
        if product_id:
            print(f"Product created with ID: {product_id}")
            
            # Test getting products
            print("\n3. Testing Get Products with Pagination...")
            test_get_products(token)
            
            # Test updating product quantity
            print("\n4. Testing Update Product Quantity...")
            test_update_product_quantity(token, product_id)
            
            # Test duplicate SKU
            print("\n5. Testing Duplicate SKU (should fail)...")
            test_duplicate_sku(token)
    
    print("\nAPI testing completed!")
