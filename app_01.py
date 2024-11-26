import requests

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
    print(response.text)

if __name__ == '__main__':
    page_content = fetch_page(url_iphone)
    print(page_content)