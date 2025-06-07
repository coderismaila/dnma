import { getAllAreaOffice } from "~~/server/database/queries/franchise";

export default defineEventHandler(async () => {
  const areaOffices = await getAllAreaOffice();

  return areaOffices;
});
