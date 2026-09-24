def analyze_email(email_text):
    """
    Analyze an email and return a basic summary and intent.
    """

    text = email_text.lower()

    if "payment" in text or "charged" in text or "refund" in text:
        intent = "Payment Issue"

    elif "meeting" in text or "schedule" in text:
        intent = "Meeting Request"

    elif "document" in text or "file" in text:
        intent = "Document Request"

    elif "security" in text or "password" in text:
        intent = "Security Issue"

    else:
        intent = "General Enquiry"

    summary = email_text[:150]

    return {
        "intent": intent,
        "summary": summary
    }
