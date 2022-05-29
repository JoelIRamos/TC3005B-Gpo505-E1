import React from 'react'
import './SelectorAtributos.css'
import Dropdown from '../Dropdown/Dropdown'

function SeleccionAtributos({headers, listasAtt}) {
    return(
        <div className="att-select-container">
            <div className="att-select-box">
            {headers.map((header, index) =>  
                <div key={index} className="tarjeta-att">
                    <div className="att-name">
                        {header}
                    </div>
                    <Dropdown header={header} listasAtt={listasAtt}/>
                </div>
            )}
            </div>
        </div>
    );
}

export default SeleccionAtributos;