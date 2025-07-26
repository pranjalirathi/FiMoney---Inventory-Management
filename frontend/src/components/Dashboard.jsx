import { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = ({ user, onLogout }) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/products/', {
        headers: {
          'Authorization': `Bearer ${user.token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const data = await response.json();
        setProducts(data.products || []);
      } else {
        setError('Failed to fetch products');
      }
    } catch (err) {
      setError('Network error. Please check if the server is running on http://127.0.0.1:8000');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <div className="header-content">
          <h1>FiMoney Dashboard</h1>
          <div className="user-info">
            <span>Welcome, {user.username}!</span>
            <button onClick={onLogout} className="logout-button">
              Logout
            </button>
          </div>
        </div>
      </header>

      <main className="dashboard-main">
        <div className="dashboard-content">
          <section className="products-section">
            <h2>Products</h2>
            
            {loading && <div className="loading">Loading products...</div>}
            
            {error && <div className="error-message">{error}</div>}
            
            {!loading && !error && (
              <div className="products-grid">
                {products.length > 0 ? (
                  products.map((product) => (
                    <div key={product.id} className="product-card">
                      <h3>{product.name}</h3>
                      <p className="product-type">{product.type}</p>
                      <p className="product-sku">SKU: {product.sku}</p>
                      <p className="product-description">{product.description}</p>
                      <div className="product-details">
                        <span className="product-quantity">Qty: {product.quantity}</span>
                        <span className="product-price">${product.price}</span>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="no-products">
                    <p>No products found. Create your first product!</p>
                  </div>
                )}
              </div>
            )}
          </section>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
