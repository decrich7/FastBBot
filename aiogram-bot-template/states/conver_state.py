from aiogram.dispatcher.filters.state import StatesGroup, State


class State_frx(StatesGroup):
    # ������� ��������� � ���� ������. ��������� ������ ��������� �������������� ��� ����������.
    # � ������ ������ Q1 - question 1, �� ���� ������ ������. � ��� ��� ����� ���� ��-�������
    await_file = State()
    choice_form = State()