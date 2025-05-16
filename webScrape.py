import requests, re, sys
from bs4 import BeautifulSoup

def isActive(url: str) -> bool:
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    if not re.match(r'^https?://\S+\.\S+', url):
        return False
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def parse_onion(url: str): 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("article")
    if container is not None:
        headline = container.find("h1")
        if headline:
            print(headline.get_text(strip=True))
        content = container.find_all("p")
        for p in content[:10]:
            print(p.get_text(strip=True))
    else:
        print("Error: Could not find article")

def parse_vn(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("div")
    if container is not None: 
        headline = container.find("h1")
        if headline:
            print(headline.get_text(strip=True))
        content = container.find_all("p")
        for p in content[:10]:
            print(p.get_text(strip=True))
    else:
        print("Error: Could not find article content")

def main():
    if len(sys.argv) < 2:
        print("Usage: python webScrape.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    if not isActive(url):
        print("Error: Invalid or unreachable URL")
        sys.exit(1)

    if "nhandan.vn" in url:
        parse_vn(url)
    elif "theonion.com" in url or "cnn.com" in url:
        parse_onion(url)
    else:
        print("Error: Unsupported site")

if __name__ == '__main__':
    main()
