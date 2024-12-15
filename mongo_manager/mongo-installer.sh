# Pull MongoDB image:
sudo docker pull mongo
# Run MongoDB container:
sudo docker run --name mongodb -d -p 27017:27017 mongo
# Check running containers:
sudo docker ps

mkdir -p ~/.docker/cli-plugins/
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-$(uname -s)-$(uname -m)" -o ~/.docker/cli-plugins/docker-compose
sudo chmod +x ~/.docker/cli-plugins/docker-compose
docker compose version
 # to stop the compose service
#docker compose down
#docker compose -f compose1.yml down
# Stop any running containers with specific compose file
#docker compose -f compose1.yml down

# Start fresh with the specified file
#docker compose -f compose1.yml up -d

# Check status
# docker ps

# INITIALIZE THE SHARD CLUSTER
# Initialize config server replica set (if not already done):
#docker compose -f compose1.yml exec cfgsvr1 mongosh --eval 'rs.initiate({_id:"cfgrs", configsvr:true, members:[{_id:0, host:"cfgsvr1:27017"}]})'
#Initialize shard replica set:
#docker compose -f compose1.yml exec shard1svr1 mongosh --eval 'rs.initiate({_id:"shard1rs", members:[{_id:0, host:"shard1svr1:27017"}]})'
# add the shard
#docker compose -f compose1.yml exec mongos mongosh --eval 'sh.addShard("shard1rs/shard1svr1:27017")'

# Check shard status
# docker compose -f compose1.yml exec shard1svr1 mongosh --eval 'rs.status()'
# check config status
# docker compose -f compose1.yml exec cfgsvr1 mongosh --eval 'rs.status()'

# Then verify the sharding status:
#docker compose -f compose1.yml exec mongos mongosh --eval 'sh.status()'

