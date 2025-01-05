import React, { useEffect, useState } from 'react';
import { getAllTickets, purchaseTicket } from '../api/ticketApi'; // Import the API functions

const TicketPage = () => {
  const [tickets, setTickets] = useState([]); // State to store tickets
  const [formData, setFormData] = useState({ EventID: '', UserID: '', Status: 'Pending' }); // State for form input

  useEffect(() => {
    // Fetch all tickets
    getAllTickets()
      .then((data) => setTickets(data))
      .catch((error) => console.error('Error fetching tickets:', error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    purchaseTicket(formData)
      .then(() => {
        alert('Ticket purchased successfully');
        setTickets((prev) => [...prev, formData]); // Update tickets locally
      })
      .catch((error) => console.error('Error purchasing ticket:', error));
  };

  return (
    <div>
      <h2>Your Tickets</h2>
      <ul>
        {tickets.map((ticket) => (
          <li key={ticket.TicketID}>
            Ticket ID: {ticket.TicketID}, Event ID: {ticket.EventID}, Status: {ticket.Status}
          </li>
        ))}
      </ul>

      <h3>Purchase a Ticket</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Event ID"
          value={formData.EventID}
          onChange={(e) => setFormData({ ...formData, EventID: e.target.value })}
        />
        <input
          type="text"
          placeholder="User ID"
          value={formData.UserID}
          onChange={(e) => setFormData({ ...formData, UserID: e.target.value })}
        />
        <input
          type="text"
          placeholder="Status"
          value={formData.Status}
          onChange={(e) => setFormData({ ...formData, Status: e.target.value })}
        />
        <button type="submit">Purchase</button>
      </form>
    </div>
  );
};

export default TicketPage;
