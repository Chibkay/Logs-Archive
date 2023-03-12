import os
import shutil
import datetime

log_dir = "/path/to/log/dir"
archive_dir = "/path/to/archive/dir"
days_to_keep = 7

# Create archive folder if it does not exist
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

# Move old log files to archive folder
today = datetime.datetime.now()
for filename in os.listdir(log_dir):
    filepath = os.path.join(log_dir, filename)
    if os.path.isfile(filepath):
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        if (today - mod_time).days >= days_to_keep:
            archive_filepath = os.path.join(archive_dir, filename)
            shutil.move(filepath, archive_filepath)
