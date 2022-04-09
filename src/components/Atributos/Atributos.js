import React from 'react'
import './Atributos.css'

// TODO: Agregar booleano para saber si es el atributo1 o el atributo2
const Atributos = ({atributos}) => {
  return (
      <div className='atributos'>
        <input type='radio' id={`radio-${atributos}`} name='atributo' value={atributos} />
        <label htmlFor={`radio-${atributos}`}>{atributos}</label>
      </div>

  )
}

export default Atributos