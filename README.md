# gh-copilot-bootcamp-python-ai-demo-2025

El Bootcamp de GitHub Copilot es una serie de clases en vivo de 4 partes diseñada para equiparte con las herramientas y el conocimiento necesarios para potenciar tu productividad en el desarrollo y aprovechar al máximo GitHub Copilot.

En este bootcamp, aprenderás a optimizar tu flujo de trabajo con GitHub Copilot, dominando todo, desde la creación de prompts efectivos hasta la automatización de tareas repetitivas como pruebas y documentación. ¡No pierdas esta oportunidad de llevar tus habilidades de codificación al siguiente nivel!

## 🎯 Descripción de la sesión

¡Ejercita tu creatividad desarrollando una aplicación web con inteligencia artificial usando Python y Flask! En esta clase, aprenderás a usar GitHub Copilot para simplificar tareas de programación, implementar modelos de machine learning y crear una interfaz web totalmente funcional. Perfecto para principiantes y entusiastas, este taller práctico te guiará desde la concepción hasta el lanzamiento del proyecto.

## Objetivos

- Introducción a Flask y al desarrollo de aplicaciones web
- Integración de IA en aplicaciones web
- Aprovechando GitHub Copilot para eficiencia

## 📚 Contenidos

1. Conoce Python y Flask.
2. Entornos de desarrollo virtual.
3. Integración de la IA en nuestro proyecto.
4. Uso de GitHub Copilot Chat para la asistencia de IA en Visual Studio Code

## 🛠 Requisitos

- Un ordenador con conexión a internet
- Un navegador web moderno (recomendamos Microsoft Edge, Google Chrome, Mozilla Firefox o Safari)
- Visual Studio Code (editor de código recomendado) con la extensión de GitHub Copilot instalada
- Ganas de aprender y experimentar

## 🎓 Cómo Inscribirse

Para inscribirte en este curso, visita [aka.ms/GitHubCopilotBootcampLATAM](https://aka.ms/GitHubCopilotBootcampLATAM) y sigue las instrucciones de inscripción para no perderte esta y las próximas sesiones.

## Instrucciones

> [!TIP]
> Para abrir enlaces te recomendamos presionar la tecla **[CTRL]** ó **[command]** y, sin soltar, dar clic en el enlace. Esto abrirá los enlaces en una nueva pestaña en tu navegador.

[![**fork**](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/manuosmx/gh-copilot-bootcamp-python-ai-demo-2025/fork)

1. Haz clic en el boton de arriba para hacer **Fork** de este repositorio. En la nueva página coloca el nombre que gustes al repositorio.
2. Cuando hayas creado el fork, puedes editarlo de la siguiente manera:
   - a) **Clonar** el repositorio:
     1. Selecciona una carpeta en tu computadora y ejecuta este comando: `git clone url_de_tu_repo`
     2. Entra a la carpeta creada con el mismo nombre de tu repositorio.
     3. Accede a la carpeta: `cd nombre-del-repositorio`
   - b) Usar **github.dev**:
     1. En la raíz de tu repositorio, presiona la tecla:  `.`.
3. Una vez clonado el proyecto, ejecuta los siguientes comandos:
    - Crear el entorno virtual:
        - Windows: `py -3 -m venv .venv`
        - MacOS/Linux: `python3 -m venv .venv`
    - Iniciar el entorno virtual:
        - Windows: `.venv\Scripts\activate`
        - MacOS/Linux: `. .venv/bin/activate`

> [!NOTE]
> En el caso de Windows los comandos pueden variar segun uses **PowerShell** ó **CMD**. 

4. Instala los requerimientos necesarios: `pip install -r requirements.txt`

5. Debes crear un archivo llamado `.env`
    - Dentro del archivo `.env` debes colocar lo siguiente:
    ```md
    AZURE_OPENAI_API_KEY=YourAPIKey
    ENDPOINT_URL=https://your-endpoint.com/
    DEPLOYMENT_NAME=YourModel
    ```
    - Sustituye cada `YourAPIKey`, `your-endpoint.com`, `YourModel` con tus verdaderas credenciales.

6. Ejecuta el proyecto con: `python3 app.py`
7. Salir del entorno virtual: `deactivate`

## Estructura del proyecto:
 ```md
 mi_proyecto/          # gh-copilot-bootcamp-python-ai-demo-2025
│
├── templates/
│   ├── layout.html        # Plantilla base (si usas herencia)
│   ├── index.html         # Plantilla para la vista principal
│   └── otros.html
│
├── static/
│   ├── css/
│   │   └── estilo.css
│   └── images/
│       └── logo.png
│
├── app.py
├── ai.py
├── .env
├── .venv
└── requirements.txt
 ```

## Recursos

- [Azure Open AI Services](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=bash%2Ckeyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-python)
- [Open AI Platform](https://platform.openai.com/docs/quickstart?language=python)
- [DeepSeek](https://api-docs.deepseek.com)

## Contribuidores

- Manuel Ortiz - [@ManuOSMx](https://github.com/manuosmx)

---

Desarrollado con ❤️ para la comunidad