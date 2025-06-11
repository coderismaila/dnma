import type { z } from "zod";

import { relations } from "drizzle-orm";
import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";
import { createInsertSchema, createSelectSchema } from "drizzle-zod";

import { transmissionStation } from "./transmissionStation";
import { user } from "./user";

export const region = sqliteTable("region", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  name: text("name").notNull().unique(),
  createdAt: integer("createdAt").notNull().$default(Date.now),
  updatedAt: integer("updatedAt").notNull().$default(Date.now).$onUpdate(Date.now),
});

export const areaOffice = sqliteTable("areaOffice", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  name: text("name").notNull().unique(),
  regionId: integer("regionId").notNull().references(() => region.id, { onDelete: "cascade" }),
  createdAt: integer("createdAt").notNull().$default(Date.now),
  updatedAt: integer("updatedAt").notNull().$default(Date.now).$onUpdate(Date.now),
});

export const InsertRegion = createInsertSchema(region, {
  name: schema => schema.min(1),
}).omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

export type InsertRegion = z.infer<typeof InsertRegion>;

export const InsertAreaOffice = createInsertSchema(areaOffice, {
  name: schema => schema.min(3),
  regionId: schema => schema.int().positive("Region is required"),
}).omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

export type InsertAreaOffice = z.infer<typeof InsertAreaOffice>;

export const regionRelation = relations(region, ({ many }) => ({
  areaOffices: many(areaOffice),
  transmissionStations: many(transmissionStation),
}));

export const areaOfficeRelation = relations(areaOffice, ({ one, many }) => ({
  region: one(region, {
    fields: [areaOffice.regionId],
    references: [region.id],
  }),
  users: many(user),
}));

export const AreaOffice = createSelectSchema(areaOffice);

export type AreaOffice = z.infer<typeof AreaOffice>;
