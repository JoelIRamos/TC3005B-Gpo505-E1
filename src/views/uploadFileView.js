import Navbar from '../components/Navbar/Navbar.js';
import '../App.css';
import DropFile from '../components/DropFile/DropFile.js';

function uploadFileView({file, onFileDrop, fileRemove, setCsvFile}) {
  return (
    <div className="App">
      <Navbar selected='upload' />
      <div className='container-up'>
       < DropFile setCsvFile={setCsvFile} file={file} onFileDrop={onFileDrop} fileRemove={fileRemove}/>
      </div>
    </div>
  );
}

export default uploadFileView;