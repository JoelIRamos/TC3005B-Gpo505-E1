import React from 'react'
import { Doughnut } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar, Line } from 'react-chartjs-2';



const Graph = ({datosGraph, chart}) => {
  if(chart === 'Grafico de Barras'){
    ChartJS.register(
      CategoryScale,
      LinearScale,
      BarElement,
      Title,
      Tooltip,
      Legend
    );
  }
  else if (chart === 'Grafico de Area'){
    ChartJS.register(
      CategoryScale,
      LinearScale,
      PointElement,
      LineElement,
      Title,
      Tooltip,
      Legend
    );
  }
  const labels = datosGraph.labels;
  if (chart === 'Grafico de Barras'){
    return (
      <Bar options={{responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Chart.js Bar Chart',
          },
        },}} data={{
          labels,
          datasets: [
            {
              label: 'Dataset 1',
              data: datosGraph.anomalyList,
              backgroundColor: 'rgba(255, 99, 132, 0.5)',
            },
          ],
        }} />
    ) 
}
  else if(chart === 'Grafico de Area'){
    return (
      <Line options={{
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Chart.js Line Chart',
              },
            },
          }} data={{
                labels,
                datasets: [
                  {
                    label: 'Dataset 1',
                    data: datosGraph.anomalyList,
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                  },
                ],
              }}
      />
    ) 
  }
}

export default Graph