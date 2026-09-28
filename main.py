import subprocess
from turtle import back

ADB = r"C:\platform-tools\adb.exe"
BACKUP_DIR = r"C:\Users\caunas\Desktop\backup"
ANDROID_ROOT = r"/sdcard"

def adb(*args):
    return subprocess.run(
        [ADB, *args],
        check=True
    )


DIRECTORIES = [
    "/DCIM/Camera",
    "/cu",
    "/Secret",
    "/Download",
    "emu",
    "/Music/eu"
]


def backup(rdevice: str, dirin: str, dirout: str):
    adb("pull", f"{rdevice}{dirin}", dirout)

def restore(rdevice: str, dirin: str, dirout: str):
    adb("push", dirin, f"{rdevice}{dirout}")

def remove(appname: str):
    adb("shell", "pm", "uninstall", "-k", "--user", "0", appname)

def do_backup():
    for dir in DIRECTORIES:
        print(f"Pulling {dir}...")
        try:
            backup(
                ANDROID_ROOT,
                dir,
                BACKUP_DIR
            )
        except Exception as e:
            print(str(e))
    else:
        print("Backup done.")

def do_debloat():
    apps = [
        "com.kwai.video",
        "com.zhiliaoapp.musically",
        "com.amazon.mp3.galaxy",
        "com.microsoft.office.officehubrow",
        "com.google.android.apps.youtube.music",
        "com.samsung.sree",
    ]

    for app in apps:
        print(f"removing {app}...")
        remove(app)
    else:
        print("Debloat done.")

def do_restore():
        for dir in DIRECTORIES:
            print(f"Pushing {dir}...")
            # COLOCAR PRA IDENTIFICAR O ULTIMO NOME DO PATH NA HORA DE SETAR O DIRETORIO NO PC
            try:
                restore(
                    ANDROID_ROOT,
                    f"{BACKUP_DIR}/{dir}",
                    dir
                )
            except Exception as e:
                print(str(e))
        else:
            print("Restore done.")

do_restore()
