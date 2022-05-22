import React from 'react'
import './Button.css'

const GenButton = ({text, viewUpdate}) =>{
  return (
    <button className="generic-btn" onClick={viewUpdate}> {text} </button>
  )
}

export default GenButton