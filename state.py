from aiogram.dispatcher.filters.state import StatesGroup, State


class Continue(StatesGroup):
    text = State()