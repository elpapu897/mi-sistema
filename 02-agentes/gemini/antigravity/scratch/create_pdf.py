from fpdf import FPDF

class UNEDPDF(FPDF):
    def header(self):
        # Top left text
        self.set_font("Times", "B", 10)
        self.cell(0, 5, "SECCIÓN DE ATENCIÓN AL ESTUDIANTE", ln=1)
        self.set_font("Times", "", 10)
        self.cell(0, 5, "FACULTAD DE CIENCIAS", ln=1)
        self.cell(0, 5, "GRADO EN FÍSICA", ln=1)
        self.cell(0, 5, "GRADUADO EN FÍSICA", ln=1)

        # We will add simulated logos using cells with green background
        self.set_fill_color(0, 100, 0)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 14)
        
        # Logo 1
        self.set_xy(140, 10)
        self.cell(30, 20, "UNED", border=0, align="C", fill=True)
        # Logo 2
        self.set_xy(175, 10)
        self.set_font("Helvetica", "B", 9)
        self.multi_cell(25, 10, "Facultad\nde Ciencias", border=0, align="C", fill=True)
        
        self.set_text_color(0, 0, 0)
        self.ln(20)

pdf = UNEDPDF()
pdf.add_page()
pdf.set_font("Times", "", 11)

# Student info (Right aligned block)
pdf.set_xy(100, 50)
pdf.cell(0, 5, "D/Dª.:MATÍAS GONZÁLEZ BARRIOS", ln=1)
pdf.set_x(100)
pdf.cell(0, 5, "AN/CATALUNYA, 102, 1º", ln=1)
pdf.set_x(100)
pdf.cell(0, 5, "25300 TÁRREGA", ln=1)
pdf.set_x(100)
pdf.cell(0, 5, "LLEIDA", ln=1)
pdf.set_x(100)
pdf.cell(0, 5, "Teléfono: 1153767293", ln=1)

pdf.ln(10)
pdf.set_x(20)
pdf.cell(0, 5, "Curso: 2026 / 2027", ln=1)
pdf.set_x(20)
pdf.cell(0, 5, "CONVOCATORIA DE JUNIO", ln=1)
pdf.set_x(20)
pdf.cell(80, 5, "Asunto: Conformidad de matrícula", ln=0)
pdf.cell(0, 5, "Madrid, a 12 de agosto de 2026", ln=1, align="R")

pdf.ln(5)

# First Table
pdf.set_font("Times", "B", 10)
pdf.cell(90, 6, "Su Refª.: 51648956", border=1)
pdf.set_font("Times", "", 10)
pdf.cell(100, 6, "Ntra. Refª.: 6104 - afc", border=1, ln=1)

pdf.set_font("Times", "B", 10)
pdf.cell(90, 6, "Apellidos y nombre: GONZÁLEZ BARRIOS,", border="LTR")
pdf.set_font("Times", "", 10)
pdf.cell(100, 6, "Doc. de identidad: 50232449", border=1, ln=1)
pdf.set_font("Times", "B", 10)
pdf.cell(90, 6, "MATÍAS", border="LBR")
pdf.set_font("Times", "", 10)
pdf.cell(100, 6, "País de expedición: Argentina", border=1, ln=1)

pdf.ln(5)
pdf.set_font("Times", "", 10)
pdf.multi_cell(0, 5, "Con esta fecha el Decano de la Facultad me comunica lo siguiente:")
pdf.ln(2)
pdf.multi_cell(0, 5, "Recibida su solicitud de matricula en esta Universidad para el curso 2026 / 2027 en el estudio de GRADO EN FISICA - GRADUADO EN FISICA y en las asignaturas que a continuacion se indican:")

pdf.ln(2)
# Second Table
pdf.set_font("Times", "B", 10)
pdf.cell(25, 6, "CODIGO", border=1)
pdf.cell(100, 6, "NOMBRE ASIGNATURA", border=1)
pdf.cell(65, 6, "NIVEL", border=1, ln=1)
pdf.set_font("Times", "", 10)
pdf.cell(25, 6, "041094", border=1)
pdf.cell(100, 6, "Fisica Computacional I", border=1)
pdf.cell(65, 6, "FORMACION BASICA", border=1, ln=1)

pdf.ln(2)
pdf.multi_cell(0, 5, "se procede a dar curso a su matricula, quedando bien entendido que la efectividad de la misma esta condicionada al cumplimiento de los requisitos exigidos por la legislacion vigente.")

pdf.ln(2)
pdf.cell(0, 5, "Numero de Expediente: 6104-12-00862", ln=1)

pdf.ln(2)
pdf.cell(0, 5, "De orden del Decano de la Facultad.", ln=1)

pdf.ln(2)
text = "Lo que traslado a Ud. para su conocimiento y efectos oportunos, haciendole saber que contra esta resolucion, que no agota la via administrativa, puede interponer recurso de alzada ante el Sr. Rector Magfco. de esta Universidad en el plazo de un mes contado desde la recepcion de la presente notificacion, de conformidad con lo dispuesto en el articulo 115.1 de la Ley 30/1992, de 26 de noviembre, de Regimen Juridico de las Administraciones Publicas y del Procedimiento Administrativo Comun, segun la redaccion dada por la Ley 4/1999 de 13 de enero."
pdf.multi_cell(0, 5, text)

pdf.ln(10)
pdf.set_font("Times", "B", 10)
pdf.cell(0, 5, "LA JEFA DE SECCION DE ATENCION AL ESTUDIANTE", ln=1, align="R")

pdf.ln(15)
pdf.set_font("Times", "", 10)
pdf.cell(0, 5, "Dona.: ISABEL GONZALEZ LINARES", ln=1, align="R")

pdf.ln(10)
pdf.set_font("Times", "", 8)
pdf.cell(0, 4, "Senda del Rey nº 9", ln=1)
pdf.cell(0, 4, "Madrid 28040", ln=1)
pdf.cell(0, 4, "TLFNO: 913989533", ln=1)
pdf.cell(0, 4, "EMAIL: mafdez@pas.uned.es", ln=1)

pdf.output("matricula_actualizada.pdf")
print("PDF generated successfully.")
