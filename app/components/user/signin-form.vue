<script lang="ts" setup>
import type { FetchError } from "ofetch";

import { UserSignIn } from "~~/server/database/schema";
import { AlertCircle, Loader2 } from "lucide-vue-next";

const formSchema = toTypedSchema(UserSignIn);
const submitError = ref<string | null>(null);

const { fetch: refreshSession } = useUserSession();

const { handleSubmit, isSubmitting } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  submitError.value = null;
  try {
    await $fetch("/api/auth/signin", {
      method: "POST",
      body: values,
    });
    await refreshSession();
    await navigateTo("/dashboard");
  }
  catch (e) {
    const error = e as FetchError;
    submitError.value = error.statusMessage || "An error occurred during sign-in.";
    console.error("User signin failed:", error);
  }
});
</script>

<template>
  <div>
    <Alert
      v-if="submitError"
      class="mb-4"
      variant="destructive"
    >
      <AlertCircle class="w-4 h-4" />
      <AlertTitle>Error</AlertTitle>
      <AlertDescription>
        {{ submitError }}
      </AlertDescription>
    </Alert>
    <form id="register-form" @submit="onSubmit">
      <div class="grid gap-4">
        <FormField v-slot="{ componentField }" name="email">
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input
                type="email"
                v-bind="componentField"
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField v-slot="{ componentField }" name="password">
          <FormItem>
            <FormLabel>Password</FormLabel>
            <FormControl>
              <Input type="password" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <Button type="submit" class="w-full">
          Sign In
          <Loader2 v-if="isSubmitting" class="w-4 h-4 ml-2 animate-spin" />
        </Button>
      </div>
    </form>
    <div class="mt-4 text-center text-sm">
      Don't have an account?
      <a href="#" class="underline">
        Please contact your line manager.
      </a>
    </div>
  </div>
</template>
