import { findUserByEmail, findUserByPayrollId, insertUser } from "~~/server/database/queries/user";
import { InsertUser } from "~~/server/database/schema";

export default defineEventHandler(async (event) => {
  const result = await readValidatedBody(event, InsertUser.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  // check if email exists
  const [existingEmail] = await findUserByEmail(result.data.email);

  if (existingEmail) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: `User with email "${result.data.email}" already exists`,
    }));
  }

  const [existingPayrollId] = await findUserByPayrollId(result.data.payrollId);

  if (existingPayrollId) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: `User with payroll ID "${result.data.payrollId}" already exists`,
    }));
  }

  result.data.password = await hashPassword(result.data.password);

  const user = await insertUser(result.data);

  if (!user) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: "Failed to create user",
    }));
  }

  return sendRedirect(event, "/auth/signin");
});
