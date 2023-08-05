import os
import tomllib
import tomli_w

from bovine.crypto import generate_ed25519_private_key, private_key_to_did_key


def main():
    config_file = "config.toml"

    print(f"Adding new user to {config_file}")

    if os.path.exists(config_file):
        with open(config_file, "rb") as fp:
            config = tomllib.load(fp)
        userlist = ", ".join(config.keys())
        print(f"Curent users: {userlist}")
    else:
        config = {}

    print()
    print("Setting up bovine")
    user = input("Please enter a name for the new entry:")

    if user in config:
        print(f"ERROR: {user} already exists in {config_file}")
        exit(1)

    host = input("Please enter your host name: ")
    print()
    private_key = generate_ed25519_private_key()
    did_key = private_key_to_did_key(private_key)

    print(f"Please add {did_key} to the access list of your ActivityPub actor")

    config[user] = {"private_key": private_key, "host": host, "handlers": {}}

    with open(config_file, "wb") as fp:
        tomli_w.dump(config, fp)

    print()
    print("Please note the handlers for this user are currently empty.")
    print("To automatically accept follow requests include the block")
    print(
        f"""[{user.handlers}]
"mechanical_bull.actions.handle_follow_request"]] = true"""
    )


if __name__ == "__main__":
    main()
