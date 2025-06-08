import { findUserByEmail } from "~~/server/database/queries/user";
import { useValidatedBody } from "h3-zod";
import { z } from "zod";

const validationSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

export default defineEventHandler(async (event) => {
  const { email, password } = await useValidatedBody(event, validationSchema);

  // attempt to find user
  const [dbUser] = await findUserByEmail(email);

  if (!dbUser) {
    throw createError({
      statusCode: 401,
      statusMessage: "Email or password incorrect",
    });
  }

  const validPassword = await verifyPassword(dbUser.password, password);

  if (!validPassword) {
    throw createError({
      statusCode: 401,
      statusMessage: "Invalid password",
    });
  }

  await setUserSession(event, {
    user: {
      id: dbUser.id,
      name: dbUser.name,
      role: dbUser.role,
      email: dbUser.email,
      image: dbUser.image,
      areaOfficeId: dbUser.areaOfficeId,
    },
  });
  return {};
});
