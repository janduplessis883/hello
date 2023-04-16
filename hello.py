import sys

name = sys.argv[1]
print(f"Hello {name}!")

import requests

# set the webhook URL
webhook_url = "https://webhook.site/17e559da-239f-4d7f-bfde-021edc1cb370"

# set the name to use in the message
name = "John"

# send the message via webhook
requests.post(webhook_url, data={"output-text": f"Hello {name}!"})
