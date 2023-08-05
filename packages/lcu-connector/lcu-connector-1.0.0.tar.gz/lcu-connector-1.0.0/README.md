# LCU Connector

This library serves to make the connection with the League Client API in a simple way, although there are others, such as [lcu-driver](https://github.com/sousa-andre/lcu-driver) (which by the way is very good), but with lcu-driver, for example, I couldn't work and structure my code the way I wanted it to, so I decided to make my own wrapper.


## Quick start
I will be brief in the explanation but I guarantee that it will be enough, as this library is simple to use. Among other things, I'm working on more elaborate documentation.

So, hand in the dough! Or rather, on the keyboard...


### Installation
Just use pip and it's fine.
```powershell
pip install lcu-connector
```

### How to use
Import the `Connector` from the `lcu_connector` module, instantiate it and start the session via the `.start()` method or passing the `start=True` parameter directly in the instance.
```python
from lcu_connector import Connector

# Method 01
conn = Connector(start=True)

# Method 02
conn = Connector()
conn.start()
```

Now have fun, the `Connector` object has the same attributes as the `requests` library and derivatives.
```python
from lcu_connector import Connector

conn = Connector(start=True)

# Getting the data of the currently connected summoner
res = conn.get('/lol-summoner/v1/current-summoner')
print(res.json())

# Getting a summoner's data by name
summoner_name = 'JohnDoe'
res = conn.get('/lol-summoner/v1/summoners?name={summoner_name}')
print(res.json())

# Performing POST request
data = {
    'foo': 'bar'
}
res = conn.post('API_URL', data=data)
if res.status_code == 200:
    do_something()

conn.stop()
```

You can see all available links for League Client through [LCU Explorer](https://github.com/HextechDocs/lcu-explorer).


## To-do
- [ ] API event watcher
- [ ] Built-in functions for commonly used tasks (like a get_summoner_by_name())
- [ ] More detailed documentation
