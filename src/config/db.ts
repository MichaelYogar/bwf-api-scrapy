var db = require('mysql2-promise')();
import * as dotenv from 'dotenv';
dotenv.config();

/** DB CONFIG */
db.configure({
    host: process.env.MYSQL_HOST || 'localhost',
    database: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASS
});

export = db;
