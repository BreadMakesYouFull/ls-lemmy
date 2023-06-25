# ls-lemmy-subs

List lemmy subscriptions for backup sharing or creating a bespoke feed

# Usage

```
ls-lemmy-subs.py [-h] instance username

Export lemmy subscriptions Login as user and export subscriptions. Could be useful incase your instance goes down, to share with another user, or to create a
bespoke feed.

positional arguments:
  instance    Lemmy instance URL
  username    Username

options:
  -h, --help  show this help message and exit
```

Example:

```
./ls-lemmy-subs.py http://lemmy.world myusername
# prompted for password
# Logs list of subscription URLs alphabetically by community name.
```
