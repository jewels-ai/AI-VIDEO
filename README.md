# AI Ad Agent (Zero-Cost Version)

This project allows jewellery retailers to generate AI-based social media ad videos automatically from product images uploaded via Google Form.

## Features
- Generate captions, ad copy, hashtags, and video script using AI
- Create 10-15 sec video ads from uploaded images
- Overlay text + background music
- Upload final videos to Google Drive and share link

## Setup
1. Install Python packages: `pip install -r requirements.txt`
2. Setup Google API service account and share your Google Sheet
3. Replace placeholders in scripts with your Sheet name and API keys
4. Place sample images in `sample_images/` and music in `sample_music/`
5. Run `main.py` to process new form submissions
