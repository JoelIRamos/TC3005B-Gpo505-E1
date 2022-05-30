import { fireEvent,querySelector, getQueriesForElement, render, screen } from '@testing-library/react';
import React from 'react';
import ReactDOM from "react-dom";
import ContenedorDatos from './ContenedorDatos';

test("Prueba 1", () => {
    const root = document.createElement("div")
    ReactDOM.render(<ContenedorDatos />, root)

    expect(root.querySelector("h1").textContent).toBe("11216");
})
test("Prueba 2", () => {
    const root = document.createElement("div")
    ReactDOM.render(<ContenedorDatos />, root)

    expect(root.querySelector("p").textContent).toBe("Total de Anomalías Detectadas");
})
