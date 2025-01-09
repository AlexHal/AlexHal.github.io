function toggleReadme(repoName) {
    const preview = document.getElementById(`preview-${repoName}`);
    const full = document.getElementById(`full-${repoName}`);
    const button = preview.nextElementSibling;

    if (preview.style.display === "none") {
        preview.style.display = "block";
        full.style.display = "none";
        button.textContent = "Read More";
    } else {
        preview.style.display = "none";
        full.style.display = "block";
        button.textContent = "Show Less";
    }
}
