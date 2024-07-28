// Banner.js
import React from 'react';

const Banner = () => {
  return (
    <div className="py-2 text-center" style={{ background: 'linear-gradient(to right, #FCD6FF, #29D8FF, #FFFD80, #F89ABF, #FCD6FF)' }}>
      <div className="container">
        <p className="font-medium">
          <span className="hidden sm:inline"> Register for your classes the moment they open -{" "} </span>
          <a href="#" className="underline underline-offset-2 font-medium">
            CourseSniper
          </a>
        </p>
      </div>
    </div>
  );
};

export default Banner;
