import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import FormAtributos from '../FormAtributos/FormAtributos'
import './ContainerDB.css'

const ContainerDB = ({datos , atributos, onSelect1, onSelect2, atributo1, atributo2, clicked, clickedLi, click, chart, showForm}) => {
  return (
      <div className='container-db-general'>
        <div className='container-db'>
            <GraphContainer showForm={showForm} atributo2={atributo2} click={click} chart={chart} data = {datos} atributo1={atributo1} clicked={clicked} clickedLi={clickedLi} />
            <div className='container-form-a'>
                < FormAtributos idForm={1} atributos={atributos} onSelect={onSelect1} showForm = {true} />
                < FormAtributos idForm={2} atributos={atributos} onSelect={onSelect2} showForm = {showForm} />
            </div>
        </div>
      </div>
  )
}

export default ContainerDB