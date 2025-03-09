from fastapi import FastAPI
from routers import router
import threading
import uvicorn
from cli import CLI
import time
import requests
app = FastAPI()

app.include_router(router)


def server_start():
    """
    Starts the FastAPI server using Uvicorn.

    Runs the server on localhost at port 8080.
    """
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

    server_thread = threading.Thread(target=server_start)

    server_thread.daemon = True
    server_thread.start()


    server_ready = False
    while not server_ready:
        try:
            response = requests.get("http://127.0.0.1:8080")
            if response.status_code == 200:
                server_ready = True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    
    run_cli()
