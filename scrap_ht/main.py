from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests


with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


def select_store(store_address: str, headers: dict) -> str:
    response = requests.get(url=store_address, headers=headers, verify=False)
    if response.status_code == 200:
        return store_address
    else:
        print('Error in selecting store. Please check the URL and try again.')
        return None

print(proxies, '-=-=-=-=-=-=-=-=--=--=-==--=')
def parse_category(base_url, full_url, headers, proxies, output_file: str) -> list:
    products = []
    print(base_url)
    sites_to_check = [
        full_url,
        full_url,
        full_url,
        full_url
    ]

    counter = 0

    with open(output_file, 'w', encoding='utf-8') as file:
        for site in sites_to_check:
            try:
                print('using the proxy:', proxies[counter])
                res = requests.get(site, proxies={
                    'http': proxies[counter],
                    'https': proxies[counter]
                }, headers=headers
                                   )
                if res.status_code == 200:
                    file.write(f"Содержимое сайта {site}:\n\n")
                    file.write(res.text + '\n\n')
                    print(f"Данные успешно записаны в {output_file}")

                    print(res.status_code)
            except:
                print('Failed!')
            finally:
                counter += 1
    return products



def get_next_filename(directory: str, base_name: str, extension: str) -> str:
    """Returns the next available filename in the specified directory."""
    index = 1
    while True:
        filename = f'{base_name}_{index}{extension}'
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        index += 1

# @click.command()
# @click.argument('source', type=click.Path(exists=True))
def main_func(base_url, category=''):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.txt'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    output_file = 'output_files/parsed_data.txt'

    base_url = base_url
    full_url = f'{base_url}/{category}'
    products = parse_category(base_url, full_url, headers, proxies, output_file)
    next_filename = get_next_filename(output_directory, base_name, extension)

    # ++++++++++++++++++++++ good write to file sample_1.txt ++++++++++++++++++++++++++++++++
    # with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
    #     for product in products:
    #         file.write(f"{product['name']}: {product['price']}\n")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # current_url = select_store(store_address, headers)
    #
    # if current_url:
    #     full_url = f'{current_url}/{category}'
    #
    #     products = parse_category(full_url, headers)
    #
    #     next_filename = get_next_filename(output_directory, base_name, extension)
    #
    #     # with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
    #     #     for product in products:
    #     #         file.write(product + '\n')
    #

if __name__ == '__main__':
    base_url = 'https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/'
    category = 'khudozhestvennaia-literatura'

    # base_url = 'https://www.okeydostavka.ru/msk'
    # category = 'kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura'      # Ваша категория товаров


    main_func(base_url, category)



'''



kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura

https://www.okeydostavka.ru/msk




https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura


https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura

#facet:&productBeginIndex:72&orderBy:2&pageView:grid&minPrice:69.99&maxPrice:4499.0&pageSize:72&



https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura



https://samokat.ru/category/90b0e15a-208c-4264-ac00-07b9cff26bba 

<a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/0be3ca72-f384-4303-8c41-16822b6e4e93"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Самокат</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/c0c38b5f-b2b9-4190-9fa3-1b4e4b1c5c6b"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Орехи</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/53008738-e6cd-4845-a991-d7152c5a7342"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Ореховые смеси</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/7add6704-b73f-4f00-a3ad-236fceabd64e"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Семечки</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/8570cc74-288f-4208-b4a8-f08ec8da67db"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Сухофрукты и цукаты</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/6299e6e8-a995-4eca-a39f-8d5e51dd3711"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Фруктовые чипсы</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/9f808b29-723d-4510-9839-106449fef56d"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Овощные чипсы</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/2023eb42-664c-4b84-99d3-b0ae0a37a20b"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Нутовые и злаковые чипсы</span></a><div data-tid="button" class="_button--size_s_10nio_100 _button--theme_secondary_10nio_51"><button class="_control_10nio_4 CategoryTagsList_showAllButton__CkfYG"><span class="_content_10nio_30"><span class="_center_10nio_36"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97 _text_10nio_43">+2</span></span></span></button></div>


/html/body/div/section/main/div[2]/div/div/div[2]/div[1]

<div class="CategoryTagsList_root__VSoO0"><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/0be3ca72-f384-4303-8c41-16822b6e4e93"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Самокат</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/c0c38b5f-b2b9-4190-9fa3-1b4e4b1c5c6b"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Орехи</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/53008738-e6cd-4845-a991-d7152c5a7342"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Ореховые смеси</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/7add6704-b73f-4f00-a3ad-236fceabd64e"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Семечки</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/8570cc74-288f-4208-b4a8-f08ec8da67db"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Сухофрукты и цукаты</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/6299e6e8-a995-4eca-a39f-8d5e51dd3711"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Фруктовые чипсы</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/9f808b29-723d-4510-9839-106449fef56d"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Овощные чипсы</span></a><a class="CategoryLink_root__SrUi8 CategoryTagsList_link__V_zUd" href="/category/2023eb42-664c-4b84-99d3-b0ae0a37a20b"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97">Нутовые и злаковые чипсы</span></a><div data-tid="button" class="_button--size_s_10nio_100 _button--theme_secondary_10nio_51"><button class="_control_10nio_4 CategoryTagsList_showAllButton__CkfYG"><span class="_content_10nio_30"><span class="_center_10nio_36"><span data-tid="text" class="_text_7xv2z_4 _text--type_p2SemiBold_7xv2z_97 _text_10nio_43">+2</span></span></span></button></div></div>







<a class="Link_root__fd7C0 Link_disguised__PSFAR ProductCardLink_root__69qxV" href="/technopark/naushniki-apple-airpods-pro-2-go-pokoleniya-2023?sid=25686"><div class="ProductCardGridLayout_root___C2h4"><div class="ProductCardGridLayout_top__V2Znc"><picture class="Picture_root__5uXZZ ProductCard_picture__lNFOz"><source type="image/webp" srcset="https://imgproxy.sbermarket.ru/imgproxy/size-220-220/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzI3NDQ2MzU5L29yaWdpbmFsLzEvMjAyMy0xMC0yNFQxMyUzQTUyJTNBMjEuNDU1ODAwJTJCMDAlM0EwMC8yNzQ0NjM1OV8xLmpwZw==.webp 1x, https://imgproxy.sbermarket.ru/imgproxy/size-220-220-2x/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzI3NDQ2MzU5L29yaWdpbmFsLzEvMjAyMy0xMC0yNFQxMyUzQTUyJTNBMjEuNDU1ODAwJTJCMDAlM0EwMC8yNzQ0NjM1OV8xLmpwZw==.webp 2x"><img class="Image_root__yieXw ProductCard_image__3jwTC" loading="lazy" width="220" height="220" src="https://imgproxy.sbermarket.ru/imgproxy/size-220-220/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzI3NDQ2MzU5L29yaWdpbmFsLzEvMjAyMy0xMC0yNFQxMyUzQTUyJTNBMjEuNDU1ODAwJTJCMDAlM0EwMC8yNzQ0NjM1OV8xLmpwZw==.jpg" srcset="https://imgproxy.sbermarket.ru/imgproxy/size-220-220-2x/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzI3NDQ2MzU5L29yaWdpbmFsLzEvMjAyMy0xMC0yNFQxMyUzQTUyJTNBMjEuNDU1ODAwJTJCMDAlM0EwMC8yNzQ0NjM1OV8xLmpwZw==.jpg 2x"></picture><div class="ProductSubscriptionsTopBadge_root__pS5JR ProductSubscriptionsTopBadge_withMargins__ZfZkR"><div class="ImageBadge_root__82OnF"><span class="SROnly_root__hLcKL">30% кешбэк Промокод APPLE (fix)</span><img class="Image_root__yieXw ImageBadge_image__63YfR" alt="30% кешбэк Промокод APPLE" src="https://static.restnproducts.ru/statics/downloads/ads-images/badge/apple_promocode_padding.png"></div></div><div class="ProductCardBadgeContainer_root__mZtIr ProductSubscriptionsBadges_root__5xH_Y CommonProductCard_subscriptionBadges__zTlrd ProductCardBadgeContainer_isBigAddToCartButton__pvzN9"><ul class="ProductCardBadgeGroup_root__XSJe2 ProductSubscriptionsBadges_group__c24_O ProductSubscriptionsBadges_leftGroup__AsJ_R"></ul></div></div><div class="ProductCardGridLayout_bottom__zjONK"><div class="ProductCard_titleContainer__5SZT1 CommonProductCard_titleContainer__3hRBp"><h3 class="ProductCard_title__iNsaD">Наушники Apple AirPods Pro 2-го поколения 2023</h3></div><div class="ProductCard_volume__PINyI"><span>1 шт.</span></div><div class="ProductCardPriceWrapper_root__Nnvhk"><div class="ProductCard_price__aRuGG CommonProductCard_price__vTnSS"><div class="ProductCardPrice_price__Kv7Q7 CommonProductCard_priceText__bW6F9"><span class="SROnly_root__hLcKL">Цена за 1 шт.</span>27&nbsp;980,00&nbsp;₽</div></div><div class="ProductCardAddToCart_root__C_TTI ProductCardAddToCart_big__bcksy CommonProductCard_addToCart__dKoib"><button class="Button_root__WicTg Button_default__fTaqt Button_primary__ifUNs Button_mdSize___etib Button_block__48waA" type="button">В корзину</button></div></div></div></div></a>






<div class="ProductCard_titleContainer__5SZT1 CommonProductCard_titleContainer__3hRBp">
    <h3 class="ProductCard_title__iNsaD">Наушники Apple AirPods Pro 2-го поколения 2023</h3>
</div>
'''