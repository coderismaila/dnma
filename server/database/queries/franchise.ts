import { getTableColumns } from "drizzle-orm";

import type { InsertAreaOffice, InsertRegion } from "../schema";

export async function getAllAreaOffice() {
  return useDB()
    .select({
      ...getTableColumns(tables.areaOffice),
      regionName: tables.region.name,
    })
    .from(tables.areaOffice)
    .innerJoin(tables.region, eq(tables.region.id, tables.areaOffice.regionId))
    .orderBy(tables.areaOffice.name, tables.region.name);
}

export async function getAreaOfficeById(id: number) {
  return useDB()
    .select({
      ...getTableColumns(tables.areaOffice),
      regionName: tables.region.name,
    })
    .from(tables.areaOffice)
    .where(eq(tables.areaOffice.id, id))
    .innerJoin(tables.region, eq(tables.region.id, tables.areaOffice.regionId))
    .orderBy(tables.areaOffice.name, tables.region.name);
}

export async function createAreaOffice(data: InsertAreaOffice) {
  return useDB()
    .insert(tables.areaOffice)
    .values(data)
    .returning();
}

export async function updateAreaOffice(id: number, data: InsertAreaOffice) {
  return useDB()
    .update(tables.areaOffice)
    .set(data)
    .where(eq(tables.areaOffice.id, id))
    .returning();
}

export async function deleteAreaOffice(id: number) {
  return useDB()
    .delete(tables.areaOffice)
    .where(eq(tables.areaOffice.id, id))
    .returning();
}

export async function deleteRegion(id: number) {
  return useDB()
    .delete(tables.region)
    .where(eq(tables.region.id, id))
    .returning();
}
export async function getAllRegion() {
  return useDB()
    .select()
    .from(tables.region)
    .orderBy(tables.region.name);
}

export async function getRegionById(id: number) {
  return useDB()
    .select()
    .from(tables.region)
    .where(eq(tables.region.id, id));
}

export async function updateRegion(id: number, data: InsertRegion) {
  return useDB()
    .update(tables.region)
    .set(data)
    .where(eq(tables.region.id, id))
    .returning();
}

export async function createRegion(data: InsertRegion) {
  return useDB()
    .insert(tables.region)
    .values(data)
    .returning();
}

export async function getRegionByName(name: string) {
  return useDB()
    .select()
    .from(tables.areaOffice)
    .where(eq(tables.areaOffice.name, name));
}

export async function getRegionWithAreaOffices(id: number) {
  return useDB()
    .query
    .region
    .findFirst({
      where: (region, { eq }) => eq(region.id, Number(id)),
      with: {
        areaOffices: true,
      },
    });
}
