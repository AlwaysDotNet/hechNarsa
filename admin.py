from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from config import admins
from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram import F
from aiogram.filters import Command
class Admin:
    def __init__(self) -> None:
        self.rout = Router()
        self.admin_list = admins
    def start_buttons(self):
        rp = ReplyKeyboardBuilder()
        ls_menu = ["User Table List","Find User By Id","Find User By FisrtName",
                   "Find User By Last_name","Filter by Language"]
        for menu in ls_menu:
            rp.add(KeyboardButton(text=menu))
        rp.adjust(2,1,2)
        return rp.as_markup(resize_keyboard=True,
                            input_field_placeholder="Iltimos menuni tanlov qiling ⬇")
        
    #Start commanda
    async def star_admin(self,msg:Message,bot:Bot):
        str = f"Assalomu aleykum admin {msg.from_user.full_name}"
        await msg.answer(text=str,reply_markup=self.start_buttons())
    #Ruyxatdan utkazish
    def register(self):
        self.rout.message.register(self.star_admin,F.from_user.id.in_(self.admin_list),Command("start"))
    @property
    def AdminRout(self):
        self.register()
        return self.rout