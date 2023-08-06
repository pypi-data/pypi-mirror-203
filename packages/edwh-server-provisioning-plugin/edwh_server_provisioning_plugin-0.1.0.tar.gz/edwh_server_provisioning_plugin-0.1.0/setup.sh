#!/bin/bash
sudo apt install python3.11 python3.11-venv
python3.11 -m pip install pipx
pipx install fabric
pipx inject fabric tabulate pyyaml
pipx install invoke
pipx inject invoke httpx humanize tabulate pyyaml
