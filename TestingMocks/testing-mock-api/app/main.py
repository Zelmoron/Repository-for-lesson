from fastapi import FastAPI
from routers import router
import threading
import time
from cli import CLI

# Create a FastAPI application instance
app = FastAPI()

# Include the router for handling API endpoints
app.include_router(router)


def server_start():
    """
    Starts the FastAPI server using Uvicorn.

    Runs the server on localhost at port 8080.
    """
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)   


def run_cli():
    """
    Runs the Command Line Interface (CLI).

    Initializes the CLI and starts the interaction loop.
    """
    cli = CLI()
    cli.start_message()


if __name__ == "__main__":
    """
    Main entry point of the application.

    Starts the server in a separate thread and then runs the CLI.
    """
    # Create a thread for running the server
    server_thread = threading.Thread(target=server_start)
    # Set the thread as daemon so it exits when the main thread exits
    server_thread.daemon = True 
    server_thread.start()
    
    # Wait for a second to ensure the server is running before starting the CLI
    time.sleep(1)
    run_cli()
