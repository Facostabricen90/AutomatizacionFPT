import pytest

@pytest.mark.sandbox
@pytest.mark.regression
def test_id_dynamic_button_reveal_text_on_click(home_page):
    home_page.navigate_home()
    home_page.click_pos_button()

    element_hidden_text = home_page.wait_for_element(home_page.HIDDEN_TEXT_LABEL)

    text_expected = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"

    assert (
        text_expected in element_hidden_text.text
    ), "El texto esperado no está presente en el elemento oculto"  


@pytest.mark.sandbox
@pytest.mark.regression
def test_button_id_dynamic_change_color_on_hover(home_page):
    home_page.navigate_home()
    button_dynamic_id = home_page.wait_for_element(home_page.DYNAMIC_ID_BUTTON)

    color_before_hover = button_dynamic_id.value_of_css_property("background-color")

    home_page.hover_over_dynamic_id_button()

    color_after_hover = button_dynamic_id.value_of_css_property("background-color")

    assert color_before_hover != color_after_hover, "El color del botón no cambió al hacer hover"
