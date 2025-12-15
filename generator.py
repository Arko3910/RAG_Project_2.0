def generate_answer(query, context):
    if context:
        return f"Based on documents: {context[0]}"
    return "No relevant document found. This is a general response."
