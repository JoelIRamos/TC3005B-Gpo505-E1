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

const HomeButtonSelection = ({path, titulo, label, color, icon}) => {
  return (
    <Link to={path} className={`contenedor-datos-home ${color}`}>
        <div className="contenedor-info">
          <div className="contenedor-icono">
            {icons[`${icon}`]}
          </div>
          <h1 className="title">{titulo}</h1>
          <p className="lable">{label}</p>
        </div>
    </Link>
  )
}

export default HomeButtonSelection