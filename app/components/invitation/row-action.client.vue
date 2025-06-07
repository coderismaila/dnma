<script setup lang="ts">
import type { Invitation } from "~~/server/database/schema";

import { MoreHorizontal } from "lucide-vue-next";
import { toast } from "vue-sonner";

defineProps<{
  invitation: Invitation;
}>();

function copy(id: string) {
  navigator.clipboard.writeText(id);
}

async function resendInvite(invitation: Invitation) {
  await $fetch("/api/invite/send", {
    method: "POST",
    body: invitation,
  });

  toast("Invite resent successfully", {
    description: `Invitation for ${invitation.email} has been resent.`,
  });
}

async function cancelInvite(id: number) {
  await $fetch(`/api/invite/${id}`, {
    method: "delete",
  });
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
      <DropdownMenuItem @click="copy(invitation.email.toString())">
        Copy email
      </DropdownMenuItem>
      <DropdownMenuItem @click="resendInvite(invitation)">
        Resend Invite
      </DropdownMenuItem>
      <DropdownMenuSeparator />
      <DropdownMenuItem class="text-red-600" @click="cancelInvite(invitation.id)">
        Cancel Invite
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
