#!/bin/bash
python3 -m venv app/env
app/env/bin/pip3 install -r requirements.txt
chmod 744 run.py
