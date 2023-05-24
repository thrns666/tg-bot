help_text: str = '''<b>/start </b> <em>- старт бота</em>
<b>/weather </b> <em>- прогноз погоды</em>
<b>/description </b> <em>- отправляет вам описание бота</em>
<b>/help</b> <em>- помощь</em>
<b>/count</b> <em>- счетчик</em>
<b>Love</b> <em>- отправь и узнаешь (spec for my Honey, love u so much)</em>
<b>Погода</b> <em>- бот соберет всю информацию для прогноза и отправит вам</em>
<em>А есче, ты можешь отправить боту ❤️ и он тебе что-то ответит))</em>'''


start_text: str = '''<em>Привет, я бот, который отправляет тебе погоду.
Работаю через Яндекс.Погода API.
Отправь мне слово Погода и я все сделаю.</em>'''


description = '''<em>Данный бот отправляет вам текущий(фактический)
прогноз погоды на основании вашего местоположения</em>'''


stickers = ['CAACAgIAAxkBAAEIA6xkBMiCRbMf5-ofYXCEa-xy59DcygACDQEAAladvQpG_UMdBUTXly4E',
            'CAACAgIAAxkBAAEIA6pkBMh6b5GEDGA1hqOOK5IvSWTHWwACBAEAAladvQreBNF6Zmb3bC4E']

sasha: str = 'CAACAgIAAxkBAAEII0JkELgrnEBFZjQsWPYtpcs-dM23RgACCC4AAv9qiEgSMpKinVUMSC8E'

weather_dict: dict = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                      'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                      'rain': 'дождь', 'moderate-rain': 'умеренно сильный дождь', 'heaavy-rain': 'сильный дождь',
                      'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                      'wet-snow': 'дождь со мнегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                      'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                      'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'}
