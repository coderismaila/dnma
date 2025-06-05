import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  modules: ["@nuxthub/core", "@nuxt/eslint", "@nuxt/icon", "shadcn-nuxt"],

  devtools: { enabled: true },

  future: { compatibilityVersion: 4 },
  compatibilityDate: "2025-03-01",

  hub: {},

  css: ["./app/assets/css/main.css"],

  shadcn: {
    prefix: "",
    componentDir: "./app/components/ui",
  },

  vite: {
    plugins: [
      tailwindcss(),
    ],
  },

  eslint: {
    config: {
      standalone: false,
    },
  },
});
