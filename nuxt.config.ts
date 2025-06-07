import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  modules: [
    "@nuxthub/core",
    "@nuxt/eslint",
    "@nuxt/icon",
    "shadcn-nuxt",
    "@vueuse/nuxt",
    "@nuxtjs/color-mode",
    "@nuxt/image",
    "nuxt-auth-utils",
    "@vee-validate/nuxt",
    "nuxt-resend",
  ],

  devtools: { enabled: true },

  future: { compatibilityVersion: 4 },
  compatibilityDate: "2025-03-01",

  hub: {
    database: true,
  },

  css: ["./app/assets/css/main.css"],

  colorMode: {
    classSuffix: "",
  },

  shadcn: {
    prefix: "",
    componentDir: "./app/components/ui",
  },

  routeRules: {
    "/settings": { redirect: "/settings/profile" },
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
