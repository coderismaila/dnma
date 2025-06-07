<script lang="ts" setup>
import { toTypedSchema } from "@vee-validate/zod";
import { InsertInvitation } from "~~/server/database/schema";
import { Loader2 } from "lucide-vue-next";
import { useForm } from "vee-validate";
import { toast } from "vue-sonner";

const formSchema = toTypedSchema(InsertInvitation);

const { handleSubmit, isSubmitting } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  try {
    await $fetch("/api/invite/send", { body: values, method: "POST" });
    toast.success("Invitation sent successfully!", {
      description: "The invitation has been sent to the user.",
      duration: 3000,
    });
    navigateTo("/users"); // Redirect to users page after successful submission
  }
  catch (error) {
    toast.error("Failed to send invitation", {
      description: "There was an error sending the invitation. Please try again.",
      duration: 5000,
    });
    console.error("Error sending invitation:", error);
  }
});
</script>

<template>
  <div class="space-y-6">
    <div class="space-y-6">
      <h3 class="text-lg font-medium">
        Invite User
      </h3>
    </div>

    <Separator />

    <div class="max-w-xl">
      <form class="space-y-6" @submit="onSubmit">
        <FormField v-slot="{ componentField }" name="email">
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input type="text" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <FormField
          v-slot="{ componentField }"
          type="radio"
          name="role"
        >
          <FormItem class="space-y-3">
            <FormLabel>Role</FormLabel>
            <FormControl>
              <RadioGroup class="flex space-y-1" v-bind="componentField">
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="user" />
                    <FormLabel>User</FormLabel>
                  </FormControl>
                </FormItem>
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="manager" />
                    <FormLabel>Manager</FormLabel>
                  </FormControl>
                </FormItem>
                <FormItem class="flex items-center space-x-2">
                  <FormControl>
                    <RadioGroupItem value="admin" />
                    <FormLabel>Admin</FormLabel>
                  </FormControl>
                </FormItem>
              </RadioGroup>
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>

        <Button type="submit">
          Submit
          <Loader2 v-if="isSubmitting" class="w-4 h-4 mr-2 animate-spin" />
        </Button>
      </form>
    </div>
  </div>
</template>
