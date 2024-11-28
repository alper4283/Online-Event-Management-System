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
  const { category, startDate, endDate, city, country, organizer } = req.body; // Added country

  console.log("Incoming filter request:", req.body);

  try {
    let query = `
      SELECT 
        e.eventid AS id, e.title AS name, e.capacity, e.description, e.eventtype AS category, 
        e.date, e.starttime, e.endtime,
        o.name AS organizer,
        json_build_object(
          'city', COALESCE(a.city, 'Unknown'),
          'country', COALESCE(a.country, 'Unknown')
        ) AS address,
        ARRAY_AGG(DISTINCT c.name) AS categories,
        ARRAY_AGG(DISTINCT s.servicetype) FILTER (WHERE s.servicetype IS NOT NULL) AS services,
        ARRAY_AGG(DISTINCT an.content) FILTER (WHERE an.content IS NOT NULL) AS announcements
      FROM events e
      JOIN organizers o ON e.organizedby = o.organizerid
      LEFT JOIN address a ON e.addressid = a.addressid
      LEFT JOIN eventcategories ec ON e.eventid = ec.eventid
      LEFT JOIN categories c ON ec.categoryid = c.categoryid
      LEFT JOIN eventservices es ON e.eventid = es.eventid
      LEFT JOIN services s ON es.serviceid = s.serviceid
      LEFT JOIN announcements an ON an.eventid = e.eventid
      WHERE 1=1
    `;
    const params = [];
    let paramIndex = 1;

    if (category) {
      query += ` AND c.name = $${paramIndex}`;
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
    if (country) { // Added country filter
      query += ` AND a.country = $${paramIndex}`;
      params.push(country);
      paramIndex++;
    }
    if (organizer) {
      query += ` AND e.organizedby = $${paramIndex}`;
      params.push(organizer);
      paramIndex++;
    }

    query += `
      GROUP BY e.eventid, o.name, a.city, a.country
    `;

    const result = await pool.query(query, params);
    console.log("Response being sent to frontend:", result.rows);

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

app.delete("/api/events/:id", async (req, res) => {
  const { id } = req.params;

  try {
    const result = await pool.query("DELETE FROM events WHERE eventid = $1", [id]);

    if (result.rowCount > 0) {
      res.status(200).json({ message: "Event deleted successfully." });
    } else {
      res.status(404).json({ error: "Event not found." });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to delete event." });
  }
});


// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
