from generator import generate_notice_pdf

def simulate_detection():
    print("🔍 Simulating BharatShield Detection...")
    
    # Fake data that would come from your ML model
    mock_data = {
        "case_id": "BS-2026-9981",
        "platform": "X (formerly Twitter)",
        "url": "https://social-platform.com/v/12345",
        "confidence_score": 98.4
    }
    
    print(f"⚠️ Deepfake detected with {mock_data['confidence_score']}% confidence!")
    
    # Trigger the legal automation
    path = generate_notice_pdf(
        case_id=mock_data["case_id"],
        platform_name=mock_data["platform"],
        video_url=mock_data["url"],
        confidence=mock_data["confidence_score"],
    )
    
    print(f"📄 Legal document generated at: {path}")

if __name__ == "__main__":
    simulate_detection()
