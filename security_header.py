import requests

# membuat fungsi terlebih dahulu
def detect_security_headers(): 
    url = input("Masukkan URL: ") # meminta input user
    response = requests.get(url) # mengambil respon dari url yang di berikan user

    if response.status_code == 200: # jika respone 200 akan melanjutkan perintah di bawah
        headers = response.headers # akan mengambil respon header
        security_headers = { # membuat dictionary dari security header
            "X-Frame-Options": "X-Frame-Options header not found",
            "Strict-Transport-Security": "Strict-Transport-Security header not found",
            "Content-Security-Policy": "Content-Security-Policy header not found",
            "X-Content-Type-Options": "X-Content-Type-Options header not found",
            "Referrer-Policy": "Referrer-Policy header not found",
            "Permissions-Policy": "Permissions-Policy header not found"
        }

        for header_name in security_headers: # untuk  header name di security headers
            if header_name in headers: # jika header name ada di variable headers di atas maka
                security_headers[header_name] = headers[header_name] #  melakukan looping  apakah security header ada di  di resepon
            else:
                security_headers[header_name] = "vuln" # jika tidak ada makan berarti Vuln

        for header_name, header_value in security_headers.items(): # mencetak hasil dari looping
            print(f"{header_name}: {header_value}")  # akan mencetak   hasilnya

    else:
        print("Failed to retrieve the URL.")

if __name__ == "__main__": # jika di di code menemukan  code  sperti di bawahnya maka  itu yang akan duluan di  jalankan
    detect_security_headers()
