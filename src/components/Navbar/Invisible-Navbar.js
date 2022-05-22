import { upload } from '@testing-library/user-event/dist/upload';
import React from 'react'
import { FaUserCircle } from "react-icons/fa"
import { Link } from "react-router-dom";
import Button from '../Button/Button.js'
import './Navbar.css'


function InvNavbar() {
  return (
      <nav className="nav-horizontal-home">
        <div className="logo-container">
          <Link to='/'>
            <button className="home-button">
              <img id='logo-nav' src="https://upload.wikimedia.org/wikipedia/commons/8/83/Ternium_Logo.svg" alt="logo" />
            </button>
          </Link>
        </div>
          <div className="user-container">
            <FaUserCircle size={50}/>
          </div>
      </nav>
  )
}

export default InvNavbar