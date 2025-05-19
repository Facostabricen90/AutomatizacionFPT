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

    def select_checkbox(self, label_text):
        assert label_text in [
            "Hamburguesa",
            "Pizza",
            "Helado",
            "Pasta",
            "Torta",
        ], "Las opciones aceptadas son: 'Hamburguesa', 'Pizza', 'Helado', 'Pasta', 'Torta'"
        checkbox_locator = (By.XPATH, f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']")
        self.select_element(checkbox_locator)

    def select_radio_button(self, option):
        assert option in ["Si", "No"], "Las opciones aceptadas son: 'Si', 'No'"
        radio_button_locator = (By.XPATH, f"//label[@class='form-check-label' and contains(., '{option}')]/preceding-sibling::input[@type='radio']")
        self.select_element(radio_button_locator)
        