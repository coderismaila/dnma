import { updateAreaOffice } from "~~/server/database/queries/franchise";
import { InsertAreaOffice } from "~~/server/database/schema";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const result = await readValidatedBody(event, InsertAreaOffice.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [updatedAreaOffice] = await updateAreaOffice(Number(id), result.data);

  return updatedAreaOffice;
});
