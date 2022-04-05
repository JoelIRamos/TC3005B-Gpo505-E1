import Navbar from '../components/Navbar/Navbar';
import Graph from '../components/Graph/Graph';
import Titulo from '../components/Titulo/Titulo';
import '../App.css';

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