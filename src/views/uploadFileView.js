import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import { DragDropContext } from 'react-beautiful-dnd';
import DropFile from '../components/DropFile/DropFile.js';
import DnDTable from '../components/DragAndDrop/DragAndDropTable.js'
import Button from '../components/Button/GenericButton.js';
import { useState } from 'react';
import { Link } from "react-router-dom";

const onDragEnd = (result, seleccionDeListas) => {
  if(!result.destination)
  {
    return;
  }
  const {source, destination} = result;

  //Si se dropea un objeto en un recuadro diferente se actualizan ambas listas
  if(source.droppableId !== destination.droppableId)
  {
    const sourceCol = seleccionDeListas[source.droppableId];
    const destCol = seleccionDeListas[destination.droppableId];
    const sourceItems = sourceCol.items;
    const destItems = destCol.items;
    const [removed] = sourceItems.splice(source.index, 1);
    destItems.splice(destItems.index, 0, removed);
    seleccionDeListas[source.droppableId].items = sourceItems;
    seleccionDeListas[destination.droppableId].items = destItems;
    console.log(seleccionDeListas[destination.droppableId].items)
  }
  //Si se droppea un objeto en el mismo recuadro, la lista solo se reordenara
  else
  {
    const column = seleccionDeListas[source.droppableId];
    const copiedItems = column.items;
    const [removed] = copiedItems.splice(source.index, 1);
    copiedItems.splice(destination.index, 0, removed);
    seleccionDeListas[source.droppableId].items = copiedItems
    console.log(seleccionDeListas[source.droppableId].items)
  }
};

function UploadFileView({file, onFileDrop, fileRemove, setCsvFile, headers, backGet}) {
  
  // HTTP request a backend (aun en prueba)
  const backPost = (internalAtt, externalAtt) => {
    const intAttJSON = JSON.stringify(internalAtt);
    const extAttJSON = JSON.stringify(externalAtt);
    var formData = new FormData();
    console.log("here")
    formData.append('internal_attributes', intAttJSON); // Array tipo JSON de los atributos internos del archivo
    formData.append('external_attributes', extAttJSON); // Array tipo JSON de los atributos externos del archivo
    formData.append('file', file); // Archivo completo
    fetch('http://localhost:8000/api/upload_file/', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(success => {
        console.log(success);
      })
      .catch(error => console.log(error))
  }

  const seleccionDeListas = 
  {
    "attE":{
      name: "Atributos Externos",
      items: []
    },
    "attL":{
      name: "Lista Atributos",
      items: headers
    },
    "attI":
    {
      name: "Atributos Internos",
      items: []
    }
  };

  const [upLoadView, setUpLoadView] = useState(true);

  const viewUpdate = () => {
    setUpLoadView(!upLoadView);
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
          <Link to='/Queue'>
            <div className='button'>
              <button onClick={() => backPost(seleccionDeListas["attI"], seleccionDeListas["attE"])}>Siguiente</button>
            </div>
          </Link>
          <div className="atrribute-container">
            <DragDropContext onDragEnd={result => onDragEnd(result, seleccionDeListas)}>
              {Object.entries(seleccionDeListas).map(([id, data]) => {
                return(
                  <DnDTable titulo={data.name} dropID={id} headers={data.items}/>
                )
              })}
            </DragDropContext>
          </div>
        </>
      }
    </div>
    
  );
}

export default UploadFileView;