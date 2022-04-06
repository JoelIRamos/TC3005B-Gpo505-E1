import '../../App.css';
import { FaSearch, FaArrowRight} from "react-icons/fa"

function barraBusqueda() {
    return (
        
        <div className="busqueda">
            <div className="icono-busqueda">
                <FaSearch id="search"/>
            </div>
            <div className="icono-flecha">
                <FaArrowRight id="search"/>
            </div>
            
            
        </div>
    );
  }
  
  export default barraBusqueda;