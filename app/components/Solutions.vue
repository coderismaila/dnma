<script lang="ts" setup>
import { solutions } from "~~/constants/solutions.contants";
</script>

<template>
  <section id="solutions" class="py-20">
    <div class="container mx-auto px-4">
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          Organized Solutions
        </h2>
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          Simple tools to help you maintain organized records and easily access
          information about your electrical distribution network assets.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
        <Card
          v-for="solution in solutions"
          :key="solution.title"
          class="relative overflow-hidden group hover:shadow-xl transition-all duration-300"
        >
          <div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-accent/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

          <CardHeader>
            <div class="inline-flex p-4 rounded-lg bg-primary/10 w-fit mb-4 group-hover:bg-primary/20 transition-colors">
              <Icon
                :name="solution.icon"
                size="30"
                class="text-primary"
              />
            </div>
            <CardTitle class="text-2xl mb-4">
              {{ solution.title }}
            </CardTitle>
          </CardHeader>

          <CardContent>
            <p class="text-muted-foreground mb-6 leading-relaxed">
              {{ solution.description }}
            </p>

            <ul class="space-y-2 mb-6">
              <li
                v-for="feature in solution.features"
                :key="feature"
                class="flex items-center text-sm"
              >
                <div class="w-1.5 h-1.5 bg-primary rounded-full mr-3" />
                {{ feature }}
              </li>
            </ul>
          </CardContent>
        </Card>
      </div>

      <div class="text-center bg-primary/5 rounded-2xl p-12 border border-primary/10">
        <h3 class="text-3xl font-bold mb-4">
          Ready to Organize Your Asset Records?
        </h3>
        <p class="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
          Start managing your electrical distribution network assets with our
          simple and efficient record-keeping system.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <Button size="lg" class="px-8">
            Get Started
          </Button>
          <Button
            variant="outline"
            size="lg"
            class="px-8"
          >
            View Features
          </Button>
        </div>
      </div>
    </div>
  </section>
</template>

<style>

</style>
