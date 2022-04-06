import React from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'
import './Graph.css'
import { FaCog } from 'react-icons/fa'
import GraphList from '../GraphList/GraphList'
import { useState } from 'react'

const graphs = ['Grafico de Barras', 'Grafico de Area', 'Grafico de Burbuja']

const Graph = ({data, atributo1}) => {

  const [click, setClick] = useState(false)

  const clicked = () => {
    setClick(!click)
  }

  return (
    <div className="graph">
      <div className="container-titulo-btn">
        <h3>Cantidad de Anomalías por {atributo1}</h3>
        <button className='btn-graph' onClick={clicked}>{< FaCog />}</button>
      </div>
      < GraphList graphs={graphs} state={click} onClick={clicked}  />
      <ResponsiveContainer width='100%' height='100%'>
        <BarChart width={500} height={300} data = {data}>
            <XAxis dataKey={atributo1} />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default Graph