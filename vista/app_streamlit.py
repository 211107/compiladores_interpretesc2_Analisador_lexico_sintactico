import streamlit as st
from analizadores.lexer import prueba
from analizadores.sintactico import parse_code

def main():
    st.title("Analizador Léxico y Sintáctico")

    # Solicitar al usuario ingresar el código
    data = st.text_area("Ingrese el código:")

    # Botón para iniciar el análisis
    if st.button("Analizar"):
        # Realizar análisis léxico
        resultado_lexico = prueba(data)
        # Realizar análisis sintáctico
        resultado_sintactico = parse_code(data)

        # Mostrar resultados en la interfaz
        st.header("Resultado del análisis léxico:")
        st.table(resultado_lexico)

        st.header("Resultado del análisis sintáctico:")
        if resultado_sintactico:
            st.success("El código es válido.")
        else:
            st.error("El código es inválido.")

if __name__ == "__main__":
    main()
