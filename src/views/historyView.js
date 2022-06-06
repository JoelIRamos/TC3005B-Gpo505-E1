import React, {useState} from 'react'
import Navbar from '../components/Navbar/Navbar.js';
import BarraBusqueda from '../components/BarraBusqueda/BarraBusqueda'
import HistorialTable from '../components/HistoryTable/HistoryTable.js'
import CircleButton from '../components/ButtonCircle/ButtonCircle.js'
import '../App.css';

//call history get

function HistoryView({setRunId}) {

  const [historyObj, setHistoryObj] = useState([])

  const scrollToTop = () => {
    document.documentElement.scrollTop = 0;
  }

  const scrollToSelected = (selected) => {
    document.getElementById(selected).scrollIntoView({
      block: "center",
      behavior: "smooth"});
  }

  return (
    <div className="App">
      <Navbar selected='history' />
      <BarraBusqueda placeholder={"Buscar"}  scrollToSelected={scrollToSelected}/>
      <HistorialTable historyObj={historyObj} setHistoryObj={setHistoryObj} setRunId={setRunId}/>
      <CircleButton event={scrollToTop}/>
    </div>
  );
}

export default HistoryView;