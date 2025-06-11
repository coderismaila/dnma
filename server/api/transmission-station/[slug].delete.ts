import { deleteTransmissionStation } from "~~/server/database/queries/transmissionStation";
import { z } from "zod";

export default defineEventHandler(async (event) => {
  const slug = getRouterParam(event, "slug");

  if (!z.string().safeParse(slug).success) {
    throw createError({
      statusCode: 422,
      statusMessage: "Invalid slug.",
    });
  }

  const { id } = await deleteTransmissionStation(String(slug));

  if (!id) {
    throw createError({
      statusCode: 404,
      statusMessage: "Transmission station not found",
    });
  }

  return {
    success: true,
  };
});
