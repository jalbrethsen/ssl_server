#!/usr/bin/env python3
import http.server
import ssl
from ssl import PROTOCOL_TLS_SERVER
import argparse
import time
from os import environ
'''
Author: Justin Albrethsen
Purpose: Create reusable simple python web server wrapped in SSL
'''

def serve(keyfile,certfile):
    # use simple http server request handler
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer((HOST, PORT), Handler)
    try:
        print("Web Server listening at => " + HOST + ":" + str(PORT))
        # create SSL context
        sslcontext = ssl.SSLContext(PROTOCOL_TLS_SERVER)
        sslcontext.load_cert_chain(keyfile=keyfile, certfile=certfile)
        # wrap http socket in our SSL context
        httpd.socket = sslcontext.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, shutting down.")
    finally:
        httpd.server_close() # Clean up the server
        httpd = None
        print("Server has been closed.")

if __name__ == '__main__':
    home_dir = environ['HOME']
    parser = argparse.ArgumentParser("ssl_server")
    parser.add_argument("--host",help="The address to bind to",
            default='0.0.0.0',type=str, required=False
    )
    parser.add_argument("--port",help="The port to bind to",
            default=8443,type=int, required=False
    )
    parser.add_argument("--keyfile",help="The path to ssl key file",
            default=f"{home_dir}/.local/certs/key.pem", required=False
    )
    parser.add_argument("--certfile",help="The path to ssl certificate",
            default=f"{home_dir}/.local/certs/cert.pem", required=False
    )
    args = parser.parse_args()
    HOST = args.host
    PORT = args.port
    keyfile = args.keyfile
    certfile = args.certfile
    serve(keyfile,certfile)

