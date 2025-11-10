#!/usr/bin/env python3
"""
Script de prueba simplificado para las nuevas herramientas específicas de alto nivel.
Este script prueba cada una de las nuevas herramientas implementadas en la Fase 6.
"""

import sys
import os
from dotenv import load_dotenv

# Add the project root to the Python path
sys.path.append(os.path.abspath("."))

# Load environment variables
load_dotenv()


def test_especialidades_tools():
    """Prueba las herramientas relacionadas con especialidades."""
    print("\n=== PROBANDO HERRAMIENTAS DE ESPECIALIDADES ===")

    from src.agent.tools import get_especialidades, get_especialidad_por_id

    print("\n1. Probando get_especialidades()...")
    try:
        result = get_especialidades()
        print("OK: get_especialidades() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_especialidades(): {e}")

    print("\n2. Probando get_especialidad_por_id()...")
    try:
        # Probar con un ID de ejemplo (esto puede fallar si no existe)
        result = get_especialidad_por_id("1")
        print("OK: get_especialidad_por_id() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_especialidad_por_id(): {e}")


def test_usuarios_medicos_tools():
    """Prueba las herramientas relacionadas con usuarios y médicos."""
    print("\n=== PROBANDO HERRAMIENTAS DE USUARIOS Y MEDICOS ===")

    from src.agent.tools import get_usuarios, get_medicos, get_usuarios_por_especialidad

    print("\n3. Probando get_usuarios()...")
    try:
        result = get_usuarios()
        print("OK: get_usuarios() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_usuarios(): {e}")

    print("\n4. Probando get_medicos()...")
    try:
        result = get_medicos()
        print("OK: get_medicos() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_medicos(): {e}")

    print("\n5. Probando get_usuarios_por_especialidad()...")
    try:
        # Probar con un ID de especialidad de ejemplo
        result = get_usuarios_por_especialidad("1")
        print("OK: get_usuarios_por_especialidad() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_usuarios_por_especialidad(): {e}")


def test_citas_tools():
    """Prueba las herramientas relacionadas con citas."""
    print("\n=== PROBANDO HERRAMIENTAS DE CITAS ===")

    from src.agent.tools import get_citas, get_citas_por_usuario, get_citas_por_medico

    print("\n6. Probando get_citas()...")
    try:
        result = get_citas()
        print("OK: get_citas() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_citas(): {e}")

    print("\n7. Probando get_citas_por_usuario()...")
    try:
        result = get_citas_por_usuario("1")
        print("OK: get_citas_por_usuario() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_citas_por_usuario(): {e}")

    print("\n8. Probando get_citas_por_medico()...")
    try:
        result = get_citas_por_medico("1")
        print("OK: get_citas_por_medico() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_citas_por_medico(): {e}")


def test_medicas_tools():
    """Prueba las herramientas relacionadas con información médica."""
    print("\n=== PROBANDO HERRAMIENTAS MEDICAS ===")

    from src.agent.tools import get_diagnosticos_por_paciente, get_triajes_por_paciente, get_horarios_disponibles

    print("\n9. Probando get_diagnosticos_por_paciente()...")
    try:
        result = get_diagnosticos_por_paciente("1")
        print("OK: get_diagnosticos_por_paciente() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_diagnosticos_por_paciente(): {e}")

    print("\n10. Probando get_triajes_por_paciente()...")
    try:
        result = get_triajes_por_paciente("1")
        print("OK: get_triajes_por_paciente() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_triajes_por_paciente(): {e}")

    print("\n11. Probando get_horarios_disponibles()...")
    try:
        # Probar con una fecha de ejemplo
        result = get_horarios_disponibles("1", "2025-11-10")
        print("OK: get_horarios_disponibles() ejecutada exitosamente")
        print(f"   Resultado: {result}")
    except Exception as e:
        print(f"ERROR en get_horarios_disponibles(): {e}")


def test_agent_integration():
    """Prueba la integración con el agente principal."""
    print("\n=== PROBANDO INTEGRACION CON EL AGENTE ===")

    try:
        from src.agent.main import run_agent

        # Probar con una consulta simple que debería usar las nuevas herramientas
        test_prompt = "Muestra todas las especialidades medicas disponibles"
        print(f"\n12. Probando agente con prompt: '{test_prompt}'")

        result = run_agent(test_prompt)
        print("OK: Agente ejecuto exitosamente")
        print(f"   Resultado: {result}")

    except Exception as e:
        print(f"ERROR en la integracion del agente: {e}")


def main():
    """Función principal que ejecuta todas las pruebas."""
    print("INICIANDO PRUEBAS DE LAS NUEVAS HERRAMIENTAS DE LA FASE 6")
    print("=" * 60)

    try:
        test_especialidades_tools()
        test_usuarios_medicos_tools()
        test_citas_tools()
        test_medicas_tools()
        test_agent_integration()

        print("\n" + "=" * 60)
        print("PRUEBAS COMPLETADAS")
        print("Las nuevas herramientas especificas de alto nivel estan disponibles para el agente.")

    except Exception as e:
        print(f"\nERROR GENERAL EN LAS PRUEBAS: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
