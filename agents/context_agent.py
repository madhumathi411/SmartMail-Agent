import json


def get_context(intent):
    """
    Retrieve useful information from the knowledge base
    based on the email intent.
    """

    try:
        with open("data/knowledge_base.json", "r") as file:
            knowledge_base = json.load(file)
    except FileNotFoundError:
        return "Knowledge base is not available."

    if intent == "Payment Issue":
        return (
            "Refunds are normally processed within "
            + knowledge_base["payment"]["refund_time"]
        )

    elif intent == "Document Request":
        return (
            "Standard documents can be requested through "
            "the customer support process."
        )

    elif intent == "Meeting Request":
        return (
            "Meeting requests should be handled during "
            + knowledge_base["support"]["hours"]
        )

    elif intent == "Security Issue":
        return (
            "Security-related emails should be reviewed "
            "carefully before sending a response."
        )

    else:
        return "No specific knowledge-base information was found."
