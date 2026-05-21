# Recon Tool

Script de reconocimiento en Python para la fase inicial de un pentest. Automatiza la recopilación de información pública sobre un dominio objetivo.

## ¿Qué hace?

Dado un dominio, el script ejecuta tres análisis automáticamente:

1. **Búsqueda de subdominios** — consulta la API pública de crt.sh para encontrar todos los subdominios con certificado SSL registrado.
2. **Escaneo de puertos** — detecta puertos abiertos y los servicios que corren en ellos (FTP, SSH, HTTP, HTTPS, MySQL, entre otros).
3. **Extracción de metadatos** — busca archivos PDF públicos en el sitio y extrae su metadata: autor, software utilizado, fechas de creación y modificación.

Esta información ayuda al equipo de seguridad a mapear la superficie de ataque y detectar qué datos están expuestos públicamente.

## Requisitos

- Python 3.x
- Librerías: `requests`, `beautifulsoup4`, `pypdf`

## Instalación
```bash
git clone https://github.com/TEKASHi19/recon-tool.git
cd recon-tool
pip install requests beautifulsoup4 pypdf
```

## Uso
```bash
python recon.py
```

Ingresa el dominio cuando el script lo solicite:
```
Ingresa el dominio a analizar (ej: gruasslp.com): ejemplo.com
```

## Ejemplo de output
```
 Analizando: google.com
==================================================

[+] SUBDOMINIOS ENCONTRADOS
------------------------------
  → accounts.google.com
  → mail.google.com
  → drive.google.com
  ...

[+] ESCANEO DE PUERTOS
------------------------------
  IP: 192.178.56.142
   Puerto 80 (HTTP) — ABIERTO
   Puerto 443 (HTTPS) — ABIERTO

[+] METADATOS DE PDFs
------------------------------
  PDF: https://ejemplo.com/documento.pdf
    /Author: Juan Lopez
    /Creator: Microsoft Word 2010
    /CreationDate: 2023-04-15
```

