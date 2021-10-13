import pymsteams

def teams_message(channel_list, message,send=False,title=None, link_txt=None,link_url=None, color=None):
    teams_msg = None
    teams_msg = pymsteams.connectorcard(channel_list.pop(0))

    # Setup Message
    teams_msg.text(message)
    if title:
        teams_msg.title(title)
    if link_txt or link_url:
        if link_txt and link_url:
            teams_msg.addLinkButton(link_txt, link_url)
        elif link_txt:
            print("You didn't give a link_url, and therefore the link text was skipped")
        else:
            print("You didn't give a link_txt, and therefore the link url was skipped")
    if color:
        teams_msg.color(color)

    # Send Message
    if send:
        teams_msg.send()
    else:
        print("This is a preview of the message(s) send to the connector(s)\nTo send the message, pass the parameter 'send=True':\n")
        teams_msg.printme()
    for url in channel_list:
        teams_msg.newHookUrl(url)
        if send:
            teams_msg.send()
        else:
            teams_msg.printme()

if __name__ == '__main__':

    channels = ["First Channel"]
    msg = "This message was sent from python"
    title = "This is a title"
    color = "#FF0000"
    link_txt = "This is a link txt"
    link_url = "https://github.com/TRG-BUILD/pyteams"
    teams_message(channels, msg, title=title,color=color,link_txt=link_txt, link_url=link_url)