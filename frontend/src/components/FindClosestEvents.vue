<template>
    <div class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg max-h-screen overflow-y-auto">
        <h2 class="text-xl font-bold mb-4">Find Closest Events</h2>
        
        <!-- Address Selector -->
        <label for="address" class="block text-gray-700">Select Address:</label>
        <select
          v-model="selectedAddress"
          id="address"
          class="border p-2 w-full mb-4"
          required
        >
          <option value="">Select an Address</option>
          <option
            v-for="address in addresses"
            :key="address.id"
            :value="address.id"
          >
            {{ address.city }}, {{ address.country }}
          </option>
        </select>
  
        <!-- Retrieve Closest Events Button -->
        <button
          class="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600 mb-4"
          @click="fetchClosestEvents"
          :disabled="!selectedAddress"
        >
          Retrieve Closest Events
        </button>
  
        <!-- Closest Events Table -->
        <div v-if="closestEvents.length" class="overflow-x-auto">
          <table class="table-auto w-full border-collapse border border-gray-300">
            <thead>
              <tr class="bg-gray-200">
                <th class="border border-gray-300 px-4 py-2">Name</th>
                <th class="border border-gray-300 px-4 py-2">Date</th>
                <th class="border border-gray-300 px-4 py-2">Start Time</th>
                <th class="border border-gray-300 px-4 py-2">End Time</th>
                <th class="border border-gray-300 px-4 py-2">Distance (meters)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="event in closestEvents" :key="event.id">
                <td class="border border-gray-300 px-4 py-2">{{ event.name }}</td>
                <td class="border border-gray-300 px-4 py-2">{{ formatDate(event.date) }}</td>
                <td class="border border-gray-300 px-4 py-2">{{ formatTime(event.starttime) }}</td>
                <td class="border border-gray-300 px-4 py-2">{{ formatTime(event.endtime) }}</td>
                <td class="border border-gray-300 px-4 py-2">{{ event.distance.toFixed(2) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
  
        <!-- Close Button -->
        <button
          class="bg-gray-500 text-white px-4 py-2 rounded mt-4"
          @click="$emit('close')"
        >
          Close
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        addresses: [], // Available addresses
        selectedAddress: "", // Selected address ID
        closestEvents: [], // Closest events data
      };
    },
    mounted() {
      this.fetchAddresses();
    },
    methods: {
      async fetchAddresses() {
        try {
          const response = await fetch("http://localhost:3000/api/addresses");
          this.addresses = await response.json();
        } catch (error) {
          console.error("Error fetching addresses:", error);
        }
      },
      async fetchClosestEvents() {
        try {
          const response = await fetch(`http://localhost:3000/api/events/closest/${this.selectedAddress}`);
          this.closestEvents = await response.json();
        } catch (error) {
          console.error("Error fetching closest events:", error);
        }
      },
      formatDate(date) {
        return new Date(date).toLocaleDateString();
      },
      formatTime(time) {
        return time.substring(0, 5); // Format HH:mm
      },
    },
  };
  </script>
  