<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header Section -->
    <AppHeader />

    <!-- Main Content Section -->
    <main class="py-10">
      <div class="container mx-auto px-4">
        <!-- Toggle Events Button -->
        <button
          class="bg-yellow-500 text-white px-4 py-2 rounded shadow hover:bg-yellow-600 mb-4"
          @click="toggleEvents"
        >
          {{ showTable ? "Hide Events" : "View Events" }}
        </button>

        <!-- Events Table -->
        <EventTable v-if="showTable" />
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
      showTable: false, // Toggles visibility of Events Table
    };
  },
  methods: {
    toggleEvents() {
      this.showTable = !this.showTable; // Toggles the table's visibility
    },
  },
};
</script>
