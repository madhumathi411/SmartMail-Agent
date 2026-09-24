def generate_response(intent, context, email_text):
    """
    Generate a basic response based on the email intent
    and retrieved context.
    """

    if intent == "Payment Issue":
        response = (
            "Hello,\n\n"
            "Thank you for contacting us regarding your payment issue. "
            "We have reviewed your request and will assist you with the "
            "necessary payment or refund process.\n\n"
            f"Information: {context}\n\n"
            "Best regards,\n"
            "SmartMail Support Team"
        )

    elif intent == "Meeting Request":
        response = (
            "Hello,\n\n"
            "Thank you for your meeting request. "
            "We will review the request and confirm a suitable time.\n\n"
            f"Information: {context}\n\n"
            "Best regards,\n"
            "SmartMail Support Team"
        )

    elif intent == "Document Request":
        response = (
            "Hello,\n\n"
            "Thank you for your request. "
            "We will help you with the requested document.\n\n"
            f"Information: {context}\n\n"
            "Best regards,\n"
            "SmartMail Support Team"
        )

    elif intent == "Security Issue":
        response = (
            "Hello,\n\n"
            "Thank you for reporting this security-related issue. "
            "Your request will be reviewed carefully by our support team.\n\n"
            f"Information: {context}\n\n"
            "Best regards,\n"
            "SmartMail Support Team"
        )

    else:
        response = (
            "Hello,\n\n"
            "Thank you for contacting SmartMail Support. "
            "We have received your enquiry and will review it shortly.\n\n"
            f"Information: {context}\n\n"
            "Best regards,\n"
            "SmartMail Support Team"
        )

    return response
