# fresh install and docker setup
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Git 
sudo yum install git -y

# no need to install python already

# install pip
sudo yum -y install python-pip