from features.gmail_service import get_emails
from ai_engine import chat_ai


def summarize_email():
    try:
        emails = get_emails()

        if not emails:
            return "📭 No emails found"

        # Combine emails
        combined = "\n\n".join(emails[:10])  # limit for performance

        prompt = f"""
Summarize the following emails in clear bullet points:

{combined}

Give short and important summary only.
"""

        summary = chat_ai(prompt)

        return f"📩 Email Summary:\n\n{summary}"

    except Exception as e:
        return f"Email Error: {str(e)}"