import os
import requests
import datetime


def parse_slack_message(message):
    message_to_return = "Today, you have:"
    for obj_ in message:
        message_to_return = message_to_return + f"\n- Performed {obj_} {message[obj_]} time(s)"
    return message_to_return


github_action = os.getenv("GITHUB_EVENT_NAME", "five")
github_user = os.getenv("GITHUB_ACTOR", "four")
slack_webhook_url = os.getenv("INPUT_SLACKURL")

url = "https://nswxbizgc7.execute-api.eu-west-1.amazonaws.com/prod/actions/"
request_body = {"userName": github_user, "triggeredBy": github_action}
response = requests.post(url=url, json=request_body)

slack_message = {}
if response.status_code == 200:
    all_actions = requests.get(url=url + github_user).json()
    todays_date = str(datetime.date.today())
    for obj in all_actions:
        if todays_date in obj['datePerformed']:
            triggered_by = obj['triggeredBy']
            if triggered_by in slack_message:
                slack_message[triggered_by] = slack_message[triggered_by] + 1
            else:
                slack_message[triggered_by] = 1

message_to_send = parse_slack_message(slack_message)
slack_obj = {'text': message_to_send}
requests.post(url=slack_webhook_url, json=slack_obj)
