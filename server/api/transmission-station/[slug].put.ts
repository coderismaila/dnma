import { updateTransmissionStation } from "~~/server/database/queries/transmissionStation";
import { updateTransmissionStationSchema } from "~~/server/database/schema";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const slug = getRouterParam(event, "slug");

  if (!z.string().safeParse(slug).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid slug.",
    });
  }

  const result = await readValidatedBody(event, updateTransmissionStationSchema.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  return updateTransmissionStation(result.data, String(slug));
});
