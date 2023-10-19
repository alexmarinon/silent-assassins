from typing import Any
from flask import Flask, render_template_string
from .routes import routes_registry

class Webserver():
    def __init__(self) -> None:
        self.app = Flask(import_name='app')
        self.routes = routes_registry
        self.register_routes()
    
    def run(self):
        self.app.run('0.0.0.0', port=8080, debug=True)

    def register_routes(self):
        for route, handler in self.routes.items():
            self.app.add_url_rule(route, view_func=handler)

app = Webserver()
