import { updateRegion } from "~~/server/database/queries/franchise";
import { InsertRegion } from "~~/server/database/schema";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const result = await readValidatedBody(event, InsertRegion.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [updatedRegion] = await updateRegion(Number(id), result.data);

  return updatedRegion;
});
