<template>
    <div class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h2 class="text-xl font-bold mb-4">Create Organizer</h2>
        <form @submit.prevent="createOrganizer">
          <!-- Name -->
          <label for="name" class="block text-gray-700">Name:</label>
          <input
            v-model="newOrganizer.name"
            id="name"
            type="text"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- Contact -->
          <label for="contact" class="block text-gray-700">Contact:</label>
          <input
            v-model="newOrganizer.contact"
            id="contact"
            type="text"
            class="border p-2 w-full mb-4"
          />
  
          <!-- Rating -->
          <label for="rating" class="block text-gray-700">Rating:</label>
          <input
            v-model="newOrganizer.rating"
            id="rating"
            type="number"
            class="border p-2 w-full mb-4"
            min="0"
            max="10"
          />
  
          <!-- Buttons -->
          <div class="flex justify-end space-x-4">
            <button
              type="button"
              @click="$emit('close')"
              class="bg-gray-500 text-white px-4 py-2 rounded"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="bg-green-500 text-white px-4 py-2 rounded"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
<script>
export default {
  data() {
    return {
      newOrganizer: {
        name: "",
        contact: "",
        rating: null,
      },
    };
  },
  methods: {
    async createOrganizer() {
      try {
        const response = await fetch("http://localhost:3000/api/organizers/create", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.newOrganizer),
        });

        if (response.ok) {
          alert("Organizer created successfully!");
          this.$emit("refresh-organizers");
          this.$emit("close");
        } else {
          alert("Failed to create organizer.");
        }
      } catch (error) {
        console.error("Error creating organizer:", error);
      }
    },
  },
};
</script>
  