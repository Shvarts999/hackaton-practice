CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100), email VARCHAR(100) UNIQUE);
INSERT INTO users (name, email) VALUES ('Алиса', 'alice@test.com'), ('Борис', 'boris@test.com') ON CONFLICT (email) DO NOTHING;
