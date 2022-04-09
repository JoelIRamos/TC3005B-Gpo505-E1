import React from 'react'
import Atributos from '../Atributos/Atributos'
import './FormAtributos.css'

const FormAtributos = ({atributos, onSelect, showForm}) => {

    const radioEvent = (e) => {
        onSelect(e.target.value)
    }

  return (
      <div className={`container-form-atributo ${!showForm && 'hide-form'}`}>
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