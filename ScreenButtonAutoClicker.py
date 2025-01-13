import pyautogui
import time

def find_and_click_button(button_image, confidence=0.8):
    """
    Ищет кнопку на экране по изображению и нажимает на неё.
    :param button_image: Путь к изображению кнопки.
    :param confidence: Уровень уверенности для поиска (от 0 до 1).
    """
    try:
        location = pyautogui.locateCenterOnScreen(button_image, confidence=confidence)
        if location:
            print(f"Кнопка найдена: {location}. Нажимаю...")
            pyautogui.click(location)
            return True
        else:
            print(f"Кнопка {button_image} не найдена.")
            return False
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def main():
    # Список изображений кнопок
    buttons = ["button1.png", "button2.png"]

    try:
        while True:  # Бесконечный цикл
            for button in buttons:
                print(f"Ищу кнопку: {button}")
                success = find_and_click_button(button)
                if not success:
                    print(f"Кнопка {button} не найдена. Продолжаю поиск...")
                time.sleep(2)  # Задержка между поисками
    except KeyboardInterrupt:
        print("\nПоиск остановлен пользователем.")

if __name__ == "__main__":
    main()
