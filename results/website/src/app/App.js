import './App.css';

import Map from './components/MapCanvas.js';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <h1 className='App-header__title'>Covering of DGFiP facilities on French territory</h1>
      </header>
      <Map/>
    </div>
  );
}

export default App;
