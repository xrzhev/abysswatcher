import falcon

import config
import Tops

CONFIG_PATH = "./abysswatcher.conf"

class CORSMiddleware:
    def __init__(self):
        self.spa_host = config.SPA["Host"]
        self.spa_port = config.SPA["Port"]

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '{0}:{1}'.format(self.spa_host, self.spa_port))
        resp.set_header('Access-Control-Allow-Headers', 'content-type')
        resp.set_header('Access-Control-Allow-Credentials', 'true')


app = falcon.API(middleware=[CORSMiddleware()])
app.add_route("/", Tops.Tops())


if __name__ == "__main__":
    from wsgiref import simple_server

    listen_host = config.Server["Host"]
    listen_port = config.Server["Port"]

    httpd = simple_server.make_server(listen_host, listen_port, app)
    httpd.serve_forever()
