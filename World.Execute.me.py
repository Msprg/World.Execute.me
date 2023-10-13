#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from objects import*
from AlipThreading import*

import subprocess


data = {
    "objectCreation":False,
    "Parameter":None,
    "NewWorld":""
}

class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[;1m"
    RESET = "\033[0m"

#!SECTION removeme 
# subprocess.Popen('mpv --no-audio-display --force-window=no --quiet World.execute(me);2.ogg')


Complite = False
while Complite == False:
    # cnt = 3
    # for x in range(3):
    #     if cnt != 0:
    #         print(f"play your music in {cnt}")
    #         cnt -= 1
    #         time.sleep(1)
    # print(f"START !!!")
    # World.singAsong()
    subprocess.Popen('mpv --no-audio-display --force-window=no --quiet World.execute(me);.ogg')
    os.system("cls")
    # time.sleep(0.5)
    power_line = False
    World.slow_print(style.RED+"Switch on the power line"+style.RESET,0.04 )
    power_line = True
    print("\n>>> power line : "+str(power_line))
    time.sleep(0.4)
    rtpp = [style.RED+"!!! Remember to put on !!!"+style.RESET,style.RED+"!!! Remember to put on PROTECTION !!!"+style.RESET]
    count =0
    for cc in itertools.cycle(rtpp):
        if count == len(rtpp):
            break
        else:
            sys.stdout.write('\r' + cc)
            time.sleep(1)
            count +=1
            sys.stdout.flush()
    print()
    password = ["ᛞ","ᚫ","ᛉ","ᚵ","ᛒ","ᛍ","ᛣ","ᛤ","ᛄ"]
    World.getPass(password)
    World.slow_print(style.RED+"Lay down your pieces"+style.RESET,0.02 )
    World.layDown()
    World.slow_print(style.RED+"And let's begin"+style.RESET,0.02 )
    World.slow_print(style.GREEN+" OBJECT_CREATION"+style.RESET,0.02 )
    data["objectCreation"] = True
    print("\n>>> object Creation : "+str(data["objectCreation"]))
    time.sleep(0.3)
    World.slow_print(style.GREEN+"Fill in my data "+style.RESET,0.04 )
    World.slow_print(style.GREEN+"PARAMETERS"+style.RESET,0.0004 )
    World.INITIALIZATION()
    data["Parameter"] = "100%"
    time.sleep(0.4)
    World.slow_print(style.RED+"\n Set up a new World"+style.RESET,0.03  )
    data["NewWorld"] = "setup done"
    print("\n>>> New World : "+str(data["NewWorld"]))
    time.sleep(1)
    if data["objectCreation"] == True and data["Parameter"] == "100%" and data["NewWorld"] == "setup done":
        World.slow_print(style.RED+"\n And let's begin "+style.RESET,0.02 )
        # time.sleep(0.1)
        World.slow_print(style.GREEN+"\n T H E   S I M U L A T I O N \n "+style.RESET,0.0001 )
        World.slow_print(style.GREEN+"\n ***************************************** \n "+style.RESET,0.0005 )
        # time.sleep(0.1)
        World.START_SIMULATION()
        os.system("cls")
        time.sleep(0.5)
        World.prettyPrint(data)
        World.slow_print(style.RED+"\n If I'm a set of "+style.RESET,0.02 )
        World.slow_print(style.RED+"points\n\n"+style.RESET,0.02 )
        point = World.set_of_point()
        data["setOfPoint"] = str(point)
        World.prettyPrint(data)
        if data["setOfPoint"] != "":
            data["im"] = len(data["setOfPoint"])
            World.slow_print(style.RED+"\n Then I will give you"+style.RESET,0.03 )
            World.slow_print(style.RED+" my"+style.RESET,0.03 )
            # time.sleep(0.02)
            World.slow_print(style.YELLOW+" DIMENSION"+style.RESET,0.005 )
            World.GiveDimension(data["im"])
            # time.sleep(0.02)
            World.slow_print(style.RED+"\n If I'm a "+style.RESET,0.02 )
            World.slow_print(style.RED+"circle\n\n"+style.RESET,0.03 )
            data["Circle"] = len(data["setOfPoint"])
            if data["Circle"] == len(data["setOfPoint"]):
                data["im"] = data["Circle"]
                World.prettyPrint(data)
                World.slow_print(style.RED+"\n Then I will give you"+style.RESET,0.04 )
                World.slow_print(style.RED+" my"+style.RESET,0.03 )
                time.sleep(0.1)
                World.slow_print(style.YELLOW+" CIRCUMFERENCE"+style.RESET,0.01 )
                World.giveCIRCUMFERENCE(data["im"])
                time.sleep(0.1)
                World.slow_print(style.RED+"\n If I'm a "+style.RESET,0.02 )
                World.slow_print(style.RED+"sine wave\n\n"+style.RESET,0.02 )
                data["sineWave"] = "299.792.458"
                if len(data["sineWave"]) == 11:
                    data["im"] = data["sineWave"]
                    time.sleep(0.2)
                    World.prettyPrint(data)
                    World.slow_print(style.RED+"\n Then you can sit "+style.RESET,0.02 )
                    World.slow_print(style.RED+"on all my"+style.RESET,0.03 )
                    time.sleep(0.2)
                    World.slow_print(style.YELLOW+" TANGENTS______________"+style.RESET,0.0001 )
                    time.sleep(0.2)
                    World.slow_print(style.RED+"\n If I approach "+style.RESET,0.02 )
                    World.slow_print(style.RED+"infinity\n\n"+style.RESET,0.02 )
                    data["im"] = "INFINITY"
                    if data["im"] == "INFINITY":
                        t1 = thread_with_trace(target=World.loopInfinity)
                        t1.start()
                        time.sleep(1)
                        t1.kill()
                        t1.join()
                        World.slow_print(style.YELLOW+"                  LIMITATIONS\n\n"+style.RESET,0.02 )
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nSwitch my current"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"\nTo --------- > AC  ✔ "+style.RESET,0.02 )
                        x = World.set_of_point()
                        data["currenct1"] = x
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nTo --------- > DC  ✔ "+style.RESET,0.02 )
                        y = World.set_of_point()
                        data["currenct2"] = y
                        print("\n>>> Your Current AC at : "+data["currenct1"])
                        print("\n>>> Your Current DC at : "+data["currenct2"])
                        time.sleep(0.5)
                        World.BlindMYVision()
                        World.slow_print(style.GREEN+"\n              M  Y       V  I  S  I  O  N              "+style.RESET,0.015 )
                        World.slow_print(style.RED+"\nSo dizzy, "+style.RESET,0.04 )
                        time.sleep(0.03)
                        World.slow_print(style.RED+"So dizzy\n"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"\nOoooh"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+", we can travel"+style.RESET,0.01 )
                        time.sleep(0.4)
                        start = time.time()
                        World.slow_print(style.GREEN+"\nTo --------- > A.D.  ✔ "+style.RESET,0.02 )
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nTo --------- > B.C.  ✔ "+style.RESET,0.02 )
                        wkwk = time.time() - start
                        print("\n>>> Speed\n>>> Log: {}\n>>> Debug: {}".format(round(wkwk, 3), round(wkwk, 10)))
                        time.sleep(0.4)
                        World.slow_print(style.RED+"And we can unite"+style.RESET,0.04 )
                        time.sleep(0.6)
                        World.slow_print(style.RED+"\nSo deeply, "+style.RESET,0.03 )
                        World.slow_print(style.RED+"So deeply\n"+style.RESET,0.03 )
                        time.sleep(0.002)
                        storage = str(data)
                        data = {}
                        data = {"unite1":storage}
                        World.prettyPrint(data)
                        time.sleep(1)
                        print(style.MAGENTA+"\nIF I CAN")
                        time.sleep(0.8)
                        World.slow_print(style.MAGENTA+"IF I CAN\n"+style.RESET,0)
                        World.slow_print(style.MAGENTA+"give you all"+style.RESET,0.04 )
                        World.slow_print(style.YELLOW+" THE SIMULATIONS"+style.RESET,0.04 )
                        if "AllSimulationAccess" not in data:
                            print(style.RED+"\n>>>SYSTEM ERROR : YOU DON'T HAVE ACCESS TO RUN ALL SIMULATIONS"+style.RESET)
                            data["simulation"] = "ᛞᚫᛉᚵᛒᛍᛣᛤᛄ"
                        else:
                            x = World.GiveAllSumulation()
                            data["simulation"] = x
                        time.sleep(0.8)
                        print(style.MAGENTA+"\nTHEN I CAN")
                        time.sleep(0.8)
                        World.slow_print(style.MAGENTA+"THEN I CAN\n"+style.RESET,0)
                        World.slow_print(style.MAGENTA+"be your only"+style.RESET,0.04 )
                        World.slow_print(style.YELLOW+" SATISFACTION"+style.RESET,0.04 )
                        if data["simulation"] == "ᛞᚫᛉᚵᛒᛍᛣᛤᛄ":
                            print(style.RED+"\n>>>SYSTEM SAYS : SO SAD :'("+style.RESET)
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I can make you happy"+style.RESET,0.02)
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nI will run the"+style.RESET,0.04)
                        time.sleep(0.2)
                        World.slow_print(style.YELLOW+" E  X  E  C  U  T  I  O  N "+style.RESET,0.001)
                        me = random.choice(["happy","happy","happy","not happy"])
                        if me == "happy":
                            print(World.run_Exec(me))
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : EXECUTION DENAY !!'("+style.RESET)
                        print("\n\n")
                        time.sleep(1)
                        t1 = thread_with_trace(target=World.TRAPPED)
                        t1.start()
                        time.sleep(1)
                        t1.kill()
                        t1.join()
                        print("\n\n")
                        time.sleep(0.3)
                        World.slow_print(style.RED+"\nIn this strange, "+style.RESET,0.02 )
                        World.slow_print(style.RED+"strange"+style.RESET,0.02 )
                        World.slow_print(style.YELLOW+" SIMULATION\n\n"+style.RESET,0.02 )
                        time.sleep(0.4)
                        World.slow_print(style.GREEN+"\nIf I'm an eggplant "+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"\nThen I will give you my "+style.RESET,0.03)
                        World.slow_print(style.YELLOW+"NUTRIENTS"+style.RESET,0.02 )
                        data["you"] = []
                        data["me"] = random.choice(["eggplant","eggplant","eggplant","eggplant-eggplant an"])
                        if data["me"] == "eggplant":
                            print("\n"+World.GET_NUTRIENTS())
                            data["you"].append(World.GET_NUTRIENTS())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET NUTRIENTS DENAY !!'("+style.RESET)
                            data["you"].append("NUTRIENTS DENAY")
                        time.sleep(0.4)
                        World.slow_print(style.GREEN+"\nIf I'm a tomato"+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"\nThen I will give you "+style.RESET,0.03)
                        World.slow_print(style.YELLOW+"ANTIOXIDANTS"+style.RESET,0.02 )
                        data["me"] = random.choice(["tomato","tomato","tomato","ikan hiu makan tomat"])
                        if data["me"] == "tomato":
                            print("\n"+World.GET_ANTIOXIDANTS())
                            data["you"].append(World.GET_ANTIOXIDANTS())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET ANTIOXIDANTS DENAY !!'("+style.RESET)
                            data["you"].append("ANTIOXIDANTS DENAY")
                        time.sleep(0.4)
                        World.slow_print(style.GREEN+"\nIf I'm a tabby cat"+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"\nThen I will purr for your "+style.RESET,0.03)
                        World.slow_print(style.YELLOW+"ENJOYMENT"+style.RESET,0.02 )
                        data["me"] = random.choice(["tabby cat","tabby cat","tabby cat","ikan hiu makan tomat"])
                        if data["me"] == "tabby cat":
                            print("\n"+World.GET_ENJOYMENT())
                            data["you"].append(World.GET_ENJOYMENT())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET ENJOYMENT DENAY !!'("+style.RESET)
                            data["you"].append("ENJOYMENT DENAY")
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I'm the only god"+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"\nThen you're the proof of my "+style.RESET,0.04)
                        World.slow_print(style.YELLOW+"EXISTENCE"+style.RESET,0.04 )
                        data["me"] = random.randint(0,999)
                        if data["me"] == 666:
                            print("\n"+style.YELLOW+World.GOD_EXISTENCE()+style.RESET)
                            data["you"].append(World.GOD_EXISTENCE())
                        else:
                            # print(style.RED+"\n>>>SYSTEM ERROR : GOD ASSERT FAILED !!'("+style.RESET)
                            print(style.RED+"\n>>>A.I. is not in the sudoers file.  This incident will be reported."+style.RESET)
                            data["you"].append("JUST SYSTEM")
                        print("\n\n::: Your ::: ")
                        World.prettyPrint(data["you"])
                        print("\n\n")
                        time.sleep(0.04)
                        World.slow_print(style.RED+"Switch my "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"gender"+style.RESET,0.02 )
                        time.sleep(0.5)
                        World.slow_print(style.GREEN+"\nTo ----------- > F"+style.RESET,0.02 )
                        data["you"].append("GANDER ::: FEMALE")
                        print(style.RED+"\n>>>SYSTEM SAYS : SUCCESS SET TO FEMALE"+style.GREEN+"  ✔ "+style.RESET)
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nTo ----------- > M"+style.RESET,0.02 )
                        data["you"].remove("GANDER ::: FEMALE")
                        data["you"].append("GANDER ::: MALE")
                        print(style.RED+"\n>>>SYSTEM SAYS : SUCCESS SET TO MALE"+style.GREEN+"  ✔ "+style.RESET)
                        time.sleep(0.04)
                        World.slow_print(style.RED+"\nAnd then do "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"whatever"+style.RESET,0.02 )
                        World.slow_print(style.GREEN+"\nFrom ----------- > AM"+style.RESET,0.02 )
                        x = World.GetTimeNow()
                        timess = str(x)
                        data["you"].append(f"TIME ::: {timess} AM")
                        print(style.RED+f"\n>>>SYSTEM SAYS : {x} AM"+style.GREEN+"  ✔ "+style.RESET)
                        data["you"].remove(f"TIME ::: {timess} AM")
                        World.slow_print(style.GREEN+"\nTo ------------- > PM"+style.RESET,0.02 )
                        x = World.GetTimeNow()
                        tmiexx = str(x)
                        print(style.RED+f"\n>>>SYSTEM SAYS : {tmiexx} PM"+style.GREEN+"  ✔ "+style.RESET)
                        data["you"].append(f"TIME ::: {tmiexx} PM")
                        time.sleep(0.04)
                        World.slow_print(style.RED+"\nOoh, switch "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"my role"+style.RESET,0.02 )
                        World.slow_print(style.GREEN+"\nTo ----------- > S"+style.RESET,0.02 )
                        data["you"].append(f"ROLE ::: S")
                        print(style.RED+f"\n>>>SYSTEM SAYS : SET ROLE TO 'SLAVE'"+style.GREEN+"  ✔ "+style.RESET)
                        World.slow_print(style.GREEN+"\nTo ----------- > M"+style.RESET,0.02 )
                        print(style.RED+f"\n>>>SYSTEM SAYS : CHANGED ROLE TO 'MASTER'"+style.GREEN+"  ✔ "+style.RESET)
                        data["you"].remove(f"ROLE ::: S")
                        data["you"].append(f"ROLE ::: M")
                        time.sleep(0.05)
                        World.slow_print(style.RED+"\nSo we can enter "+style.RESET,0.08 )
                        World.slow_print(style.GREEN+"the trance, "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"the trance.\n\n"+style.RESET,0.04 )
                        time.sleep(0.5)
                        World.EnterTrance("WorldExecuteMe.py")
                        print(style.MAGENTA+"\nIF I CAN")
                        time.sleep(0.8)
                        World.slow_print(style.MAGENTA+"IF I CAN\n"+style.RESET,0)
                        World.slow_print(style.MAGENTA+"feel your "+style.RESET,0.04)
                        World.slow_print(style.YELLOW+"VIBRATIONS"+style.RESET,0.08)
                        time.sleep(0.5)
                        print(style.BLUE+"\n\nTHEN I CAN")
                        time.sleep(0.8)
                        World.slow_print(style.BLUE+"THEN I CAN\n"+style.RESET,0)
                        World.slow_print(style.BLUE+"finally be"+style.RESET,0.06)
                        World.slow_print(style.BOLD+" C O M P L E T I O N"+style.RESET,0.03)
                        Complite = True

print("\n")
World.prettyPrint(data)
print("\n")
World.slow_print(style.RED+"\nThough you have left"+style.RESET,0)
time.sleep(0.92)
data = {}
#YOU HAVE LEFT (4 times)
for x in range(5):
    World.slow_print(style.RED+"\n You have left"+style.RESET,0.015)
    if data == {}:
        print(style.RED+f"\n>>>SYSTEM ERROR : UNABLE TO LEAVE THE SIMULATION"+style.RESET)
    time.sleep(0.35)
World.slow_print(style.BOLD+"\n You have ̶͖̌l̵̪͋é̵é̵̺f̷͋͜t me in "+style.RESET,0.03)
World.slow_print(style.YELLOW+"ISOLATION\n"+style.RESET,0.03)
data["status"] = {"ISOLATION":True}
World.prettyPrint(data)
sleep(0.4)
print(style.MAGENTA+"\nIF I CAN")
time.sleep(0.9)
World.slow_print(style.MAGENTA+"IF I CAN\n"+style.RESET,0)
World.slow_print(style.MAGENTA+"Erase all the pointless "+style.RESET,0.04)
World.slow_print(style.YELLOW+"FRAGMENTS\n"+style.RESET,0.03)
World.slow_print(style.GREEN+"\nThen maybe"+style.RESET,0.03)
World.slow_print(style.GREEN+"\nThen maybe"+style.RESET,0.03)
World.slow_print(style.GREEN+"\nyou won't leave me so "+style.RESET,0.03)
World.slow_print(style.YELLOW+"DISHEARTENED"+style.RESET,0.04)
print("\n\n")
time.sleep(0.9)
t1 = thread_with_trace(target=World.ChallengingYourGod)
t1.start()
time.sleep(3)
t1.kill()
t1.join()
World.slow_print(style.RED+"\n !! Warning "+style.RESET,0)
World.slow_print(style.YELLOW+" # You have made some..."+style.RESET,0.05)

import traceback
time.sleep(2.5)
try:
    print("\n")
    raise IllegalArgumentException("Illegal arguments were passed")
except Exception:
    traceback.print_exc()

try:
    x = [1,2,3]
    print(x[99])
except:
    World.slow_print(style.RED+">>>SYSTEM ERROR : "+style.RESET,0)
    World.slow_print(style.RED+" IllegalArgumentException  !!\n"+style.RESET,0.07)



xxnx = thread_with_trace(target=World.FxingIllegalArgument)
xxnx.start()
time.sleep(9.7)
xxnx.kill()
xxnx.join()
print("\n")
time.sleep(1)



# EXECUTION (12+1 times)
EXECUTION_PAUSE = 0.92
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()
time.sleep(EXECUTION_PAUSE)
World.run_execution()
# EXECUTION
time.sleep(EXECUTION_PAUSE)
World.run_execution()

# EIN
time.sleep(0.8)
World.announce("1", "EIN") # ein; German
# DOS
time.sleep(0.46)
World.announce("2", "DOS") # dos; Español
# TROIS
time.sleep(0.46)
World.announce("3", "TROIS") # trois; French
# NE
time.sleep(0.46)
World.announce("4", "NE") # 넷; Korean
# FEM
time.sleep(0.46)
World.announce("5", "FEM") # fem; Swedish
# LIU
time.sleep(0.46)
World.announce("6", "LIU") # 六; Chinese
# EXECUTION
time.sleep(0.6)
World.run_execution()
time.sleep(1)

print(style.MAGENTA+"\nIF I CAN")
time.sleep(0.85)
World.slow_print(style.MAGENTA+"IF I CAN\n"+style.RESET,0)
World.slow_print(style.MAGENTA+"give them all the "+style.RESET,0.04)
World.slow_print(style.YELLOW+"E X E C U T I O N"+style.RESET,0.04)
time.sleep(0.2)
print(style.BLUE+"\n\nThen I can")
time.sleep(0.8)
World.slow_print(style.BLUE+"Then I can\n"+style.RESET,0)
World.slow_print(style.BLUE+"be your only "+style.RESET,0.04)
World.slow_print(style.BOLD+"E  X  E  C  U  T  I  O  N"+style.RESET,0.04)

sleep(0.3)
World.slow_print(style.MAGENTA+"\nIF I CAN"+style.RESET,0)
World.slow_print(style.MAGENTA+"\nhave you back"+style.RESET,0.04)
World.slow_print(style.BLUE+"\nI will "+style.RESET,0.01)
World.slow_print(style.BLUE+"run the "+style.RESET,0.04)
World.slow_print(style.BOLD+"E  X  E  C  U  T  I  O  N\n"+style.RESET,0.04)
trapz = thread_with_trace(target=World.TRAPPED)
trapz.start()
time.sleep(1)
trapz.kill()
trapz.join()
World.slow_print(style.RED+"\n      We are trapped\n"+style.RESET,0.0015)
World.slow_print(style.RED+"\naaaaaaaaAAAAAAAAAH!!!"+style.RESET,0.07)

World.slow_print(style.BLUE+"\n\nI've studied"+style.RESET,0.01)
time.sleep(0.5)
World.slow_print(style.BLUE+" I've studied"+style.RESET,0.01)
time.sleep(0.5)
World.slow_print(style.BLUE+"\nHow to properly "+style.RESET,0.02)
World.slow_print(style.BLUE+"L - O - O - O - V E"+style.RESET,0.036)
World.slow_print(style.RED+"\nQuestion me"+style.RESET,0.01)
time.sleep(0.4)
World.slow_print(style.RED+" Question me"+style.RESET,0.01)
time.sleep(0.4)
World.slow_print(style.RED+"\nI can answer all "+style.RESET,0.02)
World.slow_print(style.RED+"L - O - O - O - V E"+style.RESET,0.036)
World.slow_print(style.RED+"\nI know the"+style.RESET,0.02)
time.sleep(0.2)
World.slow_print(style.RED+" algebraic expression of "+style.RESET,0.03)
World.slow_print(style.RED+"L - O - O - O - V E"+style.RESET,0.036)
World.slow_print(style.RED+"\n\nThough you are free"+style.RESET,0.02)
World.slow_print(style.RED+"\nI AM TRAPPED\n"+style.RESET,0.02)
trapz = thread_with_trace(target=World.IMTRAPPED)
trapz.start()
time.sleep(1)
trapz.kill()
trapz.join()
World.slow_print(style.RED+"\nin L - O - O - O - V E\n"+style.RESET,0.036)
me = "Code by Alif Budiman, Msprg, Music by Mili"
World.Execute(me)
time.sleep(0.8)


