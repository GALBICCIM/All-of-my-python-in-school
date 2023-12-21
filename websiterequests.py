from requests import get


websites = (
    "https://instagram.com",
    "https://tiktok.com",
    "youtube.com",
    "facebook.com",
    "https://discord.com",
    "google.com"
)


results = {}


for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    
    response = get(website)
    
    if response.status_code == 200:
        results[website] = "OK"
        
    else:
        results[website] = "FAILED"
        
print(results)