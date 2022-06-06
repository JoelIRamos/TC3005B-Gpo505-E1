import React from 'react'
import './Atributos.css'

const Atributos = ({data, onClick}) => {
  return (
    <button onClick={((e) => onClick(data))} className='atributo'>{data}</button>
  )
}

export default Atributos