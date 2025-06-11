import { getTransmissionStationBySlug } from "~~/server/database/queries/transmissionStation";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const slug = getRouterParam(event, "slug");

  if (!z.string().safeParse(slug).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid slug.",
    });
  }

  const tx = await getTransmissionStationBySlug(slug as string);
  return tx;
});
