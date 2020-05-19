import React from 'react';
import css from './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Counter } from 'components/counter/Counter';

function App() {
  return (
    <div className="App">
      <div className="wrapper">
        <Router>
          <div>
            <Link className="link" to="/">Home</Link>
            <Link className="link" to="/counter">Counter</Link>
          </div>
          <Switch>
            <Route path="/counter" exact>
              <Counter />
            </Route>
            <Route path="/">
              "Welcome"
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
