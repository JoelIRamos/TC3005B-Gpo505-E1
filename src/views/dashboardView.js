import Navbar from '../components/Navbar/Navbar.js';
import Titulo from '../components/Titulo/Titulo';
import '../App.css';
import ContenedorDatos from '../components/ContenedorDatos/ContenedorDatos.js';
import ContainerDB from '../components/ContainerDB/ContainerDB.js';
import {Navigate, Link} from 'react-router-dom';
import Button from '../components/Button/GenericButton';  
import Message from '../components/Message/Message.js';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';
import React, {useRef} from 'react'


const DashboardView = ({createGraph, graphList, atributos, deleteGraph, indexGraph, setURL, runId, infoGeneral, dashboardEnabled, runStatus}) => {
  
  const printRef = React.useRef();
  if (!dashboardEnabled) {
    var message = "Seleccione un reporte del historial o cargue un archivo para poder utilizar el Dashboard"
    var titulo = ""

    if (runStatus !== undefined && runStatus !== null) {
      if (runStatus['message'] === "Not found"){
        message = "El archivo se esta procesando..."
      }

      if (runStatus['message'] === "Error"){
        message = "Hubo un error al procesar el archivo, por favor intente de nuevo"
      }
    }

    if (runId !== undefined && runId !== null){
      titulo = runId
    }
    return <div className="App">
      <Navbar selected="dashboard"/>
      <Titulo runId={titulo}/>
      <Message title = {titulo} message={message} showButton={true}/>

      {/* <div className='message-view-container'>
          <div className='message-container'>
            <div className='message-box'>
              <h2 className='title'>{message}</h2>
            </div>
          </div>
          <Link to='/'>
            <div className="button">
                <Button text={"Pagino de inicio"}/>
            </div>
          </Link> 
      </div> */}
      
        
      </div>
    //<Navigate to='/' />
  }

  let GraphCont = {id: indexGraph, atributos: atributos, deleteGraph: deleteGraph}
  
  const handleDownloadPdf = async () => {
    const element = printRef.current;
    const canvas = await html2canvas(element);
    const data = canvas.toDataURL('image/png');

    const pdf = new jsPDF();
    const imgProperties = pdf.getImageProperties(data);
    const pdfWidth = pdf.internal.pageSize.getWidth();
    const pdfHeight =
      (imgProperties.height * pdfWidth) / imgProperties.width;

    pdf.addImage(data, 'PNG', 0, 0, pdfWidth, pdfHeight);
    pdf.save('print.pdf');
  }
  // Props: 
  //   datos = datos dummy
  //   atributos = lista de atributos
  //   onSelect = guarda el atributo para la grafica
  //   atributo1 = atributo #1 que se muestra en la grafica
  //   atributo2 = atributo #1 que se muestra en la grafica
  //   clicked = funcion para el estado del click
  //   clickedLi = funcion para el estado del click y guardar el grafico a desplegar
  //   click = estado de click
  //   chart = estado de grafico a desplegar
  //   showForm = estado para desplegar form para grafico burbuja

  return (
    <div className="App">
      <Navbar selected="dashboard" />
      < Titulo runId={runId} />
      <div ref={printRef}>
        <div className="row">
              <ContenedorDatos datos={infoGeneral["result"]["AnomalyRelations"]} label='Relaciones Anómalas' color='red'/>
              <ContenedorDatos datos={`${infoGeneral["result"]["AnomalyRelationsPercentage"]}%`} label='Porcentaje de Relaciones Anómalas' color='red'/>
              <ContenedorDatos datos={`${infoGeneral["result"]["AnomatyPercentage"]}%`} label='Porcentaje de Anomalías' color='yellow'/>
              <ContenedorDatos datos={infoGeneral["result"]["TotalAnomalys"]} label='Total de Anomalías' color='yellow'/>
        </div>
        {graphList.map((element, i) => (
          < ContainerDB runId={runId} key={element.id} indexGraph={element.id} atributos={element.atributos} deleteGraph={element.deleteGraph} setURL = {setURL} />
        ))}
      </div>
      <div className='container-button-add'><button onClick={(() => createGraph(GraphCont))} className='button-add'>+</button></div>
      <button type='button' onClick={handleDownloadPdf}>Download as PDF</button>
    </div>
  );
}

export default DashboardView;