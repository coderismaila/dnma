export interface NavLink {
  title: string;
  link: string;
  icon?: string;
  new?: boolean;
  roles?: Role[]; // Add roles property
};

export interface NavSectionTitle {
  heading: string;
  roles?: Role[]; // Add roles property
}

// Fix children type to only accept NavLink[]
export interface NavGroup {
  title: string;
  icon?: string;
  new?: boolean;
  children: NavLink[]; // Only NavLink allowed here
  roles?: Role[]; // Add roles property
}

export interface NavMenu {
  heading: string;
  items: NavMenuItems;
  roles?: Role[]; // Add roles property
}

export declare type NavMenuItems = (NavLink | NavGroup | NavSectionTitle)[];
export type Role = "user" | "manager" | "admin";
