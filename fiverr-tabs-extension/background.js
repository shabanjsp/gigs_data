let currentIndex = 0;
let usernames = [];
let activeTabs = [];

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "openTabs") {
        usernames = message.usernames;
        openNextTab();
    }
});

function openNextTab() {
    if (currentIndex >= usernames.length) return; // Stop if no more usernames

    const username = usernames[currentIndex];
    const url = `https://www.fiverr.com/${username}`;


    // `https://www.fiverr.com/gig_page/api/fetch_reviews/${gig_id}?gig_id=${gig_id}&last_star_rating_id=${last_review_id}&last_review_id=${last_review_id}&last_score=${last_score}&sort_by=relevant&page_size=5`

    chrome.tabs.create({ url: url }, (tab) => {
        console.log(`Opened tab for ${username}`);
        activeTabs.push(tab.id); // Store active tab

        if (activeTabs.length > 5) {
            let tabToClose = activeTabs.shift(); // Remove first tab from array
            chrome.tabs.remove(tabToClose, () => {
                console.log(`Closed tab ID: ${tabToClose}`);
            });
        }
    });

    currentIndex++; // Move to next username

    // Open the next tab with a delay of 3 to 11 seconds
    const delay = getRandomDelay(3000, 11000);
    setTimeout(openNextTab, delay);
}

// Function to get a random delay between a minimum and maximum value
function getRandomDelay(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}






