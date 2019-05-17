import os
from datetime import datetime

folder = #location-of-your-folder
location = input("Photo location:")
files = os.listdir(folder)
i=1

for filename in files:
    if not filename.startswith('.'):
        file = os.path.join(folder, filename)
        extension = os.path.splitext(file)

        m_time = os.path.getmtime(file)
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%Y%B%d_%H%M%S")

        new_filename = str(i) + ". " + f_time + "_" + location + extension[1]
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)
        i+=1