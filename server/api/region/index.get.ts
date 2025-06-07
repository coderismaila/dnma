import { getAllRegion } from "~~/server/database/queries/franchise";

export default defineEventHandler(async () => {
  return getAllRegion();
});
