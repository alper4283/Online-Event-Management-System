<template>
    <div class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h2 class="text-xl font-bold mb-4">Create Address</h2>
        <form @submit.prevent="createAddress">
          <!-- City -->
          <label for="city" class="block text-gray-700">City:</label>
          <input
            v-model="newAddress.city"
            id="city"
            type="text"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- Country -->
          <label for="country" class="block text-gray-700">Country:</label>
          <input
            v-model="newAddress.country"
            id="country"
            type="text"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- Zip Code -->
          <label for="zipCode" class="block text-gray-700">Zip Code:</label>
          <input
            v-model="newAddress.zipCode"
            id="zipCode"
            type="text"
            class="border p-2 w-full mb-4"
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
        newAddress: {
          city: "",
          country: "",
          zipCode: "",
        },
      };
    },
    methods: {
      async createAddress() {
        try {
          const response = await fetch("http://localhost:3000/api/addresses", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.newAddress),
          });
  
          if (response.ok) {
            alert("Address created successfully!");
            this.$emit("refresh-addresses");
            this.$emit("close");
          } else {
            alert("Failed to create address.");
          }
        } catch (error) {
          console.error("Error creating address:", error);
        }
      },
    },
  };
  </script>
  