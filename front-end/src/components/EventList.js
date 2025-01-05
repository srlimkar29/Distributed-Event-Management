import React, { useEffect, useState } from "react";
import { fetchEvents } from "../api/eventApi"; // Ensure eventApi.js is properly imported

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents()
      .then((data) => setEvents(data))
      .catch((error) => console.error("Error fetching events:", error));
  }, []);

  return (
    <div>
      <h2>Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.EventID}>{event.EventDetails.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default EventList;
