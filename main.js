var typed = new Typed(".text", {
    strings:["Web Development" , "Data science[ML]","Data Analysis","Python","Power BI","MySQL","Microsoft Office"],
    typeSpeed:50,
    backSpeed:50,
    backDelay:1000,
    loop:true
})


function toggleText(button) {
    const paragraph = button.closest('p'); // Get the parent paragraph container
    const moreText = paragraph.querySelector('.more-text'); // Get the hidden text span
    const isVisible = moreText.classList.contains('expanded'); // Check if it's currently visible

    if (isVisible) {
        moreText.classList.remove('expanded'); // Hide the text
        paragraph.classList.remove('expanded-container'); // Reset the height
        button.textContent = 'Learn More'; // Change the button text back
    } else {
        moreText.classList.add('expanded'); // Show the text
        paragraph.classList.add('expanded-container'); // Adjust the container's height
        button.textContent = 'Learn Less'; // Change the button text to 'Learn Less'
    }
}