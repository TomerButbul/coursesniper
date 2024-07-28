import React from 'react';
import Banner from './components/Banner';
import Navbar from './components/Navbar';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Hero from './components/Hero';


const HomePage = () => {
    const [error, setError] = useState('');
    const [username, setUsername] = useState('');
    const navigate = useNavigate();
    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
          navigate('/login');
          return;
        }
    
        const fetchUserData = async () => {
          try {
            const response = await axios.get('http://localhost:3000/api/users', {
              headers: { Authorization: `Bearer ${token}` },
            });
            setUsername(response.data.username);
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
    <Banner/>
<Navbar username={username} handleLogout={handleLogout}/>
<Hero/>
<div className="bg-gray-900 text-white min-h-screen">
      <header className="px-4 py-4">
        <div className="flex items-center justify-between">
        </div>
      </header>
      <main className="container mx-auto px-4 py-8">
        <section id="how-it-works" className="mb-8">
          <h2 className="text-3xl font-semibold mb-4">How CourseSniper Works</h2>
          <p className="text-lg leading-relaxed">
            CourseSniper allows you to add class codes from Purdue's catalog to your snipe list. 
            It constantly monitors class availability and notifies you via email and text when a spot opens up.
          </p>
        </section>

        <section id="dashboard" className="mb-8">
          <h2 className="text-3xl font-semibold mb-4">Dashboard</h2>
          <p className="text-lg leading-relaxed">
            The dashboard lets you add a class to your snipe list and view both active and inactive snipes.
          </p>
        </section>
      </main>

      <footer className="bg-gray-800 text-center py-4">
        <p className="text-white">&copy; 2024 CourseSniper. All rights reserved.</p>
      </footer>
    </div>

    </>
  );
};

export default HomePage;
