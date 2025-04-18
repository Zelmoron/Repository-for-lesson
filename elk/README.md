## Filebeat

Команда для запуска Filebeat: 

sudo docker run -d \
  --name=filebeat \
  --user=root \
  --volume="$(pwd)/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro" \
  --volume="/tmp/app.log:/var/log/myapp/app.log:ro" \
  --volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
  docker.elastic.co/beats/filebeat:9.0.0 filebeat -e --strict.perms=false
