export default defineEventHandler(async (event) => {
  const { user } = await getUserSession(event);

  if (event.path !== "/") {
    if (!user) {
      return sendRedirect(event, "/", 302);
    }
  }
});
