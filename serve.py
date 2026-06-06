#!/usr/bin/env python3
"""
Servidor local para o projeto game-jam.

- Raiz  /        -> index.html (jogo de dominó)
- Rota  /unity/  -> build WebGL da Unity em ./gamejam-neon2026/
- Serve arquivos Brotli (.br) com o header Content-Encoding correto,
  que é o que faz o build da Unity rodar sem o erro "Unable to parse ...br".

Uso:  python serve.py            (porta 8000)
      python serve.py 8080       (porta custom)
"""
import http.server
import os
import sys
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
UNITY_DIR = os.path.join(BASE, "gamejam-neon2026")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# tipo "real" de cada arquivo comprimido (a extensão por baixo do .br)
INNER_TYPE = {
    ".js": "application/javascript",
    ".wasm": "application/wasm",
    ".data": "application/octet-stream",
    ".json": "application/octet-stream",
}


class Handler(http.server.SimpleHTTPRequestHandler):
    # ---- roteamento: /unity -> pasta do build da Unity ----
    def translate_path(self, path):
        path = path.split("?", 1)[0].split("#", 1)[0]
        path = urllib.parse.unquote(path)

        if path == "/unity" or path.startswith("/unity/"):
            rel = path[len("/unity"):].lstrip("/")
            full = os.path.join(UNITY_DIR, rel.replace("/", os.sep))
        else:
            rel = path.lstrip("/")
            full = os.path.join(BASE, rel.replace("/", os.sep))

        if os.path.isdir(full):
            full = os.path.join(full, "index.html")
        if rel == "" and not path.startswith("/unity"):
            full = os.path.join(BASE, "index.html")
        return full

    # ---- redireciona /unity  ->  /unity/ (pra os caminhos relativos baterem) ----
    def do_GET(self):
        if self.path.rstrip() == "/unity":
            self.send_response(301)
            self.send_header("Location", "/unity/")
            self.end_headers()
            return
        super().do_GET()

    # ---- Content-Type correto pros .br (usa a extensão interna) ----
    def guess_type(self, path):
        p = str(path)
        if p.endswith(".br"):
            ext = os.path.splitext(p[:-3])[1].lower()
            return INNER_TYPE.get(ext, "application/octet-stream")
        return super().guess_type(path)

    # ---- injeta Content-Encoding: br + no-cache ----
    def send_head(self):
        self._is_br = str(self.translate_path(self.path)).endswith(".br")
        return super().send_head()

    def end_headers(self):
        if getattr(self, "_is_br", False):
            self.send_header("Content-Encoding", "br")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    os.chdir(BASE)
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Servindo game-jam em  http://localhost:{PORT}/")
        print(f"Unity WebGL em         http://localhost:{PORT}/unity/")
        print("Ctrl+C para parar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
