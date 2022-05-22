import React from 'react';
import { Droppable, Draggable } from 'react-beautiful-dnd';
import "./DragAndDrop.css"

function DragAndDropTable({titulo, headers, dropID}) {
  return (
    <div className="dnd-table">
      <div className="dnd-table-title">
        {titulo}
      </div>
      <Droppable droppableId={dropID}>
        {(provided) => (
          <ul {...provided.droppableProps} ref={provided.innerRef} className="dnd-droppableArea">
            {headers.map((header, index) => (
              <Draggable key={header} draggableId={header} index={index}>
                {(provided) => (
                  <li className="dnd-table-attribute" {...provided.draggableProps} ref={provided.innerRef} {...provided.dragHandleProps}>
                    {header}
                  </li>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </ul>
        )}
      </Droppable>
    </div>
  )
}

export default DragAndDropTable