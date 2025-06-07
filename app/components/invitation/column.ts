import type { ColumnDef } from "@tanstack/vue-table";
import type { Invitation } from "~~/server/database/schema";

import { InvitationRowAction } from "#components";
import { h } from "vue";

export const columns: ColumnDef<Invitation>[] = [
  {
    accessorKey: "email",
    header: "Email",
    cell: ({ row }) => h("span", row.getValue("email")),
  },
  {
    accessorKey: "role",
    header: "Role",
    cell: ({ row }) => h("span", row.getValue("role")),
  },
  {
    accessorKey: "createdAt",
    header: "Created At",
    cell: ({ row }) => h("span", new Date(row.getValue("createdAt")).toLocaleString()),
  },
  {
    accessorKey: "expiresAt",
    header: "Expires At",
    cell: ({ row }) => h("span", new Date(row.getValue("expiresAt")).toLocaleString()),
  },
  {
    accessorKey: "acceptedAt",
    header: "Accepted At",
    cell: ({ row }) => row.getValue("acceptedAt")
      ? h("span", new Date(row.getValue("acceptedAt")).toLocaleString())
      : h("span", "Not Accepted"),
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const invitation = row.original;

      return h("div", { class: "relative" }, h(InvitationRowAction, {
        invitation,
      }));
    },
  },
];
