import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import FormAtributos from '../FormAtributos/FormAtributos'
import './ContainerDB.css'
import { useState } from 'react';
import { useEffect } from 'react';
import {useRef} from 'react';

const ContainerDB = ({atributos, deleteGraph, indexGraph}) => {

  // Obejto de datos para graficas
  const [datos, setDatos] = useState({anomalyList: [1, 2, 3,4, 5], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});

  // URL para GET Req
  const [apiURL, setApiURL] = useState('http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/ID_TRANSPORTISTA/0/')

  // Estado de click booleano para despliegue de elementos
  const [click, setClick] = useState(false);

  // Gráfico a desplegar
  const [chart, setChart] = useState('Grafico de Barras');

  // Booleano para mostrar el form de grafico burbuja
  const [showForm, setShowForm] = useState(false);

  // Atributos para graficas
  const [atributo1, setAtributo1] = useState('ID_TRANSPORTISTA')
  const [atributo2, setAtributo2] = useState('TIPO_TRANSPORTE')

  // Effect para GET
  useEffect(() => {
    if(chart === 'Grafico de Burbuja'){
      setApiURL(`http://127.0.0.1:8000/api/getBubbleGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/${atributo1}/${atributo2}/0/`)
    } else{
      setApiURL(`http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/${atributo1}/0/`)
    }
    backGet()
      .then((res) => {
        setDatos(res)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [apiURL, chart, atributo1, atributo2])

  // Modificador booleano de click
  const clicked = () => {
    setClick(!click)
  }

  // GET req
  const backGet = async () =>{
    const response = await fetch(apiURL) 
    if(!response.ok){
      throw new Error('Data could not be fetched')
    } else {
      return response.json()
    }
  }

  // Selección de gráfico
  const clickedLi = (e, data) => {
    setChart(data)
    if (data === 'Grafico de Burbuja'){
      console.log(apiURL)
      setShowForm(true)
    } else {
      setShowForm(false)
    }
    setClick(!click)
  }
  
  // Cambio de atributo para graficas
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