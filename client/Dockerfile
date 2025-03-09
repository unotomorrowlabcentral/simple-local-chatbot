FROM node:20

WORKDIR /client

COPY package.json ./
COPY pnpm-lock.yaml ./

RUN npm install -g pnpm
RUN pnpm install

COPY . .

# Default to development mode
CMD ["pnpm", "run", "dev"]
