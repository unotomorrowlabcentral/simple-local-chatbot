// app.config.ts
import { defineAppConfig } from "nuxt/app";

export default defineNuxtPlugin(() => {
  return {
    provide: {
      layout: "default",
      pageTransition: {
        name: "fade",
        mode: "out-in",
      },
    },
  };
});
