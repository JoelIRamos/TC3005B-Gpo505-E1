import React from 'react'

const GraphListContet = ({element, onClick}) => {
  return (
    <li key={element} onClick={((e) => onClick(e, element))}>
        {element}
    </li>
  )
}

export default GraphListContet