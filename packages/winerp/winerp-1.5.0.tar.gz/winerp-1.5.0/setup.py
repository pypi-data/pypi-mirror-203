from setuptools import setup

extras = {
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions',
    ],
}

setup(
    name="winerp",
    version="1.5.0",
    description="Websocket based IPC for discord.py bots",
    long_description="""# winerp
An IPC based on Websockets. Fast, Stable, and easy-to-use, for inter-communication between your processes or discord.py bots.


### Key Features

 - **Fast** with minimum recorded response time being `< 2ms`
 - Lightweight, Stable and Easy to integrate.
 - No limitation on number of connected clients. 

## Installation
Stable:
```py
pip install -U winerp
```
Main branch (can be unstable/buggy):
```py
pip install git+https://www.github.com/BlackThunder01001/winerp
```

### Working:
This library uses a central server for communication between multiple clients. You can connect a large number of clients for sharing data, and data can be shared between any connected client.

1) Import the library:
```py
import winerp
```

2) Initialize winerp client:
```py
ipc_client = winerp.Client(local_name = "my-cool-app", port=8080)
```

3) Start the client:
```py
await ipc_client.start()
# or
asyncio.create_task(ipc_client.start())
```

- Registering routes:
```py
@ipc_client.route
async def route_name(source, user_name):
    return f"Hello {user_name}"
```

- Requesting data from another client:
```py
user_name = await ipc_client.request(route="fetch_user_name", source="another-cool-bot", user_id = 123)
```

- Sending *information* type data to other clients:
```py
data = [1, 2, 3, 4]
await ipc_client.inform(data, destinations=["another-cool-bot"])
```

## Example Usage:

Start the server on terminal using `$ winerp --port 8080`. You can also start the server using `winerp.Server`

### Client 1 (`some-random-bot`):
```py
import winerp
import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix="!", intents=discord.Intents.all())

bot.ipc = winerp.Client(local_name = "some-random-bot", port=8080)

@bot.command()
async def request(ctx):
    # Fetching data from a client named "another-bot" using route "get_some_data"
    data = await bot.ipc.request("get_some_data", source = "another-bot")
    await ctx.send(data)


@bot.ipc.route()
async def get_formatted_data(source, user_id = None):
    return f"<@{user_id}>"


@bot.ipc.event
async def on_winerp_ready():
    print("Winerp Client is ready for connections")

bot.loop.create_task(bot.ipc.start())
bot.run("TOKEN")
```

### Client 2 (`another-bot`)
```py
import winerp
import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix="?", intents=discord.Intents.all())

bot.ipc = winerp.Client(local_name = "another-bot", port=8080)

@bot.command()
async def format(ctx):
    # Fetching data from a client named "some-random-bot" using route "get_formatted_data"
    data = await bot.ipc.request("get_formatted_data", source = "some-random-bot", user_id = ctx.author.id)
    await ctx.send(data)


@bot.ipc.route()
async def get_some_data(source):
    return "You are very cool"


bot.loop.create_task(bot.ipc.start())
bot.run("TOKEN")
```

""",
    long_description_content_type="text/markdown",
    url="https://github.com/nouman0103/winerp",
    project_urls={
        "Bug Tracker": "https://github.com/nouman0103/winerp/issues",
        "Documentation": "https://winerp.readthedocs.io/en/latest/",
    },
    author="BlackThunder",
    author_email="nouman0103@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Typing :: Typed",
        
    ],
    packages=["winerp"],
    package_data={
     'winerp.lib': ['*'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'winerp=winerp.__main__:run',
            ]
        },
    install_requires=["websockets", "websocket-server", "orjson"],
    extra_requires=extras,
    python_requires=">=3.6",
)
