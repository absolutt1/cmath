import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timezone

def generate_sitemap(urls, filename="otbroski.xml"):
    # Create XML root element
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Add URL entries
    for url in urls:
        url_elem = ET.SubElement(root, "url")
        
        loc = ET.SubElement(url_elem, "loc")
        loc.text = url
        
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        
        priority = ET.SubElement(url_elem, "priority")
        priority.text = "0.4"
    
    # Generate XML string
    xml_str = ET.tostring(root, encoding="utf-8", method="xml")
    
    # Pretty-print XML
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="\t", encoding="utf-8").decode("utf-8")
    
    # Add XML declaration and comment
    final_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!-- created with www.mysitemapgenerator.com -->\n'
        + '\n'.join(pretty_xml.split('\n')[1:])  # Remove minidom's XML declaration
    )
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_xml)

# Example usage
if __name__ == "__main__":
    urls = [
        "https://docs.manim.community/en/stable/reference/manim.constants.html",
        "https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html",
        "https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html",
        "https://docs.manim.community/en/stable/reference/manim.constants.QualityDict.html",
        "https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html",
        "https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.SpecialThreeDScene.html",
        "https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html",
        "https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.html",
        "https://docs.manim.community/en/stable/reference/manim.typing.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.bezier.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.core.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.paths.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.RateFunction.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.tex_file_writing.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexFontTemplates.html",
        "https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexTemplateLibrary.html"
    ]
    
    generate_sitemap(urls)