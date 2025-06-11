ALTER TABLE `transmissionStation` ADD `slug` text NOT NULL;--> statement-breakpoint
CREATE UNIQUE INDEX `transmissionStation_slug_unique` ON `transmissionStation` (`slug`);