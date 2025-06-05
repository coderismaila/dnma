import type { NavMenu, NavMenuItems } from "~~/types/nav";

export const navMenu: NavMenu[] = [
  {
    heading: "General",
    items: [
      {
        title: "Home",
        icon: "i-lucide-home",
        link: "/",
      },
      {
        title: "Dashboard",
        icon: "i-lucide-layout-dashboard",
        link: "#",
      },
    ],
  },
  {
    heading: "Assets",
    items: [
      {
        title: "Substations",
        icon: "i-lucide-house-plug",
        children: [
          {
            title: "Transmission Stations",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "Injection Substation",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "Distribution Substation",
            icon: "i-lucide-circle",
            link: "#",
          },
        ],
      },
      {
        title: "Feeders",
        icon: "i-lucide-utility-pole",
        children: [
          {
            title: "33kV Feeders",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "11kV Feeders",
            icon: "i-lucide-circle",
            link: "#",
          },
        ],
      },
    ],
  },

  {
    heading: "Operations & Maintenance",
    items: [
      {
        title: "Maintenance",
        icon: "i-lucide-wrench",
        children: [
          {
            title: "Maintenance Schedule",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "Maintenance Report",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "NEMSA Defect Observations",
            icon: "i-lucide-circle",
            link: "#",
          },
        ],
      },
      {
        title: "Fault & Vandalization",
        icon: "i-lucide-zap-off",
        children: [
          {
            title: "Faults",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "Vandalization",
            icon: "i-lucide-circle",
            link: "#",
          },
        ],
      },
    ],

  },

  {
    heading: "Organization",
    items: [
      {
        title: "Region & Franchise",
        icon: "i-lucide-map-pin",
        children: [
          {
            title: "Regions",
            icon: "i-lucide-circle",
            link: "#",
          },
          {
            title: "Area Office",
            icon: "i-lucide-circle",
            link: "#",
          },
        ],
      },
    ],
  },
  {
    heading: "User Management",
    roles: ["admin"],
    items: [
      {
        title: "Users",
        icon: "i-lucide-users",
        roles: ["admin"],
        children: [
          {
            title: "User List",
            icon: "i-lucide-circle",
            link: "/users",
            roles: ["admin"],
          },
          {
            title: "Invitations",
            icon: "i-lucide-circle",
            link: "/users/invitations",
            roles: ["admin"],
          },
        ],
      },
    ],
  },
];

export const navMenuBottom: NavMenuItems = [
  {
    title: "Help & Support",
    icon: "i-lucide-circle-help",
    link: "#",
  },
  {
    title: "Feedback",
    icon: "i-lucide-send",
    link: "#",
  },
];
