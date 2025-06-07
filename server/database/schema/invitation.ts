import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";
import { createInsertSchema, createSelectSchema } from "drizzle-zod";
import { z } from "zod";

export const invitation = sqliteTable("invitations", {
  id: integer().primaryKey({ autoIncrement: true }),
  email: text().notNull().unique(),
  role: text({ enum: ["user", "admin", "manager"] }).notNull().default("user"),
  token: text().notNull().unique(),
  createdAt: integer("createdAt").notNull().$default(Date.now),
  updatedAt: integer("updatedAt").notNull().$default(Date.now).$onUpdate(Date.now),
  expiresAt: integer().notNull(),
  acceptedAt: integer(),
});

export const InsertInvitation = createInsertSchema(invitation, {
  email: z.string({ message: "Email is required" }).email({ message: "Invalid email address" }),
  role: z.enum(
    ["user", "manager", "admin"],
    { message: "Role is required. Please select either user, manager or admin." },
  ),
}).pick({
  email: true,
  role: true,
});

export const Invitation = createSelectSchema(invitation);

export type InsertInvitation = z.infer<typeof InsertInvitation>;
export type Invitation = z.infer<typeof Invitation>;
