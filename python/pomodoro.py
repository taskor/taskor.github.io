import time
import sys
import platform
import subprocess

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
ROUNDS_BEFORE_LONG = 4

def play_sound():
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 2500)  # 1000 Hz for 0.5 seconds
        elif system == "Darwin":  # macOS
            subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
        else:  # Linux or other Unix
            subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"])
    except Exception:
        print("🔔")  # Fallback if sound fails

def countdown(label, seconds):
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            sys.stdout.write(f"\r{label}: {mins:02d}:{secs:02d}  ")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        sys.stdout.write(f"\r{label}: 00:00  \n")
        sys.stdout.flush()
        play_sound()
    except KeyboardInterrupt:
        sys.stdout.write("\nStopped.\n")
        raise

def pomodoro(work=WORK_MIN, short_break=SHORT_BREAK_MIN, long_break=LONG_BREAK_MIN, rounds_before_long=ROUNDS_BEFORE_LONG):
    print("Pomodoro started. Ctrl+C to stop.")
    round_count = 0
    try:
        while True:
            round_count += 1
            countdown("Work", work * 60)
            if round_count % rounds_before_long == 0:
                countdown("Long break", long_break * 60)
            else:
                countdown("Short break", short_break * 60)
    except KeyboardInterrupt:
        print("Session ended. Go hydrate.")

if __name__ == "__main__":
    pomodoro()
