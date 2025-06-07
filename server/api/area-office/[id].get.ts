import { getAreaOfficeById } from "~~/server/database/queries/franchise";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const areaOffice = await getAreaOfficeById(Number(id));
  if (!areaOffice) {
    throw createError({
      statusCode: 404,
      statusMessage: `Area office with ID: ${id}, not found.`,
    });
  }

  return areaOffice;
});
