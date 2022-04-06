import React from 'react'

const GraphListContet = ({element, onClick}) => {
  return (
    <li key={element} onClick={onClick}>
        {element}
    </li>
  )
}

export default GraphListContet