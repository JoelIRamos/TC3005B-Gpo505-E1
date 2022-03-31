import React from 'react'

const Button = ({text, style, icon}) => {
  return (
    <button className={`btn ${style}`}>{icon} {text}</button>
  )
}

export default Button