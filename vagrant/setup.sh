#/bin/sh

# install some tools
sudo apt-get install -y git vim gcc build-essential python3-venv
git clone https://github.com/xiaopeng163/ansible_vs_nornir
cd ansible_vs_nornir
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt
