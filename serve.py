#!/usr/bin/env python3
"""Simple local server for the Piksort website."""
import http.server
import socketserver
import os

PORT = 3000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.webp': 'image/webp', '.svg': 'image/svg+xml'})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Piksort running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()
