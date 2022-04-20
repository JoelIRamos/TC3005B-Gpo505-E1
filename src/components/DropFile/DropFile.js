import './DropFile.css'
import { FaCloudUploadAlt, FaFileExcel } from 'react-icons/fa'
import React, { useRef, useState } from 'react'
import PropTypes from 'prop-types'

const DropFile = ({onFileChange}) => {

  const wrapperRef = useRef(null);

  const [fileList, setFileList] = useState([])

  const onDragEnter = () => wrapperRef.current.classList.add('dragover')

  const onDragLeave = () => wrapperRef.current.classList.remove('dragover')

  const onDrop = () => wrapperRef.current.classList.remove('dragover')

  const onFileDrop = (e) => {
    const newFile = e.target.files[0]
    if (newFile){
      if (newFile) {
        const updatedList = [...fileList, newFile]
        setFileList(updatedList)
        onFileChange(updatedList)
      }
    }
  }

  const fileRemove = (file) => {
    const updatedList = [...fileList]
    updatedList.splice(fileList.indexOf(file), 1)
    setFileList(updatedList)
    onFileChange(updatedList)
  }

  return (
    <>
    <div className='drop-file-input-container'>
      <div className="icon-text-container">
        <FaCloudUploadAlt className='drop-file-icon'/>
        <h2>Sube Aquí tu Archivo</h2>
      </div>
      {fileList.length === 0 && <div 
          ref={wrapperRef} 
          className='drop-file-input' 
          onDragEnter={onDragEnter} 
          onDragLeave={onDragLeave} 
          onDrop={onDrop}
        >
          <div className="drop-file-input__label">
            <p>Arrastra aquí el archivo o clickea para seleccionarlo directamente</p>
          </div>
          <input type="file" value="" onChange={onFileDrop}/>
        </div>}
        {
          fileList.length > 0 ? (
              <div className="drop-file-preview">
                  <button className="drop-file-button">
                      Listo para cargar
                  </button>
                  {
                      fileList.map((item, index) => (
                          <div key={index} className="drop-file-preview__item">
                              <div className="drop-file-preview__item__info">
                                <p>{item.name}</p>
                              </div>
                              <span className="drop-file-preview__item__del" onClick={() => fileRemove(item)}>x</span>
                          </div>
                      ))
                  }
              </div>
          ) : null
      }
    </div>
    </>
  )
}

export default DropFile