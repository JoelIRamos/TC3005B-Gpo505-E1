import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import UpFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import { useState } from 'react';

// Atributos dummy
const atributos = [
  'claveTransportista',
  'empresaTransportadora',
  'identificacion',
  'numeroProveedores',
  'UsuarioPermisoCirculacionIngreso',
  'UsuarioEgreso',
  'UsuarioPesadaEntrada',
  'UsuarioControla',
  'UsuarioInsAuditoria',
  'UsuarioInspeccion',
  'UsuarioDescarga',
  'UsuarioPesadaSalida',
]

// Datos dummy
const datos = [
  {
    id: 1,
    claveTransportista: '18',
    empresaTransportadora: '114',
    identificacion: '1346',
    numeroProveedores: '19',
    anomalias: 4203,
  },
  {
    id: 2,
    claveTransportista: '19',
    empresaTransportadora: '98',
    identificacion: '1403',
    numeroProveedores: '10',
    anomalias: 3200,
  },
  {
    id: 3,
    claveTransportista: '46',
    empresaTransportadora: '62',
    identificacion: '403',
    numeroProveedores: '60',
    anomalias: 5600,
  },
]

function App() {

  // Estado de click y chart para la lista de gráficos 
  //(es declarada en app porque dependiendo a eso se mostraran otros componentes)
  const [click, setClick] = useState(false);
  const [chart, setChart] = useState('Grafico de Barras');
  
  // Estado booleano para mostrar el otro form de atributos (para el grafico burbuja)
  const [showForm, setShowForm] = useState(false);

  // Estado de atributo para desplegar los atributos en la grafica
  const [atributo1, setAtributo1] = useState('claveTransportista')

  // Funcion que guarda el atributo nuevo para visualizar en la grafica
  const saveAtributo = (atributo) => {
    setAtributo1(atributo)
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
        <Route path='/' element={<UpFileview/>}/>
        <Route path='/Dashboard' element={<Dashboard showForm={showForm} click={click} chart={chart} clicked = {clicked} clickedLi = {clickedLi} datos={datos} atributos = {atributos} onSelect={saveAtributo} atributo1 = {atributo1}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;