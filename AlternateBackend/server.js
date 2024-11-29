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
  const { category, startDate, endDate, city, country, organizer } = req.body;

  console.log("Incoming filter request:", req.body);

  try {
    let query = `
      SELECT 
        e.eventid AS id, e.title AS name, e.capacity, e.description, 
        e.eventtype AS eventType,  -- Keep eventType for clarity
        e.date, e.starttime, e.endtime,
        o.name AS organizer,
        json_build_object(
          'city', COALESCE(a.city, 'Unknown'),
          'country', COALESCE(a.country, 'Unknown')
        ) AS address,
        ARRAY_AGG(DISTINCT c.name) AS categories, -- Retrieve all categories
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

    // Correct the category filter to use `categories.name`
    if (category) {
      query += ` AND EXISTS (
        SELECT 1 FROM eventcategories ec2
        JOIN categories c2 ON ec2.categoryid = c2.categoryid
        WHERE ec2.eventid = e.eventid AND c2.name = $${paramIndex}
      )`;
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
    if (country) {
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

    // Return the updated rows
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

app.put("/api/events/:id", async (req, res) => {
  const { id } = req.params;
  const { title, capacity } = req.body; // Only include the fields you need to update

  try {
    // Initialize query parts
    let query = "UPDATE events SET ";
    const updates = [];
    const params = [];
    let paramIndex = 1;

    // Dynamically add fields to the query if they are provided
    if (title) {
      updates.push(`title = $${paramIndex}`);
      params.push(title);
      paramIndex++;
    }
    if (capacity) {
      updates.push(`capacity = $${paramIndex}`);
      params.push(capacity);
      paramIndex++;
    }

    // If no fields are provided, return an error
    if (updates.length === 0) {
      return res.status(400).json({ error: "No fields provided for update." });
    }

    // Construct the full query
    query += updates.join(", ");
    query += ` WHERE eventid = $${paramIndex} RETURNING *`;
    params.push(id);

    // Execute the query
    const result = await pool.query(query, params);

    if (result.rowCount > 0) {
      res.status(200).json(result.rows[0]);
    } else {
      res.status(404).json({ error: "Event not found." });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to update event." });
  }
});

app.get("/api/addresses", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT addressid AS id, city, country FROM address ORDER BY city, country"
    );
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to retrieve addresses" });
  }
});


app.post("/api/events", async (req, res) => {
  const { title, description, eventType, capacity, date, startTime, endTime, addressId, organizerId, categories } = req.body;

  try {
    // Insert event into the Events table
    const eventResult = await pool.query(
      `INSERT INTO events (title, description, eventtype, capacity, date, starttime, endtime, addressid, organizedby)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9) RETURNING eventid`,
      [title, description, eventType, capacity, date, startTime, endTime, addressId, organizerId]
    );

    const eventId = eventResult.rows[0].eventid;

    // Insert selected categories into EventCategories table
    if (categories && categories.length > 0) {
      const categoryInserts = categories.map(
        (categoryId) => pool.query(
          `INSERT INTO eventcategories (eventid, categoryid) VALUES ($1, $2)`,
          [eventId, categoryId]
        )
      );

      await Promise.all(categoryInserts);
    }

    res.status(201).json({ message: "Event created successfully", eventId });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create event." });
  }
});

app.post("/api/addresses", async (req, res) => {
  const { city, country, zipCode } = req.body;

  try {
    const result = await pool.query(
      `INSERT INTO address (city, country, zipcode)
       VALUES ($1, $2, $3) RETURNING *`,
      [city, country, zipCode]
    );

    res.status(201).json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create address." });
  }
});

app.post("/api/organizers/create", async (req, res) => {
  const { name, contact, rating } = req.body;

  try {
    const result = await pool.query(
      `INSERT INTO organizers (name, contact, rating)
       VALUES ($1, $2, $3) RETURNING *`,
      [name, contact, rating]
    );

    res.status(201).json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create organizer." });
  }
});



app.get("/api/events/closest/:addressId", async (req, res) => {
  const { addressId } = req.params;

  try {
    const query = `
      SELECT 
        e.eventid AS id, 
        e.title AS name, 
        e.date,
        e.starttime,
        e.endtime,
        a.city, 
        a.country,
        ST_Distance(a.location, target.location) AS distance
      FROM events e
      JOIN address a ON e.addressid = a.addressid
      CROSS JOIN (SELECT location FROM address WHERE addressid = $1) AS target
      WHERE a.location IS NOT NULL
      ORDER BY distance
      LIMIT 10;
    `;

    const result = await pool.query(query, [addressId]);

    res.status(200).json(result.rows);
  } catch (err) {
    console.error("Error fetching closest events:", err);
    res.status(500).json({ error: "Failed to retrieve closest events." });
  }
});




// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
