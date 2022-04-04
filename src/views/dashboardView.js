import Navbar from '../components/Navbar';
import Graph from '../components/Graph';
import Titulo from '../components/Titulo';
import '../index.css';

function dashboardView() {
  return (
    <div className="App">
      <Navbar />
      <div className="container-app">
        < Titulo />
        <div className="graph">
          <Graph />
        </div>
      </div>
    </div>
  );
}

export default dashboardView;