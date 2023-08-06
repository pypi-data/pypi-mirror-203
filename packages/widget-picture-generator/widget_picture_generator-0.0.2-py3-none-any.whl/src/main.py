
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

#
#   Widget Picture Generator
#   - This library use the square dashboard to generate widget picture
# 

# This is the url used to load the widget export
SQUARE_EXPORT_URL = "https://square.sensesquare.eu/export/widget/"

class WidgetPictureGenerator:
        
    # Constructor
    def __init__(self, apikey, width=1280, height=720):

        # Prepare options for headless browser
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Set apikey
        self._apikey = apikey

        # Setup driver
        self._driver = webdriver.Chrome(options=options)

        # Set resolution
        self._driver.set_window_size(width, height)

    # Load widget and wait
    def _load_widget(self, id, state, theme="light", timeout=2):         

        # Config preparation
        config = json.dumps({
            "apikey": self._apikey,
            "id": id,
            "state": state,
            "theme": theme
        })

        # Load state and configuration info
        self._driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': "window._w_config = {};".format(config) })

        # Load page
        self._driver.get(SQUARE_EXPORT_URL)

        # Wait until loading event
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "generic-container"))
        )

        # Sleep after loading
        sleep(timeout)

    # Get widget picture byte
    def get_widget_picture_byte(self, id, state, theme="light", timeout=2):

        # Load widget
        self._load_widget(id, state, theme, timeout)

        # Generate byte object
        return self._driver.get_screenshot_as_png()

    # Get widget picture file
    def get_widget_picture_file(self, filename, id, state, theme="light", timeout=2):

        # Load widget
        self._load_widget(id, state, theme, timeout)

        # Generate byte object
        return self._driver.get_screenshot_as_file(filename)
    
    # Set window resolution
    def set_resolution(self, width, height):
        
        # Set resolution
        self._driver.set_window_size(width, height)
    
    # Close browser window
    def close(self):

        # Close window
        self._driver.close()

    # Destroy class and driver
    def destroy(self):

        # Quit driver
        self._driver.quit()



# Main example
if __name__ == "__main__": 

    # Init the generator (the constructor accept width and height)
    wpg = WidgetPictureGenerator("U1OA1O4KL0B4")

    # Generate an example picture
    wpg.get_widget_picture_file("test.png", "widget_data_chart", {
        "device": {
            "key": 'ITCAMBAT134567',
            "value": 'ITCAMBAT134567'
        },
        "period": 'settimana',
        "type": [ 'aqi' ],
        "chart_type": 'bar',
        "minutes": 10,
        "showTitle": True,
        "showGrid": True,
        "showDots": True,
        "showSmoothLine": True,
        "showLegend": True,
        "_defaultStateKey": [ 'device', 'key' ]
    })

    # Destroy the driver
    wpg.destroy()