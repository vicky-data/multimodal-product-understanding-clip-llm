import openai

def generate_tags(context):
    prompt = f"""
    Generate product tags based on this context:
    {context}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
