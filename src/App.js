import React, { useEffect, useRef, useState } from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomeScreenview from './views/homeScreen';
import UpLoadFileview from './views/uploadFileView';
import DashboardView from './views/dashboardView';
import HistorialView from './views/Historial';
import UploadFileRespView from './views/uploadFileRespView'

function App() {

  const didMount = useRef(false);

  const [file, setFile] = useState(null) // Estado archivo
  const [headersFile, setHeadersFile] = useState([]) // Estado headers para archivo

  const [indexGraph, setIndexGraph] = useState(0) // Indice de cada grafico 
  const [graphList, setGraphList] = useState([]) // Lista de graficos

  const [backPostResp, setBackPostResp] = useState(); // Respuesta backend

  const [infoGeneral, setInfoGeneral] = useState();

  // Referencia para la lista de grafico
  const graphListRef = useRef(); 

  const [listaAtributos, setListaAtributos] = useState();
  const [runId, setRunId] = useState();
  const [runInfo, setRunInfo] = useState();
  const [dashboardEnabled, setDashboardEnabled] = useState(false);
  const intervalRef = useRef();
  

  // Funcion para creacion de gráfico -- Dashboard
  const createGraph = async (x)  => {
    setIndexGraph(indexGraph+ 1)
    setGraphList([...graphList, x])
  }

  // Funcion para actualizar datos de listaDatos
  const updateList = (chart, url, id, atributo1, atributo2, showForm, paramAnomaly) =>{
    console.log(id)
    setGraphList([...graphList].map(graph =>{
      if(graph.id === id){
        return{
          ...graph, chart: chart, url: url, atributo1: atributo1, atributo2: atributo2, showForm: showForm, paramAnomaly: paramAnomaly}
      } 
      else return graph
    }))
  }
     

  useEffect(() => {
    if(!didMount.current) {
      didMount.current = true;
      return;
    }
    console.log('useEffect runId');
    console.log(runId)
    setGraphList([]);
    setRunInfo(null);
    setInfoGeneral(null);
    setDashboardEnabled(false);
    intervalRef.current = null

    if(runId === null || runId === undefined){
      return;
    }
    
    intervalRef.current = setInterval(() => {
      backGetHistory().then((res) => {
        setRunInfo(res)
        console.log(res)
      }).catch((e) => {
        console.log(e.message)
      })
    }, 500);

    return () => {
      clearInterval(intervalRef.current);
    }
  }, [runId])


  useEffect(() => {
    // console.log(runStatus)
    if (runInfo === null || runInfo === undefined){
      return;
    }

    if(runInfo['message'] === 'Not found'){
      return
    }

    if (runInfo['message'] === 'Error' || runInfo['result']['status']['code'] !== 0){
      clearInterval(intervalRef.current);
      return;
    }

    clearInterval(intervalRef.current);

    backGetInfoGeneral()
      .then((res) => {
        // console.log(res)
        console.log('infoGeneral updated')
        console.log(res)
        setInfoGeneral(res)
        setListaAtributos(
          { 
            "Atributo Interno":
            {
              name: "Atributos Internos",
              items: runInfo['result']['internal_attributes']
            },
            "Atributo Externo":{
              name: "Atributos Externos",
              items: runInfo['result']['external_attributes']
            },
            "Atributo Informativo":{
              name: "Atributos Informativos",
              items: runInfo['result']['informational_attributes']
            }
          }
        )
        //TODO: Get historyDetail
        setDashboardEnabled(true);
      })
      .catch((e) => {
        console.log(e.message)
      })
    }, [runInfo])

  useEffect(() => {
    console.log(listaAtributos)
  }, [listaAtributos])

  const backGetInfoGeneral = async () =>{
    const response = await fetch(`http://127.0.0.1:8000/api/getStatistics/${runId}/0/`) 
    if(!response.ok){
      throw new Error('Data could not be fetched')
    } else {
      // console.log(response)
      // console.log(response.json())
      return response.json()
    }
  }

  const backGetHistory = async () =>{
    const response = await fetch(`http://127.0.0.1:8000/api/getHistory/${runId}/`)
    if(!response.ok){
      throw new Error('Data could not be fetched')
    } else {
      // console.log(response)
      // console.log(response.json())
      return response.json()
    }
  }
  // Funcion para lectura del archivo cuando se dropea -- UploadFile
  const onFileDrop = (e) => {
    const newFile = e.target.files[0]
    if (newFile){
      if (newFile) {
        setFile(newFile)
      }
    }
  }

  // Funcion que quita el archivo cargado -- UploadFile
  const fileRemove = () => {
    setFile(null)
  }

  // Obtencion de headers desde el CSV y llamado a la función para POST -- UploadFile
  const processCSV = (str, delim=',') => {
    const headers = str.slice(0, str.indexOf('\n')).split(delim);
    headers[headers.length - 1] = headers[headers.length - 1].slice(0, headers[headers.length - 1].length - 1)
    const headersJson = JSON.stringify(headers);
    setHeadersFile(headers);
  }

  // Lectura de archivo -- UploadFile
  const setCsvFile = () => {
    const csvFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      const text = e.target.result;
      processCSV(text);
    }

    reader.readAsText(csvFile);
  }

  graphListRef.current = graphList
  // Eliminar en gráfico -- Dashboard
  const deleteGraph = (index) => {
    const newArray = graphListRef.current
    setGraphList(newArray.filter((graph) => graph.id !== index))
    // Splice function here
  }

  

  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomeScreenview runId={runId}/>}/>
        <Route path='/FileUpLoad' element={<UpLoadFileview setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} headers={headersFile} setBackPostResp={setBackPostResp} setListaAtributos={setListaAtributos}/>}/>
        <Route path='/FileUploadResp' element={<UploadFileRespView backPostResp={backPostResp} setRunId={setRunId}/>}/>
        <Route path='/Dashboard' element={<DashboardView updateList={updateList} infoGeneral={infoGeneral} indexGraph={indexGraph} runId={runId} deleteGraph={deleteGraph} createGraph={createGraph} graphList={graphList} atributos = {listaAtributos} dashboardEnabled = {dashboardEnabled} runInfo = {runInfo}/>}/>
        <Route path='/Historial' element={<HistorialView setRunId={setRunId}/>}/>
      </Routes>
    </Router>
  );
}

export default App;