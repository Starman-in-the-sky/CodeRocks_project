import React from 'react';
import './styles/App.css';
import Background from "./components/Background";
import Navbar from "./components/Navbar";
import Search from "./components/Search"
import SignInPage from "./pages/Sign-in-page";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component {
    render() {
        return (
            <div className="App">
                <SignInPage/>
            </div>
        );
    }
}

export default App;
