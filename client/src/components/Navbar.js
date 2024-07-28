import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import logoImage from '../assets/images/cs-high-resolution-logo-transparent.png';

const Navbar = ({ username, handleLogout }) => {
  const location = useLocation();

  return (
    <div className="bg-black">
      <div className="px-4">
        <div className="py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="relative">
              <div className="absolute w-full top-0 bottom-0 bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 blur-md"></div>
              <div className="absolute w-full top-2.1 bottom-1 bg-black rounded-full h-11 w-12"></div>
              <img src={logoImage} alt="logo" className="h-13 w-12 relative" />
            </div>
            <h1 className="text-white font-bold text-2xl ml-4 relative hidden sm:flex">{username}</h1>
          </div>
          <nav className="flex gap-6 items-center hidden sm:flex">
            <Link to="/home" className={`text-opacity-60 text-white hover:text-opacity-100 transition ${location.pathname === '/home' ? 'text-white text-lg font-bold' : 'text-opacity-100'}`}>Home</Link>
            <Link to="/dashboard" className={`text-opacity-60 text-white hover:text-opacity-100 transition ${location.pathname === '/dashboard' ? 'text-white text-lg font-bold' : 'text-opacity-100'}`}>Dashboard</Link>
            <Link to="/account" className={`text-opacity-60 text-white hover:text-opacity-100 transition ${location.pathname === '/account' ? 'text-white text-lg font-bold' : 'text-opacity-100'}`}>Account</Link>
            <Link to="/about" className={`text-opacity-60 text-white hover:text-opacity-100 transition ${location.pathname === '/about' ? 'text-white text-lg font-bold' : 'text-opacity-100'}`}>About</Link>
            
            {username ? (
              <button className="bg-white py-2 px-4 rounded-lg" onClick={handleLogout}>Log out</button>
            ) : (
              <Link to="/login" className="bg-white py-2 px-4 rounded-lg text-center">Log in</Link>
            )}
          </nav>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
