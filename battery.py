import os
import subprocess
import re

PWR_SPPLY = '/sys/class/power_supply/BAT0'
brightness_regex = re.compile(r"(\d*)")


class Battery(object):
    def __init__(self):
        if not os.path.exists(PWR_SPPLY):
            raise FileNotFoundError(
                "Default path to batter '{}' does not exist.".format(
                    PWR_SPPLY
                )
            )

    @staticmethod
    def _read_battery_descriptor(self, file):
        """
        params: files in the directory
        """
        file = os.path.join(PWR_SPPLY, file)
        if not os.path.isfile(file):
            raise FileNotFoundError(
                "Invalid path '{}': File Not Found".format(
                    file
                )
            )
        command = "cat {}".format(file)
        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                shell=True
            )
            result = process.stdout.read().decode().split("\n")[0]
        finally:
            process.stdout.close()
        return result

    @property
    def percentage_remaining(self):
        return int(_Battery._read_battery_descriptor("capacity"))

    @property
    def is_charging(self):
        return _Battery._read_battery_descriptor("status") != "Discharging"


def get_brightness():
    command = "gdbus call --session --dest org.gnome.SettingsDaemon.Power "\
        "--object-path /org/gnome/SettingsDaemon/Power "\
        "--method org.freedesktop.DBus.Properties.Get "\
        "org.gnome.SettingsDaemon.Power.Screen Brightness"

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            shell=True
        )
        result = brightness_regex.findall(process.stdout.read().decode())
    finally:
        process.stdout.close()
    return int("".join(result))


def set_brightness(value: int):
    if value not in range(101):
        raise ValueError("Value must be between 0 and 100")
    command = 'gdbus call --session --dest org.gnome.SettingsDaemon.Power '\
        '--object-path /org/gnome/SettingsDaemon/Power '\
        '--method org.freedesktop.DBus.Properties.Set '\
        'org.gnome.SettingsDaemon.Power.Screen Brightness "<int32 {}>" '\
        '> /dev/null'.format(value)

    subprocess.call(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

bat = Battery()
print(bat._read_battery_descriptor(file='charge_now'))
