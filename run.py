#!app/env/bin/python3
from app import application
application.run(host='127.0.0.1',
                port=8000,
                debug=True)