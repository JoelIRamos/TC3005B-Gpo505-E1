import React from 'react';
import { DragDropContext } from 'react-beautiful-dnd';
import Navbar from '../components/Navbar/Navbar.js';
import DnDTable from '../components/DragAndDrop/DragAndDropTable.js'
import Button from '../components/Button/GenericButton.js';
import "../App.css"
import { useState } from 'react';

const onDragEnd = (result, headers, externos, internos, setExternos, setInternos) => {
  if(!result.destination)
  {
    return;
  }
  const {source, destination} = result;

  if(source.droppableId !== destination.droppableId)
  {
    if(destination.droppableId === "interno")
    {
      /*const sourceColumn = source.droppableId;
      const destColumn = destination.droppableId;*/
      const sourceItems = headers;
      const destItems = internos;
      const [removed] = sourceItems.splice(source.index, 1);
      destItems.splice(destination.index, 0, removed);
      setInternos(destItems);
      console.log(internos);
    }
    else if (destination.droppableId === "externo")
    {
      /*const sourceColumn = source.droppableId;
      const destColumn = destination.droppableId;*/
      const sourceItems = headers;
      const destItems = externos;
      const [removed] = sourceItems.splice(source.index, 1);
      destItems.splice(destination.index, 0, removed);
      setExternos(destItems);
      console.log(externos);
    }
  }
  else
  {
    if(destination.droppableId === "interno")
    {
      const copiedItems = internos;
      const [removed] = internos.splice(source.index, 1);
      copiedItems.splice(destination.index, 0, removed);
      setInternos(copiedItems);
      console.log(internos);
    }
    else if(destination.droppableId === "externo")
    {
      const copiedItems = externos;
      const [removed] = externos.splice(source.index, 1);
      copiedItems.splice(destination.index, 0, removed);
      setExternos(copiedItems);
      console.log(externos);
    }
    else
    {
      const copiedItems = headers;
      const [removed] = headers.splice(source.index, 1);
      copiedItems.splice(destination.index, 0, removed);
      console.log(headers)
    }
  }
};

function AttributeSelection(headers) {

  const [listaAtt, setListaAtt] = useState(headers);
  const [externos, setExternos] = useState([]);
  const [internos, setInternos] = useState([]);
  console.log(headers);

    return (
      <div className="atrribute-container">
        <DragDropContext onDragEnd={result => onDragEnd(result, headers, externos, internos, setExternos, setInternos)}>
          <DnDTable titulo={"Atributos Externos"} dropID={"externo"} headers={externos}/>
          <DnDTable titulo={"Lista de Atributos"} dropID={"lista"} headers={listaAtt}/>
          <DnDTable titulo={"Atributos Internos"} dropID={"interno"} headers={internos}/>
        </DragDropContext>
      </div>
    );
  }
  
  export default AttributeSelection;