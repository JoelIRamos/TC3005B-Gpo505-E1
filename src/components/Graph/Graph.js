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
  Filler
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
      Legend,
      Filler
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
              borderWidth: 2,
              borderRadius: 10,
              borderColor: 'rgb(242, 92, 41)',
              backgroundColor: 'rgba(242, 92, 41, 0.2)',
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
                    borderColor: 'rgb(242, 92, 41)',
                    backgroundColor: 'rgba(242, 92, 41, 0.2)',
                    fill: true
                  },
                ],
              }}
      />
    ) 
  }
  else if (chart === 'Grafico de Burbuja'){
    return (
      <Bubble options = {{
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value, index, ticks) {
                // console.log(value);
                // console.log(index);
                // console.log(ticks);
                if (parseInt(value) === value) {
                  if (datosGraph.attribute2Dict === undefined || datosGraph.attribute2Dict === null){
                    return value;
                  }
                  if (Object.keys(datosGraph.attribute2Dict).length <= 10) {
                    return datosGraph.attribute2Dict[value];
                  }
                  return value;
                }
                return "";
              }
            }
          },
          x: {
            ticks: {
              callback: function(value, index, ticks) {
                // console.log(value);
                // console.log(index);
                // console.log(ticks);
                if (parseInt(value) === value) {
                  if (datosGraph.attribute1Dict === undefined || datosGraph.attribute1Dict === null){
                    return value;
                  }
                  if (Object.keys(datosGraph.attribute1Dict).length <= 25) {
                    return datosGraph.attribute1Dict[value];
                  }
                  return value;
                }
                return "";
              }
            }
          }
        },
        plugins: {
          tooltip: {
            legend: {
              display: false,
            },
            callbacks: {
              title: function(tooltipItem) {
                return "Relacion de Anomalias";
              },
              label: function(tooltipItem) {
                const x = datosGraph.attribute1Dict[tooltipItem.raw.x]
                const y = datosGraph.attribute2Dict[tooltipItem.raw.y]
                
                return [datosGraph.atributo1 + ": " + x, datosGraph.atributo2 + ": " + y];
              },
              afterLabel: function(tooltipItem) {
                return "Posicion: x = " + tooltipItem.raw.x + ", y = " + tooltipItem.raw.y;
              },
              footer: function(tooltipItem) {
                // console.log(tooltipItem)
                // console.log(datosGraph)
                const z = datosGraph.anomalyCount[tooltipItem[0].dataIndex]
                return "Cantidad de interacciones anomalas: " + z;
              }
            }
          }
        }
      }
    } data = {{
      datasets: [
        {
          label: 'Relaciones',
          data: datosGraph.data,
          borderColor: function(context) {
            // return 'rgb(255, 118, 34)';

            // if (context.dataIndex%2 == 0){
            //   return 'rgba(242, 92, 41, 0.5)';
            // }
            // else {
            //   return 'rgba(255, 168, 47, 0.5)';
            // }

            if (context.raw === undefined) {
              return 'rgba(255, 255, 255)';
            }
            if (context !== undefined && ((context.raw.x%2 === 0 && context.raw.y%2 === 0) || (context.raw.x%2 !== 0 && context.raw.y%2 !== 0))){
              return 'rgba(242, 92, 41)';
            }
            return 'rgba(255, 168, 47)';
          },
          backgroundColor: function(context) { 
            // return 'rgba(255, 118, 34, 0.5)';

            // if (context.dataIndex%2 == 0){
            //   return 'rgba(242, 92, 41, 0.5)';
            // }
            // else {
            //   return 'rgba(255, 168, 47, 0.5)';
            // }
            
            if (context.raw === undefined) {
              return 'rgba(255, 255, 255, 0.5)';
            }
            if (context !== undefined && ((context.raw.x%2 === 0 && context.raw.y%2 === 0) || (context.raw.x%2 !== 0 && context.raw.y%2 !== 0))){
              return 'rgba(242, 92, 41, 0.5)';
            }
            return 'rgba(255, 168, 47, 0.5)';
          },
        }
      ]
    }} />
    )
  }
}

export default Graph