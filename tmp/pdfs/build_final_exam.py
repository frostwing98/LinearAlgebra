from pathlib import Path

from reportlab.lib.colors import black, HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "pdf" / "linear_algebra_final_exam_draft.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("ExamSerif", str(FONT_DIR / "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("ExamSerif-Bold", str(FONT_DIR / "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("ExamSerif-Italic", str(FONT_DIR / "DejaVuSerif-Italic.ttf")))

PAGE_W, PAGE_H = A4
LEFT = 22 * mm
RIGHT = PAGE_W - 22 * mm
TOP = PAGE_H - 18 * mm
BOTTOM = 17 * mm
ACCENT = HexColor("#23395B")


def para(c, text, x, y, width, size=10.5, leading=None, bold=False, align=TA_LEFT, color=black):
    leading = leading or size * 1.45
    style = ParagraphStyle(
        name="exam",
        fontName="ExamSerif-Bold" if bold else "ExamSerif",
        fontSize=size,
        leading=leading,
        alignment=align,
        textColor=color,
        spaceAfter=0,
        spaceBefore=0,
    )
    p = Paragraph(text, style)
    _, h = p.wrap(width, PAGE_H)
    p.drawOn(c, x, y - h)
    return y - h


def line(c, x1, y1, x2, y2, width=0.6, color=black):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def answer_line(c, y, x=LEFT + 12 * mm, x2=RIGHT, label=None):
    if label:
        c.setFont("ExamSerif", 9.5)
        c.drawString(x, y + 2, label)
        x += c.stringWidth(label, "ExamSerif", 9.5) + 3 * mm
    line(c, x, y, x2, y, 0.45, HexColor("#777777"))


def matrix(c, rows, cx, y_top, cell_w=13 * mm, cell_h=7 * mm, size=10.5):
    nrows = len(rows)
    ncols = len(rows[0])
    total_w = ncols * cell_w
    total_h = nrows * cell_h
    x0 = cx - total_w / 2
    y0 = y_top - total_h
    c.setFont("ExamSerif", size)
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            s = str(value)
            tx = x0 + j * cell_w + cell_w / 2
            ty = y_top - (i + 0.72) * cell_h
            c.drawCentredString(tx, ty, s)
    pad = 3.0
    hook = 4.0
    lx = x0 - pad
    rx = x0 + total_w + pad
    line(c, lx + hook, y_top, lx, y_top, 0.85)
    line(c, lx, y_top, lx, y0, 0.85)
    line(c, lx, y0, lx + hook, y0, 0.85)
    line(c, rx - hook, y_top, rx, y_top, 0.85)
    line(c, rx, y_top, rx, y0, 0.85)
    line(c, rx, y0, rx - hook, y0, 0.85)
    return y0


def page_header(c, page_no, continuation=None):
    c.setFillColor(ACCENT)
    c.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, stroke=0, fill=1)
    c.setFillColor(black)
    c.setFont("ExamSerif", 8.5)
    c.drawString(LEFT, PAGE_H - 13 * mm, "Linear Algebra - Draft Final Examination")
    if continuation:
        c.drawRightString(RIGHT, PAGE_H - 13 * mm, continuation)
    line(c, LEFT, 14 * mm, RIGHT, 14 * mm, 0.4, HexColor("#888888"))
    c.setFont("ExamSerif", 8)
    c.drawCentredString(PAGE_W / 2, 9 * mm, f"Page {page_no} of 9")


def section(c, title, subtitle, y):
    c.setFillColor(ACCENT)
    c.setFont("ExamSerif-Bold", 13)
    c.drawString(LEFT, y, title)
    c.setFont("ExamSerif", 11)
    c.drawString(LEFT + c.stringWidth(title, "ExamSerif-Bold", 13) + 2 * mm, y, subtitle)
    c.setFillColor(black)
    return y - 8 * mm


def mcq(c, number, stem, options, y):
    y = para(c, f"<b>{number}.</b> {stem}", LEFT, y, RIGHT - LEFT, size=9.7, leading=13.0)
    y -= 2.0
    for label, text in options:
        y = para(c, f"{label}.&nbsp;&nbsp;&nbsp;{text}", LEFT + 9 * mm, y, RIGHT - LEFT - 9 * mm, size=9.25, leading=12.25)
    return y - 4.0


def workspace(c, y_top, y_bottom, spacing=9 * mm):
    y = y_top
    while y > y_bottom:
        line(c, LEFT, y, RIGHT, y, 0.32, HexColor("#D3D7DD"))
        y -= spacing


c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle("Linear Algebra Draft Final Examination")
c.setAuthor("Course instructor draft prepared from supplied example")

# Page 1 - Part I
page_header(c, 1)
y = TOP
c.setFont("ExamSerif-Bold", 18)
c.setFillColor(ACCENT)
c.drawCentredString(PAGE_W / 2, y, "LINEAR ALGEBRA")
y -= 7 * mm
c.setFont("ExamSerif-Bold", 15)
c.drawCentredString(PAGE_W / 2, y, "DRAFT FINAL EXAMINATION")
c.setFillColor(black)
y -= 10 * mm
c.setFont("ExamSerif", 9.5)
c.drawString(LEFT, y, "Name: ____________________________________")
c.drawRightString(RIGHT, y, "Student ID: __________________________")
y -= 7 * mm
c.drawString(LEFT, y, "Time allowed: __________")
c.drawRightString(RIGHT, y, "Total: 100 marks")
y -= 7 * mm
para(c, "<b>Instructions.</b> Show sufficient work in Part III. Unless instructed otherwise, exact answers are required. Write clearly in the spaces provided.", LEFT, y, RIGHT - LEFT, size=9.2, leading=12.5)
y -= 17 * mm
y = section(c, "Part I.", "Fill in the blanks. (20 marks; 2 marks each)", y)
items = [
    "For the system 2x - y = 3 and 3x + 4y = -1, the coefficient matrix is ________________________________.",
    "The reduced row echelon form of [[1, 2, 3], [0, 1, 4]] is ________________________________.",
    "For conformable matrices A and B, (AB)ᵀ = ________________________________.",
    "If A is invertible, then (A⁻¹)ᵀ = ________________________________.",
    "The determinant of an upper triangular matrix with diagonal entries -2, 3, and 5 is __________________.",
    "If T(x) = Ax is a linear transformation, then T(0) = __________________.",
    "The dimension of span{(1, 0, 1), (0, 1, 1)} is __________________.",
    "If A is an m × n matrix, then Null(A) is a subspace of __________________.",
    "The eigenvalues of the diagonal matrix [[4, 0], [0, -2]] are __________________.",
    "The Euclidean norm of (2, -1, 2) is __________________.",
]
for i, item in enumerate(items, 1):
    y = para(c, f"<b>{i}.</b>&nbsp;&nbsp;{item}", LEFT, y, RIGHT - LEFT, size=9.7, leading=13.2)
    y -= 3.5
c.showPage()

# Page 2 - Part II, questions 11-15
page_header(c, 2)
y = TOP
y = section(c, "Part II.", "Select the only correct statement. (20 marks; 2 marks each)", y)
y = mcq(c, 11, "Let A be 3 × 2 and B be 2 × 4. Which statement is correct?", [
    ("A", "BA is a 2 × 2 matrix."),
    ("B", "AB is a 2 × 3 matrix."),
    ("C", "AB is a 3 × 4 matrix."),
    ("D", "Neither product is defined."),
], y)
y = mcq(c, 12, "For a square matrix A, which condition is equivalent to A being invertible?", [
    ("A", "det(A) = 0"),
    ("B", "Ax = 0 has a nontrivial solution."),
    ("C", "The columns of A are linearly independent."),
    ("D", "A has a zero row in its reduced row echelon form."),
], y)
y = mcq(c, 13, "Suppose A = LU, where L is lower triangular and U is upper triangular. To solve Ax = b, one may solve", [
    ("A", "Ux = b, then Ly = x."),
    ("B", "Ly = b, then Ux = y."),
    ("C", "Lx = b, then Uy = x."),
    ("D", "LUy = x, then x = b."),
], y)
y = mcq(c, 14, "For conformably partitioned matrices and vectors, [[A, B], [C, D]][x; y] equals", [
    ("A", "[Ax + By; Cx + Dy]"),
    ("B", "[Ax + Cy; Bx + Dy]"),
    ("C", "[A + B; C + D][x; y]"),
    ("D", "[xA + yB; xC + yD] for arbitrary matrix x and y"),
], y)
y = mcq(c, 15, "Which pair of properties characterizes a linear transformation T?", [
    ("A", "T(u + v) = T(u) + T(v), and T(cu) = cT(u)"),
    ("B", "T(u + v) = T(u)T(v), and T(cu) = T(u) + c"),
    ("C", "T(0) = 1, and T(-u) = T(u)"),
    ("D", "T must map every vector to itself."),
], y)
c.showPage()

# Page 3 - Part II, questions 16-20
page_header(c, 3, "Part II continued")
y = TOP
y = mcq(c, 16, "If the pivot columns of the reduced row echelon form of A are columns 1 and 3, then a basis for Col(A) is formed by", [
    ("A", "columns 1 and 3 of the original matrix A."),
    ("B", "columns 1 and 3 of rref(A)."),
    ("C", "rows 1 and 3 of the original matrix A."),
    ("D", "all nonzero columns of rref(A)."),
], y)
y = mcq(c, 17, "For an inconsistent system Ax = b, every least-squares solution x̂ satisfies", [
    ("A", "Ax̂ = 0"),
    ("B", "AᵀAx̂ = Aᵀb"),
    ("C", "AAᵀx̂ = b"),
    ("D", "Aᵀx̂ = b"),
], y)
y = mcq(c, 18, "If Q is an orthogonal matrix, then", [
    ("A", "Q⁻¹ = -Q"),
    ("B", "Q⁻¹ = Qᵀ"),
    ("C", "QᵀQ = 0"),
    ("D", "the columns of Q are linearly dependent."),
], y)
y = mcq(c, 19, "An n × n matrix A is diagonalizable if and only if", [
    ("A", "A has exactly one eigenvalue."),
    ("B", "A has n linearly independent eigenvectors."),
    ("C", "A is triangular."),
    ("D", "det(A) = 1."),
], y)
y = mcq(c, 20, "If B is obtained from A by interchanging two rows, then", [
    ("A", "det(B) = det(A)"),
    ("B", "det(B) = 2det(A)"),
    ("C", "det(B) = -det(A)"),
    ("D", "det(B) = 0 for every A"),
], y)
y -= 4 * mm
para(c, "<b>End of Part II.</b> Continue to Part III and show all work.", LEFT, y, RIGHT - LEFT, size=10, color=ACCENT)
c.showPage()

# Page 4 - Question 21
page_header(c, 4)
y = TOP
y = section(c, "Part III.", "Show all your work in the space provided. (60 marks)", y)
y = para(c, "<b>21.</b> Let L be the lower triangular matrix shown below.", LEFT, y, RIGHT - LEFT, size=11, leading=15)
y -= 5 * mm
y = matrix(c, [[2, 0, 0], [1, 1, 0], [-1, 2, 1]], PAGE_W / 2, y, cell_w=18 * mm, cell_h=8 * mm, size=11)
y -= 7 * mm
y = para(c, "Find L⁻¹. Clearly show a valid method, such as Gauss-Jordan elimination or solving three triangular systems. <b>(7 marks)</b>", LEFT, y, RIGHT - LEFT, size=10.5, leading=15)
y -= 8 * mm
c.setFont("ExamSerif-Bold", 10.5)
c.drawString(LEFT, y, "Solution:")
workspace(c, y - 9 * mm, BOTTOM + 7 * mm)
c.showPage()

# Page 5 - Question 22
page_header(c, 5)
y = TOP
y = para(c, "<b>22.</b> Let", LEFT, y, RIGHT - LEFT, size=11)
y -= 4 * mm
y = matrix(c, [[1, 0, 1, 2], [0, 1, 1, -1], [1, 1, 2, 1]], PAGE_W / 2, y, cell_w=14 * mm, cell_h=8 * mm, size=11)
y -= 7 * mm
parts = [
    "(a) Find a basis for the null space of A. <b>(5 marks)</b>",
    "(b) Describe Null(A) as a parametric vector set. <b>(4 marks)</b>",
    "(c) Find a basis for the column space of A. <b>(4 marks)</b>",
    "(d) Describe Col(A) as a span or parametric vector set. <b>(3 marks)</b>",
]
for part in parts:
    y = para(c, part, LEFT + 5 * mm, y, RIGHT - LEFT - 5 * mm, size=10.3, leading=14.5)
    y -= 3.5 * mm
c.setFont("ExamSerif-Bold", 10.5)
c.drawString(LEFT, y, "Solution:")
workspace(c, y - 8 * mm, BOTTOM + 7 * mm, spacing=8.2 * mm)
c.showPage()

# Page 6 - Question 23
page_header(c, 6)
y = TOP
y = para(c, "<b>23.</b> Let a and b be real numbers. Consider the system", LEFT, y, RIGHT - LEFT, size=11)
y -= 5 * mm
eqs = ["x + y + z = a", "2x - y + 3z = b", "3x + 4z = a - b"]
c.setFont("ExamSerif", 11)
for eq in eqs:
    c.drawCentredString(PAGE_W / 2, y, eq)
    y -= 7 * mm
y -= 2 * mm
y = para(c, "(a) Determine all values of a and b for which the system is consistent. <b>(5 marks)</b>", LEFT + 5 * mm, y, RIGHT - LEFT - 5 * mm, size=10.4, leading=15)
y -= 5 * mm
y = para(c, "(b) Are there any values of a and b for which the system has exactly one solution? Justify your answer. <b>(5 marks)</b>", LEFT + 5 * mm, y, RIGHT - LEFT - 5 * mm, size=10.4, leading=15)
y -= 8 * mm
c.setFont("ExamSerif-Bold", 10.5)
c.drawString(LEFT, y, "Solution:")
workspace(c, y - 8 * mm, BOTTOM + 7 * mm)
c.showPage()

# Page 7 - Question 24
page_header(c, 7)
y = TOP
y = para(c, "<b>24.</b> Compute the determinant of the following matrix. Use determinant properties or row/column expansion, and show the main steps. <b>(10 marks)</b>", LEFT, y, RIGHT - LEFT, size=11, leading=16)
y -= 8 * mm
y = matrix(c, [[2, 0, 0, 0, 0], [1, 3, 1, 1, 1], [1, 0, 4, 0, 0], [1, 0, 2, 5, 0], [1, 0, 2, 1, 6]], PAGE_W / 2, y, cell_w=13 * mm, cell_h=8 * mm, size=11)
y -= 12 * mm
c.setFont("ExamSerif-Bold", 10.5)
c.drawString(LEFT, y, "Solution:")
workspace(c, y - 9 * mm, BOTTOM + 7 * mm)
c.showPage()

# Page 8 - Question 25
page_header(c, 8)
y = TOP
y = para(c, "<b>25.</b> Consider the symmetric matrix", LEFT, y, RIGHT - LEFT, size=11)
y -= 5 * mm
y = matrix(c, [[2, 1, 0], [1, 2, 0], [0, 0, 4]], PAGE_W / 2, y, cell_w=18 * mm, cell_h=8 * mm, size=11)
y -= 7 * mm
q25 = [
    "(a) Find the eigenvalues of A and a basis for each eigenspace. <b>(6 marks)</b>",
    "(b) Find an orthonormal basis of ℝ³ consisting of eigenvectors of A. <b>(4 marks)</b>",
    "(c) Use orthogonal diagonalization to compute A⁴. Show P, D, and the resulting matrix. <b>(7 marks)</b>",
]
for part in q25:
    y = para(c, part, LEFT + 5 * mm, y, RIGHT - LEFT - 5 * mm, size=10.4, leading=15)
    y -= 4 * mm
c.setFont("ExamSerif-Bold", 10.5)
c.drawString(LEFT, y, "Solution:")
workspace(c, y - 8 * mm, BOTTOM + 7 * mm, spacing=8.5 * mm)
c.showPage()

# Page 9 - continuation workspace
page_header(c, 9, "Question 25 continued")
y = TOP
para(c, "<b>25(c) continued:</b> Use this page for the remaining diagonalization and matrix-power work.", LEFT, y, RIGHT - LEFT, size=10.8, leading=15)
workspace(c, y - 14 * mm, BOTTOM + 18 * mm, spacing=9 * mm)
c.setFont("ExamSerif-Bold", 11)
c.setFillColor(ACCENT)
c.drawCentredString(PAGE_W / 2, BOTTOM + 9 * mm, "END OF EXAMINATION")
c.setFillColor(black)
c.save()

print(OUT)
