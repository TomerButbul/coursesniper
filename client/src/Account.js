import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Banner from './components/Banner';
import Navbar from './components/Navbar';

const Account = () => {
  const [error, setError] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      return;
    }

    const fetchUserData = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/users', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUsername(response.data.username);
        setEmail(response.data.email);
        setPhoneNumber(response.data.phone_number);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch user data');
      }
    };

    fetchUserData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    setUsername('');
    navigate('/login');
  };

  return (
    <>
      <Banner />
      <Navbar username={username} handleLogout={handleLogout} />
      <div className='bg-black text-white py-[72px]' style={{background:'linear-gradient(to bottom, #000, #200D42 50%,#4F21A1 80%,#A46EDB 99%)'}}>
        <div className="container mx-auto mt-1">
          <div className="grid grid-cols-1 md:grid-cols-1 gap-4">
            <div className="col-md-12">
              {username ? (
                <div className="text-white rounded-lg shadow-md p-6 w-full justify-center">
                  <p className="text-lg leading-relaxed">Username: {username}</p>
                  <p className="text-lg leading-relaxed">Email: {email}</p>
                  <p className="text-lg leading-relaxed">Phone Number: {phoneNumber || 'Not Provided'}</p>
                </div>
              ) : (
                <div className=" text-white rounded-lg shadow-md p-6 w-full justify-center">
                  <h2 className="text-3xl font-semibold mb-4">Account</h2>
                  <p className="text-lg leading-relaxed">You are not logged in.</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
      <footer className="bg-gray-800 text-center py-4">
        <p className="text-white">&copy; 2024 CourseSniper. All rights reserved.</p>
      </footer>
    </>
  );
};

export default Account;
