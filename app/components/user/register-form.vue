<script lang="ts" setup>
import { InsertUser } from "~~/server/database/schema";
import { Check, ChevronsUpDown, Loader2 } from "lucide-vue-next";

import { cn } from "~/lib/utils";

const props = defineProps<{
  email?: string;
  role?: "admin" | "manager" | "user";
  areaOfficeId?: number;
  payrollId?: number;
  name?: string;
  password?: string;
  token: string;
}>();

const error = ref("");

const { data } = await useFetch("/api/area-office", {
  transform: (areaOffices) => {
    return areaOffices.map(office => ({
      value: office.id,
      label: office.name,
    }));
  },
});

const formSchema = toTypedSchema(InsertUser);

const { handleSubmit, isSubmitting, setFieldValue } = useForm({
  validationSchema: formSchema,
  initialValues: {
    name: props.name,
    payrollId: props.payrollId,
    email: props.email,
    role: props.role,
    areaOfficeId: 2,
    password: props.password,
  },
});

const onSubmit = handleSubmit(async (values) => {
  try {
    await $fetch("/api/invite/accept", {
      method: "POST",
      body: { ...values, token: props.token },
    });
  }
  catch (e: any) {
    // Handle error, e.g., show an error message
    error.value = e.statusMessage;
    console.error("Registration failed:", error);
  }
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
      <div class="grid gap-4">
        <FormField v-slot="{ componentField }" name="name">
          <FormItem>
            <FormLabel>Name</FormLabel>
            <FormControl>
              <Input type="text" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="payrollId">
          <FormItem>
            <FormLabel>Payroll ID</FormLabel>
            <FormControl>
              <Input type="number" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="email">
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input
                type="text"
                v-bind="componentField"
                disabled
                readonly
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField
          v-slot="{ componentField }"
          type="radio"
          name="role"
        >
          <FormItem>
            <FormLabel>Role</FormLabel>
            <FormControl>
              <RadioGroup
                disabled
                class="flex space-y-1"
                v-bind="componentField"
              >
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="user" />
                    <FormLabel>User</FormLabel>
                  </FormControl>
                </FormItem>
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="manager" />
                    <FormLabel>Manager</FormLabel>
                  </FormControl>
                </FormItem>
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="admin" />
                    <FormLabel>Admin</FormLabel>
                  </FormControl>
                </FormItem>
              </RadioGroup>
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField name="areaOfficeId">
          <FormItem>
            <FormLabel>Area Office</FormLabel>

            <Combobox by="label">
              <FormControl>
                <ComboboxAnchor class="w-full">
                  <div class="relative w-full items-center">
                    <ComboboxInput
                      :display-value="(val) => val?.label ?? ''"
                      placeholder="Select area office..."
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
                    v-for="areaOffice in data"
                    :key="areaOffice.value"
                    :value="areaOffice"
                    @select="() => {
                      setFieldValue('areaOfficeId', areaOffice.value)
                    }"
                  >
                    {{ areaOffice.label }}
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

        <FormField v-slot="{ componentField }" name="password">
          <FormItem>
            <FormLabel>Password</FormLabel>
            <FormControl>
              <Input type="text" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <Button type="submit" class="w-full">
          Create account
          <Loader2 v-if="isSubmitting" class="w-4 h-4 ml-2 animate-spin" />
        </Button>
      </div>
    </form>
    <div class="mt-4 text-center text-sm">
      Already have an account?
      <a href="/auth/signin" class="underline">
        Sign in
      </a>
    </div>
  </div>
</template>
