import React from 'react'
import Atributos from '../Atributos/Atributos'
import './FormAtributos.css'

const FormAtributoExt = ({atributos, onSelect, showForm, idForm}) => {
    const radioEvent = (e) => {
        onSelect(e.target.value)
    }

  return (
      <div className={`container-form-atributo ${!showForm && 'hide-form'}`}>
            <h3>Atrbiuto Externo</h3>
            <form>
                <div className="container-atributos" onChange={radioEvent}>
                    {atributos["Atributo Externo"]["items"].map((element, i) => (
                        <Atributos key={i} idForm={idForm} atributos={element} />
                    ))}
                </div>
            </form>
      </div>
    
  )
}

export default FormAtributoExt