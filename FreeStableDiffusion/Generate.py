from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import datetime


def _setUpDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    driver.maximize_window()

    Webwait = WebDriverWait(driver, 80)

    return driver, Webwait


def GenerateImageFromPrompt(prompt: str, file_name):

    driver, wait = _setUpDriver()
    # go to webpage
    driver.get("https://dezgo.com/")

    # enter the prompt
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/textarea",
            )
        )
    )
    element.send_keys(prompt)

    # Press the run button
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[2]/div[2]/button",
            )
        )
    )
    element.click()

    # Get Generated Image
    try:
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='image-output']"))
        )
        current_datetime = datetime.datetime.now()
        if file_name is None:
            file_name = (
                "GeneratedImage_"
                + current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                + ".png"
            )
        else:
            file_name = os.path.join(
                file_name,
                "GeneratedImage_"
                + current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                + ".png",
            )
        # Save the image to a file
        with open(file_name, "wb") as f:
            f.write(
                driver.find_element(
                    By.XPATH, "//*[@id='image-output']"
                ).screenshot_as_png
            )
        print("Image saved as", file_name)
    except TimeoutError:
        print("Time out on wait for generated Image")
    driver.close()


def InpaintFromPrompt(MaskPrompt: str, InpaintPrompt: str, ImagePath, SavePath):
    driver, wait = _setUpDriver()
    driver.get("https://dezgo.com/text-inpainting")

    # enter the mask prompt
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/input",
            )
        )
    )
    element.send_keys(MaskPrompt)

    # enter the inpaint prompt
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/textarea",
            )
        )
    )
    element.send_keys(InpaintPrompt)

    # upload the image
    element = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[3]/div/input",
            )
        )
    )
    element.send_keys(os.path.abspath(ImagePath))
    time.sleep(4)

    # Press the run button
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[1]/div/div[2]/div[2]/button",
            )
        )
    )
    element.click()

    # press close-ad button
    element = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[@id='mmt-328f29ef-b4c4-462a-91eb-64b5791504d7_1_sticky-close']",
            )
        )
    )
    element.click()

    # Get Generated Image
    try:
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='image-output']"))
        )
        # Save the image to a file
        current_datetime = datetime.datetime.now()
        if SavePath is None:
            SavePath = (
                "InpaintedImage_"
                + current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                + ".png"
            )
        else:
            SavePath = os.path.join(
                SavePath,
                "InapintedImage_"
                + current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
                + ".png",
            )

        with open(SavePath, "wb") as f:
            f.write(
                driver.find_element(
                    By.XPATH, "//*[@id='image-output']"
                ).screenshot_as_png
            )
        print("Image saved at", SavePath)
    except TimeoutError:
        print("Time out on wait for generated Image")
    driver.close()
