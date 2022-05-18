from winotify import Notification, audio
import time

toaster = Notification(app_id="Lesson Script",
                       title="Message Title",
                       msg="Hello World!",
                       duration="short",
                       icon=r"F:\Python\TCP\icon.png")

# toaster.set_audio(audio.Mail, loop=False)
# toaster.set_audio(audio.SMS, loop=False)
toaster.set_audio(audio.LoopingAlarm, loop=True)

toaster.add_actions(label="Click Me!", launch="https://google.com")

toaster.show()
