#curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
sudo apt install nodejs python3 python3-pip
git clone https://github.com/Seeed-Studio/Seeed_Python_DHT.git
cd Seeed_Python_DHT
sudo python setup.py install
cp seeed_dht.py ..
cd ..
npm install express pug body-parser

pip3 install requests
