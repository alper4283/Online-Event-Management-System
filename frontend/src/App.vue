<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header Section -->
    <header class="bg-blue-600 text-white py-6 shadow-lg">
      <h1 class="text-3xl font-bold text-center">Welcome to Event Link</h1>
      <p class="text-center mt-2 text-blue-200">Your go-to platform for managing events effortlessly</p>
    </header>

    <!-- Main Content Section -->
    <main class="py-10">
      <div class="container mx-auto px-4">
        <div class="bg-white shadow-md rounded-lg p-6 text-center">
          <p class="text-gray-700 text-lg">
            Start managing your events by selecting an action below:
          </p>
          <div class="mt-6 space-x-4">
            <button class="bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-green-600">
              Create Event
            </button>
            <button class="bg-yellow-500 text-white px-4 py-2 rounded shadow hover:bg-yellow-600">
              View Events
            </button>
            <button class="bg-red-500 text-white px-4 py-2 rounded shadow hover:bg-red-600">
              Delete Event
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer Section -->
    <footer class="bg-gray-800 text-white py-4">
      <p class="text-center text-sm">
        © 2024 Event Link. All rights reserved.
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Optional Global Styles */
body {
  font-family: 'Inter', sans-serif;
}
</style>
