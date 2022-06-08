import React, { useEffect } from 'react'
import Acordion from '../Acordion/Acordion.js'
import './HistoryTable.css';

//if historiOBJ empty, specify: "No se econtraron archivos"
function HistoryTable({historyObj, setHistoryObj, setRunId}) {

    const url = `http://127.0.0.1:8000/api/getHistoryList/`;

    useEffect(() => {
        backGet()
    },[])

    const backGet = async () => {
        const response = await fetch(url).then((response) => 
            response.json()).then((responseData) => {
                setHistoryObj(responseData.result);
            })
            .catch((error) => console.log(error))
    }

    return (
        <div className="hist-select-container">
            <div className="hist-select-box">
                {historyObj !== undefined ?
                    historyObj.map((fileName, index) =>
                        <Acordion key={index} file={fileName} index={index} setRunId={setRunId}/>
                    )
                    :
                    <div className="history-nofile">
                        No se encontraron analisis
                    </div>
                }
            </div>
        </div>
    );
}

export default HistoryTable;