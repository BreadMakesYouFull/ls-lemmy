# ls-lemmy

List lemmy communities and subscriptions.

# Usage

```
usage: ls-lemmy [-h] instance [username]

List lemmy communities for an instance, or login to view your subscriptions.

positional arguments:
  instance    Lemmy instance URL
  username    Username

options:
  -h, --help  show this help message and exit
```

Example:

```
./ls-lemmy http://lemmy.world
# Logs list communities belonging to that instance

./ls-lemmy http://lemmy.world myusername
# prompted for password
# Logs list of subscription URLs alphabetically by community name.
```
