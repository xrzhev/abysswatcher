import falcon
from configparser import ConfigParser

from pages import *


CONFIG_PATH = "./abysswatcher.conf"

class CORSMiddleware:
    def __init__(self):
        from configparser import ConfigParser
        self.conf = ConfigParser()
        self.conf.read(CONFIG_PATH)
        self.spa_host = self.conf.get("SPA", "Host")
        self.spa_port = self.conf.getint("SPA", "Port")

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '{0}:{1}'.format(self.spa_host, self.spa_port))
        resp.set_header('Access-Control-Allow-Headers', 'content-type')
        resp.set_header('Access-Control-Allow-Credentials', 'true')


app = falcon.API(middleware=[CORSMiddleware()])
app.add_route("/", Tops())


if __name__ == "__main__":
    from wsgiref import simple_server

    conf = ConfigParser()
    conf.read(CONFIG_PATH)


    listen_host = conf.get("Server", "Host")
    listen_port = conf.getint("Server", "Port")

    httpd = simple_server.make_server(listen_host, listen_port, app)
    httpd.serve_forever()
