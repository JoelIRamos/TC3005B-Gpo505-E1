import React from 'react'
import { FaUserCircle } from "react-icons/fa"
import { Link } from "react-router-dom";
import Button from '../Button/Button'
import '../../App.css';


const Navbar = () => {
  return (
      <>
        <nav className="nav-horizontal">
            <img id='logo-nav' src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Ternium_Logo.svg/1200px-Ternium_Logo.svg.png" alt="logo" />
            < FaUserCircle id='profile-icon' />
        </nav>
        <nav className='nav-vertical'>
          <Link to='/'>
            <Button text='Subir Archivo' style='btn btn-subir-archivo' icon="cloud"/>
          </Link>
          <Link to='/Dashboard'>
            <Button text='Dashboard' style='btn' icon="chart"/>
          </Link>
          <Link to='/Historial'>
            <Button text='Historial' style='btn' icon="history"/>
          </Link>
        </nav>
    </>
  )
}

export default Navbar