import { fireEvent,querySelector, getQueriesForElement, render, screen } from '@testing-library/react';
import React from 'react';
import ReactDOM from "react-dom";
import Titulo from './Titulo';


test("Prueba 3", () => {
    const root = document.createElement("div")
    ReactDOM.render(<Titulo />, root)

    expect(root.querySelector("h1").textContent).toBe("Análisis de archivo NombreArchivo_Ejemplo");
})