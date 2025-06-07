import { desc } from "drizzle-orm";

import type { InsertInvitation, InsertUserByInvitation } from "../schema";

export async function createInvite(data: InsertInvitation, token: string, expiresAt: number) {
  return useDB()
    .insert(tables.invitation)
    .values({
      ...data,
      token,
      expiresAt,
    })
    .onConflictDoUpdate({
      target: tables.invitation.email,
      set: {
        role: data.role,
        token,
        expiresAt,
      },
      where: eq(tables.invitation.email, data.email),
    });
}

export async function getInvitationToken(token: string) {
  return useDB()
    .select()
    .from(tables.invitation)
    .where(
      eq(tables.invitation.token, token),
    )
    .limit(1);
}

export async function getAllInvitation() {
  return useDB()
    .select()
    .from(tables.invitation)
    .orderBy(desc(tables.invitation.createdAt));
}

export async function createInvitedUser(data: InsertUserByInvitation) {
  return useDB()
    .batch([
      useDB().insert(tables.user).values(data),
      useDB().update(tables.invitation).set({
        acceptedAt: Date.now(),
      }).where(eq(tables.invitation.token, data.token)),
    ]);
}

export async function deleteInvitation(id: number) {
  return useDB()
    .delete(tables.invitation)
    .where(eq(tables.invitation.id, Number(id)))
    .returning();
}
