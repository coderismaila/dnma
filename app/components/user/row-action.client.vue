<script setup lang="ts">
import type { UserWithAreaOffice } from "~~/server/database/schema";

import { MoreHorizontal } from "lucide-vue-next";

defineProps<{
  user: UserWithAreaOffice;
}>();

function copy(id: string) {
  navigator.clipboard.writeText(id);
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
      <DropdownMenuItem @click="copy(user.email.toString())">
        Edit User
      </DropdownMenuItem>
      <DropdownMenuItem>Make Admin</DropdownMenuItem>
      <DropdownMenuSeparator />
      <DropdownMenuItem class="text-red-600">
        Deactivate User
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
