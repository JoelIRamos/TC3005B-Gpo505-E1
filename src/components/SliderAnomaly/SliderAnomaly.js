import React from 'react';
import ReactSlider from 'react-slider';
import styled from 'styled-components';

const StyledSlider = styled(ReactSlider)`
    width: 100%;
    height: 1vw;
`;

const StyledThumb = styled.div`
    height: 1vw;
    line-height: 1vw;
    width: 1vw;
    text-align: center;
    background-color: #2c2c2c;
    color: #fff;
    border-radius: 50%;
    cursor: grab;
`;

    
const StyledTrack = styled.div`
top: 0;
bottom: 0;
background: ${props => (props.index === 1 ? '#ddd' : '#ffa82f')};
border-radius: 999px;
`;
    
const Thumb = (props, state) => <StyledThumb {...props}>{}</StyledThumb>;
const Track = (props, state) => <StyledTrack {...props} index={state.index} />;


const SliderAnomaly = ({setParamAnomaly, paramAnomally}) => {
    const changeHandler = (value) => {
        setParamAnomaly(value);
    }

    return (
        <div className='contenedor-slider'>
            <h3 className='title-slider'>{`Sensibilidad de anomalia: ${paramAnomally}`}</h3>
            <StyledSlider defaultValue={paramAnomally} min={-1} max={0} step={0.01} renderTrack={Track} renderThumb={Thumb} onAfterChange={(value, index) => {changeHandler(value)}}/>
        </div>
    )
}

export default SliderAnomaly;