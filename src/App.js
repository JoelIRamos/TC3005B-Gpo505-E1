import React, { useEffect } from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomeScreenview from './views/homeScreen';
import UpLoadFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import Queue from './views/fileQueueView'
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
  const [isGraph, setIsGraph] = useState(false)
  const [file, setFile] = useState(null)
  const [headersFile, setHeadersFile] = useState([])
  const [datos, setDatos] = useState();

  // Funcion para lectura del archivo cuando se dropea
  const onFileDrop = (e) => {
    const newFile = e.target.files[0]
    if (newFile){
      if (newFile) {
        setFile(newFile)
      }
    }
  }

  const backGet =  async ()  => {
    const response = await fetch('http://127.0.0.1:8000/api/getBarGraph/6286eaf06130f0d515a178ca/EMPRESA_TRANSPORTISTA/0/')
    if(!response.ok){
      throw new Error('Data coud not be fetched!')
    } else{
      return response.json()
    }
      // .then(getGraph())
  }
    useEffect(() => {
      backGet()
        .then((res) => {
          setDatos(res)
          setIsGraph(true)
        })
        .catch((e) => {
          console.log(e.message)
        })
    })

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

  // Estado de click y chart para la lista de gráficos 
  //(es declarada en app porque dependiendo a eso se mostraran otros componentes)
  const [click, setClick] = useState(false);
  const [chart, setChart] = useState('Grafico de Barras');
  
  // Estado booleano para mostrar el otro form de atributos (para el grafico burbuja)
  const [showForm, setShowForm] = useState(false);

  // Estado de atributo para desplegar los atributos en la grafica
  const [atributo1, setAtributo1] = useState('EMPRESA_TRANSPORTISTA')

  const [atributo2, setAtributo2] = useState('ID_TRANSPORTISTA')

  // Funcion que guarda el atributo nuevo para visualizar en la grafica
  const saveAtributo1 = (atributo) => {
    setAtributo1(atributo)
  }

  const saveAtributo2 = (atributo) => {
    setAtributo2(atributo)
  }

  // Funciones que cambian el estado de los clicks para la lista de graficas
  const clicked = () => {
    setClick(!click)
  }

  const clickedLi = (e, data) => {
    setChart(data)
    if (data === 'Grafico de Burbuja'){
      setShowForm(true)
    } else {
      setShowForm(false)
    }
    setClick(!click)
  }

  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomeScreenview/>}/>
        <Route path='/FileUpLoad' element={<UpLoadFileview setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} headers={headersFile} setHeadersFile={setHeadersFile}/>}/>
        <Route path='/Queue' element={<Queue/>}/>
        <Route path='/Dashboard' element={<Dashboard backGet={backGet} isGraph={isGraph} atributo2={atributo2} showForm={showForm} click={click} chart={chart} clicked = {clicked} clickedLi = {clickedLi} datos={datos} atributos = {atributos} onSelect2={saveAtributo2} onSelect1={saveAtributo1} atributo1 = {atributo1}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;