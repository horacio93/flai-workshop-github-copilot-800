import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img 
                src="/octofitapp-small.png" 
                alt="OctoFit Logo" 
                className="navbar-logo"
              />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="hero-section text-center">
                <h1 className="display-3">🏃 Welcome to OctoFit Tracker</h1>
                <p className="lead fs-4">Track your fitness activities, compete with teams, and achieve your goals!</p>
                <hr className="my-4 bg-white" />
                <p className="fs-5">Navigate using the menu above to explore different features.</p>
              </div>
              
              <div className="row mt-4">
                <div className="col-md-4 mb-3">
                  <div className="card text-center">
                    <div className="card-body">
                      <h5 className="card-title">👥 Users</h5>
                      <p className="card-text">View and manage user profiles</p>
                      <Link to="/users" className="btn btn-primary">View Users</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-3">
                  <div className="card text-center">
                    <div className="card-body">
                      <h5 className="card-title">📊 Activities</h5>
                      <p className="card-text">Track all fitness activities</p>
                      <Link to="/activities" className="btn btn-primary">View Activities</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-3">
                  <div className="card text-center">
                    <div className="card-body">
                      <h5 className="card-title">🏆 Leaderboard</h5>
                      <p className="card-text">See top performers</p>
                      <Link to="/leaderboard" className="btn btn-primary">View Leaderboard</Link>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="row">
                <div className="col-md-6 mb-3">
                  <div className="card text-center">
                    <div className="card-body">
                      <h5 className="card-title">👫 Teams</h5>
                      <p className="card-text">Explore and join teams</p>
                      <Link to="/teams" className="btn btn-primary">View Teams</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-6 mb-3">
                  <div className="card text-center">
                    <div className="card-body">
                      <h5 className="card-title">💪 Workouts</h5>
                      <p className="card-text">Get personalized workout plans</p>
                      <Link to="/workouts" className="btn btn-primary">View Workouts</Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
