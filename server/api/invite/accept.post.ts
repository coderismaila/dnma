import { createInvitedUser, getInvitationToken } from "~~/server/database/queries/invitation";
import { InsertUserByInvitation } from "~~/server/database/schema";
import { jwtVerify } from "jose";

export default defineEventHandler(async (event) => {
  const result = await readValidatedBody(event, InsertUserByInvitation.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [invitation] = await getInvitationToken(result.data.token);

  if (!invitation || invitation.acceptedAt || invitation.expiresAt < Date.now()) {
    throw createError({
      statusCode: 400,
      statusMessage: "Invitation is invalid, expired, or already accepted",
    });
  }

  const { payload } = await jwtVerify(
    result.data.token,
    // eslint-disable-next-line node/no-process-env
    new TextEncoder().encode(process.env.NUXT_JWT_SECRET),
  );

  result.data.password = await hashPassword(result.data.password);

  await createInvitedUser(result.data);

  return {
    success: true,
    data: {
      email: payload.email,
      role: payload.role,
    },
  };
});
