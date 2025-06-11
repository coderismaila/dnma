<script lang="ts" setup>
import { cn } from "~/lib/utils";

const emit = defineEmits(["selectedValue"]);

const { data: regions } = await useFetch("/api/region", {
  transform: (regions) => {
    return regions.map(region => ({
      value: region.id,
      label: region.name,
    }));
  },
});
</script>

<template>
  <FormField name="regionId">
    <FormItem>
      <FormLabel>Region</FormLabel>

      <Combobox by="label">
        <FormControl>
          <ComboboxAnchor class="w-full">
            <div class="relative w-full items-center">
              <ComboboxInput
                :display-value="(val) => val?.label ?? ''"
                placeholder="Select region..."
              />
              <ComboboxTrigger class="absolute end-0 inset-y-0 flex items-center justify-center px-3">
                <ChevronsUpDown class="size-4 text-muted-foreground" />
              </ComboboxTrigger>
            </div>
          </ComboboxAnchor>
        </FormControl>

        <ComboboxList>
          <ComboboxEmpty>
            Nothing found.
          </ComboboxEmpty>

          <ComboboxGroup>
            <ComboboxItem
              v-for="region in regions"
              :key="region.value"
              :value="region"
              @select="() => emit('selectedValue', region.value)"
            >
              {{ region.label }}
              <ComboboxItemIndicator>
                <Check :class="cn('ml-auto h-4 w-4')" />
              </ComboboxItemIndicator>
            </ComboboxItem>
          </ComboboxGroup>
        </ComboboxList>
      </Combobox>
      <FormMessage />
    </FormItem>
  </FormField>
</template>

<style>

</style>
