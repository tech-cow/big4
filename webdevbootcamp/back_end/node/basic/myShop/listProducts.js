var faker = require('faker');
counter = 1;

for (var i = 0; i < 10; i++) {
  var productName = faker.commerce.productName();
  var price = faker.commerce.price();
  console.log("");
  console.log("Product " + counter);
  console.log(productName);
  console.log("Price: $" + price);
  console.log("--------------------------");
  counter ++;
}
