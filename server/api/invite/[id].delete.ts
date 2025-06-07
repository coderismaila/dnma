import { deleteInvitation } from "~~/server/database/queries/invitation";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const [deletedInvite] = await deleteInvitation(Number(id));
  if (!deletedInvite) {
    throw createError({
      statusCode: 404,
      statusMessage: "Region not found.",
    });
  }

  return {
    success: true,
  };
});
