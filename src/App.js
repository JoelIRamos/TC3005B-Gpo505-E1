import React, { useEffect } from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomeScreenview from './views/homeScreen';
import UpLoadFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import Queue from './views/fileQueueView'
import ContainerDB from './components/ContainerDB/ContainerDB';
import SeleccionAtributos from './components/SelectorAtributos/SelectorAtributos'
import { useState } from 'react';
import { useRef } from 'react';
import dashboardView from './views/dashboardView';

// Atributos dummy
const atributos = [
  'ID_TRANSPORTISTA',
  'weightDifference',
  'D_UBICACION',
  'USUARIO_EGRESO',
  'N_PESO_TARA',
  'mediana'
]
function App() {

  const [file, setFile] = useState(null) // Estado archivo
  const [headersFile, setHeadersFile] = useState([]) // Estado headers para archivo

  const [indexGraph, setIndexGraph] = useState(0) // Indice de cada grafico 
  const [graphList, setGraphList] = useState([]) // Lista de graficos

  const [backPostResp, setBackPostResp] = useState(); // Respuesta backend

  // Referencia para la lista de grafico
  const graphListRef = useRef(); 

  // Funcion para creacion de gráfico -- Dashboard
  const createGraph = async (x)  => {
    setIndexGraph(indexGraph+ 1)
    setGraphList([...graphList, x])
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
    console.log("reading file");

    reader.onload = (e) => {
      const text = e.target.result;
      processCSV(text);
    }

    reader.readAsText(csvFile);
  }

  graphListRef.current = graphList
  // Eliminar en gráfico -- Dashboard
  const deleteGraph = (index) => {
    console.log(index)
    const newArray = graphListRef.current
    console.log(newArray)
    console.log(newArray[index])
    setGraphList(newArray.filter((graph) => graph.id !== index))
    // Splice function here
  }

  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomeScreenview/>}/>
        <Route path='/FileUpLoad' element={<UpLoadFileview setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} headers={headersFile} backPostResp={backPostResp} setBackPostResp={setBackPostResp}/>}/>
        <Route path='/Queue' element={<Queue backPostResp={backPostResp}/>}/>
        <Route path='/Dashboard' element={<Dashboard indexGraph={indexGraph} deleteGraph={deleteGraph} createGraph={createGraph} graphList={graphList} atributos = {atributos}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;