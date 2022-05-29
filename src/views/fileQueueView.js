import React, {useEffect, useRef} from 'react';
import Navbar from '../components/Navbar/Navbar.js';
import Queue from '../components/Queue/Queue.js';

function FileQueueView({backPostResp, setRunId}){
    
    const didMount = useRef(false);
    useEffect(() => {
        if(!didMount.current) {
            didMount.current = true;
            setTimeout(() => {
                setRunId(backPostResp.run_id)
            }, 1000);
            return;
        }
    });
    return (
        <div className="App">
            <Navbar selected='upload'/>
            <Queue backPostResp={backPostResp}/>
        </div>
    );
}

export default FileQueueView;