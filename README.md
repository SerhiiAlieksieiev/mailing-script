# Mailing script

Данный скрипт позволяет выполнять рассылку писем.

### Запуск
1. Скачайте репозиторий командой

  	```sh
  	git clone https://github.com/SerhiiAlieksieiev/mailing-script.git
	```
	
2. Сделайте виртуальное окружение командой

	```sh
    python -m venv --copies /полный/путь/до/папки/виртуального/окружения 
    ```
	
3. Установите зависимости  командой 

	```sh
    py -m pip install -r requirements.txt
    ```
4. Добавьте [переменные окружения](https://github.com/SerhiiAlieksieiev/mailing-script#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)

5. Замените email адреса и отредактируйте письмо

6. Запустите скрипт командой

	```sh
    python main.py
    ```
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом  с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступна 1 переменная:
- `PASSWORD` — пароль от вашей электронной почты

### Цели проекта
Код написан в учебных целях — это урок в [курсе](https://dvmn.org/referrals/khnIM90ONObdHawnJXjYOyKnwrucdRj9zsA5DEPm/) по Python на сайте [Devman](https://dvmn.org/referrals/eC72w2BASG9Zj3T7iMTSsxDbHXthCmJmeLKBNfwf/).
