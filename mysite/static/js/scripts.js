function searchCourses() {
    const input = document.getElementById('courseSearch').value.toLowerCase();
    const cards = document.querySelectorAll('.card');


    cards.forEach(
        function (card) {
            const courseTitle = card.querySelector('.card-title').innerText.toLowerCase();
            const courseDescription = card.querySelector('.card-text').innerText.toLowerCase();

            if (courseTitle.includes(input) || courseDescription.includes(input)) card.parentElement.style.display = 'block';
            else card.parentElement.style.display = 'none';
        }
    );
    console.log("Course is searching");
}

// function handleKeyPress(event) {
//     if (event.key === 'Enter') searchCourses();
// }
