# pyteams
pyteams makes it possible to send messages to Teams channels through python scripts, automating or semi-automating the task.
pyteams is a module wrapping the pymsteams library, for easier useability and error detection.
It only supports the basic functionality of pymsteams, and for more advanced usecases, please see that documentation.

# How to use
To use pyteams you have to make a connector in the  Teams channels you want to send messages to, following these steps:
- Right click the channel you want, and press "Connectors"
- Search for the "WebHook" connector, and add it to the channel
- Go to connectors again and choose Webhooks "Configure"
- Give the connection a name (for instance "python") and upload a relevant image.
- Save the connection, and COPY THE URL, specifying the path to the connector

You now have a working webhook, through the copied URL, that can be accessed by pyteams.

