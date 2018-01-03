import settings
from auto import AutoBot
from manual import ManualBot


if __name__ == '__main__':
   
    if settings.MODE == "manual":
        bot = ManualBot()
        bot.run()

    elif settings.MODE == "auto":
        bot = AutoBot() 
        bot.run()

    else:
        print("ParamError: MODE should be ['auto', 'manual'].")
