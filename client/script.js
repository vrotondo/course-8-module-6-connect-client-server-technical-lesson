fetch("/products")
  .then(response => response.json())
  .then(data => {
    // render products to the page
  });

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").value;
  const category = document.querySelector("#category").value;

  fetch("/products", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, category })
  })
    .then(response => response.json())
    .then(product => {
      // update DOM with the new product
    });
});