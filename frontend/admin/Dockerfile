# build environment
FROM node:18.10.0-alpine as prepare

ARG ENVIRONMENT=production
ARG REACT_APP_MAP_API_URL
ARG REACT_APP_SENTRY_DSN

ENV ENVIRONMENT=${ENVIRONMENT} \
	REACT_APP_MAP_API_URL=${REACT_APP_MAP_API_URL} \
	REACT_APP_SENTRY_DSN=${REACT_APP_SENTRY_DSN}

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
