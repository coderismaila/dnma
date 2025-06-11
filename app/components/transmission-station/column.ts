import type { ColumnDef } from "@tanstack/vue-table";

import { TransmissionStationRowAction } from "#components";
import { h } from "vue";

export const transmissionStationColumns: ColumnDef<TransmissionStationWithRegion>[] = [
  {
    accessorKey: "name",
    header: "Name",
    cell: ({ row }) => h("span", row.getValue("name")),
  },
  {
    accessorKey: "shortName",
    header: "Short Name",
    cell: ({ row }) => h("span", row.getValue("shortName")),
  },
  {
    accessorKey: "regionName",
    header: "Region",
    cell: ({ row }) => h("div", { class: "capitalize" }, row.getValue("regionName")),
  },
  {
    accessorKey: "installedCapacityMVA",
    header: "Installed Capacity (MVA)",
    cell: ({ row }) => h("div", { class: "text-center" }, row.getValue("installedCapacityMVA")),
  },
  {
    accessorKey: "latitude",
    header: "Latitude",
    cell: ({ row }) => h("span", row.getValue("latitude")),
  },
  {
    accessorKey: "longitude",
    header: "Longitude",
    cell: ({ row }) => h("span", row.getValue("longitude")),
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const transmissionStation = row.original;

      return h("div", { class: "relative" }, h(TransmissionStationRowAction, {
        transmissionStation,
      }));
    },
  },
];
