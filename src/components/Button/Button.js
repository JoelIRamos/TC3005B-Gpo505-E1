import React from 'react'
import { FaCloudUploadAlt } from "react-icons/fa"
import { FaChartBar } from "react-icons/fa"
import { FaHistory } from 'react-icons/fa'
import { useState } from 'react'
import './Button.css'

const Button = ({text, style, icon}) => {

  const [iconStyle, setIconStyle] = useState('')

  const onHover = () => {
    setIconStyle('icon')
  }

  const offHover = () => {
    setIconStyle('')
  }

  const icons = {
    cloud: <FaCloudUploadAlt className={iconStyle} />,
    chart: <FaChartBar className={iconStyle} />,
    history: <FaHistory  className={iconStyle}/>,
  }
  return (
    <button onMouseEnter={onHover} onMouseLeave={offHover} className={`btn ${style}`}>{icons[`${icon}`]} {text}</button>
  )
}

export default Button