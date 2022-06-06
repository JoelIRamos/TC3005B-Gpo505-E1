import React, {useState} from 'react'
import './BarraBusqueda.css';
import { FaSearch, FaTimes } from "react-icons/fa"

//TO DO: add return value to splice list

//placeHolder: Texto descriptivo para la input box
//data: Datos para la lista de busqueda
function BarraBusqueda({placeHolder, data, scrollToSelected}) {

    const [filterData, setFilterData] = useState([]);
    const [wordEntered, setWordEntered] = useState("");
    
    const handleFilter = (event) => {
        const searchWord = event.target.value;
        setWordEntered(searchWord);
        const newFilter = data.filter((value) => {
            return value.toLowerCase().includes(searchWord.toLowerCase());
        });

        if(searchWord === ""){
            setFilterData([]);
        }
        else{
            setFilterData(newFilter);
        }
    }

    const clearSearch = () => {
        setFilterData([]);
        setWordEntered("");
    }

    const getIndex = (i) => {
        console.log(i)
    }

    return (
        <div className="busqueda-container">
            <div className="busqueda">
                <div className="icono-busqueda">
                    <FaSearch id="search"/>
                </div>
                <div className="input-container">
                    <input className="input-textbox" type="text" placeholder={placeHolder} value={wordEntered} onChange={handleFilter}/>
                    {filterData.length !== 0 && (
                        <div className="busqueda-results">
                        {filterData.map((name, key) =>
                            <div key={key} className="result-item" onClick={() => {scrollToSelected(name); clearSearch()}}>
                                {name}
                            </div>
                        )}
                        </div>
                    )}
                </div>
                {wordEntered !== "" ?
                    <div className="icono-cancel" onClick={clearSearch}>
                        <FaTimes id="times"/>
                    </div>
                    :
                    <div/>
                }
            </div>
        </div>
    );
  }
  
  export default BarraBusqueda;