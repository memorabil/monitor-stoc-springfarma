import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

# Pune aici link-ul exact al produsului tau
URL = "https://springfarma.com/produs-exemplu.html" 
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def check_stock():
    try:
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Cautam textul specific in pagina
        # La Springfarma, de obicei apare un div cu clasa 'stock'
        page_text = soup.get_text().lower()
        
        if "în stoc" in page_text:
            status = "DISPONIBIL"
        else:
            status = "LIPSA STOC"
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        log_entry = f"{timestamp}, {status}\n"
        
        # Salvam rezultatul intr-un fisier
        with open("istoric_stoc.csv", "a") as f:
            f.write(log_entry)
            
        print(f"Verificare reusita: {status}")
        
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    check_stock()
