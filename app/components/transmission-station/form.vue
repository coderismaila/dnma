<script lang="ts" setup>
import type { TransmissionStation } from "~~/server/database/schema";

import { insertTransmissionStationSchema } from "~~/server/database/schema/transmissionStation";
import { AlertCircle, Check, ChevronsUpDown, Loader2 } from "lucide-vue-next";
import { toast } from "vue-sonner";

import { cn } from "~/lib/utils";

const props = defineProps<{ initialData?: TransmissionStation }>();
const error = ref("");
const formSchema = toTypedSchema(insertTransmissionStationSchema);

const { handleSubmit, isSubmitting, setFieldValue } = useForm({
  validationSchema: formSchema,
  initialValues: props.initialData,
});

const onSubmit = handleSubmit(async (values) => {
  try {
    if (props.initialData) {
      await $fetch(`/api/transmission-station/${props.initialData.slug}`, {
        method: "PUT",
        body: values,
      });
    }
    else {
      await $fetch("/api/transmission-station", {
        method: "POST",
        body: values,
      });
    }
    toast(`Transmission station ${props.initialData ? "updated" : "created"}`);
    navigateTo("/transmission-station");
  }
  catch (e: any) {
    error.value = e.statusMessage;
    console.error("Failed to save transmission station", e);
  }
});

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
  <div>
    <Alert v-if="error" variant="destructive">
      <AlertCircle class="w-4 h-4" />
      <AlertTitle>Error</AlertTitle>
      <AlertDescription>
        {{ error }}
      </AlertDescription>
    </Alert>
    <form id="register-form" @submit="onSubmit">
      <div class="grid gap-8">
        <FormField v-slot="{ componentField }" name="name">
          <FormItem>
            <FormLabel>Name</FormLabel>
            <FormControl>
              <Input type="text" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="shortName">
          <FormItem>
            <FormLabel>Short Name</FormLabel>
            <FormControl>
              <Input type="text" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField name="regionId">
          <FormItem>
            <FormLabel>Region</FormLabel>

            <Combobox by="label">
              <FormControl>
                <ComboboxAnchor>
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
                    @select="() => {
                      setFieldValue('regionId', region.value)
                    }"
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

        <div class="grid grid-cols-2 gap-4">
          <FormField v-slot="{ value }" name="installedCapacityMVA">
            <FormItem>
              <FormLabel>Installed Capacity (MVA)</FormLabel>
              <FormControl>
                <NumberField
                  id="installedCapacityMVA"
                  :step-snapping="false"
                  :format-options="{
                    minimumFractionDigits: 2,
                    maximumSignificantDigits: 5,
                    minimumIntegerDigits: 1,
                    style: 'decimal',
                  }"
                  :model-value="value"
                  @update:model-value="(v) => {
                    if (v) {
                      setFieldValue('installedCapacityMVA', v)
                    }
                    else {
                      setFieldValue('installedCapacityMVA', undefined)
                    }
                  }"
                >
                  <NumberFieldContent>
                    <NumberFieldDecrement />
                    <FormControl>
                      <NumberFieldInput />
                    </FormControl>
                    <NumberFieldIncrement />
                  </NumberFieldContent>
                </NumberField>
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <FormField v-slot="{ value }" name="latitude">
            <FormItem>
              <FormLabel>Latitude</FormLabel>
              <NumberField
                id="latitude"
                :step-snapping="false"
                :format-options="{
                  minimumFractionDigits: 6,
                  maximumSignificantDigits: 8,
                  minimumIntegerDigits: 1,
                  style: 'decimal',
                }"
                :model-value="value"
                @update:model-value="(v) => {
                  if (v) {
                    setFieldValue('latitude', v)
                  }
                  else {
                    setFieldValue('latitude', undefined)
                  }
                }"
              >
                <NumberFieldInput />
              </NumberField>
              <FormMessage />
            </FormItem>
          </FormField>

          <FormField v-slot="{ value }" name="longitude">
            <FormItem>
              <FormLabel>Longitude</FormLabel>
              <NumberField
                id="longitude"
                :step-snapping="false"
                :format-options="{
                  minimumFractionDigits: 6,
                  maximumSignificantDigits: 8,
                  minimumIntegerDigits: 1,
                  style: 'decimal',
                }"
                :model-value="value"
                @update:model-value="(v) => {
                  if (v) {
                    setFieldValue('longitude', v)
                  }
                  else {
                    setFieldValue('longitude', undefined)
                  }
                }"
              >
                <NumberFieldInput />
              </NumberField>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>

        <div class="flex gap-2 my-4">
          <Button type="submit">
            {{ props.initialData ? 'Update' : 'Create' }}
            <Loader2 v-if="isSubmitting" class="w-4 h-4 ml-2 animate-spin" />
          </Button>
          <Button variant="destructive" as-child>
            <NuxtLink href="/transmission-station">
              Cancel
            </NuxtLink>
          </Button>
        </div>
      </div>
    </form>
  </div>
</template>
