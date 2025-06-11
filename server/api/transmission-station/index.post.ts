import { createTransmissionStation } from "~~/server/database/queries/transmissionStation";
import { insertTransmissionStationSchema } from "~~/server/database/schema";

export default defineEventHandler(async (event) => {
  await requireUserSession(event);

  const result = await readValidatedBody(event, insertTransmissionStationSchema.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  await createTransmissionStation(result.data);
});
