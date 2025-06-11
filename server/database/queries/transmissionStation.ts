import { getTableColumns } from "drizzle-orm";
import slugify from "slug";

import type { InsertTransmissionStation, UpdateTransmissionStation } from "../schema";

export async function getAllTransmissionStation() {
  return useDB()
    .select({
      ...getTableColumns(tables.transmissionStation),
      regionName: tables.region.name,
    })
    .from(tables.transmissionStation)
    .innerJoin(tables.region, eq(tables.transmissionStation.regionId, tables.region.id))
    .orderBy(tables.transmissionStation.name);
}

export async function createTransmissionStation(data: InsertTransmissionStation) {
  const slugValue = slugify(data.shortName);
  return useDB()
    .insert(tables.transmissionStation)
    .values({ ...data, slug: slugValue })
    .returning();
}

export async function getTransmissionStationById(id: number) {
  const [transmissionStation] = await useDB()
    .select()
    .from(tables.transmissionStation)
    .where(eq(tables.transmissionStation.id, id))
    .limit(1);

  return transmissionStation;
}

export async function getTransmissionStationBySlug(slug: string) {
  const [transmissionStation] = await useDB()
    .select()
    .from(tables.transmissionStation)
    .where(eq(tables.transmissionStation.slug, slug))
    .limit(1);

  return transmissionStation;
}

export async function updateTransmissionStation(data: UpdateTransmissionStation, slug: string) {
  let s;
  if (data.shortName) {
    s = slugify(data.shortName);
  }
  return useDB()
    .update(tables.transmissionStation)
    .set({ ...data, slug: s })
    .where(eq(tables.transmissionStation.slug, slug))
    .returning();
}

export async function deleteTransmissionStation(slug: string) {
  const [transmissionStation] = await useDB()
    .delete(tables.transmissionStation)
    .where(eq(tables.transmissionStation.slug, slug))
    .returning({ id: tables.transmissionStation.id });

  return transmissionStation;
}
