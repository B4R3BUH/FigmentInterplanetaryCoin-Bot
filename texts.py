from aiogram.utils.markdown import hbold, hitalic, hcode
from datetime import datetime, timedelta

now = datetime.now()

start_text = f'''{hbold('Добро пожаловать в FigmentInterplanetaryCoin')}! 🎉🎉🎉\n\n\n{hbold('Вот что вы можете сделать с FIC прямо сейчас:')}\n\n💯 Зарабатывайте очки FIC: {hitalic("Играйте в нашу игру, чтобы заработать очки FIC (FICs)")}\n\n🧑 Приглашайте друзей: Приводите своих друзей, чтобы получить больше очков FIC! {hitalic("Выбирайте, кого пригласить с умом, можно пригласить только 5 друзей!")}\n\n\n{hbold('Что мы можем предложить на данный момент?')}\n\n🪙 Обилие скинов: {hitalic('У нас очень много тематических и классных скинов, и их количество постоянно увеличивается!')}\n\n⚙️ Удобная механика заработка очков.\n\n👥 Реферальная система\n\n🎶 Спец. Эффекты: {hitalic('Будут работать, если включить их в Настройках.')}\n\n🤝 Поддержка: {hitalic('Если у Вас есть какие-либо проблемы с аккаунтом в FIC - напишите @FigmentInterplanetaryCoin_SupBot, в полной ясности описав проблемы (Пр: Удалили приложение, забыли свои данные, стерли переписку с ботом, и хочется восстановить прогресс).')}\n\n📝 Вы всегда можете предлагать идеи в {hitalic('Комментариях Тг-канала FigmentInterplanetaryCoin')} или {hitalic('в @FigmentInterplanetaryCoin_SupBot!')}\n\n\nДальше больше!'''

help_text = f'''{hbold('Есть вопросы? — Вы попали куда надо')}!\n\n\nВ этом разделе бота можно найти:\n\n{hbold("1.")} Помощь по игре\n\n{hbold("2.")} Предложения для повышения уровня заработка в FIC App\n\n{hbold("3.")} Правила (их не так много)\n\n{hbold("4.")} Как правильно устанавливать и обновлять приложение\n\n\n{hitalic("Надеемся, информация, которую вы найдете на страницах этого раздела, ответит на все вас интересующие вопросы!")}\n\n{hitalic("Если ваши вопросы не совпадают с вопросами и ответами на них в разделах этого бота — перейдите в @FigmentInterplanetaryCoin_SupBot")}'''

guide_list_text = f'''{hbold('Как зарабатывать FICs?')}\n\n\n{hbold('1.')} Покупайте Бусты: {hitalic('Бусты помогут вам зарабатывать больше очков за тап и дольше тапать за сессию!')}\n\n{hbold('2.')} Если у вас закончились Кондиции - не страшно! {hitalic('Просто перезапустите приложение (полностью), и ваши Кондиции восстановятся.')}\n\n{hbold('3.')} Приглашайте друзей! {hitalic('Друзья помогут вам заработать больше очков')}\n\n{hbold("4.")} Покупайте Пассивный Фарм. {hitalic('Это лучший помощник для того, чтобы накопить нужное вам количество очков. Но для этого нужно будет немного потратиться...')}'''

rules_list_text = f'''{hbold('Правила')}\n\n\n{hbold('Главное правило:')} Быть подписанным на Тг-Канал @FigmentInterplanetaryCoin\n\n{hbold('Запрещается:')}\n{hbold('1.')} Выкладывать FIC App на разных форумах\n{hbold('2.')} Рекламировать FIC, если [Разработчик] не давал согласия на это\n{hbold('3.')} Придумывать игровые никнеймы, которые могут являться оскорбительными для [Разработчика]\n{hbold("4.")} Негативить на участников комьюнити и [Разработчика]\n\n{hbold('Разрешается:')}\n{hbold('1.')} Создавать майнинг-фермы различного типа\n{hbold('2.')} Придумывать любые иговые никнеймы, даже те, {hitalic('которые могут быть запрещены')} в других проектах/играх\n{hbold('3.')} Тапать 24/7\n\n{hbold('Поощряется:')}\n{hbold('1.')} Вносить вклад в разработку FIC App\n{hbold('2.')} Предлагать идеи для новых скинов\n\n\n{hbold("Что будет за нарушение правил?")}\n\nЗа нарушение правил обязательно будет выдана блокировка!\nБлокировка бывает двух типов: В Приложении FIC App и Полная.\n\nТип блокировки зависит от правил, которые нарушил пользователь, либо от совокупности нарушенных им правил!'''

