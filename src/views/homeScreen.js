import InvNavbar from '../components/Navbar/Invisible-Navbar.js';
import '../App.css';
import HomeSelectionBtn from '../components/HomeSelectionButton/HomeSelectionButton.js';
import Queue from '../components/Queue/Queue.js';

function homeScreen() {
  return (
    <div className="App">
      <InvNavbar/>
      <div className="home-background">
        <div className="home-btn-container">
          <HomeSelectionBtn path='/FileUpLoad' titulo='Subir Archivo' label='Crear un nuevo analisis' color='red' icon='cloud'/>
          <HomeSelectionBtn path='/Dashboard' titulo='Dashboard' label='Revisar el dashboard del analisis actual' color='yellow' icon='chart'/>
          <HomeSelectionBtn path='/Historial' titulo='Historial' label='Revisar el historial' color='gray' icon='history'/>
        </div>
      </div>
    </div>
  );
}

export default homeScreen;

          /*<Link to='/FileUpLoad'>
            <button className="home-button">
              <HomeSelectionBtn titulo='Subir Archivo' label='Crear un nuevo analisis' color='red'/>
            </button>
          </Link>
          <Link to='/Dashboard'>
            <button className="home-button">
              <HomeSelectionBtn titulo='Dashboard' label='Revisar el dashboard del analisis actual' color='yellow'/>
            </button>
          </Link>
          <Link to='/Historial'>
            <button className="home-button">
              <HomeSelectionBtn titulo='Historial' label='Revisar el historial' color='gray'/>
            </button>
          </Link>*/