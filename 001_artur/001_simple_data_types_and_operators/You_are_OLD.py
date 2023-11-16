# id_code = "38711122226"
#
# ddays = id_code[5:7]
# mmonth = id_code[3:5]
# yyears = id_code[1:3]
#
# print(f'Your date of birth: {ddays}.{mmonth}.19{yyears}')
###############################################################################################################
id_code = 38711122226
i = int(id_code [6:9])
maakond = None
maakond = {(01:010): 'Kuressaare haigla',
(011:019): 'Tartu Ülikooli Naistekliinik',
(021:150): 'Ida-Tallinna keskhaigla Pelgulinna sünnitusmaja Tallinn',
(151:160): 'Keila haigla',
(161:220): 'Rapla haigla Loksa haigla Hiiumaa haigla Kärdla',
(221:270): 'Ida-Viru keskhaigla Kohtla-Järve endine Jõhvi',
(271:370): 'Maarjamõisa kliinikum Tartu Jõgeva haigla',
(371:420): 'Narva haigla',
(421:470): 'Pärnu haigla',
(471:490): 'Haapsalu haigla',
(491:520): 'Järvamaa haigla Paide',
(521:570): 'Rakvere haigla Tapa haigla',
(571:600): 'Valga haigla',
(601:650): 'Viljandi haigla',
(651:700): 'Lõuna-Eesti haigla Võru Põlva haigla',}

if i in {maakond}:
print(f'You were born in: {maakond}')
