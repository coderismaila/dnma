export default defineNuxtConfig({
  modules: ["@nuxthub/core", "@nuxt/eslint", "@nuxt/icon"],

  devtools: { enabled: true },

  future: { compatibilityVersion: 4 },
  compatibilityDate: "2025-03-01",

  hub: {},

  eslint: {
    config: {
      standalone: false,
    },
  },
});
