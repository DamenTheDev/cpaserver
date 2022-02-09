wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py
git clone https://github.com/DamenTheDev/cpaserver
mv cpaserver/* .
rm -r cpaserver/
python3 -m pip install -r requirements.txt
chmod +x login.sh