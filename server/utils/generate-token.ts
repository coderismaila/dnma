import { SignJWT } from "jose";

export async function generateToken(data: { email: string; role: string }) {
  const jwt = await new SignJWT({ ...data })
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime("1d")

    // eslint-disable-next-line node/no-process-env
    .sign(new TextEncoder().encode(process.env.NUXT_JWT_SECRET));

  return jwt;
}
