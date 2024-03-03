function searchCourses() {
    var input = document.getElementById('courseSearch').value.toLowerCase();
    var cards = document.querySelectorAll('.card');

    cards.forEach(function(card) {
        var courseTitle = card.querySelector('.card-title').innerText.toLowerCase();
        var courseDescription = card.querySelector('.card-text').innerText.toLowerCase();
        if (courseTitle.includes(input) || courseDescription.includes(input)) {
            card.parentElement.style.display = 'block';
        } else {
            card.parentElement.style.display = 'none';
        }
    });
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        searchCourses();
    }
}
