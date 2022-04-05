import '../index.css';
import BarraBusqueda from '../BarraBusqueda/BarraBusqueda'
import TarjetaHitorial from '../TarjetaHistorial/TarjetaHistorial'
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