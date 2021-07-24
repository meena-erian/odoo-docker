docker container rm -f nginx
docker image rm nginx-app
docker build --tag nginx-app .
docker run -d --mount type=bind,source=C:\Certbot,destination=/etc/nginx/certs -p 82:82 -p 5443:443 --name nginx nginx-app