from app import create_app
import os
app = create_app()

if __name__ == '__main__':
    # Get port from Azure Web App environment variable or fallback to PORT or default 8080
    port = int(os.environ.get('WEBSITES_PORT') or os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
