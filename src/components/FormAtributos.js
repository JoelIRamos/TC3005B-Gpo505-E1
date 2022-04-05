import React from 'react'
import Atributos from './Atributos'

const FormAtributos = ({atributos, onSelect}) => {

    const radioEvent = (e) => {
        onSelect(e.target.value)
    }

  return (
      <div className='container-form-atributo'>
            <h3>Atributo Interno</h3>
            <div className="container-atributos" onChange={radioEvent}>
                {atributos.map((element) => (
                    <Atributos atributos={element} />
                ))}
            </div>
      </div>
    
  )
}

export default FormAtributos