from fastapi import FastAPI
from routers import router
import threading
import time
from cli import CLI
app = FastAPI()
app.include_router(router)


def server_start():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)   

def run_cli():
    cli = CLI()
    cli.start_message()
    
if __name__ == "__main__":
    server_thread = threading.Thread(target=server_start)
    server_thread.daemon = True 
    server_thread.start()
    time.sleep(1)
    run_cli()
    
    
    
