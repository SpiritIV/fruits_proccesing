FROM node:current-slim
LABEL maintainer="artemzraev@gmail.com"
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8180
EXPOSE 8181

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
