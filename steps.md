# Steps

## Show vulnerabilities

### Check SQL injection

1. Show database with password
2. Check user and incorrect password
3. Check user and password correct
4. Check user and password with SQL injection
5. Show Auth service

### Check unhashed password

1. Keep logs on web browser
2. Get password from logs when user logs in

## Show how to fix

### Fix SQL injection

1. Use ORM

### Fix unhashed password

1. Show database with hashed password
2. Hash password to compare
3. Do not send password to client when user logs in
