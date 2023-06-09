OPERATORS = {
            'MegaFon': 'ПАО "Мегафон", Россия, 127006, г. Москва, пер. Оружейный, д. 41, офис 48.',
            'Tele2': 'ООО "Т2 Мобайл", Россия, 603000, г. Нижний Новгород, пер. Холодный, д. 10 А',
            'Rostelecom': 'ПАО "Ростелеком", Россия, 123298, Москва, ул. 3-я Хорошевская, дом 17, корп.1, Tel.: +7 (499) 998-16-16, E-Mail: info@center.rt.ru',
            'NCNET': 'ПАО "Ростелеком", Россия, 123298, Москва, ул. 3-я Хорошевская, дом 17, корп.1, Tel.: +7 (499) 998-16-16, E-Mail: info@center.rt.ru',
            'SPBNIT': 'ПАО "Ростелеком", Россия, 123298, Москва, ул. 3-я Хорошевская, дом 17, корп.1, Tel.: +7 (499) 998-16-16, E-Mail: info@center.rt.ru',
            'Mobile TeleSystems': 'ПАО "МТС", Россия, 109147, Москва, ул. Марксистская, 4',
            'Comstar-Regions': 'ПАО "МТС", 109147, Россия, Москва, ул. Марксистская, 4',
            'MTS': 'ПАО "МТС", Россия, 109147, Москва, ул. Марксистская, 4',
            'Vimpelcom': 'ПАО "Вымпел-Коммуникации", 127083, Москва, ул. 8 Марта, д. 10, стр. 14 Tel.: +88007008378 fax-no: +74957871990',
            'Corbina': 'ПАО "Вымпел-Коммуникации 127083, Москва, ул. 8 Марта, д. 10, стр. 14 Tel.: +88007008378 fax-no: +74957871990"',
            'Electrica': ' ООО "Электрика", Россия, 160009, г. Вологда, Огородный переулок, дом 7',
            'AKADO-Stolitsa': 'ЗАО "АКАДО-Столица", 117519, Москва, Варшавское шоссе, д. 133 Tel.: +7(499) 940–00–00 E-Mail: info@akado.ru, info@akado.com',
            'Comcor': 'ЗАО "АКАДО-Столица", 117519, Москва, Варшавское шоссе, д. 133 Tel.: +7(499) 940–00–00 E-Mail: info@akado.ru, info@akado.com',
            'Hetzner Online GmbH': 'Германия, Hetzner Online GmbH, Industriestr. 25, 91710 Gunzenhausen, Deutschland, Tel.: +49(0)9831 505-0, E-Mail: info@hetzner.com',
            'Itkm ISP': 'ООО "Ивантеевские телекоммуникации, Россия, 141282, Московская обл, г. Ивантеевка, ул. Толмачева, д. 8, офис 2, Tel.: +74965367440,E-Mail: itkm@itkm.su',
            'Ivanteevskie telecommunicacii Ltd': 'ООО "Ивантеевские телекоммуникации, Россия, 141282, Московская обл, г. Ивантеевка, ул. Толмачева, д. 8, офис 2, Tel.: +74965367440,E-Mail: itkm@itkm.su',
            'Ivanteevskie telekommunikacii LLC': 'ООО "Ивантеевские телекоммуникации, Россия, 141282, Московская обл, г. Ивантеевка, ул. Толмачева, д. 8, офис 2, Tel.: +74965367440,E-Mail: itkm@itkm.su',
            'SCALEWAY': 'Франция, SCALEWAY S.A.S., BP 438, F-75366 Paris Cedex 08',
            'UK2.NET': 'Великобритания, UK-2 Limited, 5th Floor, Voyager House, Chicago Avenue, Manchester Airport M90 3DQ, United Kingdom',
            'FDCservers.net': 'США, FDC Servers.net, LLC, Tel.: 312-423-6675, E-Mail: lawenforcement@fdcservers.net',
            '100TB': 'США, Hosting Services, Inc, 517 W 100 N, Suite 225, Providence, UT 84332, Tel.: 1-888-395-0752, E-Mail: sales@100TB.com',
            'Public Joint-Stock Company "Bank Otkritie Financial Corporation"': 'ПАО «Открытие», 115114, г. Москва, ул. Летниковская, д. 2, стр. 4, info@open.ru, 8 (495) 224-44-00',
            'Navigator networks': 'ООО "Навигатор", Россия, г. Вологда, ул.Предтеченская, 31, офис 204',
            'Spectrum': 'США, Charter Communications Inc, Stamford, Connecticut, Tel.: +1-877-777-2263, E-Mail: abuse@charter.net',
            'INPL': 'Ishan Group, 360001, Rajkot, Nakshatra-IV, 2nd Floor, Dr.Radhakrishnan Road, Nr. Kathiyawad Gymkhana, E-Mail: hello@ishanitech.biz',
            'KOMTEL': 'ООО "Антенна" 155810, Ивановская область, г. Кинешма, Красногорская ул., д.6  Tel.: 8 (49331) 5-17-46',
            'Magticom Ltd': 'ООО MAGTICOM Тбилиси, ул.Анны Политковской 7, Tel.: +995 32 217 00 00 E-Mail: office@magticom.ge',
            'ACT Fibernet': 'Atria Convergence Technologies Ltd., Head Office, 8-2-618/1/2, Road No. 11, Mithila Nagar, Banjara Hills, Hyderabad Tel.:+91 - 7288999999 E-Mail: helpdesk.blr@actcorp.in',
            'PT WIRELESS INDONESIA ( WIN )': '(Индонезия) Graha Almeira 4th Floor, Jl. Bangka Raya 27A, Mampang Pela, Jakarta Selatan 12720 Tel.: +62-21-22715321 E-Mail: abuse@wirelessnet.id',
            'Bharti Airtel': 'Bharti Airtel Ltd. Airtel Center, Plot No. 16 Udhyog Vihar Gurgaon ',
            'Yandex enterprise network': 'ООО ЯНДЕКС 119021, Москва, ул. Льва Толстого 16 Tel.: 7 495 739 7000',
            'Criteo Europe': 'Criteo 32 Rue Blanche 75009 Paris E-Mail: dpo@criteo.com',
            'SLTADSL-SLT': 'Internet Division 7th floor OTS Building Sri Lanka Telecom E-Mail: abuse@slt.lk',
            'M247': '(Германия) M247 Ltd, Hanauer Landstraße 302, Hessen 60314, Frankfurt E-Mail:  ro-legal@m247.com',
            'TVINGO Telecom Ltd': 'ООО "Твиго Телеком", 362048, РСО Алания г. Владикавказ Проспект Доватора, дом 23/1. Tel.: (8672)29-00-00 E-Mail: support@tvingo.ru fax-no: (8672)52-35-98',
            'Telegram Messenger San Francisco Network': 'LLC Globalnet, Россия, Санкт-Петербург, Выборгское шоссе, д. 36 Tel.: +7(812)676-50-00,fax-no: +7(812)676-50-01, E-Mail: info@gblnet.ru',
            'MULTISTREAM-CHER': 'ООО "Мультистрим", Череповец, ул. Ленинградская, д. 43, E-Mail: office@multis.tv, Tel.: 79212530033, +7(8202)59-76-00, +7(8202)63-00-33',
            'Vodafone': 'Vodafone Group Plc., Англия, Ньюбери, Беркшир RG14 2FN, E-Mail: ukmediarelations@vodafone.com',
            'VF GR - xCH': 'Vodafone Group Plc., Англия, Ньюбери, Беркшир RG14 2FN, E-Mail: ukmediarelations@vodafone.com',
            'Webhost LLC': 'ООО «Вебхост», 115114, г. Москва, ул. Летниковская, д. 10, стр. 2, этаж 5, пом. VI, ком. 532, Tel.: +7(495)666-56-67',
            'TRANS-TELECOM': 'АО «Транстелеком», 119530, г. Москва, Очаковское шоссе, 34, офис А511, Tel.: +7(495)775-6559, +7(495)694-7940, fax-no: +7(495)775-6569 E-Mail: secretary@transtelecom.ru',
            'HostRoyale Technologies Pvt Ltd': 'ООО «Пулнет», Санкт-Петербург, проезд 7-й Предпортовый, д. 14, Литер А, помещение 97-Н, Tel.: +7812670-96-00, E-Mail: info@pulnet.ru',
            'Yandex network': 'SES. Поисковые роботы. Это автоматизированные сервисы, которые отслеживают или очищают веб-сайты, такие как поисковая система-паук или бот-система, также используемые рекламными агентствами и другими онлайн-статистическими системами',
            'SEVER-TELECOM': 'АО "СЕВЕР ТЕЛЕКОМ", г. Великий Новгород, Большая Санкт-Петербургская ул., дом. 39, 1 корпус. БЦ “ВОЛНА” 3 эт., 37 кабинет. E-Mail: info@severtm.ru, Tel.: (8162) 68-44-07',
            'Teleset LLC': 'АО «ЭР-Телеком Холдинг», Москва, 115035, Овчинниковская набережная, 20, строение 1, Tel.: +7(495)145-75-50, E-Mail: info@domru.ru',
            'Intelligence Network Online, Inc.': 'Intelligence Network Online, Inc., Лас Вегас, 3635 S. Fort Apache Road, Suite 200-39',
            'China TieTong Telecommunications Corporation': 'China TieTong Telecommunications Corporation, Китай, Jinze Mansion, 2 Guangningbo Street, Xicheng District, Beijing, Tel.: +86-13601002911, E-Mail: wpli@cmtietong.com',
            'PP "Merezha"': 'Компания "БКМ", Украина, Киев, ул. Леваневского, 34б Tel.: +38(066)777-97-09, E-Mail: support@bcm.net.ua',
            'Mail.Ru ': 'ООО "Майл.ру", Россия, 125167, г. Москва, Ленинградский проспект, д. 39, сроение 79, БЦ "SkyLight", Tel.: +7(495)7256357',
            'KGT new media': 'KGT new media, Германия, 10367, Berlin, Möllendorffstrasse, 108-109',
            'DRLINE': 'ООО "Диэрлайн", Россия, Московская область, посёлок Новый, с8, Красногорск Tel.: +7(499)705-78-48, E-Mail: noc@drline.ru',
            'Svyaz-Energo': ' ООО "Связь-энерго", Россия, г. Кострома, ул. Энергетиков, д. 5, Tel.: +7(4942)494-002, E-Mail: support@sv-en.ru',
            'Packet Exchange Limited': 'Packet Exchange Limited, Великобритания, 160, Kemp House City Road, London, EC1V 2NX, UNITED KINGDOM, E-Mail: info@packetexchange.eu',
            'Softbank BB Corp.': 'SoftBank Group Corp, Япония, Tokyo Shiodome bldg., 1-9-1, Higashi-Shimbashi, Minatoku,Tokyo, Japan',
            'Google': 'Google LLC, США, 1600 Amphitheatre Parkway, Mountain View, CA,US',
            'Kar-Tel': 'ТОО «КаР-Тел», Республика Казахстан, г.Астана, район Алматы, ул. Кадыргали Жалаири, дом 2.',
            'Deutsche Telekom AG': 'Telekom Deutschland GmbH, Германия (Представитель в России ООО "Т-Системс Си-Ай-Эс", 14, 13-я линия Васильевского острова, 199034, Санкт-Петербург, Российская Федерация)',
            'Alibaba.com': 'Alibaba Group, Китайская Народная Республика, 8 SHENTON WAY AXA TOWER, 45-01, Singapore, 068811, Singapore',
            'TE Data': 'TE Data Contact Role, Египет, 94 Tahrir Street, Dokki, 12311, Giza, Egypt, Tel.: +20-2-33320700, E-Mail: admins@tedata.net',
            'ISP "Fregat"': 'ООО "Мега Линк", 49083, Днепропетровская обл., город Днепр, УЛИЦА СОБИНОВА , дом 1, Tel.: (056) 734-44-44, E-Mail: info@fregat.com',
            'FIBIA P/S': 'Fibia P/S, Дания, Hovedgaden 36, 4520, Svinninge, DENMARK, Tel.: +4570292900, E-Mail: abuse@fibia.dk',
            'Rybinsk': 'ООО "АТЕЛ Рыбинск", Рыбинск, ул. Плеханова, д. 10, Tel.: +74855327500, E-Mail: info@atel-rybinsk.ru',
            'EarthLink Ltd': 'EarthLink Ltd. Communications&Internet Services, Ирак, Al Mansour – 14th July St.  Tel.: +9647809277493',
            'Telecel S.A.': 'Telcel, Парагвай, Calle Lago Zúrich No. 245, Edificio Telcel, Colonia Ampliación Granada, Mayors Office Miguel Hidalgo, Ciudad de México, 11529, Tel.: +595 21 618 9000, E-Mail: abuse@tigo.com.py',
            'ER-Telecom Holding': 'АО «ЭР-Телеком Холдинг», Москва, 115035, Овчинниковская набережная, 20, строение 1, Tel.: +7(495)145-75-50, E-Mail: info@domru.ru',
            'Cdn77 - PRG': 'Datacamp Ltd, Лондон, 207 Regent Street, London, United Kingdom, E-Mail: abuse@datacamp.co.uk',
            'RTA Telecom Ltd': 'ООО «РТА ТЕЛЕКОМ», 652882, Кемеровская область, г. Междуреченск, пр. Строителей, 67, Tel.: +79050683505',
            'Korea Telecom': 'Korea Network Information Center, Республика Корея, 9, Jinheung-gil, Naju-si, Jeollanam-do, 5832, Tel.: +82-1544-5118',
            'Etihad Atheeb Telecom Company': 'Etihad Atheeb Telecommunications Co., Riyadh, King Abdulaziz Road Riyadh - Kingdom of Saudi Arabia (KSA), Tel.: +966115111263',
            'Host Europe GmbH': 'Host Europe Limited, ФРГ, г. Кельн',
            'Selectel': 'ООО «Сеть дата-центров «Селектел» (сокращенное наименование ООО «Селектел»), 196084, г. Санкт-Петербург, ул. Цветочная, д. 21, лит. А, Tel.: +7(812)677-80-36, E-Mail: sales@selectel.ru',
            'TRINITY-CLNTS': 'Украина, г. Мариуполь',
            'XCOM': 'Казахстан, г. Актау',
            'Vianet Communications Pvt. Ltd': '4th Floor, Prera Business Center, Jawalakhel, Lalitpur, Bagmati Pradesh (3)',
            'A1 Telekom Austria AG': 'Австрия',
            'FLOW': 'Cable & Wireless Communications (Карибские острова)',
            'Corbina Sovam Vladivostok Broadband': 'г. Череповец',
            'OJSC Comcor': '«АКАДО Телеком», 117519, г. Москва, Варшавское ш., д.133, info@akado-telecom.ru, +7 (495) 411-71-71',
            'INETCOM': 'Инетком, 109117, г. Москва, ул. Окская, дом 5, корп. 1, info@inetcom.ru, +7 (495) 744-02-03',
            'Orange': 'Orange Business Services, Москва, 1-й Красногвардейский пр-д, 15, +7 (495) 777 0800',
            'A1 Bulgaria EAD': 'Болгария, г. София',
            'SP Kazakov Viktor Aleksandrovich': 'RealNet, Республика Крым, г. Симферополь, ул. Трубаченко, дом 7, support@realnet.ru',
            'ITC NG ltd': 'Leshem St 7, Petah Tikva, Израиль',
            'IP SERVER LLC': 'ООО "Айпи Сервер", 115419, Москва, ул. Шаболовка, 34, стр. 3',
            'Host-Telecom.com s.r.o.': 'Host-telecom.com, s.r.o. (Чехия), info@host-telecom.com, +420 391 000 777',
            'ПАО Центральный телеграф':'ПАО Центральный телеграф, 108811, Г. Москва, П. Московский, 22 КМ. Киевского ш., д.6, стр.1, тел: (495) 504-4444',
            'LLC AVANTA TELECOM':' 350087, Краснодарский край, Краснодар, ул. Пригородная, 177',
        }
