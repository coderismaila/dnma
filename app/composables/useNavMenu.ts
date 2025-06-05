import type { NavMenu, NavMenuItems, Role } from "~~/types/nav";

import { navMenu, navMenuBottom } from "~~/constants/nav.constants";

export default function () {
  const userRole = computed<Role | null>(() => "admin");

  // Helper function to filter menu items by role
  const filterByRole = (items: NavMenuItems, role: Role | null): NavMenuItems => {
    return items.filter((item) => {
      // Include item if no roles specified or user has required role
      const hasAccess = !item.roles || (role && item.roles.includes(role));

      // Process group children if it's a NavGroup
      if ("children" in item) {
        const filteredChildren = item.children.filter(child =>
          !child.roles || (role && child.roles.includes(role)),
        );
        return hasAccess && filteredChildren.length > 0;
      }

      return hasAccess;
    }).map((item) => {
      // Clone and filter children for groups
      if ("children" in item) {
        return {
          ...item,
          children: item.children.filter(child =>
            !child.roles || (role && child.roles.includes(role)),
          ),
        };
      }
      return item;
    });
  };

  // Filter main navigation
  const filteredNavMenu = computed<NavMenu[]>(() => {
    return navMenu
      .filter(section =>
        !section.roles
        || (userRole.value && section.roles.includes(userRole.value)),
      )
      .map(section => ({
        ...section,
        items: filterByRole(section.items, userRole.value),
      }))
      .filter(section => section.items.length > 0);
  });

  // Filter bottom navigation
  const filteredNavMenuBottom = computed(() =>
    filterByRole(navMenuBottom, userRole.value),
  );

  return {
    navMenu: filteredNavMenu,
    navMenuBottom: filteredNavMenuBottom,
  };
}
