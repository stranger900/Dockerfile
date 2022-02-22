docker network ls

docker network inspect bridge

Run container based on Nginx image and connect it to Bridge network. Check if you can reach port 80 from the host. Forward port 80 from container to host.
docker run -it -d -p 8080:80 --network bridge nginx:1.21-alpine

Run container based on Nginx image and connect it to Host network. Check if you can reach port 80 from the host.
docker run -it -d  --network host nginx:1.21-alpine

Run container based on Nginx image and set its name as client.
docker run -it -d  --name client nginx:1.21-alpine

Run container based on Nginx image and set its name as web-server.
docker run -it -d  --name web-server nginx:1.21-alpine

docker network inspect bridge

Connect to client and try to reach http://web-server from it with curl.
docker exec -it client sh
curl 172.17.0.2

Create custom Bridge network, add client and web-server to it.
docker network create my-network
docker network ls
docker run -it -d  --name client --network my-network nginx:1.21-alpine
docker run -it -d  --name web-server --network my-network nginx:1.21-alpine

Try to reach http://web-server from client container again.
docker network inspect my-network
docker exec -it client sh
curl 172.18.0.3
