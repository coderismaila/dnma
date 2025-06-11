import { getAllTransmissionStation } from "~~/server/database/queries/transmissionStation";

export default defineEventHandler(async (event) => {
  await requireUserSession(event);

  return getAllTransmissionStation();
});
