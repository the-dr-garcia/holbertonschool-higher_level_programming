#!/usr/bin/python3
"""Generate personalized invitation files from a template."""
import os


def generate_invitations(template, attendees):
    """Create output_X.txt files from a template and a list of attendees."""
    if not isinstance(template, str):
        print("Error: Invalid input type for template: expected str, got {}."
              .format(type(template).__name__))
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees: "
              "expected a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            if os.path.exists(filename):
                print("Warning: {} already exists, overwriting.".format(filename))
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
        except OSError as e:
            print("Error writing {}: {}".format(filename, e))