how_to_use_list_text = f'''{hbold('Правильное пользование приложением FIC App.')}\n\n\n{hbold('Как правильно обновлять и устанавливать приложение?')}\n\n{hbold('1.')} Обновление.\nС выходом новой версии приложения FIC App, чтобы обновиться, не нужно удалять приложение со старой версией.\nНужно скачать новую версию приложения, нажав на кнопку {hitalic('"Получить FIC App"')} в этом боте, в /start.\n\n{hbold('2.')} Установка.\nПосле открытия скачанного приложения появится всплывающее окно Google Play Защита или что-то похожее. В этом окне нужно нажать на кнопку {hitalic('"Подробнее"')}, появится кнопка {hitalic('"Установить без сканирования"')}, нажимаем на нее и ждем установки.\n\n\n{hbold('Как зарегистрироваться?')}\n\n{hbold('1.')} Открываете приложение FIC App. {hitalic('Вам сразу предложат зарегистрироваться')}.\n{hbold('2.')} Вводите свой User ID, который получите/получили здесь\n{hbold('3.')} Нажимаете кнопку {hitalic('"REGISTER"')} и можете начинать зарабатывать!\n\n\n{hbold('Как зайти в уже созданный ранее аккаунт?')}\n\n{hbold('1.')} В главном меню нажимаете на кнопку {hitalic('"SWAP AUTH"')}.\n{hbold('2.')} Вводите свой FIC ID {hitalic('(его можно найти в этом боте)')}\n{hbold('3.')} Нажимаете на кнопку {hitalic('"LOG IN"')} и вас перенесет на Главный экран.'''

admin_panel_text = f'''{hbold("Доступные команды админ-панели:")}\n{hitalic("(id) — telegram_user_id либо fic_id пользователя.")}\n{hitalic("(user_id) — telegram_user_id пользователя.")}\n\n\n{hbold("1.1.")} {hcode("/show (table_name) (column_name) (id)")}\n— Возвращает значение из таблицы {hitalic("table_name")}, из {hitalic("column_name")} для игрока с введенным {hitalic("id")}\n\n{hbold("1.2.")} {hcode("/show (table_name) all (id)")}\n— Возвращает {hitalic("все значения")} из таблицы {hitalic("table_name")}, из онлайн бд у игрока с введенным {hitalic("id")}\n\n{hbold("2.")} {hcode("/set (table_name) (column_name) (updated_value) (id)")}\n— Обновляет данные в таблице {hitalic("table_name")}, в колонке {hitalic("column_name")} на {hitalic("updated_value")} у игрока с введенным {hitalic("id")}\n\n{hbold("3.")} {hcode("/set_access (access_value) (id)")}\n— Обновляет значение доступа на {hitalic("access_value")} у игрока с введенным {hitalic("id")}\n\n{hbold("4.")} /on_app и /off_app\n— {hitalic("Включение")} и {hitalic("Выключение")} приложения FIC App соответственно\n\n{hbold("5.")} /players\n— Возвращает {hitalic("players.txt")}\n\n{hbold("6.1.")} {hcode("/notify (notification_text) (user_id)")}\n— Отправляет уведомление с текстом {hitalic("notification_text")} пользователю с введенным {hitalic("user_id")}\n\n{hbold("6.1.")} {hcode("/notify (notification_text) all")}\n— Отправляет уведомление с текстом {hitalic("notification_text")} {hitalic("всем пользователям @FigmentInterplanetaryCoin_bot")}'''

tech_works_now_text=f'''🛠️ {hbold("В данный момент проводятся технические работы на серверах бота.")}\n\n\nНекоторые функции могут быть недоступны или работать некорректно.\n\nМы работаем над устранением неполадок и скоро все будет работать как обычно.\n\n{hitalic(f"Примерное время завершения тех. работ — {(now + timedelta(hours=4)).strftime('%d.%m в %H:%M ')}")} по МСК, может и раньше!\n\nСпасибо за понимание!'''
tech_works_app_now_text=f'''🛠️ {hbold("В данный момент проводятся технические работы на серверах приложения.")}\n\n\nПриложение пока что не работает, но его можно скачать и установить на устройство.\n\nМы работаем над устранением неполадок и скоро все будет работать как обычно.\n\n{hitalic(f"Примерное время завершения тех. работ — {(now + timedelta(hours=4)).strftime('%d.%m в %H:%M ')}")} по МСК, может и раньше!\n\nСпасибо за понимание!'''

