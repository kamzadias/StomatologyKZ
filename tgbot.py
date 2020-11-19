#--------------------Library and Token--------------------#
import telebot
from telebot import types
TOKEN = '<1486753654:AAFqJBJRCDYOyONv_MuwQzotpL1IF-pvgsI>'
bot = telebot.TeleBot("1486753654:AAFqJBJRCDYOyONv_MuwQzotpL1IF-pvgsI")
#--------------------Command Start--------------------#
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('D:\Telegram\welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Dental clinics🦷")
    markup.add(item1)
    bot.send_message(message.chat.id,"Welcome, <i>{0.first_name}</i>!\nI'm a <b>{1.first_name}</b> bot that will help you find the suitable dental clinic!🦷\n"
          "To start using the bot, you need to click on the 'Dental clinics🦷' button.Select the desired dentistry and then the information that you need.\n"
                                     "P.S. Enter the promo code by capital letters!".format(message.from_user, bot.get_me()),
                     parse_mode='html',reply_markup=markup)

#--------------------Message like a text--------------------#

@bot.message_handler(content_types=['text'])
def usermessage(message):
     if message.chat.type == 'private':
         # -----------------------------------------------------DoctorDent INFO------------------------------------------------#
        if message.text == '📍 Addresses(DD)':
            bot.send_message(message.chat.id, "📍 <b>Nur-Sultan,Kazakhstan</b>\n Turkestan,8/2\n Kabanbai Batyr Avenue,16\n Zhenis Avenue,21" ,parse_mode='html')
        elif message.text == '📞 Contacts(DD)':
            bot.send_message(message.chat.id, '📞 <b>Nur-Sultan,Kazakhstan</b>\n+7‒777‒353‒94‒83\n+7‒775‒771‒27‒57\n+7 (7172) 41‒72‒66\n+7‒708‒551‒40‒67',parse_mode='html')
        elif message.text == '🧾 Prices(DD)':
            bot.send_message(message.chat.id, '🔴 <b>THERAPY</b>\n'
                                              'Superficial caries(1 tooth) - 9 330\n'
                                              'Deep caries(1 tooth) - 13670\n'
                                              'Filling a milk tooth caries - 13,080\n'
                                              'Thermofil (1 tooth)  - 25000-30000\n'
                                              'Whitening all tooth - 50000\n'
                                              '🟡 <b>SURGERY</b>\n'
                                              'Implantation (1 tooth)  - 100000\n'
                                              '🟢 <b>ORTHOPEDICS</b>\n'
                                              'Production and installation of ceramic veneers - 90000\n'
                                              'Root canal filling with zirconium crowns (1 tooth)- 70000\n'
                                              'Lumineers (1 tooth) - 80000\n'
                                              '🟠 <b>ORTHODONTICS</b>\n'
                                              'Installation of the Damon Clear bracket system - 200,600\n'
                                              'Installation of the Damon Clear + Q bracket system - 350,000\n'
                                              'Installation of the Damon 3 Mx bracket system - 200,000\n'
                                              'Installation of aesthetic ligature braces (ceramic / sapphire) - 229,000\n'
                                              'Installation of a metal bracket system (ligature) - 120560\n'
                                              'Production and installation of ceramic veneers - 90000\n',parse_mode='html')
        elif message.text == '🕐 Shedule(DD)':
            img =open('D:\Telegram\doctordent.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
        elif message.text == '📉 Promotions(DD)':
            sti = open('D:\Telegram\promotions.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Unfortunately, there are no promotions at the moment.')
        elif message.text == '📊 Rating(DD)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="url", url="https://doctor-dent.kz/otzyvy/")
            markup.add(url)
            bot.send_message(message.chat.id, 'Reviews of Doctor Dent',reply_markup=markup)
        elif message.text == '🌐 Social networks(DD)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="Official site", url="https://doctor-dent.kz/")
            url1 = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/doctor_dent/")
            url2 = types.InlineKeyboardButton(text="2GIS", url="https://2gis.kz/nur_sultan/firm/70000001018355777?m=71.427938%2C51.115763%2F16")
            markup.add(url,url1,url2)
            bot.send_message(message.chat.id, 'Social networks', reply_markup=markup)
        elif message.text == '🎁 Promotional code(DD)':
            bot.send_message(message.chat.id, 'Input promotianal code\nP.S. Enter the promo code in CAPITAL LETTERS!')
        if message.text == "YERKE":
            sti = open('D:\Telegram\cong.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Congratulations, now you have -15% on all therapy services of the Doctor Dent dental clinic. '
                                                  'Show this message to the administrator and get your bonus.')
        # -----------------------------------------------------DoctorDent INFO------------------------------------------------#

        # -----------------------------------------------------LabSmile INFO------------------------------------------------#
        elif message.text == '📍 Addresses(LS)':
            bot.send_message(message.chat.id, "📍 <b>Nur-Sultan,Kazakhstan</b>\nMangilik El\n"
                                              "📍 <b>Almaty,Kazakhstan</b>\n Abaya Avenue,51/53 \n"
                                              "📍 <b>Atyrau,Kazakhstan</b>\n Nursaya micro-district,73/2" ,parse_mode='html')
        elif message.text == '📞 Contacts(LS)':
            bot.send_message(message.chat.id, '📞 <b>Almaty,Kazakhstan</b>\n+7‒775‒080‒00‒17\n'
                                              '📞 <b>Atyrau,Kazakhstan</b>\n+7‒778‒509‒76‒88',parse_mode='html')
        elif message.text == '🧾 Prices(LS)':
            bot.send_message(message.chat.id, 'Diagnostic X-ray - 1 160\n'
                                              'Panoramic X-ray - 5800\n'
                                              '🟢 <b>ORTHOPEDICS</b>\n'
                                              'Manufacturing and installation of cermets on the implant - 78,900\n'
                                              'Installation of veneers - 300,000\n'
                                              'Manufacturing and installation of a metal-free zirconium crown - 100800\n'
                                              '🟠 <b>ORTHODONTICS</b>\n'
                                              'Installation bracket system - 60000\n',parse_mode='html')
        elif message.text == '🕐 Shedule(LS)':
            img = open('D:\Telegram\labsmile.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
        elif message.text == '📉 Promotions(LS)':
            sti = open('D:\Telegram\promotions.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Unfortunately, there are no promotions at the moment.')
        elif message.text == '📊 Rating(LS)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="url", url="https://www.instagram.com/lab.smile")
            markup.add(url)
            bot.send_message(message.chat.id, 'Reviews of Lab Smile', reply_markup=markup)
        elif message.text == '🌐 Social networks(LS)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="Official site", url="https://labsmile.me/SITE")
            url1 = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/lab.smile/")
            url2 = types.InlineKeyboardButton(text="2GIS", url="https://2gis.kz/nur_sultan/firm/70000001046431675")
            markup.add(url,url1,url2)
            bot.send_message(message.chat.id, 'Social networks', reply_markup=markup)
        elif message.text == '🎁 Promotional code(LS)':
            bot.send_message(message.chat.id, 'Input promotianal code\nP.S. Enter the promo code in CAPITAL LETTERS!')
        if message.text == "HTTPS":
            sti = open('D:\Telegram\cong.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Congratulations, now you have -5% on all services of the Doctor Dent dental clinic. '
                                                  'Show this message to the administrator and get your bonus.')
        # -----------------------------------------------------LabSmile INFO------------------------------------------------#

        # -----------------------------------------------------DentLux INFO------------------------------------------------#
        elif message.text == '📍 Addresses(DL)':
            bot.send_message(message.chat.id,"📍 <b>Almaty,Kazakhstan</b>\nKabanbay Batyr,122A\nRozybakiev,105\nSholokhov,15\n"
                                             "📍 <b>Nur-Sultan,Kazakhstan</b>\nAbay Avenue,28\nKazhymukan,12\nSaraishyk,5\n"
                                             "📍 <b>Atyrau,Kazakhstan</b>\nKulmanov street,1(Grand Atyrau residential complex)\n"
                                             "📍 <b>Ust-Kamenogorsk,Kazakhstan</b>\nNursultan Nazarbayev Avenue,29/23\n"
                                             "📍 <b>Kokshetau,Kazakhstan</b>\nAuelbekova,129/20\n"
                                             "📍 <b>Uralsk,Kazakhstan</b>\nIhsanova,52",parse_mode='html')
        elif message.text == '📞 Contacts(DL)':
            bot.send_message(message.chat.id, "📞 <b>Almaty,Kazakhstan</b>\n+7 (727) 312-33-33\n+7 (707) 312-33-33\n"
                                              "📞 <b>Nur-Sultan,Kazakhstan</b>\n Call center:+7 (7172) 696-333\n+7 (747) 312-33-30\n"
                                              "📞 <b>Atyrau,Kazakhstan</b>\n+7 (7122) 98-00-98\n+7 (707) 312-33-60\n"
                                              "📞 <b>Ust-Kamenogorsk,Kazakhstan</b>\nCall center:+7 (7232) 48-90-99\n+7 (747) 312-33-99\n"
                                              "📞 <b>Kokshetau,Kazakhstan</b>\n+7 (7162) 90-10-30\n+7 (747) 312-33-00\n"
                                              "📞 <b>Uralsk,Kazakhstan</b>\n+7 (7112) 98-13-11\n+7 (747) 312-33-36",parse_mode='html')
        elif message.text == '🧾 Prices(DL)':
            bot.send_message(message.chat.id, 'Diagnostic X-ray - 1 160\n'
                                              'Panoramic X-ray - 5800\n'
                                              '🔴 <b>THERAPY</b>\n'
                                              'Restoration of one tooth surface during the treatment of: superficial caries - 13 330\n'
                                              'Restoration of one tooth surface in the treatment of: deep caries - 16670\n'
                                              'Reconstruction and transformation: with treatment of complicated caries, with filling of one canal - 32120\n'
                                              'Manufacturing and installation of individual ceramic restorations (inlays) for moderate caries - 69480\n'
                                              'Filling a milk tooth with a light composite: in the treatment of superficial caries - 13,080\n'
                                              'Removal of dental plaque with the "Air Flow" apparatus (1 tooth) - 680\n'
                                              'Removal of dental plaque with ultrasound (1 tooth) - 550\n'
                                              'Photobleaching with ZOOM system - 168,000\n'
                                              '🟡 <b>SURGERY</b>\n'
                                              'Extraction of a milk tooth - 3600\n'
                                              'Easy tooth extraction - 7,200\n'
                                              'Complicated Tooth Extraction - 16800\n'
                                              'Dental screw implantation - 119,400\n'
                                              '🟢 <b>ORTHOPEDICS</b>\n'
                                              'Manufacturing and installation of cermets on the implant - 86,900\n'
                                              'Production and installation of ceramic veneers - 102,000\n'
                                              'Manufacturing and installation of a metal-free zirconium crown - 99800\n'
                                              '🟠 <b>ORTHODONTICS</b>\n'
                                              'Installation of the Damon Clear bracket system - 369,600\n'
                                              'Installation of the Damon Clear 2 bracket system	- 434,500\n'
                                              'Installation of the Damon Clear + Q bracket system - 330,000\n'
                                              'Installation of the Damon Q bracket system - 253,000\n'
                                              'Installation of the Damon 3 Mx bracket system - 230 450\n'
                                              'Installation of aesthetic ligature braces (ceramic / sapphire) - 228,000\n'
                                              'Installation of a metal bracket system (ligature) - 119460',parse_mode='html')
        elif message.text == '🕐 Shedule(DL)':
            bot.send_message(message.chat.id, "<b>Monday</b>\n08:00–20:00\n"
                                              "<b>Tuesday</b>\n08:00–20:00\n"
                                              "<b>Wednesday</b>\n08:00–20:00\n"
                                              "<b>Thurday</b>\n08:00–20:00\n"
                                              "<b>Friday</b>\n08:00–20:00\n"
                                              "<b>Saturday</b>\n09:00–16:00\n"
                                              "<b>Sunday</b>\n09:00–16:00", parse_mode='html')
        elif message.text == '📉 Promotions(DL)':
            bot.send_message(message.chat.id, '<b>VEENERS</b>\n'
                                              'From 4 units cost 74,000 tenge\n'
                                              'From 8 units cost 71,500 tenge\n'
                                              'From 12 units cost 69900 tenge\n'
                                              'Note:The promotion is valid until 01.12.2020',parse_mode='html')
        elif message.text == '📊 Rating(DL)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="url", url="https://www.dent-lux.kz/comments/")
            markup.add(url)
            bot.send_message(message.chat.id, 'Reviews of Dent Lux', reply_markup=markup)
        elif message.text == '🌐 Social networks(DL)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="Official site", url="https://www.dent-lux.kz/")
            url1 = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/dent_lux/?hl=ru")
            url2 = types.InlineKeyboardButton(text="2GIS", url="https://2gis.kz/nur_sultan/firm/70000001018065478")
            markup.add(url,url1,url2)
            bot.send_message(message.chat.id, 'Social networks', reply_markup=markup)
        elif message.text == '🎁 Promotional code(DL)':
            bot.send_message(message.chat.id, 'Input promotianal code\nP.S. Enter the promo code in CAPITAL LETTERS!')
        if message.text == "ONLYJIU":
            sti = open('D:\Telegram\cong.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Congratulations, now you have -50% on all bracket installations services of the Dent Lux dental clinic. '
                                                  'Show this message to the administrator and get your bonus.')
        # -----------------------------------------------------DENTLUX INFO------------------------------------------------#

        # -----------------------------------------------------Impladent INFO------------------------------------------------#
        elif message.text == '📍 Addresses(ID)':
            bot.send_message(message.chat.id,"📍 <b>Nur-Sultan,Kazakhstan</b>\nSyganak,19\nAlmaty,13",parse_mode='html')
        elif message.text == '📞 Contacts(ID)':
            bot.send_message(message.chat.id, '📞 <b>Nur-Sultan,Kazakhstan</b>\n+7‒775‒771‒27‒57\n+7 (7172) 41‒72‒66\n+7‒708‒551‒40‒67',parse_mode='html')
        elif message.text == '🧾 Prices(ID)':
            bot.send_message(message.chat.id, '🔴 <b>THERAPY</b>\n'
                                              'Consultation of a dentist - 1000\n'
                                              'Orthodontist consultation - 1500\n'
                                              'Restoration of teeth - 25000-40000\n'
                                              'Treatment of superficial caries completed with a filling (1 tooth) - 15,000\n'
                                              'Treatment of medium caries completed with a filling (1 tooth)- 18000\n'
                                              'Treatment of deep caries completed with a filling (1 tooth) - 21000\n'
                                              'Treatment of caries under the microscope - 28000\n'
                                              'Treatment of pulpitis completed with a filling (1 tooth) - 46000\n'
                                              'Treatment of periodontitis completed with a filling (1 tooth) - 46000\n'
                                              'Treatment of pulpitis, periodontitis under the microscope - 51000\n'
                                              'Applying devitalizing paste - 4000\n'
                                              '🟡 <b>SURGERY</b>\n'
                                              'Deleting a simple - 9000\n'
                                              'Removal of average difficulty - 13000\n'
                                              'Removal of impacted wisdom teeth - 18000-30000\n'
                                              'Resection of the top of the root of the tooth - 15000\n'
                                              'Closed sinus lift - 30,000\n'
                                              'Closed sinus lift with bone grafting - 170,000 (up to 2 impls.) 220,000 (3-4 implants)\n'
                                              'Implantation (Germany-Ancylos system) - 180000\n'
                                              'Elimination of gum recession in the implant area - 50000\n'
                                              'Microimplant - 25000\n'
                                              '🟢 <b>ORTHOPEDICS</b>\n'
                                              'Removable prosthesis (Ukraine) - 30000\n'
                                              'Removable prosthesis (Germany) - 115000\n'
                                              'Clasp prosthesis (on interlocks Germany) - 150000\n'
                                              'Ball attachment prosthesis, implants(Germany) - 250000\n'
                                              'Conditionally removable prosthesis on beam fixation - 750000\n'
                                              'Temporary plastic crown on the implant - 30000\n'
                                              'One-piece crown on the implant - 35000\n'
                                              'All-ceramic veneer (Emax) - 80000\n'
                                              'Removing the cermet crown - 4000\n'
                                              'Ceramic tab - 60000\n'
                                              'Kappa - 25000\n'
                                              '🟠 <b>ORTHODONTICS</b>\n'
                                              'Metal braces (USA, 1 jaw) - 75000'
                                              'Orthodontic plate (standard) - 25000\n'
                                              'Orthodontic plate (complex) - 35000\n'
                                              'Retention Kappa (1 jaw) - 15000\n'
                                              'Retainer (1 jaw) - 15000\n'
                                              'Plate repair - 9000\n'
                                              'Replacing the screw on the plate - 10000\n'
                                              'Fixing an orthodontic ring or bracket when peeling off - 1000\n'
                                              'Fixing the metal button - 1000\n'
                                              'Replacement elastomers - 1000\n'
                                              'Removal of the bracket system (1 jaw) - 3000',parse_mode='html')
        elif message.text == '🕐 Shedule(ID)':
            img = open('D:\Telegram\impladent.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
        elif message.text == '📉 Promotions(ID)':
            sti = open('D:\Telegram\promotions.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Unfortunately, there are no promotions at the moment.')
        elif message.text == '📊 Rating(ID)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="url", url="https://impladent.kz/about-us/")
            markup.add(url)
            bot.send_message(message.chat.id, 'Reviews of Impladent', reply_markup=markup)
        elif message.text == '🌐 Social networks(ID)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            url = types.InlineKeyboardButton(text="Official site", url="https://impladent.kz/")
            url1 = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/impladent.kz/")
            url2 = types.InlineKeyboardButton(text="2GIS", url="https://2gis.kz/nur_sultan/firm/70000001024302644")
            markup.add(url,url1,url2)
            bot.send_message(message.chat.id, 'Social networks', reply_markup=markup)
        elif message.text == '🎁 Promotional code(ID)':
            bot.send_message(message.chat.id, 'Input promotianal code\nP.S. Enter the promo code in CAPITAL LETTERS!')
        if message.text == "DIASKAMZA":
            sti = open('D:\Telegram\cong.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Congratulations, now you have -99% on all services of the Impladent dental clinic. '
                                                  'Show this message to the administrator and get your bonus.')
        # -----------------------------------------------------Impladent INFO------------------------------------------------#

        # -----------------------------------------------------Dental clinics BUTTON------------------------------------------------#
        elif message.text == 'Dental clinics🦷':
            markup_inline = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text="Doctor Dent", callback_data='DoctorDent')
            item2 = types.InlineKeyboardButton(text="Lab Smile", callback_data='LabSmile')
            item3 = types.InlineKeyboardButton(text="Dent Lux", callback_data='DentLux')
            item4 = types.InlineKeyboardButton(text="Impladent", callback_data='Impladent')
            markup_inline.add(item1, item2,item3,item4)
            bot.send_message(message.chat.id, 'Choose dental clinic🦷', reply_markup=markup_inline)
        # -----------------------------------------------------Dental clinics BUTTON------------------------------------------------#

        # -----------------------------------------------------Commands------------------------------------------------#
        elif message.text == '/dentalclinic':
            markup_inline = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text="Doctor Dent", callback_data='DoctorDent')
            item2 = types.InlineKeyboardButton(text="Lab Smile", callback_data='LabSmile')
            item3 = types.InlineKeyboardButton(text="Dent Lux", callback_data='DentLux')
            item4 = types.InlineKeyboardButton(text="Impladent", callback_data='Impladent')
            markup_inline.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Choose dental clinic🦷', reply_markup=markup_inline)
        # -----------------------------------------------------Commands------------------------------------------------#

        # -----------------------------------------------------BACK TO INLINE------------------------------------------------#
        elif message.text == '⬅️Back':
            markup_inline = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text="Doctor Dent", callback_data='DoctorDent')
            item2 = types.InlineKeyboardButton(text="Lab Smile", callback_data='LabSmile')
            item3 = types.InlineKeyboardButton(text="Dent Lux", callback_data='DentLux')
            item4 = types.InlineKeyboardButton(text="Impladent", callback_data='Impladent')
            markup_inline.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Choose dental clinic🦷', reply_markup=markup_inline)
         # -----------------------------------------------------BACK TO INLINE------------------------------------------------#

#---------------------------------------------------------------Message like a text-------------------------------------------------------#


# -----------------------------------------------------Callback Function(INLINE KEYBOARD)------------------------------------------------#
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
             # -----------------------------------------------------DOCTORDENT_INLINE------------------------------------------------#
            if call.data == 'DoctorDent':
                markup_reply_DD = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1_DD = types.KeyboardButton(text='📍 Addresses(DD)')
                button2_DD = types.KeyboardButton(text='📞 Contacts(DD)')
                button3_DD = types.KeyboardButton(text='🧾 Prices(DD)')
                button8_DD = types.KeyboardButton(text='🕐 Shedule(DD)')
                button4_DD = types.KeyboardButton(text='📉 Promotions(DD)')
                button5_DD = types.KeyboardButton(text='📊 Rating(DD)')
                button6_DD = types.KeyboardButton(text='🌐 Social networks(DD)')
                button7_DD = types.KeyboardButton(text='🎁 Promotional code(DD)')
                button9 = types.KeyboardButton(text='⬅️Back')
                markup_reply_DD.add(button1_DD, button2_DD, button3_DD,button8_DD, button4_DD, button5_DD, button6_DD,button7_DD,button9)
                sti = open('D:\Telegram\AnimatedSticker.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, '<i>Select the service</i>\n<b>Note</b>: DD it is Doctor Dent',parse_mode='html',reply_markup=markup_reply_DD)
            # -----------------------------------------------------DOCTORDENT_INLINE------------------------------------------------#

            # -----------------------------------------------------LABSMILE_INLINE------------------------------------------------#
            elif call.data == 'LabSmile':
                markup_reply_LS = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1_LS = types.KeyboardButton(text='📍 Addresses(LS)')
                button2_LS = types.KeyboardButton(text='📞 Contacts(LS)')
                button3_LS = types.KeyboardButton(text='🧾 Prices(LS)')
                button8_LS = types.KeyboardButton(text='🕐 Shedule(LS)')
                button4_LS = types.KeyboardButton(text='📉 Promotions(LS)')
                button5_LS = types.KeyboardButton(text='📊 Rating(LS)')
                button6_LS = types.KeyboardButton(text='🌐 Social networks(LS)')
                button7_LS = types.KeyboardButton(text='🎁 Promotional code(LS)')
                button9 = types.KeyboardButton(text='⬅️Back')
                sti = open('D:\Telegram\AnimatedSticker.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                markup_reply_LS.add(button1_LS, button2_LS, button3_LS,button8_LS, button4_LS, button5_LS, button6_LS ,button7_LS,button9 )
                bot.send_message(call.message.chat.id, '<i>Select the service</i>\n<b>Note</b>: LB it is Lab Smile',parse_mode='html', reply_markup=markup_reply_LS)
            # -----------------------------------------------------LABSMILE_INLINE------------------------------------------------#

            # -----------------------------------------------------DENTLUX_INLINE------------------------------------------------#
            elif call.data == 'DentLux':
                markup_reply_DL = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1_DL = types.KeyboardButton(text='📍 Addresses(DL)')
                button2_DL = types.KeyboardButton(text='📞 Contacts(DL)')
                button3_DL = types.KeyboardButton(text='🧾 Prices(DL)')
                button8_DL = types.KeyboardButton(text='🕐 Shedule(DL)')
                button4_DL = types.KeyboardButton(text='📉 Promotions(DL)')
                button5_DL = types.KeyboardButton(text='📊 Rating(DL)')
                button6_DL = types.KeyboardButton(text='🌐 Social networks(DL)')
                button7_DL = types.KeyboardButton(text='🎁 Promotional code(DL)')
                button9 = types.KeyboardButton(text='⬅️Back')
                markup_reply_DL.add(button1_DL, button2_DL, button3_DL,button8_DL,button4_DL, button5_DL, button6_DL,button7_DL,button9)
                sti = open('D:\Telegram\AnimatedSticker.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, '<i>Select the service</i>\n<b>Note</b>: DL it is Dent Lux',parse_mode='html', reply_markup=markup_reply_DL)
            # -----------------------------------------------------DENTLUX_INLINE------------------------------------------------#

            # -----------------------------------------------------IMPLADENT_INLINE------------------------------------------------#
            elif call.data == 'Impladent':
                markup_reply_ID = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1_ID = types.KeyboardButton(text='📍 Addresses(ID)')
                button2_ID = types.KeyboardButton(text='📞 Contacts(ID)')
                button3_ID = types.KeyboardButton(text='🧾 Prices(ID)')
                button8_ID = types.KeyboardButton(text='🕐 Shedule(ID)')
                button4_ID = types.KeyboardButton(text='📉 Promotions(ID)')
                button5_ID = types.KeyboardButton(text='📊 Rating(ID)')
                button6_ID = types.KeyboardButton(text='🌐 Social networks(ID)')
                button7_ID = types.KeyboardButton(text='🎁 Promotional code(ID)')
                button9 = types.KeyboardButton(text='⬅️Back')
                markup_reply_ID.add(button1_ID, button2_ID, button3_ID,button8_ID, button4_ID, button5_ID, button6_ID,button7_ID,button9)
                sti = open('D:\Telegram\AnimatedSticker.tgs' ,'rb' )
                bot.send_sticker(call.message.chat.id ,sti)
                bot.send_message(call.message.chat.id, '<i>Select the service</i>\n<b>Note</b>: ID it is Impladent',parse_mode='html', reply_markup=markup_reply_ID)
            # -----------------------------------------------------IMPLADENT_INLINE------------------------------------------------#

# -----------------------------------------------------Callback Function(INLINE KEYBOARD)------------------------------------------------#

# -----------------------------------------------------RUNNNING CODE------------------------------------------------#
bot.polling(none_stop=True,interval=0)