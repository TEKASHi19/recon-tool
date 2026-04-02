import requests
import socket
import json
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io

def extraer_metadatos(dominio):
    print("\n[+] METADATOS DE PDFs")
    print("-" * 30)
    
    try:
        url_sitio = f"https://{dominio}"
        respuesta = requests.get(url_sitio, timeout=10)
        soup = BeautifulSoup(respuesta.text, "html.parser")
        
        enlaces_pdf = []
        for enlace in soup.find_all("a", href=True):
            href = enlace["href"]
            if href.endswith(".pdf"):
                if href.startswith("http"):
                    enlaces_pdf.append(href)
                else:
                    enlaces_pdf.append(f"{url_sitio}/{href}")
        
        if not enlaces_pdf:
            print("  No se encontraron PDFs públicos")
            return
        
        for url_pdf in enlaces_pdf:
            print(f"\n  PDF: {url_pdf}")
            respuesta_pdf = requests.get(url_pdf, timeout=10)
            pdf = PdfReader(io.BytesIO(respuesta_pdf.content))
            meta = pdf.metadata
            
            if meta:
                for clave, valor in meta.items():
                    print(f"    {clave}: {valor}")
            else:
                print("    Sin metadatos disponibles")
                
    except Exception as e:
        print(f"  Error: {e}")

def escanear_puertos(dominio):
    print("\n[+] ESCANEO DE PUERTOS")
    print("-" * 30)
    
    puertos = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt"
    }
    
    try:
        ip = socket.gethostbyname(dominio)
        print(f"  IP: {ip}\n")
        
        for puerto, servicio in puertos.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((ip, puerto))
            if resultado == 0:
                print(f"  ✅ Puerto {puerto} ({servicio}) — ABIERTO")
            sock.close()
            
    except Exception as e:
        print(f"  Error: {e}")


def buscar_subdominios(dominio):
    print("\n[+] SUBDOMINIOS ENCONTRADOS")
    print("-" * 30)
    
    url = f"https://crt.sh/?q=%.{dominio}&output=json"
    
    try:
        respuesta = requests.get(url, timeout=10)
        datos = json.loads(respuesta.text)
        
        subdominios = set()
        for entrada in datos:
            nombre = entrada["name_value"]
            for sub in nombre.split("\n"):
                subdominios.add(sub.strip())
        
        for sub in sorted(subdominios):
            print(f"  → {sub}")
            
    except Exception as e:
        print(f"  Error: {e}")

def main():
    dominio = input("Ingresa el dominio a analizar (ej: gruasslp.com): ").strip()
    print(f"\n🔍 Analizando: {dominio}\n")
    print("=" * 50)
    
    buscar_subdominios(dominio)
    escanear_puertos(dominio)
    extraer_metadatos(dominio)
    

if __name__ == "__main__":
    main()

