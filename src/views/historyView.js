import Navbar from '../components/Navbar/Navbar.js';
import Tabla from '../components/Tabla';
import '../index.css';

function historyView() {
  return (
    <div className="App">
      <Navbar />
      <div className="container-app">
          <div className="area-historial">
            <Tabla/>
          </div>
      </div>
      
    </div>
  );
}

export default historyView;