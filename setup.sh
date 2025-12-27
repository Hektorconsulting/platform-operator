#!/bin/bash
cd /opt/operator || exit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp platform-operator.service /etc/systemd/system/
systemctl daemon-reexec
systemctl enable --now platform-operator.service
