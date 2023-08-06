import string
import xml.etree.ElementTree as ET

def read_annotation(xml_file: str):
    allowed_names = ["red_corrosion", "white_corrosion", "red_moss", "white_moss", "red_peeling", "green_peeling", "white_peeling", "MW", "RF", "tower", "mono_tower", "cable_dangle", "empty_boom"]
    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []
    list_all_objects = []

    for boxes in root.iter('object'):
        object_name = boxes.find("name")
        name_string = object_name.text
        if any(char in name_string for char in string.whitespace):
            name_string = name_string.replace(' ', '_') #replace space with underscore
            name_string = name_string.translate(str.maketrans('', '', string.whitespace)) #remove any type of whitespace
            object_name.text = name_string
            tree.write(xml_file) #saving modifed name

        if name_string not in allowed_names:
            continue

        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(float(boxes.find("bndbox/ymin").text))
        xmin = int(float(boxes.find("bndbox/xmin").text))
        ymax = int(float(boxes.find("bndbox/ymax").text))
        xmax = int(float(boxes.find("bndbox/xmax").text))

        dict_with_single_boxes = {"xmin":xmin, "ymin":ymin, "xmax":xmax, "ymax":ymax}
        list_with_all_boxes.append(dict_with_single_boxes)
        list_all_objects.append(name_string)

    return list_all_objects, list_with_all_boxes