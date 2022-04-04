import '../index.css';
import BarraBusqueda from './BarraBusqueda'
import TarjetaHitorial from './TarjetaHistorial'
import { FaSearch } from "react-icons/fa"

function historyView() {
    return (
        <div className="historial">
            <BarraBusqueda/>
            <TarjetaHitorial/>
            <TarjetaHitorial/>
            <TarjetaHitorial/>
        </div>
    );
  }
  
  export default historyView;