<script lang="ts" setup>
import { columns as userColumns } from "~/components/user/column";

const { data: users, status: userStatus } = await useFetch("/api/user");
</script>

<template>
  <div class=" max-w-full">
    <div class="flex flex-col md:flex-row md:justify-between md:items-center mb-4">
      <div>
        <h1 class="text-xl font-semibold">
          User Management
        </h1>
        <p class="text-sm text-muted-foreground my-1">
          Manage users in your application. You can view, edit, or suspend users.
        </p>
      </div>

      <div class="flex items-center space-x-2">
        <Button as-child>
          <NuxtLink to="#">
            Create User
          </NuxtLink>
        </Button>
        <Button variant="secondary" as-child>
          <NuxtLink to="/users/invitations">
            Invite User
          </NuxtLink>
        </Button>
      </div>
    </div>

    <div v-if="userStatus === 'pending'">
      <Skeleton class="w-full h-4" />
      <Skeleton class="w-full h-4" />
    </div>

    <ClientOnly>
      <DataTable
        v-if="users"
        :columns="userColumns"
        :data="users"
      />
    </ClientOnly>
  </div>
</template>
