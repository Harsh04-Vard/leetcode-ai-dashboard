from fpdf import FPDF


def create_roadmap_pdf(username, roadmap_text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    # ---------------- TITLE ---------------- #

    pdf.set_font("Arial", "B", 20)

    pdf.cell(
        200,
        10,
        "AI LeetCode Roadmap",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # ---------------- USERNAME ---------------- #

    pdf.set_font("Arial", "", 12)

    pdf.cell(
        200,
        10,
        f"Username: {username}",
        ln=True
    )

    pdf.ln(5)

    # ---------------- ROADMAP CONTENT ---------------- #

    pdf.set_font("Arial", size=11)

    roadmap_text = roadmap_text.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    pdf.multi_cell(
        0,
        8,
        roadmap_text
    )

    # ---------------- SAVE PDF ---------------- #

    file_name = f"{username}_roadmap.pdf"

    pdf.output(file_name)

    return file_name