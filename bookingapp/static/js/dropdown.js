document.getElementById('dropdown-toggle').addEventListener('click', function () {
    const menu = document.getElementById('dropdown-menu');
    const icon = document.getElementById('toggle-icon');
    
    if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'block'; // Show the menu
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        menu.style.display = 'none'; // Hide the menu
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }
});
