const { Pool } = require("pg");

// Configure the database connection
const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "eventlink",
  password: "42831607",
  port: 5432,
});

module.exports = pool;
