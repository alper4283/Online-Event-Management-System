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

        <!-- Country Filter -->
        <div>
          <label for="country" class="block text-gray-700">Country</label>
          <input
            v-model="filters.country"
            type="text"
            id="country"
            class="w-full border border-gray-300 rounded px-4 py-2"
            placeholder="Enter country"
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
          <th class="border border-gray-300 px-4 py-2">Date</th>
          <th class="border border-gray-300 px-4 py-2">Time Interval</th>
          <th class="border border-gray-300 px-4 py-2">Services</th>
          <th class="border border-gray-300 px-4 py-2">Announcements</th>
          <th class="border border-gray-300 px-4 py-2">Actions</th>
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
    {{ formatDate(event.date) }}
  </td>
  <td class="border border-gray-300 px-4 py-2">
    {{ formatTime(event.starttime) }} - {{ formatTime(event.endtime) }}
  </td>
  <td class="border border-gray-300 px-4 py-2">
    <ul>
      <li v-for="service in event.services" :key="service">{{ service }}</li>
    </ul>
  </td>
  <td class="border border-gray-300 px-4 py-2">
    <ul>
      <li v-for="announcement in event.announcements" :key="announcement">{{ announcement }}</li>
    </ul>
  </td>
  <td class="border border-gray-300 px-4 py-2 flex justify-center space-x-2">
  <!-- Edit Button -->
  <button
    class="bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600"
    @click="editEvent(event)"
  >
    Edit
  </button>

  <!-- Delete Button -->
  <button
    class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
    @click="deleteEvent(event.id)"
  >
    Delete
  </button>
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
    editEvent(event) {
    this.$emit("edit-event", event); // Emit event data to the parent component
  },
  
    async deleteEvent(eventId) {
    // Confirm deletion with the user
    if (!confirm("Are you sure you want to delete this event?")) return;

    try {
      // Send DELETE request to the backend
      const response = await fetch(`http://localhost:3000/api/events/${eventId}`, {
        method: "DELETE",
      });

      if (response.ok) {
        // Remove the deleted event from the table
        this.events = this.events.filter(event => event.id !== eventId);
        alert("Event deleted successfully!");
      } else {
        alert("Failed to delete event.");
      }
    } catch (error) {
      console.error("Error deleting event:", error);
      alert("An error occurred while deleting the event.");
    }
  },
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
  formatTime(time) {
    if (!time) return "N/A";
    const [hours, minutes] = time.split(":");
    const period = +hours < 12 ? "AM" : "PM";
    const formattedHours = +hours % 12 || 12;
    return `${formattedHours}:${minutes} ${period}`;
  },
  formatDate(date) {
    if (!date) return "N/A";
    const eventDate = new Date(date);
    return eventDate.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  },
},
};
</script>


