# Mechanical Bull

Mechanical Bull is an ActivityPub Client application build based on [bovine](https://codeberg.org/helge/bovine/). It's main goal is to provide a platform for automating activities undertaking in the FediVerse. Furthermore, it serves as a demonstration how ActivityPub Clients can be build with bovine.

## Installation

One can simply install mechanical_bull with pip via

```bash
pip install mechanical_bull
```

Once can then add a new user by running

```bash
python -m mechanical_bull.add_user
```

This will then ask you to enter a name, the hostname, your ActivityPub Actor lives on, then prompt you to add a new did:key to your ActivityPub Actor. This did:key will be used to authenticate mechanical_bull against your server. Once you have added the key, press enter, and mechanical_bull is running. This method of authentication is called Moo-Auth-1 and described [here](https://blog.mymath.rocks/2023-03-15/BIN1_Moo_Authentication_and_Authoriation).

The configuration is saved in `config.toml`. bovine also supports authentication through private keys and HTTP signatures. For the details on how to configure this, please consult bovine. You can add further automations there.

Then you should be able to run mechanical bull via

```bash
python -m mechanical_bull.run
```

## Writing automations

The examples of `mechanical_bull.actions.handle_follow_request` and `mechanical_bull.actions.log_to_file` should show how to write a new automation. The basic idea is that each file contains a function handle with signature

```python
async def handle(client: BovineClient, data: dict, **kwargs):
    return
```

here the kwargs are the dict given by the definiton in the handler block, i.e.

```toml
[user.handlers]
"my.package": { arg1 = "value1", arg2 = "value2 }
```
