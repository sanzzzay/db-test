#!/bin/bash

# Update package lists
sudo apt-get update

# Install Git
sudo apt-get install git -y
git --version

# Install Docker prerequisites
sudo apt-get update
sudo apt-get install ca-certificates curl -y

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
 $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again
sudo apt-get update

# Install Docker packages
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Test Docker installation
sudo docker run hello-world

# Add current user to the docker group
sudo usermod -aG docker $USER

# Apply the new group membership for current session
newgrp docker

# Install Python venv package
sudo apt-get install python3.11-venv -y

# Optional: Display successful completion message
echo "Installation complete: Git, Docker, and Python venv are now installed."

# start virtual env
python3 -m venv db-test-venv

source db-test-venv/bin/activate
git clone https://github.com/sanzzzay/db-test.git  
cd db-test/
pip install -r requirements.txt 