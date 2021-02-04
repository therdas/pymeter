from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer

svgExamples = [r'<rect width="$(size)" height="$(val)" style="fill:rgb(0,0,255)"/>']

def svgFactory(svg, percent = 0, size = 32):
    svgHeader = r'<svg version="1.1" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
    svgMid = svg.replace("$(val)", str(percent * size / 100 )).replace("$(size)", str(size))
    svgEnd = r'</svg>'
    return svgHeader + svgMid + svgEnd

def foo(percent = 0, size = 32):
    """Returns QIcon"""
    svgstr = svgFactory(svgExamples[0], percent, size)
    svg_bytes = bytearray(svgstr, encoding="utf-8")
    r = QSvgRenderer(svg_bytes)
    i = QImage(32,32, QImage.Format_ARGB32)
    i.fill(0xffffffff)
    p = QPainter(i)
    r.render(p)
    a = QPixmap.fromImage(i)
    p.end()
    print(a)
    return a