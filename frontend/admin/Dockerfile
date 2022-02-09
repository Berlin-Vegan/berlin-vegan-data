# build environment
FROM node:16.13.0-alpine as prepare

ARG ENVIRONMENT=production

ENV ENVIRONMENT=${ENVIRONMENT}

WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install $(test "$ENVIRONMENT" = production && echo "--production")
COPY . ./

# build
FROM prepare as builder
ENV SKIP_PREFLIGHT_CHECK=true
ENV DISABLE_ESLINT_PLUGIN=true
RUN yarn run build

# production environment
FROM nginx:stable-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]
