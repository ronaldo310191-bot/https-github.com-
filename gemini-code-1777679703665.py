import os

# Contenido HTML optimizado para visualización directa en el navegador
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualización: Instrucciones de Eliminación de Datos</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            color: #1c1e21;
        }
        .preview-container {
            background: #ffffff;
            width: 90%;
            max-width: 650px;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            border: 1px solid #dddfe2;
        }
        .header {
            border-bottom: 2px solid #ebedf0;
            margin-bottom: 25px;
            padding-bottom: 10px;
        }
        h1 {
            color: #1877f2;
            font-size: 24px;
            margin: 0;
        }
        h2 {
            font-size: 18px;
            color: #4b4f56;
            margin-top: 25px;
        }
        p, li {
            font-size: 15px;
            line-height: 1.5;
            color: #606770;
        }
        .step-box {
            background-color: #f5f6f7;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        .contact-highlight {
            color: #1877f2;
            font-weight: bold;
            text-decoration: none;
        }
        footer {
            margin-top: 30px;
            font-size: 12px;
            color: #90949c;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="preview-container">
        <div class="header">
            <h1>Instrucciones de Eliminación de Datos</h1>
        </div>
        
        <p>Para cumplir con las normas de Meta Platforms, Inc., detallamos a continuación los pasos para que cualquier usuario pueda solicitar la eliminación de sus datos personales vinculados a nuestra aplicación.</p>
        
        <h2>Opción 1: Configuración de Facebook</h2>
        <p>Es la forma más rápida de revocar accesos:</p>
        <ol>
            <li>Ve a tu perfil de Facebook y entra en <strong>Configuración y privacidad</strong>.</li>
            <li>Selecciona <strong>Configuración</strong> y luego busca <strong>Apps y sitios web</strong> en el menú lateral.</li>
            <li>Localiza nuestra aplicación y haz clic en <strong>Eliminar</strong>.</li>
        </ol>

        <div class="step-box">
            <h2>Opción 2: Solicitud Directa</h2>
            <p>Si deseas que eliminemos datos específicos de nuestros servidores externos, puedes contactarnos enviando un correo:</p>
            <p><strong>Email:</strong> <span class="contact-highlight">[TU_CORREO_AQUÍ]</span></p>
            <p><strong>Asunto:</strong> Solicitud de Eliminación de Datos - [NOMBRE_APP]</p>
        </div>

        <p>Una vez recibida la solicitud, procesaremos la eliminación completa de los registros en un plazo máximo de 72 horas.</p>
        
        <footer>
            Documento generado para cumplimiento de Meta Developers &copy; 2026
        </footer>
    </div>
</body>
</html>
"""

# Guardar el archivo físicamente
file_name = "visualizar_instrucciones_meta.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

print(file_name)