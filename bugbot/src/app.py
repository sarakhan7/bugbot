import streamlit as st
import core as hlpr_func  # updated from helper_functions

def main():
    st.set_page_config(
        page_title="BugBot",
        page_icon="🐛",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Load CSS theme
    with open("css/theme.txt", "r") as css_file:
        css = css_file.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Hero section
    st.markdown("""
    <div style='text-align: center; margin-top: 2rem; margin-bottom: 3rem;'>
        <h1 style='font-size: 4rem; font-weight: 800; color: white; letter-spacing: -1px;'>
            BugBot
        </h1>
        <h2 style='font-size: 2rem; font-weight: 700; margin: 0; color: white;'>
            AI Debugging Assistant Built to Break Things (and Fix Them Faster)
        </h2>
        <p style='color: #bbbbbb; font-size: 1.1rem; margin-top: 0.8rem;'>
            BugBot watches your prompt, writes code, and self-heals errors – so you can ship 10x faster.
        </p>
        <div style="margin-top: 2.2rem;">
            <a href="#code" style="padding: 0.75rem 2rem; background: linear-gradient(90deg, #00ffa3 0%, #dc1fff 100%); color: white; border-radius: 999px; font-weight: 600; text-decoration: none; margin-right: 1rem;">Get Started</a>
            <a href="https://github.com/sarakhan7/BugBot" target="_blank" style="padding: 0.75rem 2rem; border: 1px solid #888; color: white; border-radius: 999px; font-weight: 600; text-decoration: none;">View GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div id='code'></div>", unsafe_allow_html=True)
    st.markdown("---")

    # Prompt input
    user_prompt = st.text_area("Code Prompt", "Generate a function to convert the given string to upper case.", height=150)

    if st.button("Generate Code"):
        with st.spinner('Generating code...'):
            generated_code = hlpr_func.generate_code(user_prompt)
        st.session_state.generated_code = generated_code
        st.session_state.user_inputs = {}
        st.session_state.code_with_inputs = ""

    if 'generated_code' in st.session_state:
        st.subheader("Generated Code")
        st.code(st.session_state.generated_code, language='python')

        # Check if extract_function_parameters exists in hlpr_func
        if hasattr(hlpr_func, "extract_function_parameters"):
            parameters = hlpr_func.extract_function_parameters(st.session_state.generated_code)
        else:
            st.error("Error: 'extract_function_parameters' not found in core module.")
            parameters = None

        if parameters:
            st.subheader("Inputs")
            st.session_state.user_inputs = hlpr_func.render_input_fields(parameters)

        if st.button("Run Code"):
            if all(value.strip() != "" for value in st.session_state.user_inputs.values()):
                with st.spinner('Executing...'):
                    st.session_state.code_with_inputs = hlpr_func.prepare_code_for_execution(
                        st.session_state.generated_code, st.session_state.user_inputs
                    )
                st.subheader("Final Code")
                st.code(st.session_state.code_with_inputs, language='python')

                for attempt in range(5):
                    with st.spinner(f'Attempt {attempt + 1}...'):
                        success, output = hlpr_func.execute_code(
                            st.session_state.code_with_inputs, timeout=100 * (attempt + 1)
                        )
                    result, message = hlpr_func.determine_execution_success(
                        output, st.session_state.user_inputs
                    )

                    if result == "Success":
                        st.subheader("Output")
                        st.text(message)
                        st.success("Execution successful.")
                        break
                    else:
                        st.error(f"Error: {hlpr_func.handle_execution_errors(message)}")
                        if "ModuleNotFoundError" in message:
                            hlpr_func.handle_missing_modules(message)
                        if attempt < 4:
                            with st.spinner('Attempting fix...'):
                                st.session_state.code_with_inputs = hlpr_func.fix_code(
                                    st.session_state.code_with_inputs, message
                                )
                            st.subheader("Fixed Code")
                            st.code(st.session_state.code_with_inputs, language='python')

                if result != "Success":
                    st.warning("All retry attempts failed.")
            else:
                st.error("Please complete all input fields before running.")

    # Footer
    st.markdown("""
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: #888888;'>
        <p>&copy; 2025 BugBot • <a href="mailto:contact@bugbot.dev" style="color: #00ffa3;">Contact Us</a> • <a href="https://github.com/sarakhan7/BugBot" style="color: #00ffa3;">GitHub</a> • <a href="#" style="color: #00ffa3;">Privacy</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()