import shutil
import datetime

today = datetime.date.today()
date_string = today.strftime("%Y-%m-%d")

output_filename = f"backup_{date_string}"

shutil.make_archive(output_filename, "zip", "..", "section 1")

print(f"Backup created: {output_filename}.zip")

