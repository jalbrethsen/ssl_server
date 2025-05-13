# make dirs for script and certs
mkdir -p ~/.local/certs
mkdir -p ~/.local/bin
# make script part of path
export PATH="$PATH:~/.local/bin"
# make path permanent
PATH_STR='PATH="$PATH:~/.local/bin"' 
if ! grep -q -F "$PATH_STR" "$HOME/.profile"; then
  echo "$PATH_STR" >> ~/.profile
fi
# copy script and make executable
chmod +x ./ssl_server.py
cp ./ssl_server.py ~/.local/bin/
# generate certs
openssl req -x509 -newkey rsa:4096 -keyout ~/.local/certs/key.pem -out ~/.local/certs/cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
