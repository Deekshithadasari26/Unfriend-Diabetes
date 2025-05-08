import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import the Streamlit application
from app import st

# Create the WSGI application
app = st.server.server.Server.get_current()._app

# This allows Gunicorn to interface with the application
if __name__ == '__main__':
    app.run()