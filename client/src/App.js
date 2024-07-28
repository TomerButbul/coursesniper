import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Signup from './Signup';
import Login from './Login';
import Dashboard from './Dashboard';
import Account from './Account';
import Home from './Home';
import About from './About';
import axios from 'axios';
import './style.css';


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/account" element={<Account />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/home" element={ <Home/>} />
        <Route path="/about" element={<About />} />
        <Route path="/" element={<Navigate to="/home" />} /> {/* Default route */}
      </Routes>
    </Router>
  );
};

export default App;
