import os

# Список файлов, которые нужно создать
files_to_create = [
    "home.html",
    "messenger.html",
    "feed.html",
    "friends.html",
    "account.html"
]

# Папка для хранения файлов
base_path = "/mnt/data/smp_pages"
os.makedirs(base_path, exist_ok=True)

# Шаблон содержимого для новых HTML-файлов
template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
</head>
<body>
  <h1>{title}</h1>
  <p>Здесь будет контент страницы <strong>{filename}</strong>.</p>
</body>
</html>
"""

# Создание файлов
created_files = []
for filename in files_to_create:
    title = "СМП — " + filename.replace(".html", "").capitalize()
    filepath = os.path.join(base_path, filename)
    with open(filepath, "w") as f:
        f.write(template.format(title=title, filename=filename))
    created_files.append(filepath)

created_files
