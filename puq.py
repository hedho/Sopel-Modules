# coding=utf-8

from sopel import module

@module.commands('puq')
@module.example('.puq monaco')
def happy(bot, trigger):
    if not trigger.group(3):
        bot.reply("Kon je ka don me puq kallxo?!!")
        return

    bot.say("{} E puq shume  shumeee 💋💋💋💋 {}!".format(trigger.nick, trigger.group(3)))
