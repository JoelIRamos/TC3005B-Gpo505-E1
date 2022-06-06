import './Queue.css';
import React, { useRef, useState, useEffect} from 'react'

const backGetQueue = async () =>{
  const response = await fetch(`http://127.0.0.1:8000/api/getQueue/`) 
  if(!response.ok){
    throw new Error('Data could not be fetched')
  } else {
    // console.log(response)
    // console.log(response.json())
    return response.json()
  }
}

function Queue() {

  const didMount = useRef(false);
  const intervalRef = useRef();
  const [queue, setQueue] = useState([]);

  useEffect(() => {
    intervalRef.current = setInterval(() => {
      backGetQueue().then((res) => {
        setQueue(res.queue)
        // console.log(res.queue)
      }).catch((e) => {
        setQueue([])
        console.log(e.message)
      })
    }, 1000);

    return () => {
      clearInterval(intervalRef.current);
    }
  }, [queue]);

  if (queue === undefined || queue === null || queue.length === 0){
    return(
      <div className="contenedor-queue grey">
      <div className="contenedor-queue-header">
        <h1>Archivos siendo procesados</h1>
      </div>
      <div className="contenedor-queue-body-empty">
        <h1>Actualmente no se esta procesando ningun archivo</h1>
      </div>
    </div>
    )
  }
  return (
    <div className="contenedor-queue grey">
      <div className="contenedor-queue-header">
        <h1>Archivos siendo procesados</h1>
      </div>
      <div className="contenedor-queue-body">
        {queue.map((q, index) => {
          return (
            <div key={index} className="contenedor-queue-body-cell">
              {q}
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default Queue;