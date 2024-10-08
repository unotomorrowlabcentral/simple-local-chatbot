FROM node:20

# set the working directory in the container
WORKDIR /app

# copy package.json
COPY package.json ./
COPY pnpm-lock.yaml ./

# install pnpm
RUN npm install -g pnpm

# install dependencies
RUN pnpm install

# copy source code to current working directory
COPY . .

# build application
RUN pnpm run build

# expose port within container
EXPOSE 3000

# entrypoint
CMD [ "pnpm", "run", "start" ]