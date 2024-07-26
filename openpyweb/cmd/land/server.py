from openpyweb import serv
import os

try:
    port = serv.port
    host = "localhost"
    serv.run(host=host, port=port)
except KeyboardInterrupt as e:
    serv.terminated()
