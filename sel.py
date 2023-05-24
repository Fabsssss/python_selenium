from selenium import webdriver
import pyautogui
import clipboard
import time

liste = []
link = "https://aniworld.to/anime/stream/we-never-learn/staffel-2/episode-"
folgenanzahl = 13

driver_path = "./geckodriver"
k = 0
driver = webdriver.Firefox(executable_path=driver_path)
driver.maximize_window()

for i in range(1, folgenanzahl+1):
    try:
    
        driver.get(link+str(i))
        pyautogui.press('f12')

        while True:
            search = pyautogui.locateOnScreen('C:\\Users\\Fabs\\Desktop\\Python\\python_selenium\\inspektor.PNG')
            if search is not None:
                break
        
        pyautogui.moveTo(search.left,search.top)
        pyautogui.click()

        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(currentMouseX,currentMouseY-50)
        time.sleep(1)
        
        while True:
            suchen = pyautogui.locateOnScreen('C:\\Users\\Fabs\\Desktop\\Python\\python_selenium\\durchsuchen.PNG')
            if suchen is not None:
                break
        pyautogui.moveTo(pyautogui.center(suchen))
        pyautogui.click()

        time.sleep(1)

        pyautogui.typewrite("sources")
        pyautogui.press("enter")
        pyautogui.moveRel(0, 100, duration=1)
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl', 'c')

        clipboard_content = clipboard.paste()
        #print(clipboard_content)
        splitted_text = clipboard_content.split("var sources = {")
        #print(splitted_text[1])

        t = splitted_text[1].split("'")
        #with open("./links.txt", "a") as file:
        #    file.write(t[3])
        liste.append(t[3])
        k = k+1
        pyautogui.press('f12')
        time.sleep(3)

    except Exception as e:
        print(str(e))
driver.quit()
print(liste)





