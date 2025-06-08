<script setup lang="ts">
import { features } from "~~/constants/features.constants";
</script>

<template>
  <section id="features" class="py-20 bg-secondary/30">
    <div class="container mx-auto px-4">
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          Simple Asset Management
        </h2>
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          From high-voltage substations to distribution feeders, keep organized
          records of every component in your electrical network.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card
          v-for="feature in features"
          :key="feature.title"
          class="hover:shadow-lg transition-all duration-300 hover:-translate-y-1 border-border/50"
        >
          <CardHeader>
            <div class="inline-flex p-3 rounded-lg bg-secondary-50 w-fit mb-4">
              <Icon
                :name="feature.icon"
                size="30"
              />
            </div>
            <CardTitle
              class="text-xl"
            >
              {{ feature.title }}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p class="text-muted-foreground leading-relaxed">
              {{ feature.description }}
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  </section>
</template>
