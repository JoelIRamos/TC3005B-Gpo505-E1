import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import FormAtributos from '../FormAtributos/FormAtributos'
import './ContainerDB.css'
import { useState } from 'react';
import { useEffect } from 'react';

const ContainerDB = ({atributos, deleteGraph, indexGraph}) => {
  const [datos, setDatos] = useState({anomalyList: [1, 2, 3,4, 5], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});
  const [apiURL, setApiURL] = useState('http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/ID_TRANSPORTISTA/0/')
  const [click, setClick] = useState(false);
  const [chart, setChart] = useState('Grafico de Barras');
  const [showForm, setShowForm] = useState(false);

  const changeURL = (atributo) => {
    setApiURL(`http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/${atributo}/0/`)
    backGet()
  }

  useEffect(() => {
    backGet()
      .then((res) => {
        setDatos(res)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [apiURL])

  const clicked = () => {
    setClick(!click)
  }

  const backGet = async () =>{
    const response = await fetch(apiURL) 
    if(!response.ok){
      throw new Error('Data could not be fetched')
    } else {
      return response.json()
    }
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
    changeURL(atributo)
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