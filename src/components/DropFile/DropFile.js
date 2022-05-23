import './DropFile.css'
import { FaCloudUploadAlt, FaFileExcel } from 'react-icons/fa'
import React, { useRef, useState } from 'react'
import PropTypes from 'prop-types'

const DropFile = ({file, onFileDrop, fileRemove, setCsvFile, viewUpdate}) => {

  const wrapperRef = useRef(null);

  const onDragEnter = () => wrapperRef.current.classList.add('dragover')

  const onDragLeave = () => wrapperRef.current.classList.remove('dragover')

  const onDrop = () => wrapperRef.current.classList.remove('dragover')

  return (
    <>
    <div className='drop-file-input-container'>
      <div className="icon-text-container">
        <FaCloudUploadAlt className='drop-file-icon'/>
        <h2>Sube Aquí tu Archivo</h2>
      </div>
      {file === null && <div 
          ref={wrapperRef} 
          className='drop-file-input' 
          onDragEnter={onDragEnter} 
          onDragLeave={onDragLeave} 
          onDrop={onDrop}
        >
          <div className="drop-file-input__label">
            <p>Arrastra aquí el archivo o clickea para seleccionarlo directamente</p>
          </div>
          <input type="file" value="" onChange={onFileDrop} accept=".csv"/>
        </div>}
        {
          file !== null ? (
              <div className="drop-file-preview">
                  <button className="drop-file-button" onClick={() => {setCsvFile(); viewUpdate()}}>
                      Listo para cargar
                  </button>
                  <div className="drop-file-preview__item">
                      <div className="drop-file-preview__item__info">
                        <p>{file.name}</p>
                      </div>
                      <span className="drop-file-preview__item__del" onClick={() => fileRemove()}>x</span>
                  </div>
              </div>
          ) : null
      }
    </div>
    </>
  )
}

export default DropFile;