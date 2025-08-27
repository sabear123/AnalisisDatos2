import json
import xml.etree.ElementTree as ET

# Proveedor de datos de libros (Book Data Provider) que entrega XML
class BookDataProvider:
    def get_book_data_xml(self):
        return """
        <libro>
            <id>101</id>
            <nombre>El Quijote</nombre>
            <fecha_registro>2025-08-19</fecha_registro>
        </libro>
        """

# Biblioteca de análisis que solo acepta JSON
class AnalyticsLibrary:
    def analyze(self, book_json):
        print("Analizando datos de libro en JSON:")
        print(json.dumps(book_json, indent=4, ensure_ascii=False))

# Adaptador que convierte XML a JSON
class BookDataAdapter:
    def __init__(self, book_data_provider):
        self.book_data_provider = book_data_provider

    def get_book_data_json(self):
        xml_data = self.book_data_provider.get_book_data_xml()
        root = ET.fromstring(xml_data)
        data = {child.tag: child.text.strip() for child in root}
        return data

# Cliente que usa el adaptador
if __name__ == "__main__":
    provider = BookDataProvider()
    print("XML original:")
    print(provider.get_book_data_xml())

    adapter = BookDataAdapter(provider)
    book_json = adapter.get_book_data_json()

    analytics = AnalyticsLibrary()
    analytics.analyze(book_json)
 