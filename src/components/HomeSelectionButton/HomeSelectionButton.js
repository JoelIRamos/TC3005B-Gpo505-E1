import React from 'react'
import './HomeButtonSelection.css'
import { Link } from "react-router-dom";
import { FaCloudUploadAlt } from "react-icons/fa"
import { FaChartBar } from "react-icons/fa"
import { FaHistory } from 'react-icons/fa'

const icons = {
  cloud: < FaCloudUploadAlt size="7vw"/>,
  chart: <FaChartBar size="7vw"/>,
  history: <FaHistory size="7vw"/>,
}

const HomeButtonSelection = ({path, titulo, label, color, icon, runId = ''}) => {

  if (path === '/FileUpLoad' || path === '/Historial') {
    return (
      <Link to={path} className={`contenedor-datos-home-horizontal ${color}`}>
        <div className="contenedor-info-horizontal">
          <div className="contenedor-icono-horizontal">
            {icons[`${icon}`]}
          </div>
          {/* <div className="separator-horizontal"></div> */}
          <div className='contenedor-texto'>
            <h1 className="title-horizontal">{titulo}</h1>
            <p className="label-horizontal">{label}</p>
          </div>
        </div>
    </Link>
    )
  }

  if (path === '/Dashboard') {
    return (
      <Link to={path} className={`contenedor-datos-home-vertical ${color}`}>
          <div className="contenedor-info-vertical">
            <div className="contenedor-titulo-vertical">
              <div className="contenedor-icono-vertical">
                {icons[`${icon}`]}
              </div>
              <h1 className="title-vertical">{titulo}</h1>
              <p className="label-vertical">{label}</p>
            </div>
            {/* <div className="separator-vertical"></div> */}
            {runId !== '' && runId !== undefined && runId !== null
            ?
            <p className="label-vertical">Analisis actual: <br/>{runId}</p>
            :
            <p className="label-vertical">No hay ningun analisis seleccionado</p>
            }           
          </div>
      </Link>
    )
  }
}

export default HomeButtonSelection