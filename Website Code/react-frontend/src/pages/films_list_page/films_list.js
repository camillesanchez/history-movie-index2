import React from 'react';
import NavBar from "../../components/NavBar.js";

export default function FilmsList() {
    // const response = axios.get("http://127.0.0.1:5000/selected_film")
    // console.log(response)

  return (
    <>
    <NavBar />
      <div className="App">
        <h1>Films for: <br/> Modern History - World War I</h1> 
        <br/>
        <ul>
          <li>
            <h3>1917</h3>
          </li>
          <li>
            <h3>They shall not grow old</h3>
          </li>
          <li>
            <h3>Journey's end</h3>
          </li>
          <li>
            <h3>Light between oceans</h3>
          </li>
          <li>
            <h3>Titanic</h3>
          </li>
          <li>
            <h3>War Horse</h3>
          </li>
          <li>
            <h3>Tolkien</h3>
          </li>
              
        </ul>

      </div>
    </>
  );
}