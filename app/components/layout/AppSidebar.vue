<script setup lang="ts">
import type { NavGroup, NavLink, NavSectionTitle } from "~~/types/nav";

function resolveNavItemComponent(item: NavLink | NavGroup | NavSectionTitle): any {
  if ("children" in item)
    return resolveComponent("LayoutSidebarNavGroup");

  return resolveComponent("LayoutSidebarNavLink");
}

const { sidebar } = useAppSettings();

const { navMenu, navMenuBottom } = useNavMenu();
</script>

<template>
  <Sidebar
    :collapsible="sidebar.collapsible"
    :side="sidebar.side"
    :variant="sidebar.variant"
  >
    <SidebarHeader>
      <LayoutSidebarNavHeader />
    </SidebarHeader>
    <SidebarContent>
      <SidebarGroup v-for="(nav, indexGroup) in navMenu" :key="indexGroup">
        <SidebarGroupLabel v-if="nav.heading">
          {{ nav.heading }}
        </SidebarGroupLabel>
        <component
          :is="resolveNavItemComponent(item)"
          v-for="(item, index) in nav.items"
          :key="index"
          :item="item"
        />
      </SidebarGroup>
      <SidebarGroup class="mt-auto">
        <component
          :is="resolveNavItemComponent(item)"
          v-for="(item, index) in navMenuBottom"
          :key="index"
          :item="item"
          size="sm"
        />
      </SidebarGroup>
    </SidebarContent>
    <SidebarFooter>
      <LayoutSidebarNavFooter />
    </SidebarFooter>
    <SidebarRail />
  </Sidebar>
</template>

<style scoped>

</style>
