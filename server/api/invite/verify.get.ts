import { getInvitationToken } from "~~/server/database/queries/invitation";
import { jwtVerify } from "jose";
import { z } from "zod";

const TokenQuery = z.object({
  token: z.string(),
});

export default defineEventHandler(async (event) => {
  const result = await getValidatedQuery(event, TokenQuery.safeParse);

  // eslint-disable-next-line node/no-process-env
  const secret = process.env.NUXT_JWT_SECRET;

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [invitation] = await getInvitationToken(result.data.token);

  if (!invitation || invitation.acceptedAt || new Date(invitation.expiresAt) < new Date()) {
    // If the invitation is not found, already accepted, or expired
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: "Invitation is invalid, expired, or already accepted",
    }));
  }

  try {
    const { payload } = await jwtVerify(
      result.data.token,
      new TextEncoder().encode(secret),
    );

    return {
      success: true,
      data: {
        email: payload.email,
        role: payload.role,
      },
    };
  }
  catch (error) {
    console.error(error);
    return sendError(event, createError({
      statusCode: 500,
      statusMessage: "Unhandled error",
    }));
  }
});
