<script setup lang="ts">
const colorMode = useColorMode();

const logo = computed(() => {
  return colorMode.preference === "dark" ? "/ke-logo-white.svg" : "ke-logo.svg";
});
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <SidebarMenuButton
        size="lg"
        class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
      >
        <NuxtImg
          :src="logo"
          class="aspect-square size-8 flex items-center justify-center rounded-lg"
        />
        <div class="grid flex-1 text-left text-lg">
          <span class="truncate font-semibold">
            KEAR
          </span>
        </div>
      </SidebarMenuButton>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
