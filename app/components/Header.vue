<script lang="ts" setup>
const isMenuOpen = ref(false);
const { loggedIn } = useUserSession();
</script>

<template>
  <header class="bg-background/95 backdrop-blur-sm border-b border-border sticky top-0 z-50">
    <div class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <div class="p-2 bg-primary rounded-lg">
            <NuxtImg src="/ke-logo.svg" class="aspect-square size-8 flex items-center justify-center rounded-lg" />
          </div>
          <span class="text-xl font-bold">KEAR</span>
        </div>

        <nav class="hidden md:flex items-center space-x-8">
          <NuxtLink
            v-if="loggedIn"
            href="/dashboard"
            class="text-foreground hover:text-primary transition-colors"
          >
            Dashboard
          </NuxtLink>
          <NuxtLink href="#features" class="text-foreground hover:text-primary transition-colors">
            Features
          </NuxtLink>
          <NuxtLink href="#solutions" class="text-foreground hover:text-primary transition-colors">
            Solutions
          </NuxtLink>
        </nav>

        <div class="hidden md:flex items-center space-x-4">
          <Button v-if="!loggedIn" as-child>
            <NuxtLink to="/auth/signin">
              Sign In
            </NuxtLink>
          </Button>

          <Button v-else as-child>
            <NuxtLink to="/dashboard">
              Go to Dashboard
            </NuxtLink>
          </Button>
        </div>

        <button
          class="md:hidden p-2"
          @click="isMenuOpen = !isMenuOpen"
        >
          <Icon name="i-lucide-menu" class="h-6 w-6" />
        </button>
      </div>

      <!-- Mobile navigation -->
      <nav v-if="isMenuOpen" class="md:hidden mt-4 pb-4 border-t border-border pt-4">
        <div class="flex flex-col space-y-4">
          <a href="#features" class="text-foreground hover:text-primary transition-colors">
            Features
          </a>
          <a href="#solutions" class="text-foreground hover:text-primary transition-colors">
            Solutions
          </a>
          <div class="flex flex-col space-y-2 pt-4">
            <Button v-if="!loggedIn" as-child>
              <NuxtLink to="/auth/signin">
                Sign In
              </NuxtLink>
            </Button>
            <Button v-else as-child>
              <NuxtLink to="/auth/signin">
                Go to Dashboard
              </NuxtLink>
            </Button>
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>
