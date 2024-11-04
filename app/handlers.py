from aiogram import types, Router, F
from aiogram.filters import Command

from app.gpt import ask_gpt

router = Router()
gpt_on = True

@router.message(Command('start'))
async def handle_start(message: types.Message):
    text = 'Привет! Сейчас GPT отключен, поэтому ты не можешь с ним пообщаться. Чтобы включить его напиши /switch' if not gpt_on else 'Привет! Сейчас GPT включен, поэтому ты можешь с ним пообщаться. Чтобы выключить его напиши /switch'
    await message.answer(text)


@router.message(Command('switch'))
async def handle_switch(message: types.Message):
    global gpt_on
    if gpt_on:
        gpt_on = False
        await message.answer('GPT выключен!')
    else:
        gpt_on = True
        await message.answer('GPT включен!')


async def handle_message(message: types.Message):
    global gpt_on
    if gpt_on:
        gpt_response = ask_gpt(message.text)
        await message.answer(gpt_response)
    else:
        await message.answer(message.text)