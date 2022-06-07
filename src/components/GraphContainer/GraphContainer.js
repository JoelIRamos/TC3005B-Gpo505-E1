import React, {useEffect} from 'react'
import './GraphContainer.css'
import { FaCog, FaTimes, FaBookOpen } from 'react-icons/fa'
import { AiFillBook, AiOutlineBook } from "react-icons/ai";
import GraphList from '../GraphList/GraphList'
import Graph from '../Graph/Graph'

const graphs = ['Grafico de Barras', 'Grafico de Area', 'Grafico de Burbuja']


const GraphContainer = ({data, atributo1, atributo2, clicked, clickedLi, click, chart, showForm, deleteGraph, indexGraph, setDictionaryEnabled, dictionaryEnabled}) => {

  useEffect(() => {
    data.atributo1 = atributo1
    if (atributo2 !== undefined && atributo2 !== null){
      data.atributo2 = atributo2
    }
  }, [data])

  return (
    <div className="graph">
      <div className="container-titulo-btn">
        <h3>{showForm ? `Cantidad de Anomalías por ${atributo1} x ${atributo2}` : `Cantidad de Anomalías por ${atributo1}`}</h3>
        <div className='container-btn-graph'>
          {showForm ? <button className='btn-graph' onClick={() => {setDictionaryEnabled(!dictionaryEnabled)}}>{!dictionaryEnabled ? <AiFillBook/> : <FaBookOpen/>}</button> : null}
          <button className='btn-graph' onClick={clicked}>{<FaCog/>}</button>
          <button className='btn-graph red-btn' onClick={() => deleteGraph(indexGraph)} >{<FaTimes/>}</button>
        </div>
      </div>
      < GraphList graphs={graphs} state={click} onClick={clickedLi}  />
      <div className='container-graph'>
        < Graph atributo1={atributo1} chart={chart} datosGraph={data} />
      </div>
    </div>
  )
}

export default GraphContainer