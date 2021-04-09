import React, { useState, useEffect, Fragment } from 'react';
import backendLookup from '../../lookup/Components';

const Logout = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') == null) {
      window.location.replace('http://localhost:3000/login');
    } else {
      setLoading(false);
    }
  }, []);

  const handleLogout = e => {
    e.preventDefault();

    function resData(data) {
      localStorage.clear();
      window.location.replace('http://localhost:3000/login');
    };

    backendLookup(
      'http://127.0.0.1:8000/api/accounts/auth/logout/',
      'POST',
      `Token ${localStorage.getItem('token')}`,
      resData
    )    
  };

  return (
    <div>
      {loading === false && (
        <Fragment>
          <h1>Are you sure you want to logout?</h1>
          <input type='button' value='Logout' onClick={handleLogout} />
        </Fragment>
      )}
    </div>
  );
};

export default Logout;