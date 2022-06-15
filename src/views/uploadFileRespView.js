import React, {useEffect, useRef} from 'react';
import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import Message from '../components/Message/Message.js';
//import Queue from '../components/Queue/Queue.js';

function UploadFileRespView({backPostResp, setRunId}) {
    
    const didMount = useRef(false);

    useEffect(() => {
        if(!didMount.current) {
            didMount.current = true;
            return;
        }
        console.log(backPostResp);
        if (backPostResp !== undefined && backPostResp !== null) {
            setRunId(backPostResp.run_id);
        }
    }, [backPostResp]);

    

    if (backPostResp === undefined || backPostResp === null){
        return(
            <div className="App">
                <Navbar selected='upload' />
                <Message title='Se esta subiendo el archivo' message='Espere un momento por favor' showButton={false}/>
            </div>
        )
    } 

    if (backPostResp.message === 'Upload failed') {
        return(
            <div className="App">
                <Navbar selected='upload' />
                <Message title= 'Error al subir el archivo' message='Intente otra vez' showButton={true}/>
            </div>
        )
    }

    return(
        <div className="App">
            <Navbar selected='upload' />
            <Message title= 'El archivo se subio correctamente y se esta siendo procesado' message= {[`Nombre del analisis:`, <br/> ,`${backPostResp.run_id}`]} showButton={true}/>
        </div>
    )


    /* return (
        <div className="App">
            <Navbar selected='upload'/>
            <Queue backPostResp={backPostResp}/>
        </div>
    ); */
}

export default UploadFileRespView;