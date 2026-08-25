#!/usr/bin/env python3
"""Servidor do dashboard quest 003 com no-store (evita cache do navegador)."""
import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-store, max-age=0')
        super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(("0.0.0.0",8137),H) as s:
    print('serving 8137 no-store'); s.serve_forever()
