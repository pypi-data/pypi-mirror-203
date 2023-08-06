import os
from ShynaDatabase import Shdatabase


class ShynaStartTest:
    s_data = Shdatabase.ShynaDatabase()
    s_data.device_id = "termux"

    def test_tts(self):
        msg = str(os.environ.get("bossname"))
        msg = "termux-tts-speak 'hey '" + msg
        self.s_process.shyna_speaks(msg=msg)
        self.s_data.set_date_system(process_name="termux_test")


if __name__ == '__main__':
    ShynaStartTest().test_tts()

