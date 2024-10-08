import dotenv from "dotenv";
import { existsSync } from "fs";
import { defineNuxtConfig } from "nuxt/config";
import { join } from "path";

const envFile =
  process.env.NODE_ENV === "production" ? ".env.prod" : ".env.dev";

const envPath = join(process.cwd(), envFile);

if (existsSync(envPath)) {
  dotenv.config({ path: envPath });
} else {
  console.warn(`${envFile} not found`);
}

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL,
    },
  },
  css: ["@/assets/styles/main.css"],
  plugins: [{ src: "~/plugins/axios.ts", mode: "client" }],
});
