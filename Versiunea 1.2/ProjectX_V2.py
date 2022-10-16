import io
import shutil
import threading
import time
import zipfile


from Classes.PlayerVars import *
from Classes.Ui import *
from Utils.Chams import Chams, ResetChams
from Utils.Utilities import GetWindowText, GetForegroundWindow, update, is_pressed
from Utils.WallhackFunctions import SetEntityGlow, GetEntityVars
from Utils.Bhop import Bhop
from Utils.Autostrafe import AutoStrafe




def main():
    try:
        pm = pymem.Pymem("csgo.exe")
    except Exception as e:
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, '!', 'Error', 16)  
        quit(0)
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_uint(engine + dwClientState)
    cham = False
    First = True
    print("  🆅  🅴  🆉  🅸  ▉  🅳  🅾  🆁  🅸  🅽  🅰  ▉  🅿  🆁  🅸  🅽  ▉  🅿  🅴  🆁  🅴  🆃  🅸")
    print("\n\n")
    print("『O』 『i』『u』『b』『i』『m』 『p』『e』 『d』『o』『r』『i』『n』『a』")
    while True:
        time.sleep(0.0025)
        try:
            if not GetWindowText(GetForegroundWindow()).decode(
                    'cp1252') == "Counter-Strike: Global Offensive - Direct3D 9":
                time.sleep(1)
                continue
            pm.write_uchar(engine + dwbSendPackets, 1)
            player = pm.read_uint(client + dwLocalPlayer)
            if client and engine and pm:
                try:  # Getting variables
                    player, engine_pointer, glow_manager, crosshairid, getcrosshairTarget, immunitygunganme,\
                    localTeam, crosshairTeam, y_angle = GetPlayerVars(pm, client, engine, engine_pointer)
                except Exception as e:
                    print("N-o inceput runda ma pwla.")
                    time.sleep(2)
                    continue

          
            if ui.Noflash:  
                flash_value = player + m_flFlashMaxAlpha
                if flash_value:
                    pm.write_float(flash_value, float(0))
                    
            if not ui.Holdfov:  
                if ui.Togglefov and fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int(fovshit, ui.Fovvaluke)
                if not ui.Togglefov or not fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int(fovshit, 90)
                if ui.Togglefov and is_pressed(ui.Fovkey):
                    fovex = not fovex
                    time.sleep(0.25)

            if ui.Holdfov: 
                fovshit = player + m_iDefaultFOV
                if is_pressed(ui.Fovkey):
                    pm.write_int(fovshit, ui.Fovvaluke)
                else:
                    pm.write_int(fovshit, 90)

            if ui.Bhop: 
                if is_pressed("space"):
                    Bhop(pm, client, player)

            if ui.auto_strafe and y_angle: # Autostrafe
                y_angle = AutoStrafe(pm, client, player, y_angle, oldviewangle)
                oldviewangle = y_angle


            for i in range(0, 64):
                entity = pm.read_uint(client + dwEntityList + i * 0x10)
                if entity:
                    entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant = GetEntityVars(pm,
                                                                                                              entity)
                    if ui.Wallhack:
                        SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager,
                                      entity_glow, ui.Eteam, ui.healthbasedWH, ui.WRGB)
                    if ui.Radar: 
                        pm.write_int(entity + m_bSpotted, 1)
                    if ui.Chams: 
                        Chams(pm, engine, entity, ui.Healthbased, ui.Ergb, ui.Argb, ui.Allies, ui.Enemies,
                              entity_team_id, entity_hp, First, player)
                        First = False
                    if not ui.Chams and cham: 
                        ResetChams(pm, engine, entity, entity_team_id, player)
                        

            # Chams variables
            if ui.Chams:
                cham = True
            elif not ui.Chams:
                cham = False
                First = True

        except Exception as e: 
            continue


if __name__ == "__main__":
    if update(): #  Versioncontrol
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Dialog)
        Dialog.show()
        threading.Thread(target=main).start()  # Mainthread
        sys.exit(app.exec_())
    else:
        dir = os.getcwd()
        clonedir = str(dir).split("\\")[0:-1]
        stringdir = ""
        for x in clonedir:
            stringdir += f"{x}/"
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            try:
                if os.path.isfile(filepath) or os.path.islink(filepath):
                    os.unlink(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath, ignore_errors=True)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (filepath, e))
        r = requests.get("", stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(stringdir)
else:
    print("FError!")
    quit(0)
