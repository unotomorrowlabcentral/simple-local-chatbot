export default defineAppConfig({
  title: "Hello Nuxt",
  layout: "default",
  pageTransition: {
    name: "fade",
    mode: "out-in",
  },
  theme: {
    dark: true,
    colors: {
      primary: "#ff0000",
    },
  },
});
