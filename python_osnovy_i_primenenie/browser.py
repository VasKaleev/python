#import webbrowser
#webbrowser.open_new_tab('http://habrahabr.ru/')
#webbrowser.open_new('svitanok.01sh.ru')
#webbrowser.get(using='google-chrome').open_new_tab('https://vk.com')
#webbrowser.open_new_tab('https://vk.com')
#webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text={}'.format('еда'))


""" url = 'https://yandex.ru/search/?lr=10735&text={}'.format('еда')
try:
    webbrowser.get(using='firefox').open_new_tab(url)
except Exception:
    webbrowser.open_new_tab(url) """

""" import webbrowser
import re
call = input('Введите ссылку или запрос: ')
if re.search(r'\.', call):
    webbrowser.open_new_tab('https://' + call)
elif re.search(r'\ ', call):
    webbrowser.open_new_tab('https://yandex.ru/search/?text='+call)
else:
    webbrowser.open_new_tab('https://yandex.ru/search/?text=' + call) """
import webbrowser
call = input('Введите ссылку или запрос: ')
if '.' in call:
    webbrowser.get(using='windows-default').open_new_tab('https://' + call)
    #webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    #webbrowser.get('Chrome').open_new_tab('vk.com')
    #webbrowser.get(using='firefox').open_new_tab(call)
else:
    webbrowser.get(using='windows-default').open_new_tab('https://yandex.ru/search/?text=' + call)

