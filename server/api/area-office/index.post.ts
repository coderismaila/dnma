import { createAreaOffice, getRegionById, getRegionByName } from "~~/server/database/queries/franchise";
import { InsertAreaOffice } from "~~/server/database/schema";

export default defineEventHandler(async (event) => {
  const result = await readValidatedBody(event, InsertAreaOffice.safeParse);

  if (!result.success) {
    return sendZodError(event, result.error);
  }

  const [existingAreaOffice] = await getRegionByName(result.data.name);

  if (existingAreaOffice) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: `Area office with name "${result.data.name}" already exists`,
    }));
  }

  const [region] = await getRegionById(result.data.regionId);

  if (!region) {
    return sendError(event, createError({
      statusCode: 422,
      statusMessage: `Region with id "${result.data.regionId}" does not exist`,
    }));
  }

  try {
    await createAreaOffice(result.data);
  }
  catch (error) {
    console.error(error);
    return sendError(event, createError({
      statusCode: 500,
      statusMessage: "Something unexpected happened",
    }));
  }
});
