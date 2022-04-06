import React from 'react'
import './ContenedorDatos.css'

const ContenedorDatos = ({datos, label, color}) => {
  return (
    <div className={`contenedor-datos ${color}`}>
        <h1>{datos}</h1>
        <p>{label}</p>
    </div>
  )
}

export default ContenedorDatos