import React from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis, Area, AreaChart } from 'recharts'
import { Doughnut } from 'react-chartjs-2'


const Graph = ({atributo1, chart, data}) => {
    let graph
    if (chart === 'Grafico de Barras'){
        graph = 
        <BarChart width={500} height={300} data = {data}>
            <XAxis dataKey={atributo1} />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
        </BarChart>
    }
    else if (chart === 'Grafico de Area') {
        graph =
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
    }
    else if (chart === 'Grafico de Burbuja'){
        graph = <p>burbuja</p>
    }

  return (
      <ResponsiveContainer width='100%' height='100%'>{graph}</ResponsiveContainer>
  )
}

export default Graph