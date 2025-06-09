<script lang="ts" setup>
const colorMode = useColorMode();

const logo = computed(() => {
  return colorMode.preference === "dark" ? "/ke-logo-white.svg" : "ke-logo.svg";
});
</script>

<template>
  <section class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <div class="absolute inset-0 grid-pattern opacity-10" />

    <div class="absolute inset-0 electric-gradient opacity-5" />

    <div class="container mx-auto px-4 z-10">
      <div class="text-center max-w-4xl mx-auto">
        <div class="float-animation mb-8">
          <div class="inline-flex p-4 bg-primary/10 rounded-full">
            <NuxtImg :src="logo" class="aspect-square size-8 flex items-center justify-center rounded-lg" />
          </div>
        </div>

        <h1 class="text-5xl md:text-7xl font-bold mb-6 animate-fade-in">
          Kaduna Electric
          <span class="text-transparent bg-gradient-to-r from-primary to-accent bg-clip-text">
            Asset Registry
          </span>
        </h1>

        <p class="text-xl md:text-2xl text-muted-foreground mb-8 max-w-3xl mx-auto animate-slide-up">
          Internal asset management system for Kaduna Electric distribution network.
          Access and maintain records for transformers, injection substations, and feeder infrastructure.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center animate-slide-up">
          <Button
            size="lg"
            class="text-lg px-8 py-3 group"
            as-child
          >
            <NuxtLink to="/dashboard">
              Access Dashboard

              <Icon name="i-lucide-arrow-right" class="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
            </NuxtLink>
          </Button>
          <Button
            variant="outline"
            size="lg"
            class="text-lg px-8 py-3"
            as-child
          >
            <NuxtLink to="/">
              View Records
            </NuxtLink>
          </Button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 animate-slide-up">
          <div class="text-center">
            <div class="text-3xl font-bold text-primary mb-2">
              Assets
            </div>
            <div class="text-muted-foreground">
              Registered & Tracked
            </div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-primary mb-2">
              Records
            </div>
            <div class="text-muted-foreground">
              Maintained & Updated
            </div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-primary mb-2">
              Access
            </div>
            <div class="text-muted-foreground">
              Internal Use Only
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="absolute top-20 right-20 opacity-20 animate-bounce">
      <Icon name="i-lucide-building" class="h-12 w-12 text-primary" />
    </div>
    <div class="absolute bottom-20 left-20 opacity-20 animate-pulse">
      <Icon name="i-lucide-power" class="h-8 w-8 text-accent" />
    </div>
  </section>
</template>
