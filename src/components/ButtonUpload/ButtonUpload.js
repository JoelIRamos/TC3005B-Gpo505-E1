import React from 'react'
import './ButtonUpload.css'
import {FaCloudUploadAlt} from 'react-icons/fa'

const ButtonUpload = () => {
  return (
    <div className='button-up-container'>
        <div className="btn-text-container">
            < FaCloudUploadAlt className='button-up-icon'/>
            <p>Selecciona un Archivo</p>
        </div>
        <button className='button-up'>Subir Archivo</button>
    </div>
  )
}

export default ButtonUpload