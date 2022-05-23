import React from 'react'
import { Doughnut } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';



const Graph = ({datosGraph}) => {
  ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );
  
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Bar Chart',
      },
    },
  };
  
  const labels = datosGraph.labels;
  
  const data = {
    labels,
    datasets: [
      {
        label: 'Dataset 1',
        data: datosGraph.anomalyList,
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };
    // let graph
    // if (chart === 'Grafico de Barras'){
    //     graph = 
    //     <BarChart width={500} height={300} data = {data}>
    //         <XAxis dataKey={atributo1} />
    //         <YAxis />
    //         <Tooltip />
    //         <Bar dataKey='anomalias' fill='#ffa82f' />
    //     </BarChart>
    // }
    // else if (chart === 'Grafico de Area') {
    //     graph =
    //     <AreaChart
    //       width={500}
    //       height={300}
    //       data={data}
    //     >
    //       <XAxis dataKey={atributo1} />
    //       <YAxis />
    //       <Tooltip />
    //       <Area type="monotone" dataKey="anomalias" stroke="#8884d8" fill="#8884d8" />
    //     </AreaChart>
    // }
    // else if (chart === 'Grafico de Burbuja'){
    //     graph = <p>burbuja</p>
    // }

  return (
    <Bar options={options} data={data} />
      // <ResponsiveContainer width='100%' height='100%'>{graph}</ResponsiveContainer>
  )
}

export default Graph