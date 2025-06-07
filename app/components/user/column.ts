import type { ColumnDef } from "@tanstack/vue-table";
import type { UserWithAreaOffice } from "~~/server/database/schema";

import { UserRowAction } from "#components";
import { h } from "vue";

export const columns: ColumnDef<UserWithAreaOffice>[] = [
  {
    accessorKey: "name",
    header: "Name",
    cell: ({ row }) => h("span", row.getValue("name")),
  },
  {
    accessorKey: "payrollId",
    header: "Payroll ID",
    cell: ({ row }) => h("span", row.getValue("payrollId")),
  },
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
    accessorKey: "areaOffice",
    header: "Area Office",
    cell: ({ row }) => h("span", row.getValue("areaOffice")),
  },
  {
    accessorKey: "createdAt",
    header: "Created At",
    cell: ({ row }) => h("span", new Date(row.getValue("createdAt")).toLocaleString()),
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const user = row.original;

      return h("div", { class: "relative" }, h(UserRowAction, {
        user,
      }));
    },
  },
];
