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


const DashboardView = ({updateList, createGraph, graphList, atributos, deleteGraph, indexGraph, setURL, runId, infoGeneral, dashboardEnabled, runInfo}) => {
  
  const printRef = React.useRef();
  if (!dashboardEnabled) {
    var message = "Cargando información..."
    var titulo = ""

    if (runId === undefined || runId === null || runId === '' ) {
      message = "Seleccione un analisis del historial o cargue un archivo para utilizar el dashboard"
    }

    if (runInfo !== undefined && runInfo !== null) {
      if (runInfo['message'] === "Not found"){
        message = "Cargando..."
      }

      if (runInfo['message'] === "Error" || runInfo['result']['status']['code'] !== 0){
        titulo = "Error"
        var error = ""

        if (runInfo['message'] === 'Found') {
          error = runInfo['result']['status']['code']} 
        else {
          error = 'Error de conexion'
        }

        message = [`Hubo un error al cargar la información`, <br/> , `Codigo de error: ${error}`]
      }
    }

    // if (runId !== undefined && runId !== null){
    //   titulo = runId
    // }
    return <div className="App">
      <Navbar selected="dashboard"/>
      <Titulo runId={runId}/>
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

  let GraphCont = {id: indexGraph, atributos: atributos, deleteGraph: deleteGraph, chart: undefined, url: undefined, atributo1: undefined, atributo2: undefined, showForm: undefined, paramAnomaly:undefined}
  
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
    pdf.save(`${runId}.pdf`);
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
      <div className="tittle-button-cont">
        < Titulo runId={runId} />
        <button className='button-down' type='button' onClick={handleDownloadPdf}>Descarga como PDF</button>
      </div>
      <div ref={printRef}>
        <div className="row">
              <ContenedorDatos datos={infoGeneral["result"]["AnomalyRelations"]} label='Relaciones Anómalas' color='red'/>
              <ContenedorDatos datos={`${infoGeneral["result"]["AnomalyRelationsPercentage"]}%`} label='Porcentaje de Relaciones Anómalas' color='red'/>
              <ContenedorDatos datos={`${infoGeneral["result"]["AnomatyPercentage"]}%`} label='Porcentaje de Anomalías' color='yellow'/>
              <ContenedorDatos datos={infoGeneral["result"]["TotalAnomalys"]} label='Total de Anomalías' color='yellow'/>
        </div>
        {graphList.map((element, i) => (
          < ContainerDB 
            updateList={updateList} 
            runId={runId} key={element.id} 
            indexGraph={element.id} 
            atributos={element.atributos} 
            deleteGraph={element.deleteGraph} 
            setURL = {setURL} 
            currentChart={element.chart} 
            url={element.url} 
            currentAtributo1 = {element.atributo1} 
            currentAtributo2 = {element.atributo2} 
            currentShowForm={element.showForm} 
            currentParamAnomaly ={element.paramAnomaly}
          />
        ))}
      </div>
      <div className='container-button-add'><button onClick={(() => createGraph(GraphCont))} className='button-add'>+</button></div>
      
    </div>
  );
}

export default DashboardView;