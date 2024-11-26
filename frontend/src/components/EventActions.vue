<template>
    <div class="bg-white shadow-md rounded-lg p-6 text-center">
      <p class="text-gray-700 text-lg">
        Start managing your events by selecting an action below:
      </p>
      <div class="mt-6 space-x-4">
        <button
          class="bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-green-600"
        >
          Create Event
        </button>
        <button
          class="bg-yellow-500 text-white px-4 py-2 rounded shadow hover:bg-yellow-600"
          @click="$emit('show-events')"
        >
          View Events
        </button>
        <button
          class="bg-red-500 text-white px-4 py-2 rounded shadow hover:bg-red-600"
        >
          Delete Event
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "EventActions",
  };
  </script>
  