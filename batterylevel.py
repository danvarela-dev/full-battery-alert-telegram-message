import psutil
import time 
import requests

IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/jr6WBA3nGWDv-4_FS0X5c'

def post_ifttt(event, value):
    report = {}
    report["value1"] = value
    ifttt_event_url  = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, data=report)
    print("Notification has been sent!")

def main():
    while True:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged

        battery_percent = battery.percent
                
        if battery_percent >= 99 and plugged:
            post_ifttt('battery_charged',"The battery level is "+ str(battery_percent)+"% - PLEASE DISCONNECT!")
        if battery_percent <=12 and not plugged:
            post_ifttt('battery_charged',"The battery level is "+ str(battery_percent)+"% - PLEASE PLUG THE CHARGER!")


        time.sleep(7*60)


if __name__ == '__main__':
    main()








