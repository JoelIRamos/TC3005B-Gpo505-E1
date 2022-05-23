import './Queue.css';
import React, { useRef, useState } from 'react'
import Button from '../Button/GenericButton';

function Queue() {
  return (
    <div className="view-container">
        <div className="queue-container">
            <div className="queue">
                <h2 className="title">Titulo</h2>
                <p>Info</p>
            </div>
        </div>
        <div className="button">
            <Button text={"Regresar"}/>
        </div>
    </div>
  )
}

export default Queue;