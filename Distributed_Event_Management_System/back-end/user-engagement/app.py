import boto3
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from dotenv import load_dotenv
import os
from boto3.dynamodb.conditions import Key

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
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
    notifications_table = dynamodb.Table('Notifications')  # Ensure this matches the actual table name
except Exception as e:
    logger.error(f"Error connecting to DynamoDB: {str(e)}")
    notifications_table = None

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home route to verify the service is running."""
    return jsonify({'message': 'User Engagement Service is running!'}), 200

@app.route('/add_notification', methods=['POST'])
def add_notification():
    """Add a new notification to the Notifications table."""
    if notifications_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        data = request.json
        required_fields = ['UserID', 'Timestamp', 'Message']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f"'{field}' is required"}), 400

        user_id = data['UserID']
        timestamp = data['Timestamp']
        message = data['Message']

        # Insert the notification into DynamoDB
        notifications_table.put_item(
            Item={
                'UserID': user_id,
                'Timestamp': int(timestamp),  # Ensure timestamp is an integer
                'Message': message
            }
        )
        logger.info(f"Notification added for UserID: {user_id}")
        return jsonify({'status': 'Notification added successfully'}), 201
    except Exception as e:
        logger.error(f"Error adding notification: {str(e)}")
        return jsonify({'error': f"Error adding notification: {str(e)}"}), 500

@app.route('/get_notifications/<user_id>', methods=['GET'])
def get_notifications(user_id):
    """Retrieve notifications for a specific user."""
    if notifications_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = notifications_table.query(
            KeyConditionExpression=Key('UserID').eq(user_id)
        )
        items = response.get('Items', [])
        logger.info(f"Retrieved {len(items)} notifications for UserID: {user_id}")
        return jsonify(items), 200
    except Exception as e:
        logger.error(f"Error retrieving notifications for UserID {user_id}: {str(e)}")
        return jsonify({'error': f"Error retrieving notifications: {str(e)}"}), 500

@app.route('/notifications', methods=['GET'])
def get_all_notifications():
    """Retrieve all notifications from the Notifications table."""
    if notifications_table is None:
        return jsonify({'error': 'DynamoDB connection not available'}), 500

    try:
        response = notifications_table.scan()
        items = response.get('Items', [])
        logger.info(f"Retrieved {len(items)} notifications from the table")
        return jsonify(items), 200
    except Exception as e:
        logger.error(f"Error retrieving all notifications: {str(e)}")
        return jsonify({'error': f"Error retrieving all notifications: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=3003)
