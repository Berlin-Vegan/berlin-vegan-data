# build environment
FROM node:15.13.0-alpine as prepare
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn --production
COPY . ./

# build
FROM prepare as builder
RUN yarn run build

# production environment
FROM nginx:stable-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]
