import React from 'react'
import GraphListContet from '../GraphListContent/GraphListContet'
import './GraphList.css'

const GraphList = ({graphs, state, onClick}) => {
  return (
    <div className={`dropdown-graph-list ${state && 'active'}`}>
        <ul>
            {graphs.map((element, i) => (
                <GraphListContet key={i} element={element} onClick={onClick} />
            ))}
        </ul>
    </div>
  )
}

export default GraphList