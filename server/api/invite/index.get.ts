import { getAllInvitation } from "~~/server/database/queries/invitation";

export default defineEventHandler(async () => {
  const invitation = await getAllInvitation();
  return invitation;
});
