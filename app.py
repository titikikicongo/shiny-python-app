from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("My First Shiny App with VS code"),
    ui.input_slider("n", "Choose a number:", min=0, max=100, value=50),
    ui.output_text("result")
)

def server(input, output, session):
    @output()
    @render.text
    def result():
        return f"You selected: {input.n()}" 
    
app = App(app_ui, server)