import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import './ContainerDB.css'
import { useState } from 'react';
import { useLayoutEffect, useEffect } from 'react';
import {useRef} from 'react';
import ContainerAtributos from '../ContainerAtributos/ContainerAtributos';
import ContainerAtributosExt from '../ContainerAtributos/ContainerAtributosExt'

const ContainerDB = ({atributos, deleteGraph, indexGraph, runId}) => {

  // Obejto de datos para graficas
  const [datos, setDatos] = useState({anomalyList: [1, 2, 3,4, 5], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});

  

  // Estado de click booleano para despliegue de elementos
  const [click, setClick] = useState(false);

  // Gráfico a desplegar
  const [chart, setChart] = useState('Grafico de Barras');

  // Booleano para mostrar el form de grafico burbuja
  const [showForm, setShowForm] = useState(false);

  // Atributos para graficas
  const [atributo1, setAtributo1] = useState(atributos["Atributo Interno"]["items"][0])
  const [atributo2, setAtributo2] = useState(atributos["Atributo Externo"]["items"][0])

  // URL para GET Req
  const [apiURL, setApiURL] = useState(`http://127.0.0.1:8000/api/getBarGraph/${runId}/${atributo1}/0/`)

  // Lista de datos para acceder cuando se cambian las pestañas
  const [listaDatos, setListaDatos] = useState([])
  const chartRef = useRef()
  chartRef.current = chart
  // Referencia a URL para cargue de datos
  
  // Effect para agregar datos a Lista de Datos
  // useEffect(() => {
  //   setListaDatos([urlRef.current, chartRef.current])
  //   console.log(listaDatos)
  // }, [apiURL, chart])

  // Effect para cambio de URL
  useLayoutEffect(() => {
    if(chartRef.current === 'Grafico de Burbuja'){
      setApiURL(`http://127.0.0.1:8000/api/getBubbleGraph/${runId}/${atributo1}/${atributo2}/0/`)
    } else{
      setApiURL(`http://127.0.0.1:8000/api/getBarGraph/${runId}/${atributo1}/0/`)
    }
    
  }, [chart, atributo1, atributo2])

  // Effect para GET
  useLayoutEffect(() => {
    backGet()
      .then((res) => {
        setDatos(res)
        console.log(apiURL)
        console.log(chart)
        console.log(indexGraph)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [apiURL])

  // Modificador booleano de click
  const clicked = () => {
    setClick(!click)
  }

  const urlRef = useRef()
  urlRef.current = apiURL
  // console.log(urlRef.current)
  // // GET req
  const backGet = async () =>{
    const response = await fetch(urlRef.current) 
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
      setShowForm(true)
    } else {
      setShowForm(false)
    }
    setClick(!click)
  }
  
  // Cambio de atributo para graficas
  const saveAtributo1 = (atributo) => {
    console.log(atributo)
    setAtributo1(atributo)
  }
  const saveAtributo2 = (atributo) => {
    setAtributo2(atributo)
  }

  return (
      <div className='container-db-general'>
        <div className='container-db'>
        <React.StrictMode>
            <GraphContainer indexGraph={indexGraph} deleteGraph={deleteGraph} showForm={showForm} atributo2={atributo2} click={click} chart={chart} data = {datos} atributo1={atributo1} clicked={clicked} clickedLi={clickedLi} />
            <div className='container-form-a'>
              < ContainerAtributos atributo1={atributo1} atributos={atributos} onClick={saveAtributo1} />
              {chart === 'Grafico de Burbuja' && < ContainerAtributosExt atributo2={atributo2} atributos={atributos} onClick={saveAtributo2}/>}
            </div>
        </React.StrictMode>
        </div>
      </div>
  )
}

export default ContainerDB