// Page scroll event handler
window.addEventListener('scroll', function() {
  const divider = document.querySelector('.custom-divider-nav');
  // Check if scrolled more than 80 pixels
  if (window.pageYOffset > 80) {
    divider.classList.add('visible');
  } else {
  // Hide the separator
    divider.classList.remove('visible');
  }
});


// Theme switcher
// We get elements for working with the theme
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const icon = themeToggle.querySelector('i');

// Check the topic stored in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
// Apply a light theme when loading
  body.classList.add('light-theme');
  icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
}

// Theme switch click handler
themeToggle.addEventListener('click', () => {
  body.classList.toggle('light-theme');
  
  if (body.classList.contains('light-theme')) {
// Change the icon to the moon for the light theme
    icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
// Save the light theme selection
    localStorage.setItem('theme', 'light');
  } else {
// Change the icon to the sun for the dark theme
    icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
// Save the dark theme selection
    localStorage.setItem('theme', 'dark');
  }
});
