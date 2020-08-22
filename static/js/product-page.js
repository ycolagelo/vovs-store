function handleThumbnailClick(e) {
  // console.log(e.currentTarget.dataset);
  let newImageUrl = e.currentTarget.dataset.imageUrl;
  document.querySelector(".product-image").src = newImageUrl;
}

// Listen to the click event for every thumbnail image
for (let element of document.querySelectorAll(".product-thumbnail-container")) {
  element.addEventListener("click", handleThumbnailClick);
}

document
  .querySelector("#add-to-cart-form")
  .addEventListener("submit", (event) => {
    event.preventDefault();

    let productInfoData = document.querySelector("#product-info-data").dataset;
    let productId = parseInt(productInfoData.productId);
    let quantity = parseInt(document.querySelector("#quantity-input").value);

    addUpdateCart(productId, quantity)
      .then((response) => {
        showAlert(false, "Successfuly added item to cart");
        console.log("success", response);
      })
      .catch((err) => {
        showAlert(true, "Failed to add item to cart. Please try again.");
        console.error("error");
      });
  });

function showAlert(isError, alertText) {
  let alertElement = document.querySelector("#atc-alert");
  alertElement.classList.remove("d-none");
  document.querySelector("#atc-alert-text").innerText = alertText;

  if (isError) {
    alertElement.classList.add("alert-danger");
    alertElement.classList.remove("alert-success");
  } else {
    alertElement.classList.add("alert-success");
    alertElement.classList.remove("alert-danger");
  }

  hideAlertAfterNMiliseconds(2000);
}

function hideAlertAfterNMiliseconds(ms) {
  setTimeout(() => {
    let alertElement = document.querySelector("#atc-alert");
    alertElement.classList.add("d-none");
  }, ms);
}
