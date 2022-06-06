import React from 'react'
import { FaAngleUp } from 'react-icons/fa'
import './ButtonCircle.css'

function ButtonCircle({event}) {
    return(
        <div className="button-circle-container" onClick={event}>
            <div className="button-circle">
                <div className="button-icon">
                    <FaAngleUp/>
                </div>
            </div>
        </div>
    )
}

export default ButtonCircle