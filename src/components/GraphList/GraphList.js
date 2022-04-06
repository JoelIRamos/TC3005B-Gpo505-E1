import React from 'react'
import GraphListContet from '../GraphListContent/GraphListContet'
import './GraphList.css'

const GraphList = ({graphs, state, onClick}) => {
  return (
    <div className={`dropdown ${state && 'active'}`}>
        <ul>
            {graphs.map((element) => (
                <GraphListContet element={element} onClick={onClick} />
            ))}
        </ul>
    </div>
  )
}

export default GraphList