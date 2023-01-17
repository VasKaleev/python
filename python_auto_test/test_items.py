import time

# Словарь  для проверки названия кнопки
d = {"ar": "أضف الى سلة التسوق",
     "ca": "Afegeix a la cistella",
     "cs": "Vložit do košíku",
     "da": "Læg i kurv",
     "de": "In Warenkorb legen",
     "en-gb": "Add to basket",
     "el": "Προσθήκη στο καλάθι",
     "es": "Añadir al carrito",
     "fi": "Lisää koriin",
     "fr": "Ajouter au panier",
     "it": "Aggiungi al carrello",
     "ko": "장바구니 담기",
     "nl": "Voeg aan winkelmand toe",
     "pl": "Dodaj do koszyka",
     "pt": "Adicionar ao carrinho",
     "pt-br": "Adicionar à cesta",
     "ro": "Adauga in cos",
     "ru": "Добавить в корзину",
     "sk": "Pridať do košíka",
     "uk": "Додати в кошик",
     "zh-cn": "Add to basket"}


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    #2 способа найти элемент
    #1. button_add = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    #2.
    button_add = browser.find_element_by_class_name('btn-add-to-basket')

   #2 способа проверить наличие кнопки
   #1 проверка кнопки на наличие
    assert button_add, "button is not"
   #2. проверка наличия кнопки по надписи
    button_name = button_add.text
    # Получение языка, используемого  на странице
    lang = browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
    lang_button_name = d.get(lang)

    assert button_name == lang_button_name, "button is not"