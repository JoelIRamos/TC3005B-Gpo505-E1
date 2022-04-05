import React from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

const Graph = ({data, atributo1}) => {
  return (
      <ResponsiveContainer width='100%' height='100%'>
        <BarChart width={200} height={300} data = {data}>
            <CartesianGrid strokeDasharray='3 3'/>
            <XAxis dataKey={atributo1} />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
        </BarChart>
    </ResponsiveContainer>
  )
}

export default Graph