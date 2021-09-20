
from network.udp_client import Client


from conf import pneumatic_socket
client = Client(*pneumatic_socket)


class Callbacks :
    def __init__(self):
        pass

    @staticmethod
    def play(argFileName,time_code):
        cmd ="play_{}_{}".format(argFileName,time_code)
        client.send(cmd)
        print (cmd)

    @staticmethod
    def scroll(argFileName,time_code):
        cmd ="scroll_{}_{}".format(argFileName,time_code)
        client.send(cmd)
        print (cmd)

    @staticmethod
    def pause():
        cmd ="pause_db27c6d0-aea7-11ea-a267-81264a8b3918Function check_00:00:10:880"
        client.send(cmd)
        print (cmd)

    @staticmethod
    def start():
        cmd ="pneumatics_level_0.5"
        client.send(cmd)
        print (cmd)

    @staticmethod
    def exit():
        cmd ='exit_db27c6d0-aea7-11ea-a267-81264a8b3918Function check_00:00:00:000'
        client.send(cmd)
        print (cmd)

    @staticmethod
    def pump( argOpeningPercent):
        cmd  = "pump_{}".format(argOpeningPercent)
        client.send(cmd)
        print (cmd)

    @staticmethod
    def test(msg):
        client.send(msg)
        print (msg)


    @staticmethod
    def valve(argNumber, argState ):
        template  = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14"]
        states    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        states[int(argNumber)-1] = int(argState)
        cmd = [template[v]+f":{states[v]}" for v in range(0,14) ]
        cmd_str = "_".join(cmd)
        cmd_str =  "valves_" + cmd_str
        print(cmd_str)
        client.send(cmd_str)


    @staticmethod
    def lumbar(argDirection ,argState):
        cmd = "lumbar_{}_{}".format(argDirection,argState)
        client.send(cmd)
        print (cmd)

    @staticmethod
    def bolstersC(argDirection ,argState):
        cmd = "bolsterC_{}_{}".format(argDirection,argState)
        client.send(cmd)
        print (cmd)

    @staticmethod
    def bolstersB(argDirection ,argState):
        cmd = "bolsterB_{}_{}".format(argDirection,argState)
        client.send(cmd)
        print (cmd)
