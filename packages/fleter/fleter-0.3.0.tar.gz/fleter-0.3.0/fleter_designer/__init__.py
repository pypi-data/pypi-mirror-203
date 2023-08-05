import flet


def _dict_to_xml(dict_in):
    import dict2xml
    from xml.dom.minidom import parseString

    xml_str = dict2xml.dict2xml(dict_in)
    xml_raw = '<?xml version="1.0" encoding="utf-8"?>\n' + '<xml>\n' + xml_str + '\n</xml>'
    dom = parseString(xml_raw.replace('\n', ''))  # xml_raw中有\n换行，但不美观
    pretty = dom.toprettyxml(indent="   ", newl="\n", encoding="utf-8")  # bytes
    return pretty.decode("utf-8")


def fletpage_to_fletdesign(page: flet.Page, name: str = "fletdesign"):
    fletdesign = open(f"{name}.fletdesign")

    fletdesign_dict = {
        "page": {
            "object": page,
            "title": page.title,
            "tooltip": page.tooltip
        }
    }

    fletdesign_dict_xml = _dict_to_xml(fletdesign_dict)

    fletdesign.write(fletdesign_dict_xml)
    fletdesign.close()

    return fletdesign, fletdesign_dict, fletdesign_dict_xml
