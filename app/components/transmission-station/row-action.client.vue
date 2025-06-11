<script setup lang="ts">
import type { TransmissionStationWithRegion } from "~~/server/database/schema";

import { MoreHorizontal } from "lucide-vue-next";
import { toast } from "vue-sonner";

defineProps<{
  transmissionStation: TransmissionStationWithRegion;
}>();

async function deleteTransmissionStation(slug: string) {
  try {
    await $fetch(`/api/transmission-station/${slug}`, { method: "delete" });
    toast("Station deleted successfully!");
  }
  catch (e: any) {
    toast("Error deleting station!", { description: `${e.statusMessage || e.message || "Unhandled error"}` });
  }
}
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="ghost" class="w-8 h-8 p-0">
        <span class="sr-only">Open menu</span>
        <MoreHorizontal class="w-4 h-4" />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuItem as-child>
        <NuxtLink :to="`/transmission-station/${transmissionStation.slug}`">
          View Station
        </NuxtLink>
      </DropdownMenuItem>
      <DropdownMenuItem as-child>
        <NuxtLink :to="`/transmission-station/${transmissionStation.slug}/edit`">
          Edit Station
        </NuxtLink>
      </DropdownMenuItem>
      <DropdownMenuSeparator />
      <DropdownMenuItem class="text-red-600" @click="deleteTransmissionStation(transmissionStation.slug)">
        Delete Station
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
