import React from 'react'
import { FaUserCircle } from "react-icons/fa"
import { FaCloudUploadAlt } from "react-icons/fa"
import { FaChartBar } from "react-icons/fa"
import { FaHistory } from 'react-icons/fa'
import Button from './Button'

const Navbar = () => {
  return (
      <>
        <nav className="nav-horizontal">
            <img id='logo-nav' src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Ternium_Logo.svg/1200px-Ternium_Logo.svg.png" alt="logo" />
            < FaUserCircle id='profile-icon' />
        </nav>
        <nav className='nav-vertical'>
            <Button text='Subir Archivo' style='btn-subir-archivo' icon={<FaCloudUploadAlt className='' />}/>
            <Button text='Dashboard' style='btn' icon={<FaChartBar />} />
            <Button text='Historial' style='btn' icon={<FaHistory />}/>
        </nav>
    </>
  )
}

export default Navbar