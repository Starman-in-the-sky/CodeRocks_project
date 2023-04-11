import React from 'react';
import './styles/App.css';
import Background from "./components/Background";
import Navbar from "./components/Navbar";
import Search from "./components/Search"

class App extends React.Component {
    render() {
        return (
            <div className="App">
                <Search/>
            </div>
        );
    }
}

export default App;
