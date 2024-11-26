<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header Section -->
    <AppHeader />

    <!-- Main Content Section -->
    <main class="py-10">
      <div class="container mx-auto px-4">
        <!-- Show Events Button -->
        <button
          class="bg-yellow-500 text-white px-4 py-2 rounded shadow hover:bg-yellow-600 mb-4"
          @click="toggleEvents"
        >
          {{ showTable ? "Hide Events" : "View Events" }}
        </button>

        <!-- Events Table and CRUD Operations -->
        <div v-if="showTable">
          <!-- Events Table -->
          <EventTable />

          <!-- Event Operations -->
          <div class="mt-6 space-x-4">
            <button class="bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-green-600">
              Add Event
            </button>
            <button class="bg-red-500 text-white px-4 py-2 rounded shadow hover:bg-red-600">
              Delete Event
            </button>
            <button class="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600">
              Update Event
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer Section -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import EventTable from "./components/EventTable.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppFooter,
    EventTable,
  },
  data() {
    return {
      showTable: false, // Toggles visibility of Events Table and operations
    };
  },
  methods: {
    toggleEvents() {
      this.showTable = !this.showTable; // Toggles the table's visibility
    },
  },
};
</script>
