import { createRegion } from "~~/server/database/queries/franchise";
import { InsertRegion } from "~~/server/database/schema";

export default defineEventHandler(async (event) => {
  const result = await readValidatedBody(event, InsertRegion.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [existingRegion] = await useDB()
    .select()
    .from(tables.region)
    .where(sql`lower(${tables.region.name}) = ${result.data.name.toLowerCase()}`);

  if (existingRegion) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: `Region with name "${result.data.name}" already exists`,
    }));
  }

  const region = await createRegion(result.data);

  return region;
});
