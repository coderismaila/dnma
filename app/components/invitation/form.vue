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
    navigateTo("/users/invitations");
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
  <Dialog>
    <DialogTrigger as-child>
      <Button variant="outline">
        Invite User
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Invite User</DialogTitle>
        <DialogDescription>
          Fill in the details below to invite a new user to the application.
          You can specify their email and role.
        </DialogDescription>
      </DialogHeader>
      <form
        id="invite-form"
        class="space-y-6"
        @submit="onSubmit"
      >
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

        <Button
          type="submit"
          form="invite-form"
          :disabled="isSubmitting"
        >
          Submit
          <Loader2 v-if="isSubmitting" class="w-4 h-4 mr-2 animate-spin" />
        </Button>
      </form>
    </DialogContent>
  </Dialog>
</template>
