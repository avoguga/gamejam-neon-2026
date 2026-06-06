#!/usr/bin/env python3
"""
Servidor local que espelha EXATAMENTE o que o Coolify vai servir.
Serve a pasta ./deploy/ :

  /         -> deploy/index.html        (protótipo HTML de testes)
  /unity/   -> deploy/unity/index.html  (build WebGL da Unity, .unityweb)

Os arquivos .unityweb (Gzip + Decompression Fallback) NÃO precisam de header
especial — o loader.js da Unity descomprime sozinho.

Uso:  python serve.py            (porta 8000)
      python serve.py 8080       (porta custom)
"""
import http.server
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    if not os.path.isdir(BASE):
        print(f"ERRO: pasta nao encontrada: {BASE}")
        sys.exit(1)
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Protótipo  ->  http://localhost:{PORT}/")
        print(f"Unity      ->  http://localhost:{PORT}/unity/")
        print("Ctrl+C para parar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
