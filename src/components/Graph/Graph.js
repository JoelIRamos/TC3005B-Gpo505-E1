import React, {useEffect} from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis, Area, AreaChart } from 'recharts'
import './Graph.css'
import { FaCog } from 'react-icons/fa'
import GraphList from '../GraphList/GraphList'
import { useState } from 'react'

const graphs = ['Grafico de Barras', 'Grafico de Area', 'Grafico de Burbuja']


const Graph = ({data, atributo1}) => {

  const [click, setClick] = useState(false);
  const [chart, setChart] = useState('Grafico de Barras');
  const [selectedGraph,setSelectedGraph] = useState(null);

  const clicked = (data) => {
    setClick(!click)
  }

  const clickedLi = (e, data) => {
    console.log(data)
    setChart(data)
    setClick(!click)
  }

  useEffect(() => {
    //aqui los componentes
    if(chart === 'Grafico de Barras'){
      setSelectedGraph(
        <BarChart width={500} height={300} data = {data}>
            <XAxis dataKey={atributo1} />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
        </BarChart>
      )
    }
    if(chart === 'Grafico de Area'){
      setSelectedGraph(
        <AreaChart
          width={500}
          height={300}
          data={data}
        >
          <XAxis dataKey={atributo1} />
          <YAxis />
          <Tooltip />
          <Area type="monotone" dataKey="anomalias" stroke="#8884d8" fill="#8884d8" />
        </AreaChart>
      )
    }
    if(chart === 'Grafico de Burbuja'){
      setSelectedGraph(
        <p>burbuja</p>
      )
    }

  }, [chart]);


  return (
    <div className="graph">
      <div className="container-titulo-btn">
        <h3>Cantidad de Anomalías por {atributo1}</h3>
        <button className='btn-graph' onClick={clicked}>{< FaCog />}</button>
      </div>
      < GraphList graphs={graphs} state={click} onClick={clickedLi}  />
      <ResponsiveContainer width='100%' height='100%'>
        {selectedGraph===null?   
          <BarChart width={500} height={300} data = {data}>
            <XAxis dataKey={atributo1} />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
          </BarChart>
          : selectedGraph
        }
      </ResponsiveContainer>
    </div>
  )
}

export default Graph