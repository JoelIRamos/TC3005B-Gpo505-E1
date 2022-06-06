import React from 'react'
import './Atributos.css'

// TODO: Agregar booleano para saber si es el atributo1 o el atributo2
const Atributos = ({atributos, idForm}) => {
  return (
      <div className='atributos'>
        <input type='radio' id={`radio-${atributos + idForm}`} name='atributo' value={atributos}/>
        <label htmlFor={`radio-${atributos + idForm}`}>{atributos}</label>
      </div>

  )
}

export default Atributos