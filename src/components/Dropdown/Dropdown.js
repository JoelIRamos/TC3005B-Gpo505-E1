//import React from 'react'
import './Dropdown.css';
import React, { useState, useRef, useEffect } from 'react'


const add = (header, listasAtt, selected) => {
    listasAtt[selected].items.splice(0, 0, header);
    console.log(listasAtt[selected]);
}

const remove = (header, prevSelected, listasAtt) => {
    listasAtt[prevSelected].items = listasAtt[prevSelected].items.filter(e => e !== header);
    console.log(listasAtt[prevSelected]);
}

function Dropdown ({header, listasAtt}) {
    const [isActive, setIsActive] = useState(false);
    const [color , setColor] = useState('white');
    const [selected, setSelected] = useState("Atributo no seleccionado");
    const [prevSelected, setPrevSelected] = useState("Atributo no seleccionado");
    const didMount = useRef(false);

    useEffect(() => {
        if(!didMount.current) {
            didMount.current = true;
            return;
        }

        if(selected === prevSelected) {
            return;
        }

        if(prevSelected !== "Atributo no seleccionado"){
            remove(header, prevSelected, listasAtt);
        }
        setPrevSelected(selected);
        
        if(selected === "Atributo no seleccionado") {
            return;
        }

        add(header, listasAtt, selected);
    },[selected])

    return (
        <div className="dropdown-container">
            <div className={`dropdown-btn ${color}`} onClick={() => setIsActive(!isActive)}>
                {selected}
            </div>
            {isActive && (
            <div className="dropdown-content-container">
                <div className="dropdown-content">
                <div onClick={() => {
                    setSelected("Atributo no seleccionado"); 
                    setIsActive(false); 
                    setColor('white');
                    }} 
                    className="att-NS">
                    Atributo no seleccionado
                </div>
                <div onClick={() => {
                    setSelected("Atributo Interno");
                    setIsActive(false); 
                    setColor('red');
                   }} 
                    className="att-I">
                    Atributo Interno
                </div>
                <div onClick={() => {
                    setSelected("Atributo Externo"); 
                    setIsActive(false); 
                    setColor('yellow');
                    }} 
                    className="att-E">
                    Atributo Externo
                </div>
                <div onClick={() => {
                    setSelected("Atributo Informativo"); 
                    setIsActive(false); 
                    setColor('gray');
                    }} 
                    className="att-info">
                    Atributo Informativo
                </div>
                </div>
            </div>    
            )}
        </div>
    );
}
  
export default Dropdown;