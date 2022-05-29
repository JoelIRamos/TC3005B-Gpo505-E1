import React, {useEffect, useRef} from 'react';
import Navbar from '../components/Navbar/Navbar.js';
import Queue from '../components/Queue/Queue.js';

function FileQueueView({backPostResp, setRunId}){
    
    const didMount = useRef(false);
    useEffect(() => {
        if(!didMount.current) {
            if (backPostResp !== undefined){
                setRunId(backPostResp.run_id);
                didMount.current = true;
            }
            return;
        }
    }), [backPostResp];
    
    return (
        <div className="App">
            <Navbar selected='upload'/>
            <Queue backPostResp={backPostResp}/>
        </div>
    );
}

export default FileQueueView;