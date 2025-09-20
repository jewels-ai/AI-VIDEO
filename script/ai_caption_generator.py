import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_ad_text(product, occasion, audience):
    prompt = f"""
    You are a luxury jewellery ad copywriter. Write 2 short captions, 2 long captions, 
    3 ad copy variations, a 10-15 sec video script, and 10 hashtags for this jewellery:

    Product: {product}
    Occasion: {occasion}
    Audience: {audience}
    Style: Emotional + festive + luxury
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()
