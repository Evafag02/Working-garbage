from aiogram.utils import executor
import sqlite3 as sq
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery

bot = Bot(token="6199000329:AAHPgwP48UmD1WtW4K0T5fTe7V7MNuvRUKE")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# knopki
add_menu = InlineKeyboardMarkup()
btn_janrlar_kosu = InlineKeyboardButton(text="Janr kosu", callback_data="janrkosu")
btn_kino_kosu = InlineKeyboardButton(text="Kino kosu", callback_data="kinokosu")
add_menu.add(btn_kino_kosu, btn_janrlar_kosu)

kb1 = KeyboardButton('Menu')
kb2 = KeyboardButton('Избранное')
kb3 = KeyboardButton('Популярное')
btn_client = ReplyKeyboardMarkup(resize_keyboard=True)
btn_client.add(kb1, kb2).add(kb3)

b1 = KeyboardButton(text="Artqa")
client_kb = ReplyKeyboardMarkup(resize_keyboard=True)
client_kb.add(b1)

# /////////////
base = sq.connect('kino.db')

cursor = base.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS janr_turleri(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS kinolar(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                janrid INTEGER,
                movie TEXT,
                desc TEXT,
                time VARCHAR(255),
                year INTEGER,
                actors TEXT,
                photo TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS izbrannoe(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kino_id INTEGER, 
                user_id INTEGER)''')

base.commit()


# data base


async def select_all_types(message):
    inline_menu = types.InlineKeyboardMarkup()
    for ret in cursor.execute('SELECT * FROM janr_turleri').fetchall():
        btn = types.InlineKeyboardButton(text=ret[1], callback_data=ret[1])
        inline_menu.add(btn)
    await message.answer(" Bizdin Kinolar", reply_markup=inline_menu)


async def select_all(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for ret in cursor.execute('SELECT * FROM janr_turleri').fetchall():
        btn = types.KeyboardButton(text=ret[1])
        menu.add(btn)
    await message.answer("Janrdyn kai turin koskynyz keledi:", reply_markup=menu)


async def insert_kino(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO kinolar (janrid,movie,desc,time,year,actors,photo) values(?,?,?,?,?,?,?)",
                       tuple(data.values()))
    base.commit()
    print('database ok')


async def select_izbrannoe(message):
    izbrannoe = []
    for kino in cursor.execute('SELECT kino_id FROM izbrannoe').fetchall():
        izbrannoe.append(kino[0])

    d = {}
    for item in set(izbrannoe):
        d[item] = izbrannoe.count(item)
    for key in d:
        res = cursor.execute(f"SELECT * FROM kinolar WHERE id ='{key}'").fetchall()[0]
        kb1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Удалить из избранного', callback_data='alu' + str(res[0]))
        kb1.add(btn1)
        await message.answer_photo(res[-1], f'{res[2]}', reply_markup=kb1)


# admin
ID = None


class FSMAdmin(StatesGroup):
    janrlar = State()
    janrlar_id = State()
    movie = State()
    desc = State()
    time = State()
    year = State()
    actors = State()
    photo = State()


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приятного просмотра', reply_markup=btn_client)
    await message.delete()


@dp.message_handler(Text(equals='Menu'))
async def menu(message: types.Message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for ret in cursor.execute('SELECT * FROM janr_turleri').fetchall():
        btn = types.KeyboardButton(text=ret[1])
        btn_2 = types.KeyboardButton(text='Artqa')
        menu.add(btn, btn_2)
        await message.answer("Tanda:", reply_markup=menu)


@dp.message_handler(Text(equals='Избранное'))
async def izbrannoe(message: types.Message):
    await message.answer("Ваше избранное:", reply_markup=client_kb)
    await select_izbrannoe(message)


@dp.message_handler(Text(equals='Artqa'))
async def artqa(message: types.Message):
    await message.answer("Приятного просмотра", reply_markup=btn_client)


@dp.message_handler(commands='add')
async def add_command(message: types.Message):
    await message.answer("Ne qosasyz?:", reply_markup=add_menu)


@dp.callback_query_handler(Text(equals='janrkosu'))
async def janr_kosu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Atauyn engiz:")
    await state.set_state(FSMAdmin.janrlar)
    await callback.answer()


@dp.message_handler(state=FSMAdmin.janrlar)
async def load_janrlar(message: types.Message, state: FSMContext):
    print(message.text)
    cursor.execute(f"INSERT INTO janr_turleri(name) values('{message.text}')")
    base.commit()
    print('database ok')
    await state.finish()


@dp.callback_query_handler(Text(equals='kinokosu'))
async def kino_kosu(callback: CallbackQuery, state: FSMContext):
    await select_all(callback.message)
    await state.set_state(FSMAdmin.janrlar_id)
    await callback.answer()


@dp.message_handler(state=FSMAdmin.janrlar_id)
async def load_kino_id(message: types.Message, state: FSMContext):
    id = cursor.execute(f"SELECT id FROM janr_turleri WHERE name='{message.text}'").fetchall()[0][0]
    async with state.proxy() as data:
        data['id'] = id
    await state.set_state(FSMAdmin.movie)
    await message.answer("Endi atauyn engiz:")


@dp.message_handler(state=FSMAdmin.movie)
async def load_movie(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['movie'] = message.text
    await state.set_state(FSMAdmin.desc)
    await message.answer("Endi sipattamasyn engiz:")


@dp.message_handler(state=FSMAdmin.desc)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await state.set_state(FSMAdmin.time)
    await message.answer('Теперь укажи время')


@dp.message_handler(state=FSMAdmin.time)
async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await state.set_state(FSMAdmin.year)
    await message.answer('Теперь укажи год выпуска')


@dp.message_handler(state=FSMAdmin.year)
async def load_year(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = int(message.text)
    await state.set_state(FSMAdmin.actors)
    await message.answer('теперь укажи имена главных актеров')


@dp.message_handler(state=FSMAdmin.actors)
async def load_actors(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['actors'] = message.text
    await state.set_state(FSMAdmin.photo)
    await message.answer('теперь добавь постер фильма')


@dp.message_handler(state=FSMAdmin.photo, content_types=['photo'])
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await insert_kino(state)
    await state.finish()
    await message.answer("Okay")


@dp.message_handler()
async def handle_janr(message: types.Message):
    janrs = cursor.execute("SELECT name FROM janr_turleri").fetchall()
    janr_names = [janr[0] for janr in janrs]
    if message.text and message.text in janr_names:
        janr_id = cursor.execute(f"SELECT id FROM janr_turleri WHERE name='{message.text}'").fetchone()
        if janr_id:
            janr_id = janr_id[0]
            movies = cursor.execute(f"SELECT * FROM kinolar WHERE janrid={janr_id}").fetchall()
            for movie in movies:
                kb = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton(text='Добавить в избранное', callback_data="qosu" + str(movie[0]))
                kb.add(btn1)
                await message.answer_photo(movie[7],f"{movie[2]}\nОписание:{movie[3]}\nВремя:{movie[4]}\nГод выпуска:{movie[5]}\nГлавные актеры:{movie[6]}",reply_markup=kb)





l = []
for kino in cursor.execute('SELECT movie FROM kinolar ').fetchall():
    l.append(kino[0])


@dp.callback_query_handler()
async def print_kino(callback: CallbackQuery):
    global l
    if callback.data in l:
        id = cursor.execute(f"SELECT janrid  FROM kinolar WHERE movie='{callback.data}'").fetchall()[0][0]
        await handle_janr(callback.message)
        await select_all_types(callback.message)
        await callback.answer()
    elif "qosu" in callback.data:
        id = int(callback.data[callback.data.find("u") + 1:])
        kino = cursor.execute(f"SELECT id FROM izbrannoe WHERE kino_id = '{id}'").fetchall()
        print(kino)
        if kino:
            await callback.answer("Уже добавлено")
        else:
            cursor.execute(f'INSERT INTO izbrannoe (kino_id) values ({id})')
            base.commit()
            print("OK")
            await callback.answer("Добавлено")
    elif "alu" in callback.data:
        id = int(callback.data[callback.data.find("u") + 1:])
        id_del = cursor.execute(f"SELECT id FROM izbrannoe WHERE kino_id='{id}'").fetchall()
        cursor.execute(f"DELETE FROM izbrannoe WHERE id='{id_del[0][0]}'")
        await callback.answer("Удалено")
        await callback.message.delete()
        base.commit()


executor.start_polling(dp, skip_updates=True)