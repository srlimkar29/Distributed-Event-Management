import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import HomePage from './pages/HomePage';
import EventPage from './pages/EventPage';
import TicketPage from './pages/TicketPage';
import Notifications from './components/Notifications';

const App = () => {
  return (
    <Router>
      <div>
        <header>
          <h1>Distributed Event Management System</h1>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/tickets">Tickets</Link>
              </li>
              <li>
                <Link to="/notifications">Notifications</Link>
              </li>
              <li>
                <Link to="/events/1/organizer123">Event Details</Link>
                {/* Replace `/events/1/organizer123` with dynamic links when integrating */}
              </li>
            </ul>
          </nav>
        </header>
        <main>
          <Routes>
            {/* Route for Home Page */}
            <Route path="/" element={<HomePage />} />
            {/* Route for Individual Event Page */}
            <Route path="/events/:id/:organizerId" element={<EventPage />} />
            {/* Route for Ticket Purchase Page */}
            <Route path="/tickets" element={<TicketPage />} />
            {/* Notifications Component */}
            <Route path="/notifications" element={<Notifications />} />
          </Routes>
        </main>
        <footer>
          <p>&copy; 2025 Distributed Event Management System</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
