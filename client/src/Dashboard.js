import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Banner from './components/Banner';
import Navbar from './components/Navbar';
import Hero  from './components/Hero';

const Dashboard = () => {
  const [courseCode, setCourseCode] = useState('');
  const [classCodes, setClassCodes] = useState([]);
  const [activeSnipes, setActiveSnipes] = useState([]);
  const [inactiveSnipes, setInactiveSnipes] = useState([]);
  const [error, setError] = useState('');
  const [username, setUsername] = useState('');
  const [loading, setLoading] = useState(false);
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

    const fetchActiveSnipes = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/snipes', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setActiveSnipes(response.data);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch active snipes');
      }
    };

    const fetchInactiveSnipes = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/snipes/inactive', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setInactiveSnipes(response.data);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch inactive snipes');
      }
    };

    const fetchClassCodes = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/class_codes');
        setClassCodes(response.data);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch class codes');
      }
    };

    fetchUserData();
    fetchActiveSnipes();
    fetchInactiveSnipes();
  }, [navigate]);

  const handleChange = (e) => {
    let input = e.target.value.toUpperCase(); // Convert input to uppercase
    input = input.replace(/([A-Z])(?=\d)/g, '$1 '); // Add a space before a digit if preceded by a letter
    setCourseCode(input);
    setError('');
  };
  

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (inactiveSnipes.length >= 5) {
      setError('You have reached the maximum number of inactive snipes (5). Please delete some before adding more.');
      return;
    }
  
    try {
      const token = localStorage.getItem('token');
      const response = await axios.get(`http://localhost:3001/api/class_codes/${courseCode}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
  
      if (!response.data.exists) {
        const confirmed = window.confirm('Course Code does not exist in the catalog. Do you want to proceed?');
        if (!confirmed) {
          return;
        }
      }
    } catch (err) {
      console.error(err);
      setError('Error checking course code. Please try again.');
      return;
    }
  
    if (activeSnipes.includes(courseCode)) {
      setError('Course Code already added.');
      return;
    }
  
    try {
      setLoading(true);
      const token = localStorage.getItem('token');
      await axios.post('http://localhost:3001/api/snipes', { courseCode }, {
        headers: { Authorization: `Bearer ${token}` },
      });
  
      setActiveSnipes([...activeSnipes, courseCode]);
      setCourseCode('');
      setError('');
  
      // Show success alert
      alert('Class code added successfully. You will receive notifications when this class opens.');
    } catch (err) {
      console.error(err);
      if (err.response && err.response.status === 400) {
        setError('Maximum number of active snipes reached');
      } else {
        setError('Error adding course. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };
  

  const handleDeactivate = async (courseCode) => {
    try {
      const token = localStorage.getItem('token');
      await axios.put('http://localhost:3001/api/snipes/deactivate', { courseCode }, {
        headers: { Authorization: `Bearer ${token}` },
      });

      setActiveSnipes(activeSnipes.filter(code => code !== courseCode));
      setInactiveSnipes([...inactiveSnipes, courseCode]);
    } catch (err) {
      console.error(err);
      setError('Error deactivating course. Please try again.');
    }
  };

  const handleReactivate = async (courseCode) => {
    if (inactiveSnipes.length >= 5) {
      setError('You have reached the maximum number of inactive snipes (5). Please delete some before reactivating more.');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      await axios.put('http://localhost:3001/api/snipes/reactivate', { courseCode }, {
        headers: { Authorization: `Bearer ${token}` },
      });

      setInactiveSnipes(inactiveSnipes.filter(code => code !== courseCode));
      setActiveSnipes([...activeSnipes, courseCode]);
    } catch (err) {
      console.error(err);
      if (err.response && err.response.status === 400) {
        setError('Maximum number of active snipes reached');
      } else {
        setError('Error reactivating course. Please try again.');
      }
    }
  };

  const handleDelete = async (courseCode) => {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.put('http://localhost:3001/api/snipes/delete', { courseCode }, {
        headers: { Authorization: `Bearer ${token}` },
      });
  
      if (response.status === 200) {
        console.log('Course code deleted successfully');      
        // Refresh the page
        window.location.reload();
      } else {
        console.error('Failed to delete course code:', response.data);
      }
    } catch (error) {
      console.error('Error deleting course code:', error);
    }
  };
  

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
              <div className="text-white rounded-lg p-6 w-full justify-center">
                <h1 className="text-xl mb-4">Enter Class Code</h1>
                <form onSubmit={handleSubmit}>
                  <div className="mb-4">                    <input
                      type="text"
                      className="bg-gray-700 text-white border border-gray-700 rounded px-3 py-2 w-50"
                      id="courseCode"
                      value={courseCode}
                      onChange={handleChange}
                      required
                      disabled={loading}
                      placeholder='Example ABC 12345'
                    />
                  </div>
                  <button type="submit" className="bg-white hover:bg-gray-500 text-black py-2 px-4 rounded px-4 py-2 disabled:opacity-50" disabled={loading}>
                    {loading ? 'Adding...' : 'Add Course Code'}
                  </button>
                </form>
                {error && <p className="text-red-500 mt-2">{error}</p>}
              </div>
            ) : (
              <div className="bg-gray-800 text-white rounded-lg shadow-md p-4 mb-4">
                <Navbar username={username} handleLogout={handleLogout} />
              </div>
            )}
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <div className="col">
            <div className="text-white rounded-lg p-6">
              <h2 className="text-xl mb-4">Active Snipe List</h2>
              <ul className="list-none">
                {activeSnipes.map((code, index) => (
                  <li key={index} className="flex items-center justify-between rounded-lg px-4 py-2 mb-2 shadow-md">
                    <span>{code}</span>
                    <button className="bg-red-500 hover:bg-red-600 text-white rounded px-3 py-1" onClick={() => handleDeactivate(code)}>Deactivate</button>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          <div className="col">
            <div className="text-white rounded-lg  p-6">
              <h2 className="text-xl mb-4">Inactive Snipe List</h2>
              <ul className="list-none">
                {inactiveSnipes.map((code, index) => (
                  <li key={index} className="flex items-center justify-between rounded-lg px-4 py-2 mb-2 shadow-md">
                    <span>{code}</span>
                    <div>
                      <button className="bg-blue-500 hover:bg-green-600 text-white rounded px-3 py-1 mr-2" onClick={() => handleReactivate(code)}>Reactivate</button>
                      <button className="bg-red-500 hover:bg-red-600 text-white rounded px-3 py-1" onClick={() => handleDelete(code)}>Delete</button>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
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

export default Dashboard;
