let isScraping = false; // Track toggle state
let usernames = [];

// Handle the toggle button click
document.getElementById("toggle").addEventListener("click", () => {
    const button = document.getElementById("toggle");

    if (isScraping) {
        // Stop scraping: Change button text and stop any active action
        button.innerText = "Start";
        isScraping = false;
        console.log("Scraping stopped.");
    } else {
        // Start scraping: Change button text and initiate action
        button.innerText = "Stop";
        isScraping = true;
        
        // Open file input dialog
        document.getElementById("fileInput").click();
    }
});

// Handle file input change (when user selects a file)
document.getElementById("fileInput").addEventListener("change", (event) => {
    const file = event.target.files[0];

    if (file && isScraping) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const content = event.target.result;
            usernames = content.split("\n").map(line => line.trim()).filter(line => line.length > 0);
            
            // Send usernames to background script to start opening tabs
            chrome.runtime.sendMessage({ action: "openTabs", usernames: usernames });
        };
        reader.readAsText(file);
    }
});
