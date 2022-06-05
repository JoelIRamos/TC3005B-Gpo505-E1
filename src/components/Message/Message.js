import React from "react";
import "./Message.css"
import Titulo from  "../Titulo/Titulo"
import Button from '../Button/GenericButton';
import {Link} from "react-router-dom";

function Message({title, message, showButton}) {
  return (

    <div className='message-view-container'>
        <div className='message-container'>
            {title !== undefined && title !== null && title !== '' 
            ?
            <div className='message-box'>
                <h1 className="">{title}</h1>
                <h2 className='title'>{message}</h2>
            </div>
            :
            <div className='message-box'>
                <h1 className='title'>{message}</h1>
            </div>}
        </div>
        {showButton 
            ?
            <Link to='/'>
                <div className="button">
                    <Button text={"Pagino de inicio"}/>
                </div>
            </Link> 
            :
            <div/>
        }
        
    </div>
  )
}

export default Message