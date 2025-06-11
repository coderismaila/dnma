CREATE TABLE `transmissionStation` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`name` text NOT NULL,
	`shortName` text NOT NULL,
	`installedCapacityMVA` real NOT NULL,
	`latitude` real,
	`longitude` real,
	`regionId` integer NOT NULL,
	`createdAt` integer NOT NULL,
	`updatedAt` integer NOT NULL,
	FOREIGN KEY (`regionId`) REFERENCES `region`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE UNIQUE INDEX `transmissionStation_name_unique` ON `transmissionStation` (`name`);--> statement-breakpoint
CREATE UNIQUE INDEX `transmissionStation_shortName_unique` ON `transmissionStation` (`shortName`);