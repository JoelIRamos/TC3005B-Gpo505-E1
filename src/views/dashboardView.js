import Navbar from '../components/Navbar/Navbar.js';
import Graph from '../components/Graph/Graph.js';
import Titulo from '../components/Titulo/Titulo';
import '../App.css';
import ContenedorDatos from '../components/ContenedorDatos/ContenedorDatos.js';
import FormAtributos from '../components/FormAtributos/FormAtributos.js';

function dashboardView({datos, atributos, onSelect, atributo1}) {
  return (
    <div className="App">
      <Navbar selected='dashboard' />
      <div className="container-app">
        <div className='col col-1'>
          < Titulo />
          <Graph data = {datos} atributo1={atributo1} />
        </div>
        <div className="col col-2">
          <div className="row">
            <ContenedorDatos datos={11216} label='Total de Anomalías Detectadas' color='red'/>
            <ContenedorDatos datos='52%' label='Porcentaje de Anomalías' color='red'/>
          </div>
          <div className="row">
            <ContenedorDatos datos={4536} label='Anomalías Detectadas' color='yellow'/>
            <ContenedorDatos datos='39%' label='Porcentaje de Anomalías' color='yellow'/>
          </div>
          <div className='row'>
            < FormAtributos atributos={atributos} onSelect={onSelect} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default dashboardView;