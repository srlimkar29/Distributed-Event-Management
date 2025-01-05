import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'; // To access route parameters
import { fetchEventById } from '../api/eventApi'; // Import the API function

const EventPage = () => {
  const { id, organizerId } = useParams(); // Get the event ID and organizer ID from the URL
  const [event, setEvent] = useState(null); // State to store event details
  const [loading, setLoading] = useState(true); // Loading state

  useEffect(() => {
    // Fetch event details from the backend
    fetchEventById(id, organizerId)
      .then((data) => {
        setEvent(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching event details:', error);
        setLoading(false);
      });
  }, [id, organizerId]);

  if (loading) {
    return <p>Loading event details...</p>;
  }

  if (!event) {
    return <p>Event not found.</p>;
  }

  return (
    <div>
      <h2>Event Details</h2>
      <p>Name: {event.EventDetails?.Name || 'Unnamed Event'}</p>
      <p>Date: {event.EventDetails?.Date || 'No Date Provided'}</p>
      <p>Description: {event.EventDetails?.Description || 'No Description'}</p>
    </div>
  );
};

export default EventPage;
