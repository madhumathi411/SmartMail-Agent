def assign_priority(email_text, intent):
    """
    Assign a priority level based on the email content and intent.
    """

    text = email_text.lower()

    urgent_words = [
        "urgent",
        "immediately",
        "as soon as possible",
        "security",
        "fraud",
        "charged twice"
    ]

    important_words = [
        "payment",
        "refund",
        "meeting",
        "document",
        "account"
    ]

    if any(word in text for word in urgent_words):
        priority = "Urgent"

    elif intent in ["Payment Issue", "Security Issue"]:
        priority = "Important"

    elif any(word in text for word in important_words):
        priority = "Important"

    else:
        priority = "Normal"

    return priority
