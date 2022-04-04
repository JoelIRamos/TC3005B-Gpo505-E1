import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import UpFileview from './views/uploadFileView';
import Dashboard from './views/dashboardView';
import Historial from './views/historyView';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<UpFileview/>}/>
        <Route path='/Dashboard' element={<Dashboard/>}/>
        <Route path='/Historial' element={<Historial/>}/>
      </Routes>
    </Router>
  );
}

export default App;