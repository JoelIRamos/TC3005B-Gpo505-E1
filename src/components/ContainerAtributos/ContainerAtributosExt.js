import React from 'react'
import Atributos from '../Atributos/Atributos'
import './ContainerAtributos.css'
import { useState } from 'react'

const ContainerAtributosExt = ({atributos, onClick, atributo2}) => {
    const [showAtributes, setAtributes] = useState(false)
    const showAtributesClick = () =>{
        setAtributes(!showAtributes)
    }
  return (
    <div className='contenedor-atributos'>
        <h3>Eje Y</h3>
        <div className='cont-atributos'>
        <button className='titulo-atributo yellow' onClick={showAtributesClick}>{atributo2}</button> 
        <div className={`lista-atributos yellow ${showAtributes ? '' : 'no-display'}`}>
            <p>Atributo Externo</p>
            {atributos["Atributo Externo"]["items"].map((atributo, i) => <Atributos key={i} onClick={onClick} data={atributo} color="yellow"/>)}
        </div>
      </div>
      </div>
  )
}

export default ContainerAtributosExt