import subprocess
import requests
import time
from socket import gethostname,gethostbyname

# the dedicated service monitor bot token: 5845709048:AAFrL2ROthOpzXZHWKalIVDxdAEB4DehVIo
# the dedicated service monitor chat id:
class QuickMonitor:
    def __init__(self,telegram_bot_token,telegram_chat_id,service_list,freq):
        # Telegram Bot token and chat ID
        self.token = telegram_bot_token
        self.chat_id = telegram_chat_id
        # Service names to monitor
        self.services = service_list        
        self.machine_ip = gethostbyname(gethostname())
        # Command to check if the service is running
        while True:
            stopped = self.check_services()
            if len(stopped) > 0:
               service_str = ", ".join(str(x) for x in stopped)
               message = f"The following services have stopped on machine {self.machine_ip}:\n" + service_str
               self.send_telegram_message(message)
            time.sleep(freq)  # Execute the task every freq seconds  

    # Send message to Telegram
    def send_telegram_message(self,message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}
        requests.post(url, data=data)

    def check_services(self):
        stopped_services = []        
        for service in self.services:
            try:
                CHECK_COMMAND = f"systemctl is-active {service}"
                # Run the command to check if the service is running
                result = subprocess.check_output(CHECK_COMMAND.split()).decode().strip()
                # If the service is not active, append it to the list
                if result != "active":
                    stopped_services.append(service)                
            except:
                pass
        return stopped_services