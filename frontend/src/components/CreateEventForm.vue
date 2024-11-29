<template>
    <div class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg max-h-screen overflow-y-auto">
        <h2 class="text-xl font-bold mb-4">Create Event</h2>
        <form @submit.prevent="createEvent">
          <!-- Title -->
          <label for="title" class="block text-gray-700">Title:</label>
          <input
            v-model="newEvent.title"
            id="title"
            type="text"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- Description -->
          <label for="description" class="block text-gray-700">Description:</label>
          <textarea
            v-model="newEvent.description"
            id="description"
            class="border p-2 w-full mb-4"
          ></textarea>
  
          <!-- Event Type -->
          <label for="eventType" class="block text-gray-700">Event Type:</label>
          <select
            v-model="newEvent.eventType"
            id="eventType"
            class="border p-2 w-full mb-4"
            required
          >
            <option value="">Select Event Type</option>
            <option v-for="type in eventTypes" :key="type" :value="type">{{ type }}</option>
          </select>
  
          <!-- Capacity -->
          <label for="capacity" class="block text-gray-700">Capacity:</label>
          <input
            v-model="newEvent.capacity"
            id="capacity"
            type="number"
            class="border p-2 w-full mb-4"
            min="0"
            required
          />

          <!-- Categories -->
                <label for="categories" class="block text-gray-700">Categories:</label>
                <select
                v-model="selectedCategories"
                id="categories"
                class="border p-2 w-full mb-4"
                multiple
                >
                <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                >
                    {{ category.name }}
                </option>
                </select>

  
          <!-- Date -->
          <label for="date" class="block text-gray-700">Date:</label>
          <input
            v-model="newEvent.date"
            id="date"
            type="date"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- Start Time -->
          <label for="startTime" class="block text-gray-700">Start Time:</label>
          <input
            v-model="newEvent.startTime"
            id="startTime"
            type="time"
            class="border p-2 w-full mb-4"
            required
          />
  
          <!-- End Time -->
          <label for="endTime" class="block text-gray-700">End Time:</label>
          <input
            v-model="newEvent.endTime"
            id="endTime"
            type="time"
            class="border p-2 w-full mb-4"
          />
  
          <!-- Address -->
          <label for="address" class="block text-gray-700">Address:</label>
          <select
            v-model="newEvent.addressId"
            id="address"
            class="border p-2 w-full mb-4"
            required
          >
            <option value="">Select Address</option>
            <option
              v-for="address in addresses"
              :key="address.id"
              :value="address.id"
            >
              {{ address.city }}, {{ address.country }}
            </option>
          </select>
  
          <!-- Organizer -->
          <label for="organizer" class="block text-gray-700">Organizer:</label>
          <select
            v-model="newEvent.organizerId"
            id="organizer"
            class="border p-2 w-full mb-4"
            required
          >
            <option value="">Select Organizer</option>
            <option
              v-for="organizer in organizers"
              :key="organizer.id"
              :value="organizer.id"
            >
              {{ organizer.name }}
            </option>
          </select>
  
          <!-- Save and Cancel Buttons -->
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
        newEvent: {
          title: "",
          description: "",
          eventType: "",
          capacity: 0,
          date: "",
          startTime: "",
          endTime: "",
          addressId: "",
          organizerId: "",
        },
        selectedCategories: [], // To hold selected categories
        categories: [], // Dynamically fetched categories
        addresses: [],
        organizers: [],
        eventTypes: [
          "Hackathon", "Concert", "Sports", "Conference", "Theatre",
          "Workshop", "Festival", "Webinar", "Exhibition", "Meetup",
          "Networking", "Seminar", "Tournament", "Charity", "Comedy",
          "Dance", "Other"
        ],
      };
    },
    mounted() {
      this.fetchCategories();
      this.fetchAddresses();
      this.fetchOrganizers();
    },
    methods: {
      async fetchCategories() {
        try {
          const response = await fetch("http://localhost:3000/api/categories");
          this.categories = await response.json();
        } catch (error) {
          console.error("Error fetching categories:", error);
        }
      },
      async fetchAddresses() {
        try {
          const response = await fetch("http://localhost:3000/api/addresses");
          this.addresses = await response.json();
        } catch (error) {
          console.error("Error fetching addresses:", error);
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
      async createEvent() {
        try {
          const response = await fetch("http://localhost:3000/api/events", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              ...this.newEvent,
              categories: this.selectedCategories, // Include selected categories
            }),
          });
  
          if (response.ok) {
            alert("Event created successfully!");
            this.$emit("refresh-events");
            this.$emit("close");
          } else {
            alert("Failed to create event.");
          }
        } catch (error) {
          console.error("Error creating event:", error);
        }
      },
    },
  };
  </script>
  