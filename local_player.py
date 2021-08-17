from os import error
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

class ForceQuit(Exception):
    pass

class LocalPlayer():
    def __init__(self) -> None:
        self.muted = False

    def play_video(self, video_path: str) ->None:
        video=cv2.VideoCapture(video_path)
        player = MediaPlayer(video_path)
        player.set_mute(self.muted)

        fps = video.get(cv2.CAP_PROP_FPS)
        sleep_ms = int(np.round((1/fps)*1000) /3)

        while True:
            grabbed, frame=video.read()
            audio_frame, val = player.get_frame()
            if not grabbed:
                break
                    
            if cv2.waitKey(sleep_ms) & 0xFF == ord("q"):
                raise ForceQuit("user quit application")
            
            if cv2.waitKey(sleep_ms) & 0xFF == ord("n"):
                break

            if cv2.waitKey(sleep_ms) & 0xFF == ord("m"):
                player.set_mute(not player.get_mute())
                self.muted = True

            cv2.imshow("Search Result Viewer", frame)
            if val != 'eof' and audio_frame is not None:
                img, t = audio_frame

        video.release()
        cv2.destroyAllWindows()