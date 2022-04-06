import Navbar from '../components/Navbar/Navbar.js';
import Tabla from '../components/Tabla/Tabla';
import '../App.css';

function historyView() {
  return (
    <div className="App">
      <Navbar selected='history' />
      <div className="container-app">
          <div className="area-historial">
            <Tabla/>
          </div>
      </div>
      
    </div>
  );
}

export default historyView;