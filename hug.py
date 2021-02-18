# coding=utf-8

from sopel import module

@module.commands('qaf')
@module.example('.qaf monaco')
def happy(bot, trigger):
    if not trigger.group(3):
        bot.reply("Kon je ka don me qaf kallxo?")
        return

    bot.say("{} E qaf shume  shumeee 🤗 {}!".format(trigger.nick, trigger.group(3)))
