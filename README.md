# SSL Server
This project creates a simple reusable python http server that is wrapped in ssl. While it is easy to spin up a simple python http server using
```
python3 -m http.server
```
There is no equivalent for using SSL (HTTPS).

I created this project to fill the gap and give me a quick and easy way to spin up a python web server and also protect the communications with SSL.

# Getting started
To get started, first clone the project
```
git clone https://github.com/jalbrethsen/ssl_server.git
```
Next go to the project directory and make the install script executable
```
cd ssl_server
chmod +x install.sh
```
Now you can run the install script which uses openssl to generate a keypair
and installs the certs and script to your $HOME/.local directory and adds to
your path
```
./install.sh
```
Now you can use these keys to serve a simple python http server with SSL
```
ssl_server.py
```
