import React from 'react'
import './Button.css'

const GenButton = ({text, funcCall}) =>{
  return (
    <button className="generic-btn" onClick={funcCall}> {text} </button>
  )
}

export default GenButton