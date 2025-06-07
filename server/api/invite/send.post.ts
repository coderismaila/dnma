import { createInvite } from "~~/server/database/queries/invitation";
import { InsertInvitation } from "~~/server/database/schema/invitation";
import { addHours, getUnixTime } from "date-fns";

export default defineEventHandler(async (event) => {
  const result = await readValidatedBody(event, InsertInvitation.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const token = await generateToken({ email: result.data.email, role: result.data.role! });
  const expiresAt = getUnixTime(addHours(new Date(), 24)) * 1000;

  await createInvite(result.data, token, expiresAt);

  const inviteLink = `${getRequestURL(event).origin}/auth/register?token=${token}`;

  const { emails } = useResend();

  await emails.send({
    from: "info@megamaxlightworkltd.com",
    to: result.data.email,
    subject: "Invitation to Join Our Platform",
    html: `<p>You have been invited to join our platform. Click the link below to register:</p>
    <p><a href="${inviteLink}">Register Now</a></p>
    <p>This link will expire in 24 hours.</p>`,
  }).catch((error) => {
    console.error("Error sending invitation email:", error);
    throw createError({
      statusCode: 500,
      message: "Failed to send invitation email.",
    });
  });

  return {
    success: true,
    data: { inviteLink },
  };
});
