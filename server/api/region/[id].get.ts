import { getRegionWithAreaOffices } from "~~/server/database/queries/franchise";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, "id");

  if (!z.coerce.number().safeParse(id).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid id.",
    });
  }

  const region = await getRegionWithAreaOffices(Number(id));

  return region;
});