was_blocked_text=f'''❌ {hbold("Похоже, что ты был заблокирован в FIC!")}\n\nЭто означает, что ты не можешь пользоваться ни одним из продуктов FIC.\nЧаще всего, блокировки происходят из-за нарушения Правил Пользования.\n\n{hitalic("Если это произошло не по твоей вине — как можно быстрее свяжись с поддержкой (@FigmentInterplanetaryCoin_SupBot).")}'''

for_referral_link_text = '''\nДавай зарабатывать вместе со мной в FIC!\n\nНажми ниже, чтобы присоединиться к веселью. 🌟'''


start_support_text = f'''{hbold('Добро пожаловать в Поддержку FigmentInterplanetaryCoin')}!\n\n\nЕсли вы попали сюда, значит, что у вас есть нестандартные вопросы к Разработчику.\n\nПеред тем, как интересоваться у Разработчика, вам следует {hitalic("прочесть Все разделы данного бота")}, чтобы все произошло {hitalic("быстро и без ошибок")}!\n\n\n<i>В разделе {hbold('"Как работает бот"')} вы сможете найти, какие функции бота поддержки мы можем предложить на данный момент.\n\nВ разделе {hbold('"Как взаимодействовать"')} вы сможете найти, как правильно {hitalic("Поинтересоваться у Разработчика")}, а также, как правильно {hitalic("предлагать идеи Разработчику")}</i>'''

htbws_support_text = f'''{hbold('Как работает бот FigmentInterplanetaryCoin Support')}?\n\n\nДанный бот работет по принципу {hbold("Задай вопрос — Получи ответ")}, {hitalic("без траблов")}, {hitalic("с полной анонимностью")}.\n\nПока что бот FigmentInterplanetaryCoin Support выглядит, словно был написан на коленке и представляет из себя пустышку.\nДа, пока так, но со временем мы улучшим его, чтобы вопросы можно было задавать {hitalic("еще удобнее и быстрее")}!\n\n\n{hbold("Из функций данного бота мы можем предложить:")}\n\n/question — {hitalic("для того, чтобы интересоваться у Разработчика")}\n/my_questions — {hitalic("для просмотра статистики своих вопросов")}\n/close_question — {hitalic("для закрытия своего вопроса")}\n/idea — {hitalic("для того, чтобы предлагать свои идеи для разваития проекта Разработчику")}\n/my_ideas — {hitalic("для просмотра статистики своих предложенных идей")}'''

hdq_support_text = f'''{hbold('Как правильно интересоваться у Разработчика')}?\n\n\nВсе просто! Вписываете {hcode("/question [краткий вопрос со знаком вопроса] [полное описание вашего вопроса]")} — {hitalic("все это без квадратных скобок")}\n\nПотом, после проверок сообщения, ответа Разработчика на ваш вопрос и отправления вам ответа от него, вам придет {hitalic("уведомление с ответом")}.\n\nВы сможете {hitalic("закрыть ваш вопрос")}, ознакомившись с ответом Разработчика, {hitalic("нажав на соответствующую кнопку под уведомлением с ответом")}, или {hitalic("использовать соответствующую команду бота!")}\n\n\n{hbold("Как правильно предлагать идеи Разработчику?")}\n\nТо же самое, что и с вопросами, только:\nДля предложения идеи > {hcode("/idea [текст вашей идеи]")} — {hitalic("без квадратных скобок")}'''

admin_panel_support_text = f'''{hbold("Доступные команды админ-панели Support-Бота:")}\n\n\n{hbold("1.")} /questions\n— Возвращает сообщение со списком всех заданных вопросов (Номер в бд, Вопрос, Дата Время, Текст вопроса, Автор, Открыт или нет)\n\n{hbold("2.")} {hcode("/answer (question_num) (question_answer)")}\n— Отправляет пользователю, задавшему вопрос с {hitalic("ID в базе данных (question_num)")}, {hitalic("ответ (question_answer)")}, а также {hitalic("обновляет базу данных и ставит ответ там.")}\n\n{hbold("3.")} /ideas\n— Возвращает сообщение со списком всех предложенных идей (Номер в бд, Идея, Дата Время, Автор, Статус рассмотрения)\n\n{hbold("4.")} {hcode("/accept (idea_num) (idea_accept_value)")}\n— Отправляет пользователю, предложившему идею с {hitalic("ID в базе данных (idea_num)")}, {hitalic("ответ, зависящий от (idea_accept_value) {0-На рассмотрении, 1-Принята к сведению, 2-Отклонена}")}, а также {hitalic("обновляет базу данных и ставит статус там.")}'''