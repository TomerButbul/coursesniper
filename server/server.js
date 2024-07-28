const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const cors = require('cors');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const app = express();
const port = 3001;

const corsOptions = {
  origin: ['http://localhost:3000', 'http://127.0.0.1:3000'],
  optionsSuccessStatus: 200
};

app.use(cors(corsOptions));
app.use(bodyParser.json());

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Tomcar123!', // Ensure this matches your MySQL password
  database: 'coursesniper'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    throw err;
  }
  console.log('MySQL connected...');
});

const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization'] && req.headers['authorization'].split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, 'secret_key', (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// POST signup endpoint
app.post('/api/signup', async (req, res) => {
  const { username, email, password, phone_number } = req.body;

  // Check if email or phone number already exists
  let checkQuery = 'SELECT * FROM users WHERE email = ?';
  let checkValues = [email];

  if (phone_number) {
    checkQuery += ' OR (phone_number = ? AND phone_number IS NOT NULL)';
    checkValues.push(phone_number);
  }

  db.query(checkQuery, checkValues, async (err, results) => {
    if (err) {
      console.error('Error checking user existence:', err);
      return res.status(500).send('Error checking user existence');
    }

    if (results.length > 0) {
      const existingUser = results[0];
      if (existingUser.email === email) {
        return res.status(409).json({ error: 'Account already exists. Please log in.' });
      } else if (existingUser.phone_number === phone_number) {
        return res.status(409).json({ error: 'Phone number already exists. Please use a different phone number or log in.' });
      }
    }

    // If email and phone number are unique, proceed with signup
    try {
      const hashedPassword = await bcrypt.hash(password, 10);
      const insertQuery = 'INSERT INTO users (username, email, password, phone_number) VALUES (?, ?, ?, ?)';
      db.query(insertQuery, [username, email, hashedPassword, phone_number], (err, result) => {
        if (err) {
          console.error('Error saving user to database:', err);
          return res.status(500).send('Error saving user to database');
        }
        res.status(200).send('User registered successfully');
      });
    } catch (err) {
      console.error('Error hashing password:', err);
      res.status(500).send('Error hashing password');
    }
  });
});

app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  const query = 'SELECT * FROM users WHERE email = ?';

  db.query(query, [email], async (err, results) => {
    if (err) {
      console.error('Error fetching user from database:', err);
      res.status(500).send('Error fetching user from database');
      return;
    }

    if (results.length === 0) {
      res.status(401).send('Invalid email or password');
      return;
    }

    const user = results[0];
    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      res.status(401).send('Invalid email or password');
      return;
    }

    const token = jwt.sign({ id: user.id, username: user.username }, 'secret_key', { expiresIn: '1h' });

    res.status(200).json({ token });
  });
});

// GET active snipes
app.get('/api/snipes', authenticateToken, (req, res) => {
  const query = `
    SELECT s.course_code 
    FROM snipes s 
    JOIN user_snipes us ON s.id = us.snipe_id 
    WHERE us.user_id = ? AND us.status = ?`;

  db.query(query, [req.user.id, 'active'], (err, results) => {
    if (err) {
      console.error('Error fetching active snipes from database:', err);
      res.status(500).send('Error fetching active snipes from database');
      return;
    }
    res.status(200).json(results.map(row => row.course_code));
  });
});

// GET active snipe count
const getActiveSnipeCount = (userId) => {
  return new Promise((resolve, reject) => {
    const query = `
      SELECT COUNT(*) AS count 
      FROM user_snipes 
      WHERE user_id = ? AND status = ?`;
    db.query(query, [userId, 'active'], (err, results) => {
      if (err) {
        return reject(err);
      }
      resolve(results[0].count);
    });
  });
};

// GET inactive snipes
app.get('/api/snipes/inactive', authenticateToken, (req, res) => {
  const query = `
    SELECT s.course_code 
    FROM snipes s 
    JOIN user_snipes us ON s.id = us.snipe_id 
    WHERE us.user_id = ? AND us.status = ?`;

  db.query(query, [req.user.id, 'inactive'], (err, results) => {
    if (err) {
      console.error('Error fetching inactive snipes from database:', err);
      res.status(500).send('Error fetching inactive snipes from database');
      return;
    }
    res.status(200).json(results.map(row => row.course_code));
  });
});

// POST new snipe or reactivate existing snipe
app.post('/api/snipes', authenticateToken, async (req, res) => {
  const { courseCode } = req.body;
  const maxActiveSnipes = 3; // Set the maximum number of active snipes allowed

  try {
    // Check if the course code already exists in snipes table
    const checkQuery = `
      SELECT s.id, s.status 
      FROM snipes s 
      WHERE s.course_code = ?`;
    
    db.query(checkQuery, [courseCode], async (err, results) => {
      if (err) {
        console.error('Error checking existing snipes:', err);
        return res.status(500).send('Error checking existing snipes');
      }

      if (results.length > 0) {
        const snipeId = results[0].id;
        const snipeStatus = results[0].status;

        // Check if user already has a snipe with this course code
        const userSnipeQuery = `
          SELECT status 
          FROM user_snipes 
          WHERE user_id = ? AND snipe_id = ?`;
        
        db.query(userSnipeQuery, [req.user.id, snipeId], async (err, results) => {
          if (err) {
            console.error('Error checking user snipes:', err);
            return res.status(500).send('Error checking user snipes');
          }

          if (results.length > 0) {
            const status = results[0].status;
            if (status === 'active') {
              return res.status(400).send('Course code already added to active snipes');
            } else if (status === 'inactive') {
              return res.status(400).send('Course code already added to inactive snipes. Reactivate instead.');
            }
          }

          // Reactivate the snipe if it exists but is not active for the user
          const reactivateQuery = `
            INSERT INTO user_snipes (user_id, snipe_id, status) 
            VALUES (?, ?, 'active') 
            ON DUPLICATE KEY UPDATE status = 'active'`;
          
          db.query(reactivateQuery, [req.user.id, snipeId], (err) => {
            if (err) {
              console.error('Error reactivating course code:', err);
              return res.status(500).send('Error reactivating course code');
            }
            // Update the status in the snipes table
            const updateSnipeStatusQuery = `UPDATE snipes SET status = 'active' WHERE id = ?`;
            db.query(updateSnipeStatusQuery, [snipeId], (err) => {
              if (err) {
                console.error('Error updating snipe status:', err);
                return res.status(500).send('Error updating snipe status');
              }
              res.status(200).send('Course code reactivated successfully');
            });
          });
          return;
        });
        
      } else {
        // Proceed to add new snipe if not already added
        const activeSnipeCount = await getActiveSnipeCount(req.user.id);
        if (activeSnipeCount >= maxActiveSnipes) {
          return res.status(400).send('Maximum number of active snipes reached');
        }

        const insertQuery = 'INSERT INTO snipes (course_code, status) VALUES (?, ?)';
        const insertUserSnipeQuery = 'INSERT INTO user_snipes (user_id, snipe_id, status) VALUES (?, ?, ?)';

        db.query(insertQuery, [courseCode, 'active'], (err, result) => {
          if (err) {
            console.error('Error adding course code to database:', err);
            return res.status(500).send('Error adding course code to database');
          }

          const snipeId = result.insertId;

          db.query(insertUserSnipeQuery, [req.user.id, snipeId, 'active'], (err) => {
            if (err) {
              console.error('Error adding user snipe to database:', err);
              return res.status(500).send('Error adding user snipe to database');
            }
            res.status(200).send('Course code added successfully');
          });
        });
      }
    });
  } catch (err) {
    console.error('Error adding course code:', err);
    res.status(500).send('Error adding course code');
  }
});

// Example backend endpoint to check if course code exists
app.get('/api/class_codes/:courseCode', (req, res) => {
  const { courseCode } = req.params;
  const query = 'SELECT COUNT(*) AS count FROM class_codes WHERE class_code = ?';

  db.query(query, [courseCode], (err, results) => {
    if (err) {
      console.error('Error checking course code:', err);
      return res.status(500).json({ error: 'Internal Server Error' });
    }

    const exists = results[0].count > 0;
    res.json({ exists });
  });
});

// Deactivate snipe
app.put('/api/snipes/deactivate', authenticateToken, (req, res) => {
  const { courseCode } = req.body;

  // First, deactivate the snipe for the current user
  const updateUserSnipeQuery = `
    UPDATE user_snipes us
    JOIN snipes s ON us.snipe_id = s.id
    SET us.status = 'inactive'
    WHERE s.course_code = ? AND us.user_id = ?`;

  db.query(updateUserSnipeQuery, [courseCode, req.user.id], (err) => {
    if (err) {
      console.error('Error deactivating course code for user:', err);
      res.status(500).send('Error deactivating course code for user');
      return;
    }

    // Check if any other user has this snipe active
    const checkOtherUsersQuery = `
      SELECT COUNT(*) AS count 
      FROM user_snipes us
      JOIN snipes s ON us.snipe_id = s.id
      WHERE s.course_code = ? AND us.status = 'active' AND us.user_id != ?`;

    db.query(checkOtherUsersQuery, [courseCode, req.user.id], (err, results) => {
      if (err) {
        console.error('Error checking other users for course code:', err);
        res.status(500).send('Error checking other users for course code');
        return;
      }

      if (results[0].count === 0) {
        // If no other user has this snipe active, deactivate the snipe in the snipes table
        const deactivateSnipeQuery = `
           UPDATE snipes s
          SET s.status = 'inactive'
          WHERE s.course_code = ?`;

        db.query(deactivateSnipeQuery, [courseCode], (err) => {
          if (err) {
            console.error('Error deactivating course code in snipes table:', err);
            res.status(500).send('Error deactivating course code in snipes table');
            return;
          }
          res.status(200).send('Course code deactivated successfully');
        });
      } else {
        res.status(200).send('Course code deactivated successfully for user');
      }
    });
  });
});

// Reactivate snipe (change status to active)
app.put('/api/snipes/reactivate', authenticateToken, async (req, res) => {
  const { courseCode } = req.body;
  const maxActiveSnipes = 3; // Set the maximum number of active snipes allowed

  try {
    const activeSnipeCount = await getActiveSnipeCount(req.user.id);
    if (activeSnipeCount >= maxActiveSnipes) {
      return res.status(400).send('Maximum number of active snipes reached');
    }

    // Check if the snipe exists and is inactive in the snipes table
    const checkSnipeQuery = `
      SELECT s.id, s.status 
      FROM snipes s 
      WHERE s.course_code = ?`;

    db.query(checkSnipeQuery, [courseCode], (err, results) => {
      if (err) {
        console.error('Error checking snipe status:', err);
        return res.status(500).send('Error checking snipe status');
      }

      if (results.length > 0) {
        const snipeId = results[0].id;
        const snipeStatus = results[0].status;

        if (snipeStatus === 'inactive') {
          // Activate the snipe in the snipes table
          const activateSnipeQuery = `
            UPDATE snipes 
            SET status = 'active' 
            WHERE id = ?`;

          db.query(activateSnipeQuery, [snipeId], (err) => {
            if (err) {
              console.error('Error activating snipe in snipes table:', err);
              return res.status(500).send('Error activating snipe in snipes table');
            }

            // Reactivate the snipe for the user in the user_snipes table
            const updateUserSnipeQuery = `
              UPDATE user_snipes us
              SET us.status = 'active'
              WHERE us.snipe_id = ? AND us.user_id = ?`;

            db.query(updateUserSnipeQuery, [snipeId, req.user.id], (err) => {
              if (err) {
                console.error('Error reactivating course code for user:', err);
                return res.status(500).send('Error reactivating course code for user');
              }
              res.status(200).send('Course code reactivated successfully');
            });
          });
        } else {
          // Reactivate the snipe for the user in the user_snipes table
          const updateUserSnipeQuery = `
            UPDATE user_snipes us
            SET us.status = 'active'
            WHERE us.snipe_id = ? AND us.user_id = ?`;

          db.query(updateUserSnipeQuery, [snipeId, req.user.id], (err) => {
            if (err) {
              console.error('Error reactivating course code for user:', err);
              return res.status(500).send('Error reactivating course code for user');
            }
            res.status(200).send('Course code reactivated successfully');
          });
        }
      } else {
        res.status(400).send('Snipe not found');
      }
    });
  } catch (err) {
    console.error('Error fetching active snipe count:', err);
    res.status(500).send('Error fetching active snipe count');
  }
});


// GET user info
app.get('/api/users', authenticateToken, (req, res) => {
  const query = 'SELECT username, phone_number, email, password FROM users WHERE id = ?';

  db.query(query, [req.user.id], (err, results) => {
    if (err) {
      console.error('Error fetching user info from database:', err);
      res.status(500).send('Error fetching user info from database');
      return;
    }
    if (results.length === 0) {
      res.status(404).send('User not found');
      return;
    }
    res.status(200).json(results[0]);
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// PUT update phone number
app.put('/api/user/phone', authenticateToken, (req, res) => {
  const { phoneNumber } = req.body;

  // Check if the phone number is already in use
  const checkQuery = 'SELECT * FROM users WHERE phone_number = ?';
  db.query(checkQuery, [phoneNumber], (err, results) => {
    if (err) {
      console.error('Error checking phone number existence:', err);
      return res.status(500).send('Error checking phone number existence');
    }

    if (results.length > 0) {
      return res.status(409).json({ error: 'Phone number already exists. Please use a different phone number.' });
    }

    // If phone number is unique, update it
    const updateQuery = 'UPDATE users SET phone_number = ? WHERE id = ?';
    db.query(updateQuery, [phoneNumber, req.user.id], (err) => {
      if (err) {
        console.error('Error updating phone number:', err);
        return res.status(500).send('Error updating phone number');
      }
      res.status(200).send('Phone number updated successfully');
    });
  });
});

// PUT mark snipe as deleted
app.put('/api/snipes/delete', authenticateToken, async (req, res) => {
  const { courseCode } = req.body;

  try {
    const updateQuery = `
      UPDATE user_snipes us
      JOIN snipes s ON us.snipe_id = s.id
      SET us.status = ?
      WHERE s.course_code = ? AND us.user_id = ?`;

    db.query(updateQuery, ['deleted', courseCode, req.user.id], (err) => {
      if (err) {
        console.error('Error marking course code as deleted:', err);
        return res.status(500).send('Error marking course code as deleted');
      }
      res.status(200).send('Course code marked as deleted successfully');
    });
  } catch (err) {
    console.error('Error marking course code as deleted:', err);
    res.status(500).send('Error marking course code as deleted');
  }
});

// Example endpoint to fetch user data
app.get('/api/users', authenticateToken, (req, res) => {
  const userId = req.user.id; // Assuming you have userId in the JWT payload
  
  // Fetch user data based on userId
  db.query('SELECT username, email, phone_number FROM users WHERE id = ?', [userId], (err, results) => {
    if (err) {
      console.error('Error fetching user data:', err);
      return res.status(500).send('Error fetching user data');
    }
    if (results.length === 0) {
      return res.status(404).send('User not found');
    }
    const userData = results[0];
    res.status(200).json(userData);
  });
});


