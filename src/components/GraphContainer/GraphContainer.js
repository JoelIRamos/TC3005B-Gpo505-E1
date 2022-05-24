import React from 'react'
import './GraphContainer.css'
import { FaCog, FaTimes } from 'react-icons/fa'
import GraphList from '../GraphList/GraphList'
import Graph from '../Graph/Graph'

const graphs = ['Grafico de Barras', 'Grafico de Area', 'Grafico de Burbuja']


const GraphContainer = ({data, atributo1, atributo2, clicked, clickedLi, click, chart, showForm, deleteGraph, indexGraph}) => {
  return (
    <div className="graph">
      <div className="container-titulo-btn">
        <h3>{showForm ? `Cantidad de Anomalías por ${atributo1} x ${atributo2}` : `Cantidad de Anomalías por ${atributo1}`}</h3>
        <div className='container-btn-graph'>
          <button className='btn-graph' onClick={() => deleteGraph(indexGraph)} >{< FaTimes />}</button>
          <button className='btn-graph' onClick={clicked}>{< FaCog />}</button>
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