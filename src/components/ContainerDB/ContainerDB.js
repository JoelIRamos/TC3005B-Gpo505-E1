import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import FormAtributos from '../FormAtributos/FormAtributos'
import './ContainerDB.css'
import { useState } from 'react';

const ContainerDB = ({datos , atributos, deleteGraph, indexGraph}) => {
  const [click, setClick] = useState(false);
  const [chart, setChart] = useState('Grafico de Barras');
  const [showForm, setShowForm] = useState(false);
  const clicked = () => {
    setClick(!click)
  }

  const clickedLi = (e, data) => {
    setChart(data)
    if (data === 'Grafico de Burbuja'){
      setShowForm(true)
    } else {
      setShowForm(false)
    }
    setClick(!click)
  }
  const [atributo1, setAtributo1] = useState('EMPRESA_TRANSPORTISTA')
  const [atributo2, setAtributo2] = useState('ID_TRANSPORTISTA')
  const saveAtributo1 = (atributo) => {
    setAtributo1(atributo)
  }

  const saveAtributo2 = (atributo) => {
    setAtributo2(atributo)
  }
  return (
      <div className='container-db-general'>
        <div className='container-db'>
            <GraphContainer indexGraph={indexGraph} deleteGraph={deleteGraph} showForm={showForm} atributo2={atributo2} click={click} chart={chart} data = {datos} atributo1={atributo1} clicked={clicked} clickedLi={clickedLi} />
            <div className='container-form-a'>
                < FormAtributos idForm={1} atributos={atributos} onSelect={saveAtributo1} showForm = {true} />
                < FormAtributos idForm={2} atributos={atributos} onSelect={saveAtributo2} showForm = {showForm} />
            </div>
        </div>
      </div>
  )
}

export default ContainerDB