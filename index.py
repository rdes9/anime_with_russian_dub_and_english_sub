import os

def find_index_html_files(start_dir):
    index_files = []
    for root, dirs, files in os.walk(start_dir):
        if 'index.html' in files:
            relative_path = os.path.relpath(root, start_dir)
            index_files.append(os.path.join(relative_path, 'index.html'))
    return index_files

def create_main_index_html(index_files, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlock the magic of anime while mastering Russian! Welcome to our subtitle reading site, where every episode is a lesson in language</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
            padding: 20px;
            background-color: #ffdab9;
            color: #000000;
            transition: background-color 0.3s, color 0.3s;
        }
        h2, h3 {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            text-decoration: underline;
            color: inherit;
        }
        .theme-selector {
            text-align: center;
            margin: 20px 0;
        }
        .theme-button {
            padding: 10px 20px;
            margin: 0 10px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s, transform 0.3s;
        }
        .theme-button:hover {
            background-color: #f0a500;
            transform: scale(1.05);
        }
    </style>
    <script>
        function setTheme(theme) {
            let bgColor, textColor;
            switch (theme) {
                case 'dark':
                    bgColor = '#121212';
                    textColor = '#ffffff';
                    break;
                case 'light':
                    bgColor = '#ffffff';
                    textColor = '#000000';
                    break;
                case 'dracula':
                    bgColor = '#282a36';
                    textColor = '#f8f8f2';
                    break;
                case 'peachpuff':
                    bgColor = '#ffdab9';
                    textColor = '#000000';
                    break;
                default:
                    bgColor = '#ffffff';
                    textColor = '#000000';
            }
            document.body.style.backgroundColor = bgColor;
            document.body.style.color = textColor;
        }
    </script>
</head>
<body onload="setTheme('peachpuff')">
    <h2>Unlock the magic of anime while mastering Russian!</h2>
    <h3>Откройте магию аниме, осваивая русский язык!</h3>
    <h2>Welcome to our subtitle reading site,</h2>
    <h3>Добро пожаловать на наш сайт для чтения субтитров,</h3>
    <h2>where every episode is a lesson in language</h2>
    <h3>где каждый эпизод - это урок языка</h3>
    <div class="theme-selector">
        <button class="theme-button" onclick="setTheme('light')">Light Mode</button>
        <button class="theme-button" onclick="setTheme('dark')">Dark Mode</button>
        <button class="theme-button" onclick="setTheme('dracula')">Dracula Mode</button>
        <button class="theme-button" onclick="setTheme('peachpuff')">Peach Puff Mode</button>
    </div>
    <ul>''')
        
        for file in index_files:
            f.write(f'<li><a href="{file}">{file}</a></li>\n')
        
        f.write('''
    </ul>
</body>
</html>''')

def main():
    current_directory = os.getcwd()
    index_files = find_index_html_files(current_directory)
    output_index_file = os.path.join(current_directory, 'index.html')
    create_main_index_html(index_files, output_index_file)
    print(f'Main index.html created at: {output_index_file}')

if __name__ == '__main__':
    main()
