from modules.Jackbooooks import *
from colorama import init
from time import sleep as wait
import sys
import random
import psutil
import platform
from modules.CustomItems import *
from modules.ResistorColorCode import *
import os
import subprocess as sp
init()
roots = False
col = ColorsNText.rgbtoall(255,255,255,67,67,67)
settings = [['MaxPyLinux.sysroot{ boot }', True, 'Critical'], ['TerminalStyleCursor', 0, 'Design(0-2)'], ['HostEnable', False, 'Normal'], ['HostName', "MaxPyLinux", 'Design']]
sizedisk = psutil.disk_usage('C:\\')
conv = 1073741824
s = os.path.dirname(os.path.abspath(__file__))
j = lambda tw:os.path.join(s, 'sys', tw)
disk = [f'''{sizedisk.free/conv:.1f}''',f'''{sizedisk.used/conv:.1f}''',f'''{sizedisk.total/conv:.1f}''']
lang = 'ru'
name = ''
MUI = {
    'ru':{
        'help':"""ПОМОЩЬ
Подсказки:
/ - Есть альтернатива имени
() - Подсказка
Программы:
changename
sd (shutdown)
MaxCasino
RealAnswer
WIPTestProgram
EightBall / 8Ball
Python
about
helpemail
settingsroot (Требуется рут-права для поключения [+!root])
spd (SkrePyDOS)
cresistor
cmd
+!root
-!root
lang
paint""",
        'questionsRA':['ГимпБлокнот копировал и вставлял код сюда?','MaxPyLinux это улучшение MaxPyOS?','Это было основано на трёхцветном коте Макс?','ГимпБлокнот НЕ автор этой ОС на пайтон?'],
        'answersRA':{
            'yes':'Правильно!',
            'no':'Неправильно!'
        },
        'rules':'Правила:',
        'howtoSR':'''Как пользоваться:
1. При видении такой штуки: True или False (или другое значение) -
вы можете переключить их
2. НЕ ВЫКЛЮЧАТЬ MaxPyLinux.sysroot{ boot }
Команды:
1) Просмотреть
2) Изменить один 
Выбор из команд:''',
        'allquestionsCR':['''Введите список по такому примеру:
[1 цвет (0-9)], [2 цвет (0-9)], [Множитель (0-11)], [Допуск (1-2,5-8,10-11)]
(ПРЕДУПРЕЖДЕНИЕ - ПОСЛЕ ЗАПЯТЫХ СТАВЬТЕ ПРОБЕЛ!)
Ввод:''','''Введите список по такому примеру:
[1 цвет (0-9)], [2 цвет (0-9)], [3 цвет (0-9)], 
[Множитель (0-11)], [Допуск (1-2,5-8,10-11)]
(ПРЕДУПРЕЖДЕНИЕ - ПОСЛЕ ЗАПЯТЫХ СТАВЬТЕ ПРОБЕЛ!
И ЕЩЁ: НЕ ИСПОЛЬЗУЙТЕ ПЕРЕНОС!)
Ввод:''','''Введите список по такому примеру:
[1 цвет (0-9)], [2 цвет (0-9)], [3 цвет (0-9)], 
[Множитель (0-11)], [Допуск (1-2,5-8,10-11)],
[Цвет тепл.коэфф. (1-4,6-7,9)]
(ПРЕДУПРЕЖДЕНИЕ - ПОСЛЕ ЗАПЯТЫХ СТАВЬТЕ ПРОБЕЛ!
И ЕЩЁ: НЕ ИСПОЛЬЗУЙТЕ ПЕРЕНОС!)
Ввод:'''],
        'system':{
            'uRname':f'Ты теперь пользователь с другим именем.',
            'name':'Имя:',
            'restartValue':'Перезапустите программу settingsroot, чтобы продолжить.',
            'uwantValue':'Какую переменную хотите изменить?',
            'DoneValue':'Установлено!',
            'NoValue':'Не найдено'
        }
    },
    'en':{'help':'''HELP
Hints:
/ - There is an alternative name
() - Hint
Programs:
changename
sd (shutdown)
MaxCasino
RealAnswer
WIPTestProgram
EightBall / 8Ball
Python
about
helpemail
settingsroot (Requires root rights to connect [+!root])
spd (SkrePyDOS)
cresistor
cmd
+!root
-!root
lang
paint''',
        'questionsRA':['Did GimpNotepad copy and paste the code here?','Is MaxPyLinux an improvement on MaxPyOS?','Was it based on the tricolor (calico) cat Max?','GimpNotepad is NOT the author of this Python OS?'],
        'answersRA':{
            'yes':'Correct!',
            'no':'NOT Correct.'
        },
        'rules':'Rules:',
        'howtoSR':'''How to use:
1. When you see something like this: True or False (or other value) -
you can switch them
2. DO NOT TURN OFF MaxPyLinux.sysroot{ boot }
Commands:
1) View
2) Change one
Choose from commands:''',
        'allquestionsCR':['''Enter a list like this:
[1 color (0-9)], [2 color (0-9)], [Multiplier (0-11)], [Tolerance (1-2,5-8,10-11)]
(WARNING - USE A SPACE AFTER THE COMMAS!)
Input:''','''Enter a list like this:
[1 color (0-9)], [2 color (0-9)], [3 color (0-9)],
[Multiplier (0-11)], [Tolerance (1-2,5-8,10-11)]
(WARNING - USE A SPACE AFTER THE COMMAS!
AND ALSO: DO NOT USE NEWLINES!)
Input:''','''Enter a list like this:
[1 color (0-9)], [2 color (0-9)], [3 color (0-9)],
[Multiplier (0-11)], [Tolerance (1-2,5-8,10-11)],
[Color heat coeff. (1-4,6-7,9)]
(WARNING - USE A SPACE AFTER THE COMMAS!
AND ALSO: DO NOT USE NEWLINES!)
Input:'''],
    'system': {
        'uRname': f'You are now user with a different name.',
        'name': 'Name:',
        'restartValue': 'Restart the settingsroot program to continue.',
        'uwantValue': 'Which variable do you want to change?',
        'DoneValue': 'Set!',
        'NoValue': 'Not found'
    }
    }
}
wait(1)
print('SDAEMU')
wait(2)
Helpful.clearterminal()
print(ColorsNText.rgbtotext(100,200,255)+ColorsNText.rgbtobg(50,100,127)+'[root activated]'+ColorsNText.rgbtotext(100,200,25)+ColorsNText.rgbtobg(50,10,7)+'\n[root]:activating [/dev/sda/0/session]')
print(ColorsNText.rgbtotext(100,200,255)+'''Loading initial ramdisk ...

[    0.000000] MAXPyLinux version 6.8.0-31-generic (buildd@lcy02-amd64-051) (gcc (MAXPL 11.4.0-1MAXPL1~22.04) 11.4.0, GNU ld (- MAXPL) 2.38) #31-MAXPL SMP PREEMPT_DYNAMIC 
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.8.0-31-generic root=UUID=YOUR_UUID_HERE ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000] Disabled fast string operations
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001 (x87 FPU, SSE)
[    0.000000] x86/fpu: xstate_sanitize: Disabling XSAVES due to unknown fields 0x0.
''')
wait(1)
Helpful.clearterminal()
print('''[    1.234567] pci 0000:00:02.0: vgaarb: setting as primary device
[    1.234567] sd 2:0:0:0: [sda] 2000409264 512-byte logical blocks: unknown/unknown
[    1.234567] sd 2:0:0:0: [sda] Write Protect is off
[    1.234567] sd 2:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.234567] sd 2:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.234567]  sda: sda1 sda2 sda3''')
wait(0.3)
Helpful.clearterminal()
print('''[    1.234567] sd 2:0:0:0: [sda] Attached SCSI disk
[    2.123456] EXT4-fs (sda2): mounted filesystem with ordered data mode. Quota mode: none.
[    2.123456] VFS: Mounted root (ext4 filesystem) on device 8:2.
[    2.123456] devtmpfs: mounted
[    2.123456] Freeing initrd memory: 25616K
[    2.123456] systemd[1]: System has not been booted with systemd as init system (PID 1). Can't operate.''')
wait(3)
Helpful.clearterminal()
print(ColorsNText.rgbtoall(190,190,190,255,255,255)+r'''                     ___         __ _                  
  /\/\   __ ___  __ / _ \_   _  / /(_)_ __  _   ___  __
 /    \ / _` \ \/ // /_)/ | | |/ / | | '_ \| | | \ \/ /
/ /\/\ \ (_| |>  </ ___/| |_| / /__| | | | | |_| |>  < 
\/    \/\__,_/_/\_\/     \__, \____/_|_| |_|\__,_/_/\_\
                         |___/                         '''+col)
wait(4)
Helpful.clearterminal()
name = str(input('Имя пользователя (Username):'))
print(f'''Приветствую, {name}! Если нужна помощь, пиши help или ? (Hello, {name}! Type help if you need.)''')
while True:
    def cur():
        if str(settings[1][1]) == '0':
            return ':#$'
        elif str(settings[1][1]) == '1':
            return '%$'
        elif str(settings[1][1]) == '2':
            return '>$'
        else:
            return ':#$'
    cmd = input(f'''{name}{f'@{settings[3][1]}' if settings[2][1] else f''}{cur()}''')
    if cmd == 'help' or cmd == '?':
        print(MUI[lang]['help'])
    elif cmd == 'Python':
        print('Можно код запускать только один раз (неудобно) [Only 1 run...]')
        c = input(">>>")
        exec(c)
    elif cmd == '+!root':
        roots = True
    elif cmd == '-!root':
        roots = False
    elif cmd == 'changename':
        setname_ = input(MUI[lang]['system']['name'])
        name = setname_
        print(MUI[lang]['system']['uRname'])
    elif cmd == 'sd':
        Helpful.clearterminal()
        print(ColorsNText.rgbtoall(110,110,110,60,60,60)+r'''                     ___         __ _                  
  /\/\   __ ___  __ / _ \_   _  / /(_)_ __  _   ___  __
 /    \ / _` \ \/ // /_)/ | | |/ / | | '_ \| | | \ \/ /
/ /\/\ \ (_| |>  </ ___/| |_| / /__| | | | | |_| |>  < 
\/    \/\__,_/_/\_\/     \__, \____/_|_| |_|\__,_/_/\_\
                         |___/                         
                shutting down...                       ''')
        wait(2)
        sys.exit()
    elif cmd == "WIPTestProgram":
        print(f'''Work In Progress Testing Program
[root]: i <3 u
{name}:awww thanks''')
    elif cmd == "RealAnswer":
        listc = [[MUI[lang]['questionsRA'][0], 0], [MUI[lang]['questionsRA'][1], 1], [MUI[lang]['questionsRA'][2], 1], [MUI[lang]['questionsRA'][3], 0]]
        chosenqna = random.choice(listc)
        xn = input(chosenqna[0]+"\nY/N:")
        if xn == 'Y' or xn == 'y':
            if chosenqna[1] == 1:
                print(MUI[lang]['answersRA']['yes'])
            else:
                print(MUI[lang]['answersRA']['no'])
        elif xn == 'N' or xn == 'n':
            if chosenqna[1] == 0:
                print(MUI[lang]['answersRA']['yes'])
            else:
                print(MUI[lang]['answersRA']['no'])
    elif cmd == 'MaxCasino':
        print(MUI[lang]['rules']+
'''0 = 0
1 = 500
2 = 10000
3 = 5000000
4 = 100000000
5 = 50000000000
6 = 1000000000000
7 = 100000000000000000000''')
        coins = 0
        x = [random.randint(0,7),random.randint(0,7),random.randint(0,7)]
        xstr = ''.join(str(b) for b in x)
        print(str(xstr))
        for z in x:
            if z==1:
                coins=coins+500
            elif z==2:
                coins=coins+10000
            elif z==3:
                coins=coins+5000000
            elif z==4:
                coins=coins+100000000
            elif z==5:
                coins=coins+50000000000
            elif z==6:
                coins=coins+1000000000000
            elif z==7:
                coins=coins+100000000000000000000
            else:
                coins=coins+0
        print(f'Ты выиграл: {coins} коинов!')
        print(f'You won, your coins: {coins}!')
    elif cmd == 'EightBall' or cmd == '8Ball':
        ex = ["Да", 'Почти да', 'Уверен', 'Я не знаю', 'Не уверен', 'Вряд-ли', 'Почти нет', 'Нет']
        exen = ["Yes", 'Almost yes', 'I am sure', 'I do not know', 'Not sure', 'Hardly', 'Almost no', 'No']
        input('Введите вопрос (Type question):')
        if lang == 'en':
            print(random.choice(exen))
        else:
            print(random.choice(ex))
    elif cmd == 'settingsroot':
        if roots:
            m = input(MUI[lang]['howtoSR'])
            if m == '1':
                print(settings[0][0]+'|'+str(settings[0][1])+'|'+settings[0][2]+'\n'+settings[1][0]+'|'+str(settings[1][1])+'|'+settings[1][2]+'\n'+settings[2][0]+'|'+str(settings[2][1])+'|'+settings[2][2]+'\n'+settings[3][0]+'|'+str(settings[3][1])+'|'+settings[3][2])
                print(MUI[lang]['system']['restartValue'])
            elif m == '2':
                r = input(MUI[lang]['system']['uwantValue'])
                f = any(r in subl for subl in settings)
                if f:
                    print('Найдено!')
                    ji = next(i for i, sublist in enumerate(settings) if r in sublist)
                    def typeof():
                        if r == "TerminalStyleCursor":
                            return 'Число (Number)' 
                        elif r == "HostEnable":
                            return 'Выключатель (T/F)'
                        elif r == "HostName":
                            return 'Текст (Text)'
                        else:
                            return 'Неизвестный тип (Unknown)'
                    print(f"Являестя {ji} параметром (It's {ji} parameter)")
                    print(f'{typeof()}')
                    v = input(f'Значение для {r} (Value for {r}):')
                    if (r == 'MaxPyLinux.sysroot{ boot }' and v == 'F') or (r == 'MaxPyLinux.sysroot{ boot }' and v == 'f'):
                        print('''SyntaxError: invalid syntax
IndentationError: expected an indented block
touch: cannot touch '/sda/': Permission denied''')
                        wait(2)
                        print('sda emulation crashed. it will be closed at 3 seconds (Sorry for my bad english.)')
                        wait(3)
                        sys.exit()
                    elif r == "TerminalStyleCursor":
                        settings[ji][1] = int(v)
                        print(MUI[lang]['system']['DoneValue'])
                    elif r == "HostName":
                        settings[ji][1] = str(v)
                        print(MUI[lang]['system']['DoneValue'])
                    elif r == "HostEnable":
                        settings[ji][1] = True if v == 'T' or v == 't' else False
                        print(MUI[lang]['system']['DoneValue'])
                else:
                    print(MUI[lang]['system']['NoValue'])
                    continue
    elif cmd == 'about':
        print(r'''                     ___         __ _                  
  /\/\   __ ___  __ / _ \_   _  / /(_)_ __  _   ___  __
 /    \ / _` \ \/ // /_)/ | | |/ / | | '_ \| | | \ \/ /
/ /\/\ \ (_| |>  </ ___/| |_| / /__| | | | | |_| |>  < 
\/    \/\__,_/_/\_\/     \__, \____/_|_| |_|\__,_/_/\_\
                         |___/                         
                    by gimpnotepad                     ''')
        print(ColorsNText.rgbtobg(255,0,0)+' '+ColorsNText.rgbtobg(255,100,0)+' '+ColorsNText.rgbtobg(255,255,0)+' '+ColorsNText.rgbtobg(0,255,0)+' '+ColorsNText.rgbtobg(0,255,255)+' '+ColorsNText.rgbtobg(0,0,255)+' '+ColorsNText.rgbtobg(100,0,255)+' '+ColorsNText.rgbtobg(255,0,255)+' '+'\n'+ColorsNText.rgbtobg(255,255,255)+' '+ColorsNText.rgbtobg(200,200,200)+' '+ColorsNText.rgbtobg(150,150,150)+' '+ColorsNText.rgbtobg(100,100,100)+' '+ColorsNText.rgbtobg(75,75,75)+' '+ColorsNText.rgbtobg(50,50,50)+' '+ColorsNText.rgbtobg(25,25,25)+' '+ColorsNText.rgbtobg(0,0,0)+' '+ColorsNText.clear()+"\n"+ColorsNText.clear()+f'''{disk[0]}ГБ|{disk[1]}ГБ, полностью: {disk[2]}ГБ
ЦП (CPU state):{psutil.cpu_percent(interval=1):.1f}%
ОЗУ (RAM state):{psutil.virtual_memory().percent:.1f}'''+ColorsNText.rgbtoall(255,255,255,67,67,67))
        print('Тип процессора (Type of CPU):'+platform.uname().machine+'\n'+'Процессор (CPU):'+platform.uname().processor+'\n'+f'Python {sys.version}'+'\n'+f'{platform.uname().system} {platform.uname().version}')
    elif cmd == '':
        pass
    elif cmd == 'helpemail':
        print('Мой email для связи:')
        print('gimpnotepadofficial@gmail.com')
        print('''В дополнении, можно связаться в тг:
gimpnotepad''')
        print('My email for communication:')
        print('gimpnotepadofficial@gmail.com')
        print('''In addition, you can contact in tg:
gimpnotepad''')
    elif cmd == 'cresistor':
        t = input('''c(alculate color code from)Resistor
[1]4-Значные (4th color code)
[2]5-Значные (5th color code)
[3]5-значные с ppm (5th color code with ppm)
[4]Помощь (help)
[5]Выйти (exit)
Выбор:''')
        if t == '1':
            n = input(MUI[lang]['allquestionsCR'][0]).split(', ')
            o,p = RC.calculate4(int(n[0]),int(n[1]),int(n[2]),int(n[3]))
            print('--'+RC.color(int(n[0]))+RC.color(int(n[1]))+RC.color(int(n[2]))+RC.color(int(n[3]))+col+'--')
            print(f'{o}Ω {p}'+col)
        elif t == '2':
            n = input(MUI[lang]['allquestionsCR'][1]).split(', ')
            o,p = RC.calculate5(int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4]))
            print('--'+RC.color(int(n[0]))+RC.color(int(n[1]))+RC.color(int(n[2]))+RC.color(int(n[3]))+RC.color(int(n[4]))+col+'--')
            print(f'{o}Ω {p}'+col)
        elif t == '3':
            n = input(MUI[lang]['allquestionsCR'][2]).split(', ')
            o,p = RC.calculate5(int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4]))
            print('--'+RC.color(int(n[0]))+RC.color(int(n[1]))+RC.color(int(n[2]))+RC.color(int(n[3]))+RC.color(int(n[4]))+RC.color(int(n[5]))+col+'--')
            q = RC.ppm(int(n[5]))
            print(q)
            print(f'{o}Ω {p}'+col)
        elif t == '4':
            info = {
    0: (RC.color(0), 0, 1, None, None),
    1: (RC.color(1), 1, 10, "±1%", 100),
    2: (RC.color(2), 2, 100, "±2%", 50),
    3: (RC.color(3), 3, 1000, None, 15),
    4: (RC.color(4), 4, 10000, None, 25),
    5: (RC.color(5), 5, 100000, "±0.5%", None),
    6: (RC.color(6), 6, 1000000, "±0.25%", 10),
    7: (RC.color(7), 7, 10000000, "±0.1%", 5),
    8: (RC.color(8), 8, None, "±0.05%", None),
    9: (RC.color(9), 9, None, None, None),
    10: (RC.specialcolor(1), None, 0.1, "±5%", None),
    11: (RC.specialcolor(2), None, 0.01, "±10%", None)
}
            print('''1 - Цвет (Color)
2 - Число (Number)
3 - Множитель (Multiplier)
4 - Допуск (Tolerance)
5 - Тепловой коэффициент (ppm)''')
            for k in info:
                c, n, m, t, p = info[k]
                print(f'{c}|{n}|{m}|{t}|{p}')
            print("Перезапустите приложение для продолжения (reset this app for continue)"+col)
        elif t == '5':
            pass
    elif cmd == 'spd':
                Helpful.clearterminal()
                ColorsNText.clear()
                print('SkrePyDOS - коллаборация с MaxPyLinux! [Collab with MaxPyLinux!] (Напишите help) [Type help]')
                x = True
                while x:
                    g = input(">")
                    if g == 'help':
                        print('''help - помощь (help)
col - менять цвет по rgb (chenge color by rgb)
clear - чистка терминала (clear treminal)
calc - простой калькулятор (calculator)
ver - версия (version)
exit - выход обратно в MaxPylinux (с пасхалкой!)[Exit with surprise!]''')
                    elif g == 'col':
                        try:
                            r, g, b = input('''Пишите по такому примеру (Type like this): r,g,b
Ввод:''').split(',')
                            print(ColorsNText.rgbtotext(r,g,b)+"Заменено!")
                        except ValueError as r:
                            print("""ОШИБКА!""")
                    elif g == "clear":
                        Helpful.clearterminal()
                    elif g == "calc":
                        print(str(eval(input("Введите формулу (для степени используй **)[ВЗЯТО С MPL](Python calc, ^ = ** [FROM MPL])"))))
                    elif g == 'ver':
                        print('SkrePyDOS (MaxPyLinux версия/version)')
                    elif g == 'exit':
                        print('Выключение/Shutting down...')
                        x = False
                        print(r'''Traceback (most recent call last):
  File "\MaxPyLinux.py", line 333, in <module>:
ValueError: Выключение завершено/Shutted down.'''+col)
    elif cmd == 'calc':
        print(str(eval(input("Введите формулу (для степени используй **)(Python calc, ^ = **)"))))
    elif cmd == 'cmd':
        sp.Popen(['python', j('cmd.py')])
    elif cmd == 'lang':
        t = input('Только ru или en (Only ru or en.)')
        lang = t
    elif cmd == 'paint':
        sp.Popen(['python', j('paint.py')])
    else:
        print('unknown program')