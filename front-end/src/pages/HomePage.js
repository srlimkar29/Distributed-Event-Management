import React, { useEffect, useState } from 'react';
import { fetchEvents } from '../api/eventApi'; // Import the API function
import { Link } from 'react-router-dom'; // Import Link for navigation to Event Page

const HomePage = () => {
  const [events, setEvents] = useState([]); // State to store events
  const [loading, setLoading] = useState(true); // Loading state

  useEffect(() => {
    // Fetch events from the backend
    fetchEvents()
      .then((data) => {
        setEvents(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching events:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading events...</p>;
  }

  return (
    <div>
      <h2>Welcome to the Event Management System</h2>
      <h3>Available Events</h3>
      <ul>
        {events.map((event) => (
          <li key={event.EventID}>
            <Link to={`/events/${event.EventID}/${event.OrganizerID}`}>
              {event.EventDetails?.Name || 'Unnamed Event'} - {event.EventDetails?.Date || 'No Date'}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
