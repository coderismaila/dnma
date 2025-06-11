<script lang="ts" setup>
definePageMeta({
  validate: async (route) => {
    return typeof route.params.slug === "string";
  },
});

const route = useRoute();

const { data } = await useFetch(`/api/transmission-station/${route.params.slug}`);
</script>

<template>
  <div>
    <TransmissionStationForm :initial-data="data" />
  </div>
</template>
