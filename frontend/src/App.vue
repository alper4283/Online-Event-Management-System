<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header Section -->
    <AppHeader />

    <!-- Main Content Section -->
    <main class="py-10">
      <div class="container mx-auto px-4">
        <!-- Buttons Section -->
        <div class="flex space-x-4 mb-4">
          <!-- Toggle Events Button -->
          <button
            class="bg-yellow-500 text-white px-4 py-2 rounded shadow hover:bg-yellow-600"
            @click="toggleEvents"
          >
            {{ showTable ? "Hide Events" : "View Events" }}
          </button>

          <!-- Add Event Button -->
          <button
            class="bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-green-600"
            @click="openCreateEventForm"
          >
            Add Event
          </button>

          <!-- Add Address Button -->
          <button
            class="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600"
            @click="openCreateAddressForm"
          >
            Add Address
          </button>

          <!-- Add Organizer Button -->
          <button
            class="bg-purple-500 text-white px-4 py-2 rounded shadow hover:bg-purple-600"
            @click="openCreateOrganizerForm"
          >
            Add Organizer
          </button>
        </div>

        <!-- Events Table -->
        <EventTable 
          ref="eventTable" 
          v-if="showTable" 
          @edit-event="openEditForm" 
          @refresh-events="refreshEvents" 
        />
      </div>
    </main>

    <!-- Edit Event Form -->
    <EditEventForm
      v-if="selectedEvent"
      :event="selectedEvent"
      @update-event="updateEventInTable"
      @close="closeEditForm"
    />

    <!-- Create Event Form -->
    <CreateEventForm
      v-if="creatingEvent"
      @close="closeCreateEventForm"
      @refresh-events="refreshEvents"
    />

    <!-- Create Address Form -->
    <CreateAddressForm
      v-if="creatingAddress"
      @close="closeCreateAddressForm"
      @refresh-addresses="refreshAddresses"
    />

    <!-- Create Organizer Form -->
    <CreateOrganizerForm
      v-if="creatingOrganizer"
      @close="closeCreateOrganizerForm"
      @refresh-organizers="refreshOrganizers"
    />

    <!-- Footer Section -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import EventTable from "./components/EventTable.vue";
import EditEventForm from "./components/EditEventForm.vue";
import CreateEventForm from "./components/CreateEventForm.vue";
import CreateAddressForm from "./components/CreateAddressForm.vue";
import CreateOrganizerForm from "./components/CreateOrganizerForm.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppFooter,
    EventTable,
    EditEventForm,
    CreateEventForm,
    CreateAddressForm,
    CreateOrganizerForm,
  },
  data() {
    return {
      showTable: false, // Toggles visibility of Events Table
      selectedEvent: null, // Holds the event being edited
      creatingEvent: false, // Toggles visibility of Create Event Form
      creatingAddress: false, // Toggles visibility of Create Address Form
      creatingOrganizer: false, // Toggles visibility of Create Organizer Form
    };
  },
  methods: {
    refreshEvents() {
      console.log("Refresh events triggered.");
      if (this.showTable) {
        fetch("http://localhost:3000/api/events/filter", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({}), // Fetch all events with no filters
        })
          .then(response => response.json())
          .then(updatedEvents => {
            const eventTable = this.$refs.eventTable;
            if (eventTable) {
              eventTable.events = updatedEvents.map(event => ({
                ...event,
                id: event.eventid, // Map eventid to id for consistency
              }));
            } else {
              console.warn("EventTable reference is undefined.");
            }
          })
          .catch(error => {
            console.error("Error refreshing events:", error);
          });
      }
    },
    toggleEvents() {
      this.showTable = !this.showTable;
    },
    openEditForm(event) {
      this.selectedEvent = { ...event };
    },
    closeEditForm() {
      this.selectedEvent = null;
    },
    updateEventInTable(updatedEvent) {
      const eventTable = this.$refs.eventTable;
      if (!eventTable) {
        console.error("EventTable reference is undefined.");
        return;
      }

      const index = eventTable.events.findIndex(event => event.id === updatedEvent.id);
      if (index !== -1) {
        eventTable.events.splice(index, 1, updatedEvent); // Replace the old event with the updated one
      } else {
        console.warn("Event not found in the table.");
      }
    },
    openCreateEventForm() {
      this.creatingEvent = true;
    },
    closeCreateEventForm() {
      this.creatingEvent = false;
    },
    openCreateAddressForm() {
      this.creatingAddress = true;
    },
    closeCreateAddressForm() {
      this.creatingAddress = false;
    },
    refreshAddresses() {
      console.log("Addresses refreshed.");
    },
    openCreateOrganizerForm() {
      this.creatingOrganizer = true;
    },
    closeCreateOrganizerForm() {
      this.creatingOrganizer = false;
    },
    refreshOrganizers() {
      console.log("Organizers refreshed.");
    },
  },
};
</script>
