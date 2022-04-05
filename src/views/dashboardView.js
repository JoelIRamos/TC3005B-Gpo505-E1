import Navbar from '../components/Navbar';
import Graph from '../components/Graph';
import Titulo from '../components/Titulo';
import '../index.css';
import ContenedorDatos from '../components/ContenedorDatos';
import FormAtributos from '../components/FormAtributos';

function dashboardView({datos, atributos, onSelect, atributo1}) {
  return (
    <div className="App">
      <Navbar />
      <div className="container-app">
        <div className='col col-1'>
          < Titulo />
          <div className="graph">
            <Graph data = {datos} atributo1={atributo1} />
          </div>
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