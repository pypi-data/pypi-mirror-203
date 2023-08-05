import os
import time

absoluteVar = 7896134278961342789613427861342786134278613427862134786342178621347861342786134278613427861342786

startMes = ""

IName = ""
IItem = ""

#event = {}

Items = {}
myBag = []
NPCs = {}

class AlreadyNPCError(Exception):
    def __init__(self):
        super().__init__("That NPC is an existing NPC[이미 있는 NPC 에러]")

class NotFoundEventError(Exception):
    def __init__(self):
        super().__init__("Event is not founded")

class AddressNotCorrect(Exception):
    def __init__(self):
        super().__init__("Server Addres is not corrected")

class VersionNotCorrect(Exception):
    def __init__(self):
        super().__init__("Version is not corrected")

class NPC:
    def __init__():
        pass

    def createNPC(NPCName, answer):
        if NPCName not in NPCs:
            NPCs[NPCName] = answer
        else:
            raise AlreadyNPCError()
    
    def changeNPC(NPCName, answer):
        if NPCName in NPCs:
            del NPCs[NPCName]
            NPCs[NPCName] = answer

    def deleteNPC(NPCName):
        #NPCs.remove(NPCName)
        del NPCs[NPCName]
    
    def listNPC():
        print(NPCs.keys())

    def talkNPC(NPCName):
        
        #for i in NPCs:
        #    if i == NPCName:
        #        print(say + " -> " + i)
        print(NPCName + " : " + NPCs[NPCName])

class CLIOption:
    def title(title):
        os.system("title " + title)

class ServerOption:
    def startMessage(startMes, self):
        self.startMes = startMes

    def playerMax(max, verbose=False):
        memberMax = max
        if verbose == True:
            print(memberMax)

    def serverAddress(address, version):
        serverAdr = address
        serverVer = version
        f = open("serverAddress.txt", "w")
        f.write(serverAdr + "\n" + serverVer)
        f.close()

    def serverName(name, description, verbose=False):
        serverNm = name
        serverDes = description
        if verbose == True:
            print("서버 이름 : " + serverNm)
            print("서버 설명 : " + serverDes)

    def setwelcomeMessage(welcomeMes, self):
        self.welcomeMes = welcomeMes

class Item:
    def createItem(name, description):
        if name not in Items:
            Items[name] = description
            #if not isinstance(event, dict):
            #    event = {}
            #event[name] = eventName
        else:
            print(name + " 은 이미 있는 아이템 입니다.")

    def viewItemInfo(name):
        itInfo = [Items[name]]
        print(itInfo)

    def listItem():
        print(Items.keys())

    def giveItem(name):
        myBag.append(name)

def run():
    def runandMain():
        option = ServerOption()
        print("--- 시작 메세지 ---")
        print(option.startMes)
        time.sleep(3.25)

        print()
        print("스킵 하고 싶다면 아무 글자나 입력해주세요.")
        skip = input("SKIP>>> ")
        
        if skip != absoluteVar:
            os.system("cls")
            time.sleep(0.5)
            print(option.welcomeMes)
            time.sleep(1.5)

            def runMain():
                for i in NPCs:
                    print(i, end="   ")
                print()
                print("명령어 : 내 가방")
                print("         아이템")
                print()
                select = input("\n메인>>> ")
                if select in NPCs:
                    os.system("cls")
                    NPC.talkNPC(select)
                    print()

                if select == "내 가방":
                    os.system("cls")
                    for i in myBag:
                        print(i, end="   ")
                    print()
                    print("명령어 : 돌아가기")
                    print("         사용하기")
                    selectBag = input("\n가방>>> ")
                    if selectBag == "돌아가기":
                        runMain()
                    
                    if selectBag == "사용하기":
                        os.system("cls")
                        print("--- 사용할수 있는 아이템들 ---")
                        for i in myBag:
                            print(i, end="   ")
                        print()
                        print("명령어 : [아이템 이름]")
                        selectBagChoose = str(input("\n아이템>>> "))
                        if selectBagChoose in myBag:
                            myBag.remove(selectBagChoose)
                            print(selectBagChoose + " 아이템을 사용했습니다!")
                            #if selectBagChoose in event:
                            #    print(event[selectBagChoose])
                            #else:
                            #    raise NotFoundEventError()

                if select == "아이템":
                    os.system("cls")
                    print("--- 바닥에 있는 아이템들 ---")
                    for i in Items:
                        print(i, end="   ")
                    print()
                    print("명령어 : 돌아가기")
                    print("         줍기")
                    selectItem = input("\n아이템>>> ")
                    if selectItem == "돌아가기":
                        runMain()

                    if selectItem == "줍기":
                        os.system("cls")
                        print("--- 주울수 있는 아이템들 ---")
                        for i in Items:
                            print(i, end="   ")
                        print()
                        print("명령어 : [아이템 이름]")
                        selectItemPick = input("\n아이템>>> ")
                        if selectItemPick in Items:
                            Item.giveItem(selectItemPick)
                            del Items[selectItemPick]
                            print(selectItemPick + " 아이템을 주웠습니다!")
        while True:
            runMain()
    while True:
        runandMain()