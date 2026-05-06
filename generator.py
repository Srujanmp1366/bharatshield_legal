from __future__ import annotations

from datetime import date as date_type
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Optional, Union

from docx2pdf import convert
from docxtpl import DocxTemplate


PathLike = Union[str, Path]


def generate_notice_pdf(
    case_id: str,
    platform_name: str,
    video_url: str,
    confidence: Union[str, float, int],
    notice_date: Optional[Union[str, date_type]] = None,
    template_path: PathLike = "notice_template.docx",
    output_pdf_path: PathLike = "notice_output.pdf",
) -> Path:
    """
    Render a DOCX notice template and export it as a PDF.

    The template is expected to contain placeholders:
    case_id, platform_name, video_url, confidence, date.
    """
    template_path = Path(template_path)
    output_pdf_path = Path(output_pdf_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    if notice_date is None:
        rendered_date = date_type.today().isoformat()
    elif isinstance(notice_date, date_type):
        rendered_date = notice_date.isoformat()
    else:
        rendered_date = str(notice_date)

    context = {
        "case_id": case_id,
        "platform_name": platform_name,
        "video_url": video_url,
        "confidence": str(confidence),
        "date": rendered_date,
    }

    doc = DocxTemplate(str(template_path))
    doc.render(context)

    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

    # Render into a temporary DOCX, then convert that DOCX to PDF.
    with NamedTemporaryFile(suffix=".docx", delete=False) as tmp_file:
        temp_docx_path = Path(tmp_file.name)

    try:
        doc.save(str(temp_docx_path))
        convert(str(temp_docx_path), str(output_pdf_path))
    finally:
        if temp_docx_path.exists():
            temp_docx_path.unlink()

    return output_pdf_path


if __name__ == "__main__":
    pdf_path = generate_notice_pdf(
        case_id="CASE-12345",
        platform_name="ExamplePlatform",
        video_url="https://example.com/video/abc123",
        confidence=0.94,
    )
    print(f"PDF created at: {pdf_path.resolve()}")
