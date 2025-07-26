import { useState } from 'react';
import './Login.css';

const Login = ({ onLogin }) => {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [isRegisterMode, setIsRegisterMode] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    // Clear messages when user starts typing
    if (error) setError('');
    if (success) setSuccess('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    const endpoint = isRegisterMode ? '/register' : '/login';
    const url = `http://127.0.0.1:8000${endpoint}`;

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        if (isRegisterMode) {
          // Registration successful
          setSuccess(data.message || 'Registration successful! You can now login.');
          setIsRegisterMode(false); // Switch to login mode
          setFormData({ username: '', password: '' }); // Clear form
        } else {
          // Login successful
          localStorage.setItem('token', data.access_token);
          localStorage.setItem('username', formData.username);
          
          // Call parent function to update app state
          onLogin(data.access_token, formData.username);
        }
      } else {
        // Handle different error cases
        if (response.status === 400 && isRegisterMode) {
          setError(data.message || 'Username already taken');
        } else if (response.status === 401 && !isRegisterMode) {
          setError('Incorrect username or password');
        } else {
          setError(data.detail || data.message || `${isRegisterMode ? 'Registration' : 'Login'} failed`);
        }
      }
    } catch (err) {
      setError('Network error. Please check if the server is running on http://127.0.0.1:8000');
    } finally {
      setLoading(false);
    }
  };

  const toggleMode = () => {
    setIsRegisterMode(!isRegisterMode);
    setError('');
    setSuccess('');
    setFormData({ username: '', password: '' });
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h2>{isRegisterMode ? 'Register for FiMoney' : 'Login to FiMoney'}</h2>
        
        {success && <div className="success-message">{success}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              placeholder="Enter your username"
              minLength={3}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              placeholder="Enter your password"
              minLength={3}
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button 
            type="submit" 
            className="login-button"
            disabled={loading}
          >
            {loading 
              ? (isRegisterMode ? 'Registering...' : 'Logging in...') 
              : (isRegisterMode ? 'Register' : 'Login')
            }
          </button>
        </form>

        <div className="login-footer">
          <p>
            {isRegisterMode ? 'Already have an account?' : "Don't have an account?"}{' '}
            <button 
              type="button" 
              className="toggle-mode-button" 
              onClick={toggleMode}
              disabled={loading}
            >
              {isRegisterMode ? 'Login here' : 'Register here'}
            </button>
          </p>
        </div>

        <div className="api-info">
          <small>
            Backend API: http://127.0.0.1:8000/{isRegisterMode ? 'register' : 'login'}
          </small>
        </div>
      </div>
    </div>
  );
};

export default Login;
