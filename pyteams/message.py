import pymsteams

def message(channel_list, message,title=None, link_txt=None,link_url=None, color=None):
    teams_msg = None
    teams_msg = pymsteams.connectorcard(channel_list.pop(0))
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


    teams_msg.printme()
    for url in channel_list:
        teams_msg.newHookUrl(url)
        print(teams_msg.printme())

if __name__ == '__main__':
    channels = ["https://aaudk.webhook.office.com/webhookb2/29bf0ebf-e12e-4f34-a06e-48e1ffbf86b1@f5dbba49-ce06-496f-ac3e-0cf14361d934/IncomingWebhook/9fce1787450e4178b4146b8fd9d08294/b65bd886-d940-47e5-bdb5-8b7ef2fb58ef"]
    msg = "This message was sent from python"
    message(channels, msg)