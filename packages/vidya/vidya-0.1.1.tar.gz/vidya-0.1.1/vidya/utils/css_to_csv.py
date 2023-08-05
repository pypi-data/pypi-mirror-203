import csv
import cssutils


def transform_css_to_csv(css_file, csv_file):
    css = cssutils.parseString(css_file.read())
    rows = []
    properties = set()
    for rule in css:
        if isinstance(rule, cssutils.css.CSSStyleRule):
            style = rule.style.cssText
            style_items = [item.strip()
                           for item in style.split(';') if item.strip()]
            for item in style_items:
                key, value = [part.strip() for part in item.split(':')]
                properties.add(key)
    header = ["Element"] + sorted(properties)
    rows.append(header)
    for rule in css:
        if isinstance(rule, cssutils.css.CSSStyleRule):
            selector = rule.selectorText
            style = rule.style.cssText
            style_items = [item.strip()
                           for item in style.split(';') if item.strip()]
            style_dict = {}
            for item in style_items:
                key, value = [part.strip() for part in item.split(':')]
                style_dict[key] = value
            row = [selector] + [style_dict.get(prop, "")
                                for prop in sorted(properties)]
            rows.append(row)

    writer = csv.writer(csv_file)
    writer.writerows(rows)
