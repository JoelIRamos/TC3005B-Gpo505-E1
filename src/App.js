import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import UpFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';
import { useState } from 'react';

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

  const [atributo1, setAtributo1] = useState('claveTransportista')

  const saveAtributo = (atributo) => {
    setAtributo1(atributo)
  }

  return (
    <Router>
      <Routes>
        <Route path='/' element={<UpFileview/>}/>
        <Route path='/Dashboard' element={<Dashboard datos={datos} atributos = {atributos} onSelect={saveAtributo} atributo1 = {atributo1}/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;