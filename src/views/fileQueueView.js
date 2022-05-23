import React from 'react';
import Navbar from '../components/Navbar/Navbar.js';
import Queue from '../components/Queue/Queue.js';

function FileQueueView(){

    return (
        <div className="App">
            <Navbar selected='upload'/>
            <Queue/>
        </div>
    );
}

export default FileQueueView;