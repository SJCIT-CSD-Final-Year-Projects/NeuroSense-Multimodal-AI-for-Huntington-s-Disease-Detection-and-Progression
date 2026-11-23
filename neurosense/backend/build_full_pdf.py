import os
import sys
import re

# Resolve paths relative to this script's directory
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class VTUReportCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self.pages)
        # Find where Chapter 1 starts
        # For our document, preliminaries are pages 1 to 9 (cover, cert, dec, abs, ack, toc, lof)
        # We can dynamically detect or set threshold at page 9
        for page in self.pages:
            self.__dict__.update(page)
            p_num = self._pageNumber
            
            # Don't draw header/footer on cover (1) and certificate (2)
            if p_num > 2:
                self.saveState()
                self.setFont("Helvetica", 8.5)
                self.setFillColor(colors.HexColor("#475569"))

                if p_num <= 9:
                    # Preliminaries: Roman numerals i to vii
                    romans = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
                    idx = p_num - 2
                    p_str = romans[idx] if idx < len(romans) else str(idx)
                    self.drawCentredString(A4[0] / 2.0, 36, p_str)
                else:
                    # Chapters: Arabic numerals starting from 1
                    arabic_str = str(p_num - 9)
                    
                    # Header
                    self.drawString(54, A4[1] - 36, "Dept. of CSD, SJCIT")
                    self.drawCentredString(A4[0] / 2.0, A4[1] - 36, "2026-2027")
                    self.drawRightString(A4[0] - 54, A4[1] - 36, "NeuroSense: Multi-Modal HD Staging")

                    # Thin rule
                    self.setStrokeColor(colors.HexColor("#cbd5e1"))
                    self.setLineWidth(0.75)
                    self.line(54, A4[1] - 42, A4[0] - 54, A4[1] - 42)

                    # Footer
                    self.drawCentredString(A4[0] / 2.0, 36, arabic_str)

                self.restoreState()
            super().showPage()
        super().save()

def sanitize_md_to_rl(text):
    # Convert markdown bold and italics to reportlab XML tags
    text = text.replace('&', '&amp;')
    # Replace math tags
    text = re.sub(r'\$(.*?)\$', r'<i>\1</i>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Code tags
    text = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', text)
    # Clean stray div and br
    text = re.sub(r'</?(div|span|center)[^>]*>', '', text)
    text = text.replace('<br>', '<br/>').replace('<br/>', '<br/>')
    return text.strip()

def build_pdf_from_md():
    md_file = os.path.join(_SCRIPT_DIR, 'report/NeuroSense_Project_Report.md')
    pdf_file = os.path.join(_SCRIPT_DIR, 'report/NeuroSense_Project_Report.pdf')

    with open(md_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_vtu = ParagraphStyle('VTUTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=1, textColor=colors.HexColor('#0f172a'))
    sub_vtu = ParagraphStyle('VTUSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor('#334155'))
    rep_title = ParagraphStyle('RepTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14.5, leading=20, alignment=1, textColor=colors.HexColor('#1e3a8a'))
    normal_center = ParagraphStyle('NormCenter', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor('#1e293b'))
    normal_center_bold = ParagraphStyle('NormCenterB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor('#0f172a'))

    ch_num = ParagraphStyle('ChNum', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=1, textColor=colors.HexColor('#1e3a8a'), spaceBefore=8, spaceAfter=4, keepWithNext=True)
    ch_title = ParagraphStyle('ChTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=16, leading=22, alignment=1, textColor=colors.HexColor('#0f172a'), spaceAfter=14, keepWithNext=True)
    
    sec_head = ParagraphStyle('SecHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=colors.HexColor('#1e3a8a'), spaceBefore=12, spaceAfter=5, keepWithNext=True)
    subsec_head = ParagraphStyle('SubSecHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#0f172a'), spaceBefore=9, spaceAfter=4, keepWithNext=True)

    body = ParagraphStyle('BodyJustified', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13.5, alignment=4, textColor=colors.HexColor('#1e293b'), spaceAfter=6)
    bullet = ParagraphStyle('BulletText', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13.5, alignment=4, textColor=colors.HexColor('#1e293b'), leftIndent=14, spaceAfter=3)

    fig_cap = ParagraphStyle('FigCap', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, alignment=1, textColor=colors.HexColor('#334155'), spaceBefore=5, spaceAfter=12, keepWithNext=True)
    tbl_cell = ParagraphStyle('TblCell', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor('#1e293b'))
    tbl_cell_b = ParagraphStyle('TblCellB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#0f172a'))
    tbl_hdr = ParagraphStyle('TblHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10.5, alignment=1, textColor=colors.white)

    story = []

    # Partition by page breaks in preliminaries
    pages = md_text.split('<div style="page-break-after: always;"></div>')
    print(f"Total markdown sections separated by page breaks: {len(pages)}")

    # Section 0: Cover Page
    # Section 1: Certificate
    # Section 2: Declaration
    # Section 3: Abstract
    # Section 4: Acknowledgement
    # Section 5: Table of Contents & List of Figures/Tables
    # Section 6 onwards: Chapters 1 through 10, Bibliography, Appendix

    for sec_idx, section in enumerate(pages):
        lines = section.strip().split('\n')
        i = 0
        in_table = False
        table_rows = []

        while i < len(lines):
            line = lines[i].strip()

            # Handle Table
            if line.startswith('|') and line.endswith('|'):
                # Check if separator line
                if re.match(r'^\|[\s\-:|]+\|$', line):
                    i += 1
                    continue
                # Extract cells
                raw_cells = [c.strip() for c in line.split('|')[1:-1]]
                table_rows.append(raw_cells)
                i += 1
                # Check if next line is also table
                if i < len(lines) and lines[i].strip().startswith('|'):
                    continue
                else:
                    # End of table, process it
                    if table_rows:
                        # Determine column widths
                        num_cols = max(len(r) for r in table_rows)
                        avail_width = 486.0  # A4 width (595) - 2 * 54 (margins)
                        col_w = avail_width / num_cols
                        
                        # Custom column widths for specific known tables
                        col_widths = [col_w] * num_cols
                        if num_cols == 2:
                            col_widths = [140.0, 346.0]
                        elif num_cols == 3:
                            col_widths = [65.0, 350.0, 71.0]
                        elif num_cols == 4:
                            col_widths = [60.0, 160.0, 210.0, 56.0]
                        elif num_cols == 6:
                            col_widths = [75.0, 75.0, 85.0, 85.0, 75.0, 91.0]

                        formatted_table_data = []
                        for r_idx, row in enumerate(table_rows):
                            # Pad row if needed
                            while len(row) < num_cols:
                                row.append('')
                            formatted_row = []
                            for c_idx, cell_str in enumerate(row):
                                sanitized = sanitize_md_to_rl(cell_str)
                                if r_idx == 0 and ('No.' in cell_str or 'Metric' in cell_str or 'ID' in cell_str or 'Sl' in cell_str or 'Parameter' in cell_str or 'Layer' in cell_str or 'Method' in cell_str or 'Abbreviation' in cell_str or 'Study' in cell_str or 'Component' in cell_str or 'Language' in cell_str):
                                    formatted_row.append(Paragraph(sanitized, tbl_hdr))
                                else:
                                    if '<b>' in sanitized or sanitized.startswith('Figure') or sanitized.startswith('Table') or sanitized.startswith('TC-') or sanitized.startswith('FR') or sanitized.startswith('1SJ'):
                                        formatted_row.append(Paragraph(sanitized, tbl_cell_b))
                                    else:
                                        formatted_row.append(Paragraph(sanitized, tbl_cell))
                            formatted_table_data.append(formatted_row)

                        tbl = Table(formatted_table_data, colWidths=col_widths, hAlign='CENTER')
                        t_style = [
                            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
                            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
                            ('TOPPADDING', (0,0), (-1,-1), 2.5),
                            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
                            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                        ]
                        # Alternating row background
                        for r_i in range(1, len(formatted_table_data)):
                            bg = colors.HexColor('#f8fafc') if r_i % 2 == 1 else colors.white
                            t_style.append(('BACKGROUND', (0, r_i), (-1, r_i), bg))
                        tbl.setStyle(TableStyle(t_style))
                        story.append(tbl)
                        story.append(Spacer(1, 8))
                        table_rows = []
                    continue

            # Handle Images
            # Matches <img src="..." alt="..." width="..."/> or ![...](...)
            img_match = re.search(r'<img\s+src=["\']([^"\']+)["\'][^>]*>', line)
            md_img_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            
            if img_match or md_img_match:
                img_src = img_match.group(1) if img_match else md_img_match.group(2)
                # Resolve relative path: if starts with ../, strip ../
                clean_src = img_src
                if clean_src.startswith('../'):
                    clean_src = clean_src[3:]
                elif clean_src.startswith('./'):
                    clean_src = clean_src[2:]
                
                if os.path.exists(clean_src):
                    try:
                        im = PILImage.open(clean_src)
                        w, h = im.size
                        aspect = h / float(w)
                        
                        target_w = 440.0
                        target_h = target_w * aspect
                        if target_h > 300.0:
                            target_h = 300.0
                            target_w = target_h / aspect
                        
                        story.append(Spacer(1, 4))
                        story.append(Image(clean_src, width=target_w, height=target_h))
                        story.append(Spacer(1, 2))
                    except Exception as e:
                        print(f"Warning: could not load image {clean_src}: {e}")
                i += 1
                continue

            # Handle Headings
            if line.startswith('# '):
                h_text = line[2:].strip()
                if 'CHAPTER' in h_text:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), ch_num))
                elif 'VISVESVARAYA' in h_text:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), title_vtu))
                elif 'CERTIFICATE' in h_text or 'DECLARATION' in h_text or 'ABSTRACT' in h_text or 'ACKNOWLEDGEMENT' in h_text or 'TABLE OF CONTENTS' in h_text or 'LIST OF FIGURES' in h_text or 'BIBLIOGRAPHY' in h_text or 'APPENDIX' in h_text:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), ch_title))
                else:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), ch_title))
                i += 1
                continue
            elif line.startswith('## '):
                h_text = line[3:].strip()
                if 'NeuroSense:' in h_text or 'A Project Report' in h_text:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), rep_title))
                else:
                    story.append(Paragraph(sanitize_md_to_rl(h_text), ch_title))
                i += 1
                continue
            elif line.startswith('### '):
                h_text = line[4:].strip()
                story.append(Paragraph(sanitize_md_to_rl(h_text), sec_head))
                i += 1
                continue
            elif line.startswith('#### '):
                h_text = line[5:].strip()
                story.append(Paragraph(sanitize_md_to_rl(h_text), subsec_head))
                i += 1
                continue

            # Handle Figure / Table Captions
            if line.startswith('**Figure ') or line.startswith('*Figure ') or line.startswith('Figure '):
                story.append(Paragraph(sanitize_md_to_rl(line), fig_cap))
                i += 1
                continue

            # Handle Bullet points
            if line.startswith('* ') or line.startswith('- ') or line.startswith('• '):
                bullet_text = line[2:].strip()
                story.append(Paragraph("• " + sanitize_md_to_rl(bullet_text), bullet))
                i += 1
                continue

            # Handle Numbered items
            num_match = re.match(r'^(\d+[\.\)])\s+(.*)', line)
            if num_match:
                prefix = num_match.group(1)
                item_text = num_match.group(2)
                story.append(Paragraph(f"<b>{prefix}</b> " + sanitize_md_to_rl(item_text), bullet))
                i += 1
                continue

            # Skip horizontal rules
            if line.startswith('---'):
                i += 1
                continue

            # Regular paragraph
            if line:
                sanitized = sanitize_md_to_rl(line)
                if sanitized:
                    story.append(Paragraph(sanitized, body))

            i += 1

        # Break page after each major markdown section
        story.append(PageBreak())

    print(f"Generated {len(story)} flowables. Building final PDF...")
    doc.build(story, canvasmaker=VTUReportCanvas)
    print(f"Successfully compiled {pdf_file} from Markdown!")

if __name__ == '__main__':
    build_pdf_from_md()
