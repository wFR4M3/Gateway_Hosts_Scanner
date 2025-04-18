import subprocess
import time
import threading

print("""                 _  __      
     Made by:   | |/_ |     
 __   _____ _ __| |_| |_  __
 \ \ / / _ \ '__| __| \ \/ /
  \ V /  __/ |  | |_| |>  < 
   \_/ \___|_|   \__|_/_/\_\ 


""")


def run_nmap_scan(gateway_ip):
    nmap_command = ["sudo", "nmap", "-sn", gateway_ip+"/24"]

    try:
        result = subprocess.run(nmap_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "::Error::   " + str(e)

def print_nmap_output(gateway_ip):
    while True:
        scan_result = run_nmap_scan(gateway_ip)
        subprocess.run("clear", shell=True)
        print(scan_result)
        time.sleep(5)

if __name__ == "__main__":
    gateway_ip = input(":: GATEWAY IP ::   ")
    threading.Thread(target=print_nmap_output, args=(gateway_ip,), daemon=True).start()
    while True:
        time.sleep(1)
##real