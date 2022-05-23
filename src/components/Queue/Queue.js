import './Queue.css';
import React, { useRef, useState } from 'react'
import Button from '../Button/GenericButton';
import { Link } from "react-router-dom";

var lastID = " ";

function Queue(backPostResp) {
  return (
    <div className="view-container">
        <div className="queue-container">
            <div className="queue-box">
              {console.log(backPostResp["backPostResp"])}
              {backPostResp["backPostResp"]["backPostResp"] === undefined 
                ? <h2 className="title">Enviando Archivo...</h2>
                : 
                <>
                  <h2 className="title">Archivo Enviado</h2>
                  <div className="queue">
                    {backPostResp["backPostResp"]["backPostResp"].queue.map((q) => {
                      return (
                        <div>
                          {q}
                        </div>
                      )
                    })}
                  </div>
                </>
              }
            </div>
        </div>
        <Link to='/'>
          <div className="button">
              <Button text={"Regresar"}/>
          </div>
        </Link>
    </div>
  )
}

export default Queue;