from src.reporting.generator import generar_pdf, generar_excel


def test_report_generation():
    """
    Tests the PDF and Excel report generation functions.
    """
    print("Testing report generation...")

    # Sample data (list of dictionaries)
    datos_ejemplo = [
        {"ID": 1, "Nombre": "Juan Perez", "Edad": 34, "Diagnostico": "Hipertensión"},
        {"ID": 2, "Nombre": "Maria Lopez", "Edad": 45, "Diagnostico": "Diabetes"},
        {"ID": 3, "Nombre": "Carlos Sanchez", "Edad": 29, "Diagnostico": "Asma"},
        {"ID": 4, "Nombre": "Ana Gomez", "Edad": 52, "Diagnostico": "Artritis"},
    ]

    # Generate PDF
    try:
        generar_pdf(datos_ejemplo, "reporte_de_prueba.pdf")
    except Exception as e:
        print(f"Error generating PDF: {e}")

    # Generate Excel
    try:
        generar_excel(datos_ejemplo, "reporte_de_prueba.xlsx")
    except Exception as e:
        print(f"Error generating Excel: {e}")


if __name__ == "__main__":
    test_report_generation()
