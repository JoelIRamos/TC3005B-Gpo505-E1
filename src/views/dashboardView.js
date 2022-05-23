import Navbar from '../components/Navbar/Navbar.js';
import Titulo from '../components/Titulo/Titulo';
import '../App.css';
import ContenedorDatos from '../components/ContenedorDatos/ContenedorDatos.js';
import FormAtributos from '../components/FormAtributos/FormAtributos.js';
import GraphContainer from '../components/GraphContainer/GraphContainer.js';
import ContainerDB from '../components/ContainerDB/ContainerDB.js';

function dashboardView({datos , atributos, onSelect1, onSelect2, atributo1, atributo2, clicked, clickedLi, click, chart, showForm, backGet}) {

  // Props: 
  //   datos = datos dummy
  //   atributos = lista de atributos
  //   onSelect = guarda el atributo para la grafica
  //   atributo1 = atributo #1 que se muestra en la grafica
  //   atributo2 = atributo #1 que se muestra en la grafica
  //   clicked = funcion para el estado del click
  //   clickedLi = funcion para el estado del click y guardar el grafico a desplegar
  //   click = estado de click
  //   chart = estado de grafico a desplegar
  //   showForm = estado para desplegar form para grafico burbuja

  return (
    <div className="App">
      <Navbar selected='dashboard' />
      < Titulo />
      <div className="row">
            <ContenedorDatos datos={11216} label='Total de Anomalías Detectadas' color='red'/>
            <ContenedorDatos datos='52%' label='Porcentaje de Anomalías' color='red'/>
            <ContenedorDatos datos={4536} label='Anomalías Detectadas' color='yellow'/>
            <ContenedorDatos datos='39%' label='Porcentaje de Anomalías' color='yellow'/>
      </div>
      < ContainerDB datos={datos} atributos={atributos} onSelect1={onSelect1} onSelect2={onSelect2} atributo1={atributo1} atributo2={atributo2} clicked={clicked} clickedLi={clickedLi} click={click} chart={chart} showForm={showForm} />
      <div className='container-button-add'><button onClick={backGet} className='button-add'>+</button></div>
    </div>
  );
}

export default dashboardView;