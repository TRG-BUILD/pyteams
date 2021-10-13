import pytest
from unittest.mock import call, patch, MagicMock
from .pyteams import teams_message

@patch("pyteams.pyteams.pymsteams")
@pytest.mark.parametrize("channels",[
    (["First Channel"]),
    (["First Channel", "Second Channel"]),
    (["First Channel", "Second Channel", "Third Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel", "Sixth Channel"]),
])
def test_pyteams_can_send_a_basic_message_to_any_amount_of_connectors(mock_pymsteams, channels):
    mock_message = MagicMock()
    mock_message.send.return_value = MagicMock()
    mock_message.text.return_value = MagicMock()
    mock_message.title.return_value = MagicMock()
    mock_message.addLinkButton.return_value = MagicMock()
    mock_message.color.return_value = MagicMock()

    mock_pymsteams.connectorcard.return_value = mock_message
    channels = channels
    expected_init_channel = channels[0]
    expected_channel_amount = len(channels)
    msg = "This message was sent from python"
    send = True,

    teams_message(channels, msg, send)

    mock_pymsteams.connectorcard.assert_called_once_with(expected_init_channel)
    assert expected_channel_amount == mock_message.send.call_count
    mock_message.text.assert_called_with(msg)
    assert not mock_message.title.called
    assert not mock_message.addLinkButton.called
    assert not mock_message.color.called


@patch("pyteams.pyteams.pymsteams")
@pytest.mark.parametrize("channels",[
    (["First Channel"]),
    (["First Channel", "Second Channel"]),
    (["First Channel", "Second Channel", "Third Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel", "Sixth Channel"]),
])
def test_pyteams_can_send_a_full_message_to_any_amount_of_connectors(mock_pymsteams, channels):
    mock_message = MagicMock()
    mock_message.send.return_value = MagicMock()
    mock_message.text.return_value = MagicMock()
    mock_message.title.return_value = MagicMock()
    mock_message.addLinkButton.return_value = MagicMock()
    mock_message.color.return_value = MagicMock()

    mock_pymsteams.connectorcard.return_value = mock_message
    channels = channels
    expected_init_channel = channels[0]
    expected_channel_amount = len(channels)
    msg = "This message was sent from python"
    send = True,
    title = "This is a title"
    color = "#FF0000"
    link_txt = "This is a link txt"
    link_url = "https://github.com/TRG-BUILD/pyteams"

    teams_message(channels, msg, send, title=title,color=color,link_txt=link_txt, link_url=link_url)

    mock_pymsteams.connectorcard.assert_called_once_with(expected_init_channel)
    assert expected_channel_amount == mock_message.send.call_count
    mock_message.text.assert_called_with(msg)
    mock_message.title.assert_called_with(title)
    mock_message.color.assert_called_with(color)
    mock_message.addLinkButton.assert_called_with(link_txt, link_url)

@patch("pyteams.pyteams.pymsteams")
@pytest.mark.parametrize("channels",[
    (["First Channel"]),
    (["First Channel", "Second Channel"]),
    (["First Channel", "Second Channel", "Third Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel"]),
    (["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel", "Sixth Channel"]),
])
def test_pyteams_wont_send_message_if_not_set_actively_to_do_it(mock_pymsteams, channels):
    mock_message = MagicMock()
    mock_message.send.return_value = MagicMock()
    mock_pymsteams.connectorcard.return_value = mock_message
    channels = channels
    msg = "This message was sent from python"

    teams_message(channels, msg)

    mock_pymsteams.connectorcard.assert_called_once_with("First Channel")
    assert 0 == mock_message.send.call_count

@patch("pyteams.pyteams.pymsteams")
def test_pyteams_sends_to_each_specified_channel(mock_pymsteams):
    mock_message = MagicMock()
    mock_message.send.return_value = MagicMock()
    mock_message.newHookUrl.return_value = MagicMock()

    mock_pymsteams.connectorcard.return_value = mock_message
    channels = ["First Channel", "Second Channel", "Third Channel", "Fourth Channel", "Fifth Channel", "Sixth Channel"]
    expected_init_channel = channels[0]
    msg = "This message was sent from python"
    send = True

    teams_message(channels, msg, send)

    mock_pymsteams.connectorcard.assert_called_once_with(expected_init_channel)
    mock_message.newHookUrl.assert_has_calls([
        call("Second Channel"),
        call("Third Channel"),
        call("Fourth Channel"),
        call("Fifth Channel"),
        call("Sixth Channel"),
    ])