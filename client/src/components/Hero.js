import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Hero = () => {
    const location = useLocation();

    return (
      <div className='bg-black'>
        <div className="px-4">
        <div className="py-3 flex items-center justify-between">
        <div className="container">
            <div className='flex items-center justify-center'>
            
            <a href = "#" className='border py-1 px-2 rounded-lg border-white/30'>
                <span className='bg-gradient-to-r from-pink-500 via-purple-500 via-yellow-500 to-blue-500 bg-clip-text text-transparent text-xl'> Version 1.0 is here</span>
            </a>
            </div>
        </div>
      </div>
      </div>
      </div>
    );
  };

  export default Hero;