from google_sheet_connect import get_form_responses
from ai_caption_generator import generate_ad_text
from video_creator import create_video
from upload_to_drive import upload_to_drive

import os

df = get_form_responses()

for index, row in df.iterrows():
    product = row['Product Name']
    occasion = row['Occasion']
    audience = row['Target Audience']
    image_path = row['Uploaded Image Path']  # Make sure to download from Drive

    # Generate captions + video script
    ad_text = generate_ad_text(product, occasion, audience)

    # Create video
    output_file = f"outputs/videos/{product.replace(' ','_')}.mp4"
    create_video(image_path, ad_text, output_path=output_file)

    # Upload to Google Drive
    link = upload_to_drive(output_file)
    print(f"Video ready for {product}: {link}")
