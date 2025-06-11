import { relations } from "drizzle-orm";
import { integer, real, sqliteTable, text } from "drizzle-orm/sqlite-core";
import { createInsertSchema, createSelectSchema, createUpdateSchema } from "drizzle-zod";
import { z } from "zod";

import { region } from "./franchise";

export const transmissionStation = sqliteTable("transmissionStation", {
  id: integer().primaryKey({ autoIncrement: true }),
  name: text().notNull().unique(),
  shortName: text().notNull().unique(),
  installedCapacityMVA: real().notNull().$default(() => 0.0),
  latitude: real(),
  longitude: real(),
  regionId: integer().references(() => region.id).notNull(),
  slug: text().unique().notNull(),
  createdAt: integer().notNull().$default(Date.now),
  updatedAt: integer().notNull().$default(Date.now).$onUpdate(Date.now),
});

export const transmissionStationRelations = relations(transmissionStation, ({ one }) => ({
  region: one(region, {
    fields: [transmissionStation.regionId],
    references: [region.id],
  }),
}));

export const insertTransmissionStationSchema = createInsertSchema(transmissionStation).omit({
  id: true,
  slug: true,
  createdAt: true,
  updatedAt: true,
});

export const transmissionStationSchema = createSelectSchema(transmissionStation);
export const updateTransmissionStationSchema = createUpdateSchema(transmissionStation);

export const transmissionStationWithRegionSchema = transmissionStationSchema.extend({
  regionName: z.string(),
});

export type InsertTransmissionStation = z.infer<typeof insertTransmissionStationSchema>;
export type TransmissionStation = z.infer<typeof transmissionStationSchema>;
export type UpdateTransmissionStation = z.infer<typeof updateTransmissionStationSchema>;
export type TransmissionStationWithRegion = z.infer<typeof transmissionStationWithRegionSchema>;
