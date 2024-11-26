<template>
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-xl font-bold mb-4">Events Table</h2>
      <table class="table-auto w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-200">
            <th class="border border-gray-300 px-4 py-2">Name</th>
            <th class="border border-gray-300 px-4 py-2">Capacity</th>
            <th class="border border-gray-300 px-4 py-2">Category</th>
            <th class="border border-gray-300 px-4 py-2">Organizator</th>
            <th class="border border-gray-300 px-4 py-2">Address</th>
            <th class="border border-gray-300 px-4 py-2">Services</th>
            <th class="border border-gray-300 px-4 py-2">Announcements</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="event in events" :key="event.id">
            <td class="border border-gray-300 px-4 py-2">{{ event.name }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ event.capacity }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ event.category }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ event.organizator }}</td>
            <td class="border border-gray-300 px-4 py-2">
              {{ event.address.city }}, {{ event.address.country }}
            </td>
            <td class="border border-gray-300 px-4 py-2">
              <ul>
                <li v-for="service in event.services" :key="service.id">
                  {{ service.name }}
                </li>
              </ul>
            </td>
            <td class="border border-gray-300 px-4 py-2">
              <ul>
                <li v-for="announcement in event.announcements" :key="announcement.id">
                  {{ announcement.content }}
                </li>
              </ul>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "EventTable",
    data() {
      return {
        events: [], // Placeholder for fetched events
      };
    },
    mounted() {
      // Fetch events data when the component is mounted
      this.fetchEvents();
    },
    methods: {
      async fetchEvents() {
        try {
          // Replace with your actual API endpoint
          const response = await fetch("http://localhost:3000/api/events");
          this.events = await response.json();
        } catch (error) {
          console.error("Error fetching events:", error);
        }
      },
    },
  };
  </script>
  