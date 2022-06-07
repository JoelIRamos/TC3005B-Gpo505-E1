import React from 'react'
import Atributos from '../Atributos/Atributos'
import './ContainerAtributos.css'
import { useState } from 'react'

const ContainerAtributos = ({atributos, onClick, atributo1}) => {

    const [showAtributes, setAtributes] = useState(false)
    const showAtributesClick = () =>{
        setAtributes(!showAtributes)
    }

  return (
      <div className='contenedor-atributos'>
        <h3>Eje X</h3>
        <div className='cont-atributos'>
        <button className='titulo-atributo red' onClick={showAtributesClick}>{atributo1}</button> 
        <div className={`lista-atributos red ${showAtributes ? '' : 'no-display'}`}>
          <p>Atributo Interno</p>
            {atributos["Atributo Interno"]["items"].map((atributo, i) => <Atributos key={i} onClick={onClick} data={atributo} color="red"/>)}
          <p>Atributo Informativo</p>
          {atributos["Atributo Informativo"]["items"].map((atributo, i) => <Atributos key={i} onClick={onClick} data={atributo} color="red"/>)}
        </div>
      </div>
      </div>
  )
}

export default ContainerAtributos