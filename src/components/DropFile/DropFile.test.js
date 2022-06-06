import { fireEvent,querySelector, getQueriesForElement, render, screen } from '@testing-library/react';
import React from 'react';
import ReactDOM from "react-dom";
import DropFile from './DropFile';

//Esta prueba no funciona sin borrar {file.name} de DropFile.js
//Descomentar para probrar
test("Prueba 1", () => {
    const root = document.createElement("div")
    //ReactDOM.render(<DropFile />, root)

    //expect(root.querySelector("h2").textContent).toBe("Sube Aquí tu Archivo");
})