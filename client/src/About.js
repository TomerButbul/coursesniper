import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Banner from './components/Banner';
import Navbar from './components/Navbar';

const About = () => {
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
        const response = await axios.get('http://localhost:3001/api/users', {
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
      <Banner />
      <Navbar username={username} handleLogout={handleLogout} />
      <div className="bg-gray-900 text-white min-h-screen">
        <header className="px-4 py-4">
          <div className="flex items-center justify-between"></div>
        </header>
        <main className="container mx-auto px-4 py-8">
          <section id="how-it-works" className="mb-8">
            <h2 className="text-3xl font-semibold mb-4">About CourseSniper</h2>
            <ul className="list-disc pl-4">
              <li className="text-lg leading-relaxed">
                Built by a Computer Engineering Student to solve the problem of getting into classes.
              </li>
              <li className="text-lg leading-relaxed">
                Automates class registration without requiring technical expertise.
              </li>
              <li className="text-lg leading-relaxed">
                Instantly alerts students when a spot opens up in their desired class.
              </li>
            </ul>
          </section>

          <section id="dashboard" className="mb-8">
            <h2 className="text-3xl font-semibold mb-4">Contact Us</h2>
            <ul className="list-disc pl-4">
              <li className="text-lg leading-relaxed">
                Actively expanding to support more schools across the country.
              </li>
              <li className="text-lg leading-relaxed">
                Contact us if your school is not yet supported.
              </li>
              <li className="text-lg leading-relaxed">
                For any issues with CourseSniper, feel free to reach out to us via email.
              </li>
            </ul>
          </section>
        </main>

        <footer className="bg-gray-800 text-center py-4">
          <p className="text-white">&copy; 2024 CourseSniper. All rights reserved.</p>
        </footer>
      </div>
    </>
  );
};

export default About;
