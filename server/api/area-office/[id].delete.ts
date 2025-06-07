import { deleteAreaOffice } from "~~/server/database/queries/franchise";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const [deletedAreaOffice] = await deleteAreaOffice(Number(id));

  if (!deletedAreaOffice) {
    throw createError({
      statusCode: 404,
      statusMessage: "Area office not found.",
    });
  }

  return deletedAreaOffice;
});
