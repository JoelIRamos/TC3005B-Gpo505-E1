import { upload } from '@testing-library/user-event/dist/upload';
import React from 'react'
import { FaUserCircle } from "react-icons/fa"
import { Link } from "react-router-dom";
import Button from '../Button/Button.js'
import './Navbar.css'

const Navbar = ({selected}) => {
  return (
      <>
        <nav className="nav-horizontal">
          <div className="logo-container">
            <Link to='/'>
              <button className="home-button">
                <img id='logo-nav' src="https://upload.wikimedia.org/wikipedia/commons/8/83/Ternium_Logo.svg" alt="logo" />
              </button>
            </Link>
          </div>
            <div className="button-container">
              <Link to='/FileUpLoad'>
                <Button text='Subir Archivo' style={`btn ${'upload' === selected ? 'btn-selected' : ''}`}/>
              </Link>
              <Link to='/Dashboard'>
                <Button text='Dashboard' style={`btn ${'dashboard' === selected ? 'btn-selected' : ''}`}/>
              </Link>
              <Link to='/Historial'>
                <Button text='Historial' style={`btn ${'history' === selected ? 'btn-selected' : ''}`}/>
              </Link>
            </div>
            <div className="user-container">
              <FaUserCircle size={50}/>
            </div>
        </nav>
    </>
  )
}

export default Navbar