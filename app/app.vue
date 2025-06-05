<script setup lang="ts">
const colorMode = useColorMode();

const color = computed(() => colorMode.value === "dark" ? "dark" : "light");

useHead({
  meta: [
    { charset: "utf-8" },
    { name: "viewport", content: "width=device-width, initial-scale=1" },
    { key: "theme-color", name: "theme-color", content: color },
  ],
  link: [
    { rel: "icon", href: "/favicon.ico" },
  ],
  htmlAttrs: {
    lang: "en",
  },
  bodyAttrs: {
  },
});

const title = "DNMA - DIstribution Network Management Application";
const description = "DNMA is a web application for managing distribution networks, providing tools for monitoring, analysis, and optimization.";

useSeoMeta({
  title,
  description,
  ogTitle: title,
  ogDescription: description,
  twitterTitle: title,
  twitterDescription: description,
  twitterCard: "summary_large_image",
});

const router = useRouter();

defineShortcuts({
  "G-H": () => router.push("/"),
  "G-D": () => router.push("/dashboard"),
});
</script>

<template>
  <NuxtRouteAnnouncer />
  <NuxtLoadingIndicator />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
