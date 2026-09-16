from http.server import HTTPServer, SimpleHTTPRequestHandler


class UTF8Handler(SimpleHTTPRequestHandler):

    def guess_type(self, path):
        tipo = super().guess_type(path)

        if path.endswith(".html") or path.endswith(".htm"):
            return "text/html; charset=utf-8"

        if path.endswith(".css"):
            return "text/css; charset=utf-8"

        if path.endswith(".js"):
            return "application/javascript; charset=utf-8"

        return tipo


server = HTTPServer(
    ("localhost", 8000),
    UTF8Handler
)

print("Servidor rodando em http://localhost:8000")
server.serve_forever()