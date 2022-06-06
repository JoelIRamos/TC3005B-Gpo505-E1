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
import { Bar, Line, Bubble } from 'react-chartjs-2';



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
  else if(chart === 'Grafico de Burbuja'){
    ChartJS.register(LinearScale, PointElement, Tooltip, Legend);
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
            display: false,
          },
        },}} data={{
          labels,
          datasets: [
            {
              label: 'Número de Anomalías',
              data: datosGraph.anomalyList,
              backgroundColor: 'rgb(255,168,47)',
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
                display: false,
              },
            },
          }} data={{
                labels,
                datasets: [
                  {
                    label: 'Número de Anomalías',
                    data: datosGraph.anomalyList,
                    borderColor: 'rgb(255,168,47)',
                    backgroundColor: 'rgb(255,168,47)',
                  },
                ],
              }}
      />
    ) 
  }
  else if (chart === 'Grafico de Burbuja'){
    return (
      <Bubble options = {{scales: {
        y: {
          beginAtZero: true,
        },
      },}
    } data = {{
      datasets: [
        {
          label: '',
          data: datosGraph.data,
          backgroundColor: 'rgba(53, 162, 235, 0.5)',
        }
      ]
    }} />
    )
  }
}

export default Graph