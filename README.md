# 🧪 Automatización con Python + Selenium + Pytest

Este proyecto permite automatizar pruebas en páginas web utilizando **Python**, **Selenium WebDriver** y **Pytest** como framework de pruebas.

## 📦 Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- Google Chrome (u otro navegador que quieras usar)
- ChromeDriver (o el WebDriver correspondiente)

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/selenium-pytest-automation.git
cd selenium-pytest-automation

python -m venv venv
venv\Scripts\activate

python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt

📁 Estructura recomendada del proyecto
selenium-pytest-automation/
├── tests/
│   └── test_example.py
├── pages/
│   └── login_page.py
├── conftest.py
├── requirements.txt
├── README.md

🧰 requirements.txt
selenium>=4.0.0
pytest
pytest-html
