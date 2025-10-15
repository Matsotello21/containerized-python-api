from flask import Flask , jsonify

#Initializing the Flask Application
app = Flask(__name__)

#Defining the /status endpoint 
@app.route('/status', methods=['GET'])
def get_status():
    """
    This endpoint returns the current status of the API.
    It's a simple health check.
     """
    return jsonify({
        "status": "ok",
        "version": "1.0.0"

    })

# Main entry point for the application 
if __name__ == '__main__':
    # The host = '0.0.0.0' is crucial for Docker 
    # It makes the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)