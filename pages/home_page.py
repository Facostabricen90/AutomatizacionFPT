from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    DYNAMIC_ID_BUTTON = (By.XPATH, "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]")
    HIDDEN_TEXT_LABEL = (By.XPATH, "//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]")

    def navigate_home(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )


    def click_pos_button(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def click_boton_id_dynamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)