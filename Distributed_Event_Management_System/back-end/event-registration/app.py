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
    event_table = dynamodb.Table('Events')
except Exception as e:
    logger.error(f"Error connecting to DynamoDB: {str(e)}")
    event_table = None

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home route to verify the service is running."""
    return jsonify({'message': 'Event Registration Service is running!'}), 200

@app.route('/add_event', methods=['POST'])
def add_event():
    """Add a new event to the Events table."""
    if event_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    data = request.json
    required_fields = ['EventID', 'OrganizerID', 'EventDetails']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    event_id = data['EventID']
    organizer_id = data['OrganizerID']
    event_details = data.get('EventDetails', {})
    max_capacity = data.get('MaxCapacity', 0)

    try:
        event_table.put_item(
            Item={
                'EventID': event_id,
                'OrganizerID': organizer_id,
                'EventDetails': event_details,
                'MaxCapacity': max_capacity,
                'RegisteredUsers': 0
            }
        )
        return jsonify({'status': 'Event added successfully'}), 201
    except Exception as e:
        logger.error(f"Error adding event: {str(e)}")
        return jsonify({'error': f"Error adding event: {str(e)}"}), 500

@app.route('/get_event/<event_id>/<organizer_id>', methods=['GET'])
def get_event(event_id, organizer_id):
    """Retrieve a specific event by EventID and OrganizerID."""
    if event_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = event_table.get_item(
            Key={
                'EventID': event_id,
                'OrganizerID': organizer_id
            }
        )
        item = response.get('Item')
        if item:
            return jsonify(item), 200
        else:
            return jsonify({'error': 'Event not found'}), 404
    except Exception as e:
        logger.error(f"Error retrieving event: {str(e)}")
        return jsonify({'error': f"Error retrieving event: {str(e)}"}), 500

@app.route('/events', methods=['GET'])
def get_events():
    """Retrieve all events."""
    if event_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = event_table.scan()
        items = response.get('Items', [])
        if not items:
            return jsonify({'message': 'No events found'}), 200
        return jsonify(items), 200
    except Exception as e:
        logger.error(f"Error retrieving events: {str(e)}")
        return jsonify({'error': f"Error retrieving events: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
