import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import DropFile from '../components/DropFile/DropFile.js';
import SeleccionAtributos from '../components/SelectorAtributos/SelectorAtributos.js';
import BarraBusqueda from '../components/BarraBusqueda/BarraBusqueda.js';
import CircleButton from '../components/ButtonCircle/ButtonCircle.js';
import React, { useState, useRef, useEffect } from 'react';
import { Link } from "react-router-dom";


function UploadFileView({file, onFileDrop, fileRemove, setCsvFile, headers, setBackPostResp, setListaAtributos}) {
  
  useEffect(() => {
    setBackPostResp(null)
  }, []);

  // HTTP request a backend (aun en prueba)
  const backPost = (listaAtt) => {
    setListaAtributos(listaAtt);
    const intAttJSON = JSON.stringify(listaAtt["Atributo Interno"].items);
    const extAttJSON = JSON.stringify(listaAtt["Atributo Externo"].items);
    const infoAttJSON = JSON.stringify(listaAtt["Atributo Informativo"].items);
    var formData = new FormData();
    console.log("Posting to backend...")
    formData.append('internal_attributes', intAttJSON); // Array tipo JSON de los atributos internos del archivo
    formData.append('external_attributes', extAttJSON); // Array tipo JSON de los atributos externos del archivo
    formData.append('informational_attributes', infoAttJSON)
    formData.append('file', file); // Archivo completo
    fetch('http://localhost:8000/api/upload_file/', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(success => {
        setBackPostResp(success);
      })
      .catch(error => console.log(error))
  }

  const listasAtt = 
  { 
    "Atributo Interno":
    {
      name: "Atributos Internos",
      items: []
    },
    "Atributo Externo":{
      name: "Atributos Externos",
      items: []
    },
    "Atributo Informativo":{
      name: "Atributos Informativos",
      items: []
    }
  };

  const [upLoadView, setUpLoadView] = useState(true);

  const listAttRef = useRef(listasAtt);
  
  const viewUpdate = () => {
    setUpLoadView(!upLoadView);
  }

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
      <Navbar selected='upload'/>
      {upLoadView ?
        <div className='container-up'>
          <DropFile setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove} setUpLoadView={setUpLoadView} viewUpdate={viewUpdate}/>
        </div>
        :
        <>
          <div className="att-options-container">
            <Link to='/FileUploadResp'>
                <button className='button-gen' onClick={() => backPost(listAttRef.current)}>Siguiente</button>
            </Link>
          </div>
          <CircleButton event={scrollToTop}/>
          <BarraBusqueda placeholder={"Buscar Atributos"} data={headers} scrollToSelected={scrollToSelected}/>
          <SeleccionAtributos headers={headers} listasAtt={listAttRef.current}/>
        </>
      }
    </div>
  );
}

export default UploadFileView;