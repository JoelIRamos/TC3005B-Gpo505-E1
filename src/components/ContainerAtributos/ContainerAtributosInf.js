import React from 'react'
import Atributos from '../Atributos/Atributos'
import './ContainerAtributos.css'
import { useState } from 'react'


const ContainerAtributosInf = ({atributos, onClick}) => {
    const [showAtributes, setAtributes] = useState(false)
    const showAtributesClick = () =>{
        setAtributes(!showAtributes)
    }
  return (
      
    <div className='cont-atributos'>
        <button className='titulo-atributo' onClick={showAtributesClick}>{atributos["Atributo Informativo"]["name"]}</button> 
        <div className={showAtributes ? '' : 'no-display'}>
            {atributos["Atributo Informativo"]["items"].map((atributo, i) => <Atributos key={i} onClick={onClick} data={atributo}/>)}
        </div>
      </div>
  )
}

export default ContainerAtributosInf