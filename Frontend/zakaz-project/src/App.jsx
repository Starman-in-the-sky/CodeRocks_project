import React from 'react';
import './styles/App.css';
import Background from "./components/Background";
import Navbar from "./components/Navbar";

class App extends React.Component {
    render() {
        return (
            <div className="App">
                <Background/>
                <Navbar/>
                YESSSSS
            </div>
        );
    }
}

export default App;
