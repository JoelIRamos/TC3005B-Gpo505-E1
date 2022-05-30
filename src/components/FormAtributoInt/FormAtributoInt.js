import React from 'react'
import Atributos from '../Atributos/Atributos'
import './FormAtributos.css'

const FormAtributoInt = ({atributos, onSelect, showForm, idForm}) => {

    const radioEvent = (e) => {
        onSelect(e.target.value)
    }

  return (
      <div className={`container-form-atributo ${!showForm && 'hide-form'}`}>
            <h3>Atributo Interno</h3>
            <form>
                <div className="container-atributos" onChange={radioEvent}>
                    {atributos["Atributo Interno"]["items"].map((element, i) => (
                        <Atributos key={i} idForm={idForm} atributos={element} />
                    ))}
                </div>
            </form>
      </div>
    
  )
}

export default FormAtributoInt