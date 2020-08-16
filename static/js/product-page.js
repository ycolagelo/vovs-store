

function handleThumbnailClick(e) {
    // console.log(e.currentTarget.dataset);
    let newImageUrl = e.currentTarget.dataset.imageUrl;
    document.querySelector(".product-image").src = newImageUrl;
}

// Listen to the click event for every thumbnail image
for(let element of document.querySelectorAll(".product-thumbnail-container")) {
    element.addEventListener("click", handleThumbnailClick);
}
