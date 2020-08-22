function addUpdateCart(product_id, quantity) {
  // cart/add-update
  return axios({
    method: "post",
    url: "/cart/add-update",
    data: {
      product_id,
      quantity,
    },
  });
}
