<script lang="ts" setup>
import { AlertCircle, Loader } from "lucide-vue-next";

definePageMeta({
  layout: "blank",
});
const route = useRoute();

const errors = ref();
const loading = ref(false);
const user = ref<{
  email: string;
  role: "admin" | "manager" | "user";
}>();

const token = route.query.token as string;

onMounted(async () => {
  loading.value = true;
  try {
    const result = await $fetch(`/api/invite/verify?token=${token}`, { method: "get" });
    if (result.data) {
      user.value = result.data;
    }
  }
  catch (error: any) {
    errors.value = error.statusMessage || "An error occurred while verifying the token.";
  }
  finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="flex min-h-svh flex-col items-center justify-center gap-6 bg-muted p-6 md:p-10">
    <Card class="flex w-full max-w-sm flex-col gap-6">
      <CardHeader>
        <CardTitle class="text-xl">
          Create your account
        </CardTitle>
        <CardDescription>
          You have been invited to create an account. Please fill in the details below to get started.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div v-if="loading" class="flex items-center justify-center gap-2">
          Validating token <Loader class="animate-spin size-4" />
        </div>
        <Alert v-else-if="errors" variant="destructive">
          <AlertCircle class="w-4 h-4" />
          <AlertTitle>Error</AlertTitle>
          <AlertDescription>
            {{ errors }}
          </AlertDescription>
        </Alert>

        <UserRegisterForm
          v-else-if="user"
          :email="user.email"
          :role="user.role"
          :token="token"
        />
      </CardContent>
    </Card>
  </div>
</template>
