from aiogram.dispatcher.filters.state import State, StatesGroup

class FilesState(StatesGroup):
    waiting_for_a_name = State()