from aiogram.dispatcher.filters.state import StatesGroup, State


class State_frx(StatesGroup):
    # Создаем состояние в этой группе. Называйте каждое состояние соответственно его назначению.
    # В данном случае Q1 - question 1, то есть первый вопрос. У вас это может быть по-другому
    await_file = State()
    choice_form = State()