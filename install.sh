echo Installing pip
sudo apt-get -y install python3-pip

echo Installing Requirements
sudo pip3 install -r requirements.txt

echo Setting server to autostart
sudo sed -i "`wc -l < /etc/rc.local`i\\python3 $PWD/main.py &\\" /etc/rc.local
