<script lang="ts" setup>
import { transmissionStationColumns } from "~/components/transmission-station/column";

const { data: transmissionStations, status } = await useFetch("/api/transmission-station");
</script>

<template>
  <div class=" max-w-full">
    <div class="flex flex-col md:flex-row md:justify-between md:items-center mb-4">
      <div>
        <h1 class="text-xl font-semibold">
          TransmissionStation
        </h1>
        <p class="text-sm text-muted-foreground my-1">
          Manage transmission stations in your application. You can view, edit, or delete transmission stations.
        </p>
      </div>

      <div class="flex items-center space-x-2">
        <Button as-child>
          <NuxtLink to="/transmission-station/new">
            Create Transmission Station
          </NuxtLink>
        </Button>
      </div>
    </div>

    <div v-if="status === 'pending'">
      <Skeleton class="w-full h-4" />
      <Skeleton class="w-full h-4" />
    </div>

    <ClientOnly>
      <DataTable
        v-if="transmissionStations"
        :columns="transmissionStationColumns"
        :data="transmissionStations"
      />
    </ClientOnly>
  </div>
</template>
