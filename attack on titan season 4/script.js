
        document.addEventListener('DOMContentLoaded', () => {
            const themeSwitcher = document.getElementById('theme');
            themeSwitcher.addEventListener('change', (event) => {
                document.body.className = event.target.value;
            });
            // Set the initial theme based on previous selection if available
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme) {
                document.body.className = savedTheme;
                themeSwitcher.value = savedTheme;
            }
            themeSwitcher.addEventListener('change', (event) => {
                const selectedTheme = event.target.value;
                document.body.className = selectedTheme;
                localStorage.setItem('theme', selectedTheme);
            });
        });
        