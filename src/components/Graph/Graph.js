import React from 'react'
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

const data = [
    {
        id: 'ID_1',
        anomalias: 6100,
    },
    {
        id: 'ID_2',
        anomalias: 4500,
    },
    {
        id: 'ID_3',
        anomalias: 2200,
    },
    {
        id: 'ID_4',
        anomalias: 600,
    },
]

const Graph = () => {
  return (
        <BarChart width={500} height={300} data = {data}>
            <CartesianGrid strokeDasharray='3 3'/>
            <XAxis dataKey='id' />
            <YAxis />
            <Tooltip />
            <Bar dataKey='anomalias' fill='#ffa82f' />
        </BarChart>
  )
}

export default Graph