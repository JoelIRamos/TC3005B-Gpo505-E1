import React from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis, Area, AreaChart } from 'recharts'
import './GraphContainer.css'
import { FaCog } from 'react-icons/fa'
import GraphList from '../GraphList/GraphList'
import { useState } from 'react'
import Graph from '../Graph/Graph'

const graphs = ['Grafico de Barras', 'Grafico de Area', 'Grafico de Burbuja']


const GraphContainer = ({data, atributo1, clicked, clickedLi, click, chart}) => {
  return (
    <div className="graph">
      <div className="container-titulo-btn">
        <h3>Cantidad de Anomalías por {atributo1}</h3>
        <button className='btn-graph' onClick={clicked}>{< FaCog />}</button>
      </div>
      < GraphList graphs={graphs} state={click} onClick={clickedLi}  />
      < Graph atributo1={atributo1} chart={chart} data={data} />
    </div>
  )
}

export default GraphContainer