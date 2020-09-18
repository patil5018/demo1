import time
from plyer import notification

if __name__ == "__main__":
	while(True):
		notification.notify(
			title = "please drink water",
			message = "Drinking Water Helps Maintain transportation of nutrients, and maintenance of body temperature.",
		#app_icon = "E:\Repositry\water_drink\icon.ico",
			timeout=10
		)
		time.sleep(60*60)
		