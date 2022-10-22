INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (1, 'bojan_58', '%CEF+riRw6', 'Пимен Иосифович Селезнев', '83711755445', 1);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (2, 'samsonovavera', 'luIr)6HL$5', 'Пахом Бенедиктович Дементьев', '89541383909', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (3, 'novikovmaksimiljan', ')kO6e6LcjI', 'Ефим Харитонович Мамонтов', '72512336609', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (4, 'moke_29', 'gEDV44o7e)', 'Федосий Ермилович Гришин', '83116822717', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (5, 'nbeljakova', 'N*5KxiG*4q', 'Алла Альбертовна Логинова', '70087300035', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (6, 'oksana_59', 'I6JQ79jD%m', 'Бирюков Денис Гурьевич', '80330854745', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (7, 'sitnikovaakulina', '*tVu8Boy@h', 'Андроник Харлампьевич Беляков', '71179259549', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (8, 'fedoseevvladimir', ')nWYjB4^K3', 'Жданов Дементий Ефимьевич', '86900545799', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (9, 'agata83', 'f7iTh_vx(A', 'Милен Жанович Третьяков', '74807670282', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (10, 'anike2003', '+^(JHOmVn2', 'Нина Кузьминична Тарасова', '71219008872', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (11, 'markovprohor', '1sLkR7ac&)', 'Колобова Евдокия Никифоровна', '82575410260', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (12, 'arhip2017', 'fX@%4rGqJr', 'Дарья Алексеевна Гусева', '85233078581', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (13, 'afinogen95', '!2vlBb8cvy', 'Валерий Арсеньевич Давыдов', '84678696038', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (14, 'melnikovamilitsa', '@xW5h(idm7', 'Прокл Борисович Зыков', '83997242872', 2);
INSERT INTO user (id, login, password, full_name, phone, role)
VALUES (15, 'noskovaverjan', '7(Sw1Qvt+1', 'Эмиль Федосьевич Носов', '82373953471', 2);
INSERT INTO region (id, name)
VALUES (1, 'Югорск');
INSERT INTO region (id, name)
VALUES (2, 'Котлас');
INSERT INTO region (id, name)
VALUES (3, 'Алагир');
INSERT INTO region (id, name)
VALUES (4, 'Дудинка');
INSERT INTO region (id, name)
VALUES (5, 'Онега');
INSERT INTO region (id, name)
VALUES (6, 'Неплюевка');
INSERT INTO region (id, name)
VALUES (7, 'Забайкальск');
INSERT INTO region (id, name)
VALUES (8, 'Дальнереченск');
INSERT INTO region (id, name)
VALUES (9, 'Туруханск');
INSERT INTO region (id, name)
VALUES (10, 'Губкинский');
INSERT INTO region (id, name)
VALUES (11, 'Можайск');
INSERT INTO region (id, name)
VALUES (12, 'Пышма');
INSERT INTO region (id, name)
VALUES (13, 'Киренск');
INSERT INTO region (id, name)
VALUES (14, 'Шоровые пруды');
INSERT INTO region (id, name)
VALUES (15, 'Сызрань');
INSERT INTO region (id, name)
VALUES (16, 'Иваново');
INSERT INTO region (id, name)
VALUES (17, 'Ведено');
INSERT INTO region (id, name)
VALUES (18, 'Соль-Илецк');
INSERT INTO region (id, name)
VALUES (19, 'Холмск');
INSERT INTO region (id, name)
VALUES (20, 'Кемерово');
INSERT INTO mountain (id, region_id, name, height)
VALUES (1, 1, 'Бандук', 4380);
INSERT INTO mountain (id, region_id, name, height)
VALUES (2, 2, 'Аныйтайга', 2973);
INSERT INTO mountain (id, region_id, name, height)
VALUES (3, 3, 'Дан-Бланш', 3907);
INSERT INTO mountain (id, region_id, name, height)
VALUES (4, 4, 'Нархиях', 3671);
INSERT INTO mountain (id, region_id, name, height)
VALUES (5, 5, 'Кекеш', 2189);
INSERT INTO mountain (id, region_id, name, height)
VALUES (6, 6, 'Гестола', 4279);
INSERT INTO mountain (id, region_id, name, height)
VALUES (7, 7, 'Лостун', 2481);
INSERT INTO mountain (id, region_id, name, height)
VALUES (8, 8, 'Метеген', 2909);
INSERT INTO mountain (id, region_id, name, height)
VALUES (9, 9, 'Конгур', 2223);
INSERT INTO mountain (id, region_id, name, height)
VALUES (10, 10, 'Варгилам', 2139);
INSERT INTO difficulty (id, name, rating)
VALUES (1, 'Легкий', 1);
INSERT INTO difficulty (id, name, rating)
VALUES (2, 'Нормальный', 2);
INSERT INTO difficulty (id, name, rating)
VALUES (3, 'Средний', 3);
INSERT INTO difficulty (id, name, rating)
VALUES (4, 'Тяжелый', 4);
INSERT INTO difficulty (id, name, rating)
VALUES (5, 'Очень тяжелый', 5);
INSERT INTO tag (id, name)
VALUES (1, 'Экскурсионные');
INSERT INTO tag (id, name)
VALUES (2, 'Джип-туры');
INSERT INTO tag (id, name)
VALUES (3, 'Пещеры');
INSERT INTO tag (id, name)
VALUES (4, 'Проживание в отеле');
INSERT INTO tag (id, name)
VALUES (5, 'Наличие душа');
INSERT INTO tag (id, name)
VALUES (6, 'Наличие питания');
INSERT INTO tag (id, name)
VALUES (7, 'Зимние');
INSERT INTO tag (id, name)
VALUES (8, 'С экипировкой');
INSERT INTO tag (id, name)
VALUES (9, 'На вершины');
INSERT INTO tag (id, name)
VALUES (10, 'Ночные');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (1, 5, 1, 11, 'Чудеса зимнего Байкала', 'Для одних – мощное место силы, для других — удивительный природный объект с уникальной эко-системой, для третьих – священное место, овеянное легендами. Часто говорят, Зимний Байкал —  это самый большой каток в мире. С этим трудно поспорить. Но природа задумала его явно для другого.');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (2, 2, 2, 12, 'Красоты Дагестана', 'Вы всё ещё думаете, куда съездить, чтобы за короткое время увидеть сразу множество удивительных мест? ');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (3, 3, 4, 13, 'Счастье в горах', 'Счастье не за горами, счастье в горах!  Хотите хорошо отдохнуть и увидеть множество прекрасных и удивительных мест за короткое время? Тогда нам точно по пути !');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (4, 7, 1, 14, 'Загадки каспийских берегов', '«Загадки каспийских берегов» покорит ваше сердце навсегда! вас ожидают увлекательнейшее путешествие через пески и море, старинные крепости и невероятные высокогорные аулы! Именно в этом туре вы сможете ощутить себя настоящим первооткрывателем!');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (5, 3, 5, 15, 'Пленительный Северный Кавказ', 'Насыщенная программа включает природные красоты и достопримечательности Северного Кавказа.');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (6, 8, 2, 16, 'Мульти-каникулы в горах', 'Проведите каникулы с детьми активно, на свежем воздухе и вы обязательно вернетесь в город полными сил!');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (7, 1, 4, 17, 'Путешествие «Золотое кольцо Алтая»', 'Золотое кольцо Алтая – самый популярный туристический маршрут для путешественников, которые хотят открыть для себя регион Горного Алтая с комфортным передвижением на микроавтобусе и полноценным отдыхом в домиках в ночное время. ');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (8, 6, 4, 18, 'Впечатления на всю жизнь', 'Тур позволяет увидеть все знаковые места «Вокруг Эльбруса», включая горные группы «Перевал Актопрак», «Чегемское ущелье», сохранившие нетронутую дикую природу Кавказа. В  первый день баня, и во второй подъем на канатной дороге  на самую высокую гору в Европе, ну  а после  купание в целебных термальных источниках!');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (9, 5, 1, 19, 'Вдоль хребта', 'Добраться до самой высокой точки Европы, увидеть легендарные озера и водопады, а так же  влюбиться в пейзажи Кавказа и познакомиться с гостеприимством этого края.');
INSERT INTO tour (id, mountain_id, difficulty_id, starting_point_id, name, description)
VALUES (10, 9, 2, 20, 'Впервые в Абхазию', 'В программе этого путешествия -  знаковые места маленькой кавказской республики Этот тур  идеален для тех, кто поедет в Абхазию впервые. Но даже если вы уже здесь бывали, наверняка, вы найдёте в ней что-то новое.');
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (1, 1, 9);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (2, 1, 9);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (3, 1, 2);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (4, 2, 6);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (5, 2, 5);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (6, 2, 3);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (7, 3, 2);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (8, 3, 1);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (9, 4, 9);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (10, 4, 10);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (11, 4, 6);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (12, 4, 2);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (13, 4, 3);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (14, 5, 7);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (15, 5, 8);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (16, 5, 3);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (17, 5, 1);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (18, 5, 1);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (19, 6, 5);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (20, 6, 4);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (21, 6, 2);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (22, 6, 3);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (23, 7, 1);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (24, 7, 10);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (25, 7, 7);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (26, 7, 2);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (27, 7, 8);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (28, 8, 9);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (29, 8, 9);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (30, 9, 7);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (31, 9, 4);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (32, 9, 5);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (33, 10, 7);
INSERT INTO tour_tag (id, tour_id, tag_id)
VALUES (34, 10, 3);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (1, 5, '2022-11-22 10:00:00', '2022-11-29 10:00:00', 10, 49000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (2, 1, '2022-12-17 15:00:00', '2022-12-25 15:00:00', 14, 15000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (3, 3, '2022-12-17 16:00:00', '2022-12-22 16:00:00', 9, 32000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (4, 4, '2022-11-03 15:00:00', '2022-11-13 15:00:00', 14, 51000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (5, 5, '2022-12-20 10:00:00', '2022-12-30 10:00:00', 5, 15000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (6, 2, '2022-12-12 14:00:00', '2022-12-21 14:00:00', 11, 52000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (7, 2, '2022-12-18 11:00:00', '2022-12-28 11:00:00', 7, 11000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (8, 5, '2022-12-14 11:00:00', '2022-12-22 11:00:00', 13, 13000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (9, 3, '2022-12-08 12:00:00', '2022-12-17 12:00:00', 9, 53000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (10, 9, '2022-12-30 13:00:00', '2023-01-06 13:00:00', 7, 52000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (11, 5, '2022-11-30 13:00:00', '2022-12-09 13:00:00', 12, 60000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (12, 4, '2022-12-14 16:00:00', '2022-12-20 16:00:00', 5, 53000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (13, 7, '2022-11-12 14:00:00', '2022-11-21 14:00:00', 15, 41000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (14, 7, '2022-12-14 16:00:00', '2022-12-22 16:00:00', 5, 60000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (15, 9, '2022-11-13 16:00:00', '2022-11-18 16:00:00', 11, 40000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (16, 9, '2022-12-11 11:00:00', '2022-12-20 11:00:00', 11, 49000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (17, 8, '2022-12-14 11:00:00', '2022-12-24 11:00:00', 10, 39000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (18, 5, '2022-12-29 15:00:00', '2023-01-06 15:00:00', 12, 29000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (19, 7, '2022-12-07 13:00:00', '2022-12-16 13:00:00', 5, 59000.0);
INSERT INTO offer (id, tour_id, starting_at, ending_at, max_reservations, price)
VALUES (20, 10, '2022-11-10 15:00:00', '2022-11-18 15:00:00', 7, 46000.0);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (1, 17, 9, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (2, 20, 8, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (3, 2, 13, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (4, 2, 15, 2, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (5, 10, 13, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (6, 2, 2, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (7, 16, 12, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (8, 17, 12, 2, 2);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (9, 18, 4, 1, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (10, 16, 4, 2, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (11, 16, 10, 2, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (12, 16, 11, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (13, 2, 1, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (14, 19, 12, 2, 2);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (15, 7, 10, 1, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (16, 5, 5, 1, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (17, 3, 14, 2, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (18, 10, 5, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (19, 13, 13, 1, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (20, 1, 15, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (21, 3, 1, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (22, 9, 8, 2, 2);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (23, 9, 6, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (24, 20, 12, 1, 2);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (25, 16, 9, 2, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (26, 9, 2, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (27, 5, 4, 3, 1);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (28, 16, 7, 1, 2);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (29, 10, 11, 1, 3);
INSERT INTO reservation (id, offer_id, user_id, reservations, status)
VALUES (30, 11, 12, 3, 3);
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (1, 29, 8, 'Всё чудесно!', '2022-10-18 23:59:08');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (2, 3, 10, 'Это была моя первая поездка в горы', '2022-10-10 15:00:52');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (3, 11, 9, null, '2022-10-05 12:47:13');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (4, 17, 9, null, '2022-10-12 15:11:04');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (5, 17, 7, 'Природа уникальная, красота нереальная.', '2022-10-19 22:07:00');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (6, 28, 7, null, '2022-10-09 19:13:43');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (7, 24, 8, 'Походы, поездки, полет на параплане, все было здорово!', '2022-10-01 01:13:57');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (8, 22, 2, 'Очень опасное приключение!', '2022-10-04 23:53:38');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (9, 7, 10, 'В одиночку было бы не так интересно, спасибо организаторам за атмосферу и ребятам за хорошую компанию', '2022-10-05 18:43:19');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (10, 26, 5, null, '2022-10-12 00:18:37');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (11, 11, 1, 'Всё ужасно!', '2022-09-30 16:14:54');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (12, 1, 5, null, '2022-10-11 05:17:10');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (13, 13, 7, 'Это была замечательная поездка с проживанием в горах.', '2022-09-22 03:36:46');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (14, 21, 6, null, '2022-10-10 06:38:12');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (15, 9, 2, 'Организация оставляет желать лучшего', '2022-10-21 11:01:20');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (16, 14, 2, null, '2022-09-22 14:22:37');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (17, 2, 2, 'Ничего удивительного не показали', '2022-10-13 01:50:10');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (18, 20, 10, null, '2022-10-18 14:34:29');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (19, 16, 3, 'Я думал, что тур будет интересней', '2022-09-25 04:20:58');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (20, 17, 9, 'Все прошло очень хорошо и эмоции нас захлестнули', '2022-10-20 17:30:31');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (21, 17, 6, null, '2022-10-11 06:57:11');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (22, 12, 3, 'Не стоит своих денег', '2022-09-29 09:12:27');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (23, 8, 1, null, '2022-09-27 18:51:09');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (24, 5, 2, 'Не удовлетворяет описанию', '2022-10-07 02:32:12');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (25, 19, 7, 'Парни с хорошим чувством юмора, веселили нас всю поездку. Знают историю и традиции и очень увлекательно было слушать!', '2022-10-15 15:12:10');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (26, 20, 10, null, '2022-10-16 05:41:25');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (27, 21, 7, null, '2022-10-08 18:08:52');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (28, 5, 10, 'Горы - это моя любовь! Безумно красивые, воздух кристально чистый, природа сказочная. Многообразие пейзажей и мест от которых захватывает дух!', '2022-09-28 00:29:18');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (29, 8, 8, null, '2022-09-25 01:42:26');
INSERT INTO review (id, reservation_id, rating, comment, created_at)
VALUES (30, 22, 9, 'Станислав интересно рассказывал и отвечал на все вопросы. Буду рекомендовать в дальнейшем своим знакомым)', '2022-09-30 10:46:13');
