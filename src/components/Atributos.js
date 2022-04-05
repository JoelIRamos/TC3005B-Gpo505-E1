import React from 'react'

const Atributos = ({atributos}) => {
  return (
      <div className='atributos'>
        <input type='radio' id={`radio-${atributos}`} name='atributo' value={atributos} />
        <label htmlFor={`radio-${atributos}`}>{atributos}</label>
      </div>

  )
}

export default Atributos