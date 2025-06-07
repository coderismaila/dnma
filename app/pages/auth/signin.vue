<script lang="ts" setup>
definePageMeta({
  layout: "blank",
});
</script>

<template>
  <div class="flex min-h-svh flex-col items-center justify-center gap-6 bg-muted p-6 md:p-10">
    <Card class="flex w-full max-w-sm flex-col gap-6">
      <CardHeader>
        <CardTitle class="text-xl">
          Welcome back
        </CardTitle>
        <CardDescription>
          Enter your details to sign in to your account.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <UserSigninForm />
      </CardContent>
    </Card>
  </div>
</template>
