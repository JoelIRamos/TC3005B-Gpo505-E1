import React from 'react'
import GraphContainer from '../GraphContainer/GraphContainer'
import './ContainerDB.css'
import { useState, useLayoutEffect, useEffect, useRef  } from 'react';
import ContainerAtributos from '../ContainerAtributos/ContainerAtributos';
import ContainerAtributosExt from '../ContainerAtributos/ContainerAtributosExt'
import BubbleGraphDictionary from '../BubbleGraphDictionary/BubbleGraphDictionary';
import SliderAnomaly from '../SliderAnomaly/SliderAnomaly';

const ContainerDB = ({updateList, atributos, deleteGraph, indexGraph, runId, currentChart, url, currentAtributo1, currentAtributo2, currentShowForm, currentParamAnomaly}) => {

  // Obejto de datos para graficas
  const [datos, setDatos] = useState({anomalyList: [1, 2, 3,4, 5], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});
  const [paramAnomaly, setParamAnomaly] = useState(currentParamAnomaly === undefined ? 0 : currentParamAnomaly);

  const [dictionaryEnabled, setDictionaryEnabled] = useState(false);

  // Estado de click booleano para despliegue de elementos
  const [click, setClick] = useState(false);

  // Gráfico a desplegar
  const [chart, setChart] = useState(currentChart === undefined ? 'Grafico de Barras': currentChart);

  // Booleano para mostrar el form de grafico burbuja
  const [showForm, setShowForm] = useState(currentShowForm === undefined ? false : currentShowForm);

  // Atributos para graficas
  const [atributo1, setAtributo1] = useState(currentAtributo1 === undefined ? atributos["Atributo Interno"]["items"][0] : currentAtributo1)
  const [atributo2, setAtributo2] = useState(currentAtributo2 === undefined ? atributos["Atributo Externo"]["items"][0] : currentAtributo2)

  // URL para GET Req
  const [apiURL, setApiURL] = useState(url === undefined ?`http://127.0.0.1:8000/api/getBarGraph/${runId}/${atributo1}/${paramAnomaly}/` : url)

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
      setApiURL(`http://127.0.0.1:8000/api/getBubbleGraph/${runId}/${atributo1}/${atributo2}/${paramAnomaly}/`)
    } else{
      setApiURL(`http://127.0.0.1:8000/api/getBarGraph/${runId}/${atributo1}/${paramAnomaly}/`)
    }
    
    
  }, [chart, atributo1, atributo2, paramAnomaly])

  // Effect para GET
  useLayoutEffect(() => {
    backGet()
      .then((res) => {
        setDatos(res)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [apiURL])

  useEffect(() => {
    updateList(chart, urlRef.current, indexGraph, atributo1, atributo2, showForm, paramAnomaly)
  }, [chart, atributo1, atributo2, showForm, paramAnomaly])

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


  const attributes_dictionary_condition = () => {
    if(dictionaryEnabled && chart === 'Grafico de Burbuja'){
      return (
        <div className='container-form-a'>
          <BubbleGraphDictionary dictionaryAtt1={datos.attribute1Dict} dictionaryAtt2={datos.attribute2Dict} attribute1={atributo1} attribute2={atributo2}/>
        </div>
      )
    }

    if(chart !== 'Grafico de Burbuja'){
      return(
        <div className='container-form-a'>
          <ContainerAtributos atributo1={atributo1} atributos={atributos} onClick={saveAtributo1}/>
          <div className='contenedor-atributos'></div>
          <SliderAnomaly setParamAnomaly={setParamAnomaly} paramAnomally={paramAnomaly}/>
        </div>
      )
    }

    return (
      <div className='container-form-a'>
        <ContainerAtributos atributo1={atributo1} atributos={atributos} onClick={saveAtributo1}/>
        <ContainerAtributosExt atributo2={atributo2} atributos={atributos} onClick={saveAtributo2}/>
        <SliderAnomaly setParamAnomaly={setParamAnomaly} paramAnomally={paramAnomaly}/>
      </div>
    )
  }

  return (
      <div className='container-db-general'>
        <div className='container-db'>
        <React.StrictMode>
            <GraphContainer indexGraph={indexGraph} deleteGraph={deleteGraph} showForm={showForm} atributo2={atributo2} click={click} chart={chart} data = {datos} atributo1={atributo1} clicked={clicked} clickedLi={clickedLi} setDictionaryEnabled={setDictionaryEnabled} dictionaryEnabled={dictionaryEnabled}/>
            {attributes_dictionary_condition()}
              {/* < ContainerAtributos atributo1={atributo1} atributos={atributos} onClick={saveAtributo1} />
              {chart === 'Grafico de Burbuja' && < ContainerAtributosExt atributo2={atributo2} atributos={atributos} onClick={saveAtributo2}/>} */}

        </React.StrictMode>
        </div>
      </div>
  )
}

export default ContainerDB