# pyteams
`pyteams` makes it possible to send messages to Teams channels through python scripts, automating or semi-automating the task.
`pyteams` is a module wrapping the `pymsteams` library, for easier useability and error detection.
It only supports the basic functionality of `pymsteams`, and for more advanced usecases, please see that documentation.

# How to use
To use `pyteams` you have to make a connector in the  Teams channels you want to send messages to, following these steps:
- Right click the channel you want, and press "Connectors"
- Search for the "WebHook" connector, and add it to the channel
- Go to connectors again and choose Webhooks "Configure"
- Give the connection a name (for instance "python") and upload a relevant image.
- Save the connection, and COPY THE URL, specifying the path to the connector

You now have a working webhook, through the copied URL, that can be accessed by pyteams.
To use `pyteams` to make a simple message

```python
    from pyteams import teams_message

    list_of_connections = ["<Your Connector Url>"]
    text = "Some message you want to send"
    teams_message(list_of_connections, text, send=True)
```

The message should now be sent to your teams channel, showing the chosen image from before as the sender.

## Parameters
`pyteams` does presently support the following parameters, called in the following way:

```python
    teams_message(
        connections: List(url),
        text: string,
        send: bool,
        title: string,
        link_txt: string,
        link_url: url,
        color: hex_color
    )
```

- `connections` is mandatory, and contains all the connector urls (set to a Teams Channel) you want to send the message to. All connectors will receive the exact same message.
- `text` is the message you want to send.
- `send` if set to `True` will send the message, otherwise will print the output as a preview of the message to the console. 
Defaults to `False`.
- `title` is optional, and gives the message a title
- `link_txt` is optional, and creates a link_txt. If no `link_url` is specified, the `link_txt` will not be used.
- `link_url` is optional, and specifies any given url. If no `link_txt` is specified, the `link_url` will not be used.
- `color` is optional and specifies the color of the message, and must use a valid hex colouring code, ie. #FF0000 for red for instance.

