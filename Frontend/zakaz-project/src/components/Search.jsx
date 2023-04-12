import React from 'react';
import "../styles/Search.css"
import * as mdb from 'mdb-ui-kit';

const Search = (props) => {
    return(
        <div className='search-box'>
            <input
                className="search-field"
                type="text"
                placeholder="Вакансии"
            />
            <button
                className="search-button"
                onClick={alert('Clicked!')}>Найти
            </button>
        </div>
    );
}

export default Search;