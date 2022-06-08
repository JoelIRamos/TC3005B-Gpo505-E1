import React from "react";
import "./BubbleGraphDictionaryElement.css";

const BubbleGraphDictionaryElement = ({id, name}) => {
    return (
        <div className={'bubblegraph-dictionary-element'}>
            <div className={'bubblegraph-dictionary-element-id'}>
                {id}
            </div>
            <div className={'bubblegraph-dictionary-element-name'}>
                {name}
            </div>
        </div>
    )
}
export default BubbleGraphDictionaryElement;