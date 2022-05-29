import React from 'react';
import Navbar from '../components/Navbar/Navbar.js';
import Queue from '../components/Queue/Queue.js';

function FileQueueView(backPostResp, setRunId){
    setRunId(backPostResp["run_id"]);

    return (
        <div className="App">
            <Navbar selected='upload'/>
            <Queue backPostResp={backPostResp}/>
        </div>
    );
}

export default FileQueueView;