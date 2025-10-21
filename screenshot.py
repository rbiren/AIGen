#!/usr/bin/env python3
import subprocess
import time
import os

# Start a simple HTTP server in the background
os.chdir('/home/user/AIGen/frontend/dist')

# Start server
print("Starting HTTP server on port 8080...")
server = subprocess.Popen(['python3', '-m', 'http.server', '8080'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

time.sleep(2)
print(f"Server started with PID: {server.pid}")
print("Visit http://localhost:8080 to view the application")
print("\nPress Ctrl+C to stop the server...")

try:
    server.wait()
except KeyboardInterrupt:
    print("\nStopping server...")
    server.terminate()
    server.wait()
