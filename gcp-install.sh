sudo apt-get update
sudo apt-get install git -y
git --version

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world

# docker command was not running. Hence # Add your current user to the docker group
sudo usermod -aG docker $USER

# Apply the new group membership (temporary solution for current session)
newgrp docker

sudo apt install python3.11-venv -y

# start virtual env
python3 -m venv db-test-venv

source db-test-venv/bin/activate
git clone https://github.com/sanzzzay/db-test.git  
cd project-name/
pip install -r requirements.txt 