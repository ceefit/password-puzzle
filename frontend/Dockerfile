FROM node:11.15.0
RUN mkdir -p /frontend
WORKDIR /frontend
ADD . /frontend
ADD .env.production /frontend/.env
RUN npm install -g -s --no-progress yarn && \
    yarn && \
    yarn run build && \
    yarn cache clean
CMD [ "yarn", "start" ]
EXPOSE 3000