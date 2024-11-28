<template>
    <div v-if="localEvent" class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h2 class="text-xl font-bold mb-4">Edit Event</h2>
        <form @submit.prevent="saveChanges">
          <label for="title">Title:</label>
          <input
            v-model="localEvent.title"
            id="title"
            type="text"
            class="border p-2 w-full mb-4"
          />
  
          <label for="capacity">Capacity:</label>
          <input
            v-model="localEvent.capacity"
            id="capacity"
            type="number"
            class="border p-2 w-full mb-4"
          />
  
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
              class="bg-blue-500 text-white px-4 py-2 rounded"
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
    props: ["event"], // Receive event as a prop
    data() {
      return {
        localEvent: { ...this.event }, // Create a local copy of the prop
      };
    },
    methods: {
        async saveChanges() {
  try {
    const response = await fetch(`http://localhost:3000/api/events/${this.localEvent.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(this.localEvent),
    });

    if (response.ok) {
      const updatedEvent = await response.json();
      console.log("Updated event response:", updatedEvent); // Debug the response
      alert("Event updated successfully!");
      this.$emit("update-event", updatedEvent); // Emit updated event to parent
      this.$emit("close"); // Close the form
    } else {
      console.error("Failed to update event:", response); // Log the error response
      alert("Failed to update event.");
    }
  } catch (error) {
    console.error("Unexpected error updating event:", error); // Debug the caught error
    alert("An unexpected error occurred while updating the event.");
  }
},

    },
  };
  </script>
  