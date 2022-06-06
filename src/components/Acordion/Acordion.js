import React, {useState} from 'react'
import { Link } from "react-router-dom";
import { FaRegTimesCircle, FaRegCheckCircle } from 'react-icons/fa'
import './Acordion.css'
// Agregar espacio para boton de VER corridaa

function Acordion({file, index, setRunId}) {
    const [selected, setSelected] = useState(null);

    const toggle = (i) => {
        if(selected === i)
        {
            return setSelected(null)
        }

        setSelected(i);
    }

    return(
        <div id={file.base_file_name} className="acordion">
            <div className={selected === index ? 'tarjeta-acordion selected' : 'tarjeta-acordion'} onClick={() => toggle(index)}>
                <div className="tarjeta-name" >
                    {file.base_file_name}
                </div>
            </div>
            <div className={selected === index ? 'content-wrapper show' : 'content-wrapper'}>
                {file.versions.map((fileVersion, i) =>
                    <div key={i} className="tarjeta-content">
                        <div className="tarjeta-content-name">
                            {fileVersion._id}
                        </div>
                        {fileVersion.status.code === 0 ?
                        <div className="tarjeta-content-status">
                            {"Status:"}
                            <div className="thick-status-icon">
                                <FaRegCheckCircle/>
                            </div>
                        </div>
                        :
                        <div className="tarjeta-content-status">
                            {"Status:"}
                            <div className="cross-status-icon">
                                <FaRegTimesCircle/>
                            </div>
                        </div>
                        }
                        <div className="tarjeta-content-view-button">
                            <Link className="view-button"  to={'/Dashboard'}>
                                <div onClick={() => {setRunId(fileVersion._id)}}>
                                    Ver en Dashboard
                                </div>
                            </Link>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Acordion;