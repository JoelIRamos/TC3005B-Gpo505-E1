import React, { useEffect } from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomeScreenview from './views/homeScreen';
import UpLoadFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import Queue from './views/fileQueueView'
import ContainerDB from './components/ContainerDB/ContainerDB';
//import SeleccionAtributos from './views/attributeSelectionView'
import { useState } from 'react';
import { wait } from '@testing-library/user-event/dist/utils';

// Atributos dummy
const atributos = [
  'ID_TRANSPORTISTA',
  'EMPRESA_TRANSPORTISTA',
  'C-ID-ORDEN-CABECERA',
  'C_POSICION_ORDEN',
  'Q_CANTIDAD',
]

// Datos dummy

function App() {
  // Archivo .csv
  
  const [file, setFile] = useState(null)
  const [headersFile, setHeadersFile] = useState([])
  const [datos, setDatos] = useState({anomalyList: [3456, 423, 4325,435, 5345], labels: ['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5']});
  const [indexGraph, setIndexGraph] = useState(0)
  const [graphList, setGraphList] = useState([])
  let graphList2
  // console.log(graphList2)
  // Respuesta del post al backend
  const [backPostResp, setBackPostResp] = useState();

  // Funcion para lectura del archivo cuando se dropea
  const onFileDrop = (e) => {
    const newFile = e.target.files[0]
    if (newFile){
      if (newFile) {
        setFile(newFile)
      }
    }
  }


  const backGet =  (x)  => {
    setIndexGraph(indexGraph+ 1)
    setGraphList([...graphList, x])
    // const response = await fetch('http://127.0.0.1:8000/api/getBarGraph/6286eaf06130f0d515a178ca/EMPRESA_TRANSPORTISTA/0/')
    // if(!response.ok){
    //   throw new Error('Data coud not be fetched!')
    // } else{
    //   return response.json()
    // }
  }
    // useEffect(() => {
    //   backGet()
    //     .then((res) => {
    //       setDatos(res)
    //       setIsGraph(true)
    //     })
    //     .catch((e) => {
    //       console.log(e.message)
    //     })
    // })

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
    console.log(graphList)
    console.log(graphList[index])
  }

  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomeScreenview/>}/>
        <Route path='/FileUpLoad' element={<UpLoadFileview setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} headers={headersFile} backPostResp={backPostResp} setBackPostResp={setBackPostResp}/>}/>
        <Route path='/Queue' element={<Queue backPostResp={backPostResp}/>}/>
        <Route path='/Dashboard' element={<Dashboard indexGraph={indexGraph} deleteGraph={deleteGraph} backGet={backGet} graphList={graphList} datos={datos} atributos = {atributos}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;