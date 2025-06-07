import type { InsertUser } from "../schema";

export function findUserByEmail(email: string) {
  return useDB()
    .select()
    .from(tables.user)
    .where(eq(tables.user.email, email))
    .limit(1);
}

export function findUserByPayrollId(payrollId: number) {
  return useDB()
    .select()
    .from(tables.user)
    .where(eq(tables.user.payrollId, payrollId))
    .limit(1);
}

export function insertUser(user: InsertUser) {
  return useDB()
    .insert(tables.user)
    .values(user)
    .returning();
}
