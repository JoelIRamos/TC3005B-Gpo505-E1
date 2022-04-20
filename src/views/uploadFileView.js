import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import DropFile from '../components/DropFile/DropFile.js';

function uploadFileView() {
  return (
    <div className="App">
      <Navbar selected='upload' />
      <div className='container-up'>
       < DropFile />
      </div>
    </div>
  );
}

export default uploadFileView;