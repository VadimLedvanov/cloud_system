import requests
import time


BACKEND_HOST = 'backend'  
BACKEND_PORT = 8080  

def main():
    while True:
        try:
            print("Отправка запроса к backend...")
            response = requests.get(f'http://{BACKEND_HOST}:{BACKEND_PORT}/')
            print(f"Ответ от backend: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к backend: {e}")
        time.sleep(5)  

if __name__ == "__main__":
    main()
