import React from 'react'
import './Titulo.css'

const Titulo = ({runId}) => {
  return (
    <div className='container-titulo'>
        <h1>
            {runId}
        </h1>
    </div>
  )
}

export default Titulo