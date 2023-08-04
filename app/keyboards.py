from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


# Для пользователя кнопки
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

# Для админа кнопки
main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

# Админские кнопки
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку').add('Меню')

# Для котолога
catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', callback_data='t-shirt'),
                 InlineKeyboardButton(text='Шорты', callback_data='shorts'),
                 InlineKeyboardButton(text='Кроссовки', callback_data='sneakers'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('/cancel')
