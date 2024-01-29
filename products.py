import requests

def price_search(product):
    url = "https://api.mercadolibre.com/sites/MLB/search"
    
    params = {
        'q': product,
        'limit': 5  
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        
        resultados = response.json()['results']
        
        for resultado in resultados:
            print(f"product: {resultado['title']}")
            print(f"Preço: {resultado['price']} {resultado['currency_id']}")
            print(f"Link: {resultado['permalink']}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    product_desejado = input("Digite o nome do produto: ")
    price_search(product_desejado)
    

