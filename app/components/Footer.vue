<script lang="ts" setup>

</script>

<template>
  <footer class="bg-secondary/50 border-t border-border">
    <div class="container mx-auto px-4 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-2 mb-4">
            <div class="p-2 bg-primary rounded-lg">
              <NuxtImg src="/ke-logo.svg" class="aspect-square size-8 flex items-center justify-center rounded-lg" />
            </div>
            <span class="text-xl font-bold">KEAR</span>
          </div>
          <p class="text-muted-foreground mb-6 max-w-md">
            Simple and efficient electricity distribution network asset management
            for organized record keeping and easy access to equipment information.
          </p>
          <div class="text-sm text-muted-foreground">
            © 2024 KEAR. All rights reserved.
          </div>
        </div>

        <div>
          <h4 class="font-semibold mb-4">
            Features
          </h4>
          <ul class="space-y-2">
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Asset Database
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Record Management
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Documentation
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Search & Reports
              </a>
            </li>
          </ul>
        </div>

        <div>
          <h4 class="font-semibold mb-4">
            Support
          </h4>
          <ul class="space-y-2">
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                User Guide
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Contact Support
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                Training
              </a>
            </li>
            <li>
              <a href="#" class="text-muted-foreground hover:text-primary transition-colors">
                System Status
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>
