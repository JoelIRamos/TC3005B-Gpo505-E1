import Navbar from '../components/Navbar/Navbar.js';
import Titulo from '../components/Titulo/Titulo';
import '../App.css';
import ContenedorDatos from '../components/ContenedorDatos/ContenedorDatos.js';
import ContainerDB from '../components/ContainerDB/ContainerDB.js';


function dashboardView({createGraph, graphList, atributos, deleteGraph, indexGraph, setURL, runId, infoGeneral}) {

  let GraphCont = {id: indexGraph, atributos: atributos, deleteGraph: deleteGraph}

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
      < Titulo runId={runId} />
      <div className="row">
            <ContenedorDatos datos={infoGeneral["result"]["AnomalyRelations"]} label='Relaciones Anómalas' color='red'/>
            <ContenedorDatos datos={`${infoGeneral["result"]["AnomalyRelationsPercentage"]}%`} label='Porcentaje de Relaciones Anómalas' color='red'/>
            <ContenedorDatos datos={`${infoGeneral["result"]["AnomatyPercentage"]}%`} label='Porcentaje de Anomalías' color='yellow'/>
            <ContenedorDatos datos={infoGeneral["result"]["TotalAnomalys"]} label='Total de Anomalías' color='yellow'/>
      </div>
      {graphList.map((element, i) => (
        < ContainerDB runId={runId} key={element.id} indexGraph={element.id} atributos={element.atributos} deleteGraph={element.deleteGraph} setURL = {setURL} />
      ))}
      <div className='container-button-add'><button onClick={(() => createGraph(GraphCont))} className='button-add'>+</button></div>
    </div>
  );
}

export default dashboardView;