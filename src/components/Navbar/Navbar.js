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
            <img id='logo-nav' src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Ternium_Logo.svg/1200px-Ternium_Logo.svg.png" alt="logo" />
        </nav>
        <nav className='nav-vertical'>
          <Link to='/'>
            <Button text='Subir Archivo' style={`btn ${'upload' === selected ? 'btn-selected' : ''}`} icon="cloud"/>
          </Link>
          <Link to='/Dashboard'>
            <Button text='Dashboard' style={`btn ${'dashboard' === selected ? 'btn-selected' : ''}`} icon="chart"/>
          </Link>
          <Link to='/Historial'>
            <Button text='Historial' style={`btn ${'history' === selected ? 'btn-selected' : ''}`} icon="history"/>
          </Link>
        </nav>
    </>
  )
}

export default Navbar