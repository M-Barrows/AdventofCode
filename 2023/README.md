# 2023

## Getting Started
Before you get started, you will need to copy your session token from adventofcode.com. To do so, you'll need to log into AoC and then open the developer tools (F12). Then, under the newtwork tab, view the GET request for file `/`. In the Cookies section, there should be a `session` cookie. Copy that value and enter it in a .env file under this directory labeled as `AOC_SESSION=<yourtokenhere>`

Now, you can create a virtual environment, activate it, and install the necessary packages: 

```bash
python3 -m virtualenv .venv
source ./.venv/bin/activate
pip3 install -r ./requirements.txt
```

Once this is complete, you should be able to run any of the scripts under this 2023 directory! 