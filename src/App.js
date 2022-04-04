import Navbar from './components/Navbar';
import Graph from './components/Graph';
import Titulo from './components/Titulo';

function App() {
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

export default App;
