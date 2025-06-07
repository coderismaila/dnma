<script lang="ts" setup>
import { columns as invitationColummns } from "~/components/invitation/column";

const { data: invitations, status } = await useFetch("/api/invite");
</script>

<template>
  <div>
    <div>
      <div class="flex justify-between items-center mb-4">
        <div>
          <h1 class="text-xl font-semibold">
            Invitation Management
          </h1>
          <p class="text-sm text-muted-foreground my-1">
            Manage user invitations. You can view, resend, or delete invitations.
          </p>
        </div>

        <Button as-child>
          <InvitationForm />
        </Button>
      </div>

      <Skeleton v-if="status === 'pending'" />
      <ClientOnly>
        <InvitationDataTable
          v-if="invitations"
          :columns="invitationColummns"
          :data="invitations"
        />
      </ClientOnly>
    </div>
  </div>
</template>
