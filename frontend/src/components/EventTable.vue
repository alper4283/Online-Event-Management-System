<template>
  <div class="bg-white shadow-md rounded-lg p-6">
    <h2 class="text-xl font-bold mb-4">Events Table</h2>

    <!-- Filter Form -->
    <form @submit.prevent="applyFilters" class="mb-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Category Filter -->
        <div>
          <label for="category" class="block text-gray-700">Category</label>
          <select
            v-model="filters.category"
            id="category"
            class="w-full border border-gray-300 rounded px-4 py-2">
            <option value="">All Categories</option>
            <option v-for="category in categories" :key="category.id" :value="category.name">
            {{ category.name }}
            </option>
          </select>
        </div>

        <!-- Date Range Filter -->
        <div>
          <label for="startDate" class="block text-gray-700">Start Date</label>
          <input
            v-model="filters.startDate"
            type="date"
            id="startDate"
            class="w-full border border-gray-300 rounded px-4 py-2"
          />
        </div>
        <div>
          <label for="endDate" class="block text-gray-700">End Date</label>
          <input
            v-model="filters.endDate"
            type="date"
            id="endDate"
            class="w-full border border-gray-300 rounded px-4 py-2"
          />
        </div>

        <!-- City Filter -->
        <div>
          <label for="city" class="block text-gray-700">City</label>
          <input
            v-model="filters.city"
            type="text"
            id="city"
            class="w-full border border-gray-300 rounded px-4 py-2"
            placeholder="Enter city"
          />
        </div>

        <!-- Organizer Filter -->
        <div>
          <label for="organizer" class="block text-gray-700">Organizer</label>
          <select
            v-model="filters.organizer"
            id="organizer"
            class="w-full border border-gray-300 rounded px-4 py-2"
          >
            <option value="">All Organizers</option>
            <option v-for="organizer in organizers" :key="organizer.id" :value="organizer.id">
              {{ organizer.name }}
            </option>
          </select>
        </div>
      </div>

      <!-- Submit Button -->
      <div class="mt-4">
        <button
          type="submit"
          class="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600"
        >
          Retrieve Events
        </button>
      </div>
    </form>

    <!-- Events Table -->
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
          <td class="border border-gray-300 px-4 py-2">{{ event.organizer }}</td>
          <td class="border border-gray-300 px-4 py-2">
            {{ event.address.city }}, {{ event.address.country }}
          </td>
          <td class="border border-gray-300 px-4 py-2">
  <ul>
    <li v-for="service in event.services" :key="service">
      {{ service }}
    </li>
  </ul>
</td>
<td class="border border-gray-300 px-4 py-2">
  <ul>
    <li v-for="announcement in event.announcements" :key="announcement">
      {{ announcement }}
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
      filters: {
        category: "",
        startDate: "",
        endDate: "",
        city: "",
        organizer: "",
      },
      categories: [], // Dynamically fetched categories
      organizers: [], // Dynamically fetched organizers
    };
  },
  mounted() {
    this.fetchOrganizers();
    this.fetchCategories();
  },
  methods: {
    async fetchOrganizers() {
      try {
        const response = await fetch("http://localhost:3000/api/organizers");
        this.organizers = await response.json();
      } catch (error) {
        console.error("Error fetching organizers:", error);
      }
    },
    async fetchCategories() {
      try {
        const response = await fetch("http://localhost:3000/api/categories");
        this.categories = await response.json();
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    },
    async applyFilters() {
      try {
        const response = await fetch("http://localhost:3000/api/events/filter", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.filters),
        });
        this.events = await response.json();
      } catch (error) {
        console.error("Error fetching filtered events:", error);
      }
    },
  },
};
</script>


