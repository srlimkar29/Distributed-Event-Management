import boto3
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load environment variables from .env file
load_dotenv()

# Load AWS credentials and region from environment variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1') 

# Connect to DynamoDB
try:
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    ticket_table = dynamodb.Table('Tickets')  # Ensure this matches the actual table name
except Exception as e:
    logger.error(f"Error connecting to DynamoDB: {str(e)}")
    ticket_table = None

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home route to verify the service is running."""
    return jsonify({'message': 'Ticketing Service is running!'}), 200

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    """Add a new ticket to the Tickets table."""
    if ticket_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    data = request.json
    required_fields = ['TicketID', 'EventID', 'UserID']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    ticket_id = data['TicketID']
    event_id = data['EventID']
    user_id = data['UserID']
    status = data.get('Status', 'Pending')  # Default to "Pending" if not provided

    try:
        # Add ticket to DynamoDB
        ticket_table.put_item(
            Item={
                'TicketID': ticket_id,
                'EventID': event_id,
                'UserID': user_id,
                'Status': status
            }
        )
        logger.info(f"Ticket added: {ticket_id}")
        return jsonify({'status': 'Ticket purchased successfully'}), 201
    except Exception as e:
        logger.error(f"Error adding ticket: {str(e)}")
        return jsonify({'error': f"Error adding ticket: {str(e)}"}), 500

@app.route('/get_ticket/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Retrieve a ticket by TicketID."""
    if ticket_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = ticket_table.get_item(
            Key={
                'TicketID': ticket_id
            }
        )
        item = response.get('Item')
        if item:
            logger.info(f"Ticket retrieved: {ticket_id}")
            return jsonify(item), 200
        else:
            logger.warning(f"Ticket not found: {ticket_id}")
            return jsonify({'error': 'Ticket not found'}), 404
    except Exception as e:
        logger.error(f"Error retrieving ticket {ticket_id}: {str(e)}")
        return jsonify({'error': f"Error retrieving ticket: {str(e)}"}), 500

@app.route('/tickets', methods=['GET'])
def get_all_tickets():
    """Retrieve all tickets."""
    if ticket_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = ticket_table.scan()
        items = response.get('Items', [])
        logger.info(f"Retrieved {len(items)} tickets")
        return jsonify(items), 200
    except Exception as e:
        logger.error(f"Error retrieving all tickets: {str(e)}")
        return jsonify({'error': f"Error retrieving all tickets: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3002)
