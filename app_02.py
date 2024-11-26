import requests
from bs4 import BeautifulSoup

url_iphone = (
    "https://www.mercadolivre.com.br/apple-iphone-16-pro-512-gb-titnio-"
    "natural-distribuidor-autorizado/p/MLB1040287844?pdp_filters=item_id:"
    "MLB3845989489#is_advertising=true&searchVariation=MLB1040287844&position"
    "=1&search_layout=stack&type=pad&tracking_id=68d3f446-0b8a-4b4b-b334-"
    "a51ddd4a5938&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1"
    "&ad_click_id=NWMxMzU0ZGQtNmVlMC00OTA5LTk4YjEtNzJlMDYzMTUxMGE2"
)

def fetch_page(url):
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_= 'ui-pdp-title').get_text()
    prices = soup.find_all('span', class_ = 'andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', ''))
    new_price: int = int(prices[1].get_text().replace('.', ''))
    installment_price: int = int(prices[2].get_text().replace('.', ''))
    #cents = soup.find('span', class_= 'andes-money-amount__cents').get_text()
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price
    }

if __name__ == '__main__':
    page_content = fetch_page(url_iphone)
    product_info = parse_page(page_content)
    print(product_info)