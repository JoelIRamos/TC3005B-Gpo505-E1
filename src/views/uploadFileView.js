import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import ButtonUpload from '../components/ButtonUpload/ButtonUpload.js';

function uploadFileView() {
  return (
    <div className="App">
      <Navbar selected='upload' />
      <div className='container-up'>
       < ButtonUpload />
      </div>
    </div>
  );
}

export default uploadFileView;