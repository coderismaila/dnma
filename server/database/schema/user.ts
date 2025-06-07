import { relations } from "drizzle-orm";
import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";
import { createInsertSchema, createSelectSchema } from "drizzle-zod";
import { z } from "zod";

import { areaOffice } from "./franchise";

export const user = sqliteTable("user", {
  id: integer().primaryKey({ autoIncrement: true }),
  payrollId: integer().notNull().unique(),
  name: text().notNull(),
  role: text({ enum: ["user", "admin", "manager"] }).notNull().default("user"),
  areaOfficeId: integer().notNull().references(() => areaOffice.id, { onDelete: "cascade" }),
  email: text().notNull().unique(),
  password: text().notNull(),
  image: text(),
  createdAt: integer().notNull().$default(() => Date.now()),
  updatedAt: integer().notNull().$default(() => Date.now()).$onUpdate(() => Date.now()),
});

export const userRelation = relations(user, ({ one }) => ({
  areaOffice: one(areaOffice, {
    fields: [user.areaOfficeId],
    references: [areaOffice.id],
  }),
}));

export const UserSignIn = createInsertSchema(user).pick({
  email: true,
  password: true,
});

export const InsertUser = createInsertSchema(user, {

}).omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

export const User = createSelectSchema(user)
  .omit({ password: true });

export type User = z.infer<typeof User>;

export const InsertUserByInvitation = InsertUser.extend({
  token: z.string(),
});

export const UserWithAreaOffice = createSelectSchema(user).extend({
  areaOffice: z.string(),
}).omit({
  password: true,
});

export type UserSignIn = z.infer<typeof UserSignIn>;
export type InsertUser = z.infer<typeof InsertUser>;
export type InsertUserByInvitation = z.infer<typeof InsertUserByInvitation>;
export type UserWithAreaOffice = z.infer<typeof UserWithAreaOffice>;
