import React, { useEffect } from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomeScreenview from './views/homeScreen';
import UpLoadFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import Queue from './views/fileQueueView'
//import SeleccionAtributos from './views/attributeSelectionView'
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

// Datos dummy

function App() {
  // Archivo .csv
  
  const [file, setFile] = useState(null)
  const [headersFile, setHeadersFile] = useState([])
  const [datos, setDatos] = useState({anomalyList: [1, 2, 3,4, 5], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});
  const [indexGraph, setIndexGraph] = useState(0)
  const [graphList, setGraphList] = useState([])
  const [apiURL, setApiURL] = useState('http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/ID_TRANSPORTISTA/0/')
  // console.log(graphList2)
  // Respuesta del post al backend
  const [backPostResp, setBackPostResp] = useState();
  const stateRef = useRef();
  stateRef.current = graphList

  const createGraph = async (x)  => {
    setIndexGraph(indexGraph+ 1)
    setGraphList([...graphList, x])
  }

  useEffect(() => {
    backGet()
      .then((res) => {
        setDatos(res)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [apiURL])

  var graphListUp
  useEffect(() =>{
    graphListUp = graphList
    //console.log(graphListUp)
  }, [graphList])

  // Funcion para lectura del archivo cuando se dropea
  const onFileDrop = (e) => {
    const newFile = e.target.files[0]
    if (newFile){
      if (newFile) {
        setFile(newFile)
      }
    }
  }


  const changeURL = (atributo) => {
    setApiURL(`http://127.0.0.1:8000/api/getBarGraph/Analisis_Chatarra_Ene21-ene22_2022-05-23_18-48-13/${atributo}/0/`)
    backGet()
  }

  const backGet = async () =>{
    const response = await fetch(apiURL) 
    if(!response.ok){
      throw new Error('Data could not be fetched')
    } else {
      return response.json()
    }
  }

  // Funcion que quita el archivo cargado
  const fileRemove = () => {
    setFile(null)
  }

  // Obtencion de headers desde el CSV y llamado a la función para POST
  const processCSV = (str, delim=',') => {
    const headers = str.slice(0, str.indexOf('\n')).split(delim);
    headers[headers.length - 1] = headers[headers.length - 1].slice(0, headers[headers.length - 1].length - 1)
    const headersJson = JSON.stringify(headers);
    setHeadersFile(headers);
  }

  // Lectura de archivo
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

  function arrayRemove(arr, value){
    return arr.filter(function(geeks){
      return geeks!= value
    })
  }

  const deleteGraph = (index) =>{
    const newArray = stateRef.current
    newArray.splice(index, 1)
    console.log(newArray)
    //setGraphList([])
    // Splice function here
  }

  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomeScreenview/>}/>
        <Route path='/FileUpLoad' element={<UpLoadFileview setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} headers={headersFile} backPostResp={backPostResp} setBackPostResp={setBackPostResp}/>}/>
        <Route path='/Queue' element={<Queue backPostResp={backPostResp}/>}/>
        <Route path='/Dashboard' element={<Dashboard setURL={changeURL} indexGraph={indexGraph} deleteGraph={deleteGraph} createGraph={createGraph} graphList={graphList} datos={datos} atributos = {atributos}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;