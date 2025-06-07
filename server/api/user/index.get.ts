import { getTableColumns } from "drizzle-orm";

export default defineEventHandler(async () => {
  const { password, ...rest } = getTableColumns(tables.user);

  const users = await useDB()
    .select({
      ...rest,
      areaOffice: tables.areaOffice.name,
    })
    .from(tables.user)
    .innerJoin(tables.areaOffice, eq(tables.user.areaOfficeId, tables.areaOffice.id));

  return users;
});
