from docxtpl import DocxTemplate

from get_lab_info import get_lab_info


doc = DocxTemplate("template.docx")
info = get_lab_info(doc)
# подставляем контекст в шаблон
doc.render(info)
# сохраняем и смотрим, что получилось 
doc.save(f"{info['student'].strip()} тарировка микроманометра.docx")

print(info)