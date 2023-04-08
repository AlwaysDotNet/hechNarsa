from config import API
from aiogram import Dispatcher
from admin import *
from asyncio import run
class StarBot:
    def __init__(self) -> None:
        self.dp = Dispatcher()
        self.bot = Bot(token=API)
        self.admin = Admin()
    async def start(self):
        self.dp.include_router(self.admin.AdminRout)
        try:
            await self.dp.start_polling(self.bot)
        except Exception as e:
            await self.bot.session.close()
if __name__ == "__main__":
    st = StarBot()
    run(st.start())
    