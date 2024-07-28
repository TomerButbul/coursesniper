import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import Banner from './components/Banner';
const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { email, password } = formData;

    try {
      const response = await axios.post('http://localhost:3001/api/login', {
        email,
        password
      });

      localStorage.setItem('token', response.data.token); // Store the token in local storage
      console.log(response.data);
      setError('');
      // Redirect to dashboard upon successful login
      navigate('/home');
    } catch (err) {
      console.error(err);
      setError('Invalid email or password');
    }
  };

  return (
    <>
    <Banner />
    <div className='bg-black text-white py-[72px]' style={{background:'linear-gradient(to bottom, #000, #200D42 50%,#4F21A1 80%,#A46EDB 99%)'}}>
      <div className="py-5">
        <div className="flex justify-center">
          <div className="w-full max-w-md">
            <div className="text-white rounded-lg shadow-md p-6">
              <h1 className="text-center mb-3 text-xl">Login</h1>
              <form onSubmit={handleSubmit}>
                <div className="mb-4">
                  <label className="block mb-2">Email:</label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className="bg-gray-700 text-white rounded-lg w-full px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>
                <div className="mb-4">
                  <label className="block mb-2">Password:</label>
                  <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    className="bg-gray-700 text-white rounded-lg w-full px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>
                {error && <p className="text-red-500">{error}</p>}
                <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg w-full">Log In</button>
              </form>
              <p className="mt-3 text-center">
                Don't have an account? <Link to="/signup" className="text-blue-500 hover:underline">Sign up</Link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </>
);
};


export default Login;
