import React from 'react'
import './Atributos.css'

const Atributos = ({data, onClick, color}) => {
  return (
    <button onClick={((e) => onClick(data))} className={`atributo ${color}`}>{data}</button>
  )
}

export default Atributos