# script/test_run.py
from ai_caption_generator import generate_ad_text
from video_creator import create_video

def test_run():
    # Sample jewellery details
    product = "Gold Necklace with Ruby Stones"
    occasion = "Wedding"
    audience = "Young brides"

    # 1. Generate AI ad text
    print("📝 Generating ad text...")
    ad_text = generate_ad_text(product, occasion, audience)
    print("\nGenerated Ad Text:\n", ad_text)

    # 2. Create video with sample image + music
    print("\n🎥 Creating video...")
    image_path = "sample_images/demo_jewellery.jpg"
    music_path = "sample_music/background.mp3"
    output_file = "outputs/videos/demo_test.mp4"

    video_path = create_video(image_path, ad_text, music_path, output_file)

    print(f"\n✅ Test complete! Video saved at: {video_path}")

if __name__ == "__main__":
    test_run()
