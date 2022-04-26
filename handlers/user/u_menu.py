from aiogram import types
from loader import dp, db, cursor
from keyboards import mainMenu, subMenu, osAdminMenu, netMenu, orderMenu, netEquipment
from data.config import admins_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import random

order_d = []
job_n_d = []
job_d = []


class FSMorders(StatesGroup):
    job_name = State()
    job_description = State()


@dp.message_handler(text="/start")
async def command_call_main_menu(message: types.Message):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.chat.id}")
    a_u = cursor.fetchone()
    print(a_u)
    if a_u == 1:
        for admin_id in admins_id:
            if str(admin_id) == str(message.from_user.id):
                admin_s = "1"
                sql_user_reg = "INSERT INTO users (user_id, f_name, l_name, user_status, date ,admin_status) " \
                               "VALUES (%s, %s, %s, %s, %s, %s)"
                val_user_reg = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, '1',
                                message.date, admin_s,)
                cursor.execute(sql_user_reg, val_user_reg)
                db.commit()
                await message.answer(f"Добро пожаловать, Админ: {message.from_user.full_name}", reply_markup=mainMenu)
            elif str(admin_id) != str(message.from_user.id):
                sql_user_reg = "INSERT INTO users (user_id, f_name, l_name, user_status, date ,admin_status) " \
                               "VALUES (%s, %s, %s, %s, %s, %s)"
                val_user_reg = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, '1',
                                message.date, admin_s,)
                cursor.execute(sql_user_reg, val_user_reg)
                db.commit()
                await message.answer(f"Добро пожаловать: {message.from_user.full_name}", reply_markup=mainMenu)
    else:
        cursor.execute(f"SELECT * FROM users WHERE user_id = {message.chat.id}")
        a_u_s = cursor.fetchone()[-1]
        print(a_u_s)
        if a_u_s == 1:
            await message.answer(f"Добро пожаловать, Админ: {message.from_user.full_name}", reply_markup=mainMenu)
        else:
            await message.answer(f"Добро пожаловать: {message.from_user.full_name}", reply_markup=mainMenu)


# --- Main Menu ---
@dp.message_handler(text=["Услуги 🏷", "Товары 💲", "Корзина 📌", 'Главное меню'])
async def main_menu(message: types.Message):
    if message.text == "Услуги 🏷":
        await message.answer(f"{message.from_user.full_name},\n Вы выбрали раздел:\n {message.text}\n"
                             f" Выберете интересующий раздел ", reply_markup=subMenu)
    elif message.text == "Товары 💲":
        await message.answer(f"{message.from_user.full_name},\n Вы выбрали раздел:\n {message.text}",
                             reply_markup=netEquipment)
    elif message.text == "Корзина 📌":
        cursor.execute(f"SELECT * FROM orders WHERE client_id = {message.chat.id}")
        all_orders = cursor.fetchall()
        db.commit()
        # print(all_orders)
        if len(all_orders) == 0:
            await message.answer("У вас еще нет заказов!")
        else:
            for cl_order in all_orders:
                o_n = str(cl_order[1])
                j_n = cl_order[2]
                j_d = cl_order[3]
                j_s = cl_order[4]
                j_date = cl_order[6]
                # print(all_orders)
                await message.answer(f"{message.from_user.full_name}\n Номер заказа: {o_n}"
                                     f"\n Наименование: {j_n}\n Описание: {j_d}\n"
                                     f" Статус: {j_s}\n Дата: {j_date}")

    elif message.text == 'Главное меню':
        await message.answer(f"{message.text}", reply_markup=mainMenu)


# --- Sub Menu ---
@dp.message_handler(text=['Нстройка OS Linux/Windows/MacOS', 'Нстройка сетевого оборудования', "Назад"])
async def sub_menu(message: types.Message):
    if message.text == 'Нстройка OS Linux/Windows/MacOS':
        await message.answer(f"{message.from_user.full_name},\n Вы выбрали раздел:\n {message.text}\n"
                             f" Выберете интересующий раздел ", reply_markup=osAdminMenu)
    elif message.text == 'Нстройка сетевого оборудования':
        await message.answer(f"{message.from_user.full_name},\n Вы выбрали раздел:\n {message.text}",
                             reply_markup=netMenu)
    elif message.text == "Назад":
        await message.answer(f"{message.text}", reply_markup=subMenu)


# --- network order ---
@dp.message_handler(text=['Маршрутизатор(ы)', 'Коммутатор(ы)', 'Маршрутизатор(ы)/Коммутатор(ы)/Точка WiFi',
                          'Точка WiFi'], state=None)
async def net_job(message: types.Message):
    await FSMorders.job_name.set()
    await message.answer("Укажите Бренд(ы) и модель(и) обрудования", reply_markup=orderMenu)


# ---OS order ---
@dp.message_handler(text=['Linux', 'Windows', 'MacOS'], state=None)
async def os_job(message: types.Message):
    await FSMorders.job_name.set()
    await message.answer(f"Уточните дистрибутив {message.text}", reply_markup=orderMenu)


# --- FSM start ---
@dp.message_handler(state=FSMorders.job_name)
async def job_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job_name'] = message.text
    await FSMorders.next()
    await message.answer("Укажите работы для выполнения")


# --- Order cancel ---
@dp.message_handler(state="*", commands='Отменить Заказ')
@dp.message_handler(state="*", text='Отменить Заказ')
async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        # return
        await message.answer("Заказ отменен, вы возвращены в главное меню", reply_markup=mainMenu)
        await state.finish()


@dp.message_handler(state=FSMorders.job_description)
async def job_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job_description'] = message.text
    await message.answer(message.text)
    async with state.proxy() as data:
        order_number = random.randint(1000, 999999999)

        await message.answer(f"{message.chat.full_name}\n Номер заказа:\n {order_number}\n Наименование услуги:\n"
                             f" {list(data.values())[0]} \n Описание задачи:\n {list(data.values())[1]}"
                             f"\n Подтвердите или Отмените заказ")

        ins1 = str(list(data.values())[0])
        ins2 = str(list(data.values())[1])
        # print(ins1)
        # print(ins2)

        order_d.append(order_number)
        job_n_d.append(ins1)
        job_d.append(ins2)
        await state.finish()


@dp.message_handler(text=['Подтвердить заказ', 'Отменить Заказ'])
async def save_to_bd(message: types.Message):
    if message.text == 'Подтвердить заказ':
        print(order_d, job_n_d, job_d)
        sql_order_reg = "INSERT INTO orders (order_number, job_name, job_description, status, client_id, " \
                        "order_date) VALUES (%s, %s, %s, %s, %s, %s)"
        val_order_reg = (order_d[0], job_n_d[0], job_d[0], '0', message.from_user.id, message.date)
        cursor.execute(sql_order_reg, val_order_reg)
        db.commit()
        order_d.clear()
        job_n_d.clear()
        job_d.clear()
        await message.answer('В ближайшее время с вами свяжется специалист по вашему заказу', reply_markup=mainMenu)
    elif message.text == 'Отменить Заказ':
        order_d.clear()
        job_n_d.clear()
        job_d.clear()
        await message.answer('Ваш заказ отменен', reply_markup=mainMenu)
