const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const pool = require("./db");

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Endpoint to retrieve filtered events
app.post("/api/events/filter", async (req, res) => {
    const { category, startDate, endDate, city, organizer } = req.body;
  
    console.log("Incoming filter request:", req.body); // Debugging request
  
    try {
      // Base query
      let query = `
  SELECT 
    e.eventid AS id, e.title AS name, e.capacity, e.eventtype AS category, 
    e.description, e.date, e.starttime, e.endtime,
    o.name AS organizer,
    json_build_object('city', a.city, 'country', a.country) AS address
  FROM events e
  JOIN organizers o ON e.organizedby = o.organizerid
  JOIN address a ON e.addressid = a.addressid
  WHERE 1=1
`;

      const params = [];
      let paramIndex = 1;
  
      // Add filters dynamically
      if (category) {
        query += ` AND e.eventtype = $${paramIndex}`;
        params.push(category);
        paramIndex++;
      }
      if (startDate && endDate) {
        query += ` AND e.date BETWEEN $${paramIndex} AND $${paramIndex + 1}`;
        params.push(startDate, endDate);
        paramIndex += 2;
      }
      if (city) {
        query += ` AND a.city = $${paramIndex}`;
        params.push(city);
        paramIndex++;
      }
      if (organizer) {
        query += ` AND e.organizedby = $${paramIndex}`;
        params.push(organizer);
        paramIndex++;
      }
  
      // Execute the query
      const result = await pool.query(query, params);
  
      console.log("Response being sent to frontend:", result.rows); // Debugging response
  
      res.json(result.rows);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: "Failed to retrieve events" });
    }
  });
  
  
  

// Endpoint to retrieve categories
app.get("/api/categories", async (req, res) => {
  try {
    const result = await pool.query("SELECT categoryid AS id, name FROM categories ORDER BY name");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to retrieve categories" });
  }
});

// Endpoint to retrieve organizers
app.get("/api/organizers", async (req, res) => {
  try {
    const result = await pool.query("SELECT organizerid AS id, name FROM organizers ORDER BY name");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to retrieve organizers" });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
