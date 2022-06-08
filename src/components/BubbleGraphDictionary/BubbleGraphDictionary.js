import React from 'react'
import {useState, useEffect, useRef} from 'react'
import BubbleGraphDictionaryElement from '../BubbleGraphDictionaryElement/BubbleGraphDictionaryElement'
import './BubbleGraphDictionary.css'

const BubbleGraphDictionary = ({dictionaryAtt1, dictionaryAtt2, attribute1, attribute2}) => {
  const [selected, setSelected] = useState()
  const selectedAtt = useRef()

  useEffect(() => {
    setSelected(attribute1)
    selectedAtt.current = dictionaryAtt1
  }, [])


  if(dictionaryAtt1 === undefined || dictionaryAtt2 === undefined || dictionaryAtt1 === null || dictionaryAtt2 === null || attribute1 === null || attribute2 === null || attribute1 === undefined || attribute2 === undefined){
    return(
      <div className={'bubblegraph-dictionary-container'}>
        Cargando...
      </div>    
    )
  }  



  return (
    <div className={'bubblegraph-dictionary-container'}>
      <div className={'bubblegraph-dictionary-attribute-selector'}>
          <div className={`bubblegraph-dictionary-attribute-selector-title corners-left red ${selected !== attribute1 ? 'unselected-attribute-title-red':''}`} onClick={() => {setSelected(attribute1); selectedAtt.current = dictionaryAtt1;}}>
            <div>
              {attribute1}
            </div>
          </div>
          <div className={`bubblegraph-dictionary-attribute-selector-title corners-right yellow ${selected !== attribute2 ? 'unselected-attribute-title-yellow':''}`} onClick={() => {setSelected(attribute2); selectedAtt.current = dictionaryAtt2;}}> 
            {attribute2}
          </div>
      </div>
      <div className={'bubblegraph-dictionary-attribute-list'}>
        {selectedAtt.current !== undefined && Object.entries(selectedAtt.current).map((dict, i) => {
            return (
              <BubbleGraphDictionaryElement key={i} id={dict[0]} name={dict[1]}/>
            )
          })}
      </div>
    </div>
  )
}

export default BubbleGraphDictionary